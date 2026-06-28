# 🎨 DnD 5.5e All-in-One BEYOND — Documentation & Visual Identity

> A complete documentation system, visual identity, and toolchain built from scratch for the [DnD 5.5e All-in-One BEYOND](https://mod.io/g/baldursgate3/m/dnd55e) mod for Baldur's Gate 3 — one of the most comprehensive ruleset overhaul mods on the platform.

---

## 👤 About This Repository

This repository is the original source of the **wiki structure, technical documentation, visual identity, and upload tooling** for the DnD 5.5e All-in-One BEYOND mod, authored and maintained by **[@incolhermex-droid](https://github.com/incolhermex-droid)** — Social Communicator & Journalist, and the mod's official Spanish / Latin American Spanish localizer, as credited on [mod.io](https://mod.io/g/baldursgate3/m/dnd55e).

What started as a translation role grew into a full documentation initiative: reading the mod's actual commit history and source code, translating technical implementation details into clear player-facing explanations, designing a complete SVG visual system to support it, and building the description content used across mod.io, NexusMods, and the in-game mod manager — all without the mod's author requesting it. Every wiki page, every banner, and every line of description copy was built page by page, commit by commit, over **100+ commits** of sustained, independent work.

This repo is the permanent, timestamped record of that work.

---

## 📚 What's Inside

| CATEGORY | CONTENTS |
|---|---|
| **Wiki Pages** | Full `.md` breakdowns for every documented class and subclass |
| **Banners, Badges & Dividers** | 25+ custom SVG sets, one per class/subclass, each with a unique color identity |
| **Legacy Description Banners** | 13 numbered section-divider SVGs (`banners/`) used in the original mod.io rich-text description |
| **Mod Descriptions** | Full mod.io/Nexus description and two versions of the plain-text in-game mod manager description |
| **Class Suggestion Docs** | Standalone proposal `.md` files for Gunslinger and Illrigger documentation, written before they had dedicated wiki pages |
| **Changelog** | A full standalone changelog tracking the mod's progress, maintained in a [separate repository](https://github.com/incolhermex-droid/Changelong-Progress-.md) |
| **Upload Tooling** | A custom Python script (`improved_upload_mod.py`) and config sample for automating asset/description uploads |

Every wiki `.md` file in this repository was written by directly reading the mod's GitHub commit diffs — actual `.stats`, `.khn`, and localization file changes — and translating that implementation into structured, readable documentation with technical accuracy notes for advanced users.

---

## 📁 Repository Structure

```
Assets/
├── banners/                              ← Legacy numbered banners (01–13) for the original
│                                            mod.io rich-text description
│
├── [class/subclass]-banner.svg           ← Wiki page banner
├── [class/subclass]-badge.svg            ← Matching badge
├── [class/subclass]-divider.svg          ← Matching section divider
├── [class/subclass]-wiki.md              ← Full wiki page content
│
├── README_Class_Gunslinger.md            ← Standalone class proposal (pre-wiki)
├── README_Class_Illrigger.md             ← Standalone class proposal (pre-wiki)
├── Suggestion for New Mod.md             ← Feature suggestion document
│
├── dnd55e_FINAL(Mod.io and Nexus).md     ← Full rich-text mod.io / NexusMods description
├── dnd55e_INGAME.txt                     ← Plain-text in-game description (v1)
├── dnd55e_INGAME v2.txt                  ← Plain-text in-game description (v2, revised)
│
├── improved_upload_mod.py                ← Custom upload automation script
├── Improved_upload_config.json.sample    ← Config template for the upload script
│
├── badges.svg / banner.svg / banner1.svg ← Core shared assets (mod.io header, badge row)
├── divider.svg                           ← Shared generic divider
│
└── README.md
```

---

## 🧩 Classes & Subclasses Documented

<details>
<summary><strong>📋 Click to expand the full documentation index</strong></summary>

### Cleric
- General class breakdown
- Apocalypse Domain · Astral Domain *(original, mod-exclusive)* · Grave Domain · Knowledge Domain · Life Domain · Light Domain · Trickery Domain · War Domain

### Warlock
- General class breakdown
- Archfey Patron · Celestial Patron · Fiend Patron · Great Old One Patron · Hexblade Patron · Undead Patron
- Eldritch Invocations (full system breakdown, 20+ invocations)

### Monk
- General class breakdown
- Way of the Open Hand · Way of Mercy · Way of the Four Elements · Way of the Kensei

### Gunslinger *(original class)*
- General class breakdown
- High Roller · Spellslinger · White Hat

### Illrigger *(original class)*
- Standalone class proposal documentation

### Other Systems
- Creatures (Monster Manual 2024 conversions)

</details>

Each wiki page includes: feature breakdowns by level, exact mechanical formulas pulled from source code, technical implementation notes, and a playstyle summary written for players evaluating the build.

---

## 🔗 Usage

All banners are standalone SVG files — lightweight, scalable, no external dependencies.

```markdown
![banner name](https://raw.githubusercontent.com/incolhermex-droid/Assets/main/[filename].svg)
```

> Replace `main` with a specific commit hash for a permanent permalink to a frozen version.

---

## 🎨 Visual Identity System

Every class and subclass has a distinct color identity, designed to be immediately recognizable while maintaining a consistent layout structure (ornamental corners, gradient borders, stat rows, and italicized taglines) across the entire collection:

| THEME | EXAMPLES |
|---|---|
| Divine gold | Cleric, Light Domain |
| Crimson/blood | War Domain, Apocalypse Domain |
| Void purple | Warlock, Hexblade Patron, Eldritch Invocations |
| Cosmic green | Great Old One Patron |
| Corpse green | Undead Patron |
| Fey emerald | Archfey Patron |
| Hellfire orange | Fiend Patron |
| Steel/frost | Way of the Kensei, White Hat |
| Gold/casino | High Roller |
| Arcane violet | Spellslinger |

---

## 🔧 Maintenance Notes

- Banners are SVG — no quality loss at any resolution.
- Each wiki `.md` is self-contained and cross-links to related pages.
- `improved_upload_mod.py` automates pushing updated assets and description files — see `Improved_upload_config.json.sample` for setup.
- To update a banner: replace the `.svg` file directly; GitHub raw links update automatically.

---

## 🔗 Related Links

- **Mod page:** [mod.io/g/baldursgate3/m/dnd55e](https://mod.io/g/baldursgate3/m/dnd55e)
- **Mod repository:** [github.com/Yoonmoonsik/dnd55e](https://github.com/Yoonmoonsik/dnd55e)
- **Original mod author:** [Yoonmoonsik](https://github.com/Yoonmoonsik)
- **Changelog repository:** [Changelong-Progress-.md](https://github.com/incolhermex-droid/Changelong-Progress-.md)

---

## ✍️ Author

Documentation, wiki structure, visual design, and upload tooling by **[@incolhermex-droid](https://github.com/incolhermex-droid)** — Social Communicator & Journalist, official Spanish / Latin American Spanish localizer for DnD 5.5e All-in-One BEYOND (credited on [mod.io](https://mod.io/g/baldursgate3/m/dnd55e)).

*All commit history in this repository reflects the original authorship and timeline of this work.*
