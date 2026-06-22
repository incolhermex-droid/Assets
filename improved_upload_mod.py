"""
Nexus Mods file uploader script - Versión Mejorada (2026)
Optimizado: progreso real, bajo uso de memoria, más opciones y robustez.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree as ET

import requests

BASE_URL = "https://api.nexusmods.com/v3"
MULTIPART_THRESHOLD = 100 * 1024 * 1024  # 100 MiB


class _ProgressReader:
    """Wrapper para mostrar progreso real sin cargar el archivo completo en memoria."""
    def __init__(self, file_obj, total: int):
        self._file = file_obj
        self._total = total
        self._done = 0

    def read(self, size: int = -1) -> bytes:
        chunk = self._file.read(size)
        if chunk:
            self._done += len(chunk)
            pct = self._done * 100 // self._total
            mb_done = self._done / 1024 / 1024
            mb_total = self._total / 1024 / 1024
            print(f"\r  {mb_done:.1f} MiB / {mb_total:.1f} MiB  ({pct}%)", end="", flush=True)
        return chunk

    def __len__(self) -> int:
        return self._total


def load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.exists():
        sys.exit(f"[ERROR] Archivo de configuración no encontrado: {config_path}")

    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)

    # Soporte variable de entorno (más seguro que poner la key en JSON)
    if not cfg.get("api_key"):
        cfg["api_key"] = os.getenv("NEXUS_API_KEY")
    if not cfg.get("api_key"):
        sys.exit("[ERROR] No se encontró api_key ni en config ni en variable NEXUS_API_KEY")

    return cfg


def make_headers(api_key: str) -> dict:
    return {"apikey": api_key, "Content-Type": "application/json"}


def find_latest_zip(folder: str) -> tuple[Path, str]:
    search_path = Path(folder)
    if not search_path.is_dir():
        sys.exit(f"[ERROR] Carpeta no encontrada: {folder}")

    zips = list(search_path.glob("*.zip"))
    if not zips:
        sys.exit(f"[ERROR] No se encontraron archivos .zip en: {folder}")

    latest = max(zips, key=lambda p: p.stat().st_ctime)
    version = latest.stem
    print(f"[INFO] Archivo encontrado : {latest.name}")
    print(f"[INFO] Versión detectada   : {version}")
    return latest, version


def _parse_signed_headers(presigned_url: str) -> list[str]:
    qs = parse_qs(urlparse(presigned_url).query)
    raw = qs.get("X-Amz-SignedHeaders", [""])[0]
    return [h.strip() for h in raw.split(";") if h.strip()]


# ====================== UPLOAD SESSION ======================

def create_upload_session(api_key: str, file_path: Path, debug: bool = False) -> dict:
    size_bytes = file_path.stat().st_size
    filename = file_path.name

    payload = {"size_bytes": size_bytes, "filename": filename}

    if size_bytes >= MULTIPART_THRESHOLD:
        print(f"[INFO] Archivo grande ({size_bytes / 1024 / 1024:.1f} MiB) → multipart")
        endpoint = f"{BASE_URL}/uploads/multipart"
    else:
        print(f"[INFO] Archivo pequeño ({size_bytes / 1024 / 1024:.1f} MiB) → single-part")
        endpoint = f"{BASE_URL}/uploads"

    resp = _post_with_retry(endpoint, make_headers(api_key), payload)
    data = resp.json()["data"]

    if debug:
        print(f"[DEBUG] Upload ID: {data.get('id')}")

    return data


# ====================== SINGLE PART ======================

def upload_single(presigned_url: str, file_path: Path, cfg: dict, debug: bool = False) -> None:
    signed_headers = _parse_signed_headers(presigned_url)

    put_headers: dict[str, str] = {}
    if "content-type" in signed_headers:
        ct = cfg.get("upload_content_type") or "application/octet-stream"
        put_headers["Content-Type"] = ct
    if "content-disposition" in signed_headers:
        cd = cfg.get("upload_content_disposition") or f'attachment; filename="{file_path.name}"'
        put_headers["Content-Disposition"] = cd

    if debug:
        print(f"[DEBUG] PUT headers: {put_headers}")

    print(f"[INFO] Subiendo {file_path.name} ...")
    with open(file_path, "rb") as f:
        progress_reader = _ProgressReader(f, file_path.stat().st_size)
        resp = requests.put(presigned_url, data=progress_reader, headers=put_headers, timeout=900)

    if resp.status_code not in (200, 204):
        sys.exit(f"[ERROR] Single-part upload falló ({resp.status_code}):\n{resp.text}")

    print("\n[INFO] Single-part upload completado.")


# ====================== MULTIPART ======================

def upload_multipart(session_data: dict, file_path: Path) -> None:
    part_size = session_data["part_size_bytes"]
    part_urls = session_data["part_presigned_urls"]
    complete_url = session_data["complete_presigned_url"]
    etags: list[tuple[int, str]] = []

    print(f"[INFO] Subiendo en {len(part_urls)} partes...")
    with open(file_path, "rb") as f:
        for part_number, url in enumerate(part_urls, start=1):
            chunk = f.read(part_size)
            print(f"  Parte {part_number}/{len(part_urls)} ...", end=" ", flush=True)
            resp = requests.put(url, data=chunk, timeout=600)
            if resp.status_code not in (200, 204):
                sys.exit(f"\n[ERROR] Parte {part_number} falló: {resp.status_code}")
            etag = resp.headers.get("ETag", "").strip('"')
            etags.append((part_number, etag))
            print("✅")

    xml_body = _build_complete_xml(etags)
    print("[INFO] Finalizando multipart...")
    resp = requests.post(complete_url, data=xml_body, timeout=60)
    if resp.status_code not in (200, 204):
        sys.exit(f"[ERROR] Complete multipart falló: {resp.status_code}")

    print("[INFO] Multipart upload completado.")


def _build_complete_xml(etags: list[tuple[int, str]]) -> str:
    root = ET.Element("CompleteMultipartUpload")
    for part_number, etag in etags:
        part = ET.SubElement(root, "Part")
        ET.SubElement(part, "PartNumber").text = str(part_number)
        ET.SubElement(part, "ETag").text = etag
    return ET.tostring(root, encoding="unicode")


# ====================== FINALIZACIÓN ======================

def finalise_upload(api_key: str, upload_id: str) -> None:
    print(f"[INFO] Finalizando upload {upload_id} …")
    resp = requests.post(
        f"{BASE_URL}/uploads/{upload_id}/finalise",
        headers=make_headers(api_key),
        timeout=30,
    )
    _raise_for_status(resp, "finalise upload")
    print("[INFO] Upload finalizado.")


def wait_for_available(api_key: str, upload_id: str, timeout: int = 120) -> None:
    print("[INFO] Esperando que el upload esté disponible …")
    deadline = time.time() + timeout
    while time.time() < deadline:
        resp = requests.get(
            f"{BASE_URL}/uploads/{upload_id}",
            headers=make_headers(api_key),
            timeout=15,
        )
        _raise_for_status(resp, "get upload state")
        state = resp.json()["data"]["state"]
        if state == "available":
            print("[INFO] Upload disponible.")
            return
        print(f"  Estado: {state} — esperando …")
        time.sleep(5)
    sys.exit("[ERROR] El upload no estuvo disponible en el tiempo límite.")


# ====================== CREAR ARCHIVO EN NEXUS ======================

def create_mod_file(api_key: str, upload_id: str, cfg: dict) -> dict:
    print("[INFO] Creando nuevo archivo de mod …")
    payload = {
        "upload_id": upload_id,
        "mod_id": cfg["mod_id"],
        "name": cfg["name"],
        "version": cfg["version"],
        "file_category": cfg["file_category"],
    }
    _add_optional(payload, cfg, "description")
    _add_optional(payload, cfg, "primary_mod_manager_download")
    _add_optional(payload, cfg, "allow_mod_manager_download")
    _add_optional(payload, cfg, "show_requirements_pop_up")

    resp = requests.post(f"{BASE_URL}/mod-files", headers=make_headers(api_key), json=payload, timeout=30)
    _raise_for_status(resp, "create mod file")
    return resp.json()["data"]


def create_mod_file_version(api_key: str, upload_id: str, mod_file_id: str, cfg: dict) -> dict:
    print(f"[INFO] Creando nueva versión para mod_file_id {mod_file_id} …")
    payload = {
        "upload_id": upload_id,
        "name": cfg["name"],
        "version": cfg["version"],
        "file_category": cfg["file_category"],
    }
    _add_optional(payload, cfg, "description")
    _add_optional(payload, cfg, "primary_mod_manager_download")
    _add_optional(payload, cfg, "allow_mod_manager_download")
    _add_optional(payload, cfg, "show_requirements_pop_up")
    _add_optional(payload, cfg, "archive_existing_file")
    _add_optional(payload, cfg, "previous_version_id")

    resp = requests.post(
        f"{BASE_URL}/mod-files/{mod_file_id}/versions",
        headers=make_headers(api_key),
        json=payload,
        timeout=30,
    )
    _raise_for_status(resp, "create mod file version")
    return resp.json()["data"]


# ====================== HELPERS ======================

def _add_optional(payload: dict, cfg: dict, key: str) -> None:
    if cfg.get(key) is not None:
        payload[key] = cfg[key]


def _post_with_retry(url: str, headers: dict, payload: dict, max_retries: int = 5) -> requests.Response:
    wait = 60
    for attempt in range(max_retries):
        resp = requests.post(url, headers=headers, json=payload, timeout=30)
        if resp.status_code != 429:
            _raise_for_status(resp, f"POST {url}")
            return resp
        retry_after = max(int(resp.headers.get("Retry-After", 0)), wait)
        print(f"[WARN] Rate limit (429). Esperando {retry_after}s (intento {attempt + 1})…")
        time.sleep(retry_after)
        wait = min(wait * 2, 300)
    sys.exit("[ERROR] Rate limit no resuelto.")


def _raise_for_status(resp: requests.Response, action: str) -> None:
    if not resp.ok:
        try:
            detail = resp.json()
        except Exception:
            detail = resp.text
        sys.exit(f"[ERROR] {action} falló ({resp.status_code}): {detail}")


# ====================== MAIN ======================

def main() -> None:
    parser = argparse.ArgumentParser(description="Subir mod a Nexus Mods - Versión Mejorada")
    parser.add_argument("--config", default=Path(__file__).parent / "upload_config.json",
                        help="Ruta al archivo de configuración")
    parser.add_argument("--zip", type=Path, help="Forzar un archivo .zip específico")
    parser.add_argument("--dry-run", action="store_true", help="Simular sin subir nada")
    parser.add_argument("--debug", action="store_true", help="Modo debug")
    args = parser.parse_args()

    cfg = load_config(str(args.config))

    # Validaciones
    required = ["api_key", "search_folder", "name", "file_category"]
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        sys.exit(f"[ERROR] Faltan campos requeridos: {', '.join(missing)}")

    if cfg["file_category"] not in ("main", "optional", "miscellaneous"):
        sys.exit("[ERROR] file_category debe ser: main, optional o miscellaneous")

    # Buscar archivo
    if args.zip:
        file_path = args.zip
        version = file_path.stem
        print(f"[INFO] Usando archivo forzado: {file_path.name}")
    else:
        file_path, version_from_zip = find_latest_zip(cfg["search_folder"])
        if not cfg.get("version"):
            cfg["version"] = version_from_zip

    if args.dry_run:
        print("[DRY-RUN] Simulación completada. No se subió nada.")
        return

    api_key = cfg["api_key"]
    mod_file_id = cfg.get("mod_file_id")

    # 1. Crear sesión
    session = create_upload_session(api_key, file_path, args.debug)
    upload_id = session.get("id")
    if not upload_id:
        sys.exit("[ERROR] No se recibió upload_id")

    # 2. Subir archivo
    if "part_presigned_urls" in session:
        upload_multipart(session, file_path)
    else:
        upload_single(session["presigned_url"], file_path, cfg, args.debug)

    # 3. Finalizar
    finalise_upload(api_key, upload_id)
    wait_for_available(api_key, upload_id)

    # 4. Crear archivo o versión
    if mod_file_id:
        result = create_mod_file_version(api_key, upload_id, mod_file_id, cfg)
    else:
        result = create_mod_file(api_key, upload_id, cfg)

    print("\n[SUCCESS] ¡Mod subido correctamente a Nexus Mods!")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
