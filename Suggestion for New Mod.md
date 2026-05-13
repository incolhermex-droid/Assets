# Baldur's Gate 3 - Difficulty Mod  
**Design & Feature Suggestions**

**Documento de referencia estructurado para el desarrollador del mod**

---

## 1. Overview & Philosophy

Este documento detalla las sugerencias de características para un nuevo mod de dificultad de Baldur's Gate 3.

**El objetivo NO es** replicar mods existentes como la suite de Relia (Extra Encounters, More Enemies, Enemies Reworked). Aunque están bien hechos, causan crashes frecuentes en multijugador (caídas silenciosas al escritorio).

Esta propuesta sigue una filosofía diferente e independiente:

- Dificultad a través de **inteligencia táctica**, no solo más HP o más enemigos.
- **Estabilidad en multijugador** como requisito innegociable.
- Escalado inteligente según número de jugadores y progresión por Acto.
- Compatibilidad dual: debe funcionar tanto con el nivel máximo 12 (vanilla) como con mods de Level 20.

---

## 2. Core Design Constraint: Multiplayer Stability

Esta es la restricción técnica más importante.

### Triggers de crashes conocidos a evitar:
- Modificar `CombatGroupID` después de que un personaje haya muerto.
- Añadir o remover enemigos durante el combate (todo debe configurarse antes de iniciar combate).
- Spawns duplicados por tags de facción conflictivos.
- Cambios que se activen como triggers pasivos durante el turno de otro jugador.

### Buenas prácticas recomendadas:
- Todas las modificaciones de encuentros se aplican al cargar la escena.
- Probar **siempre** cada cambio en sesiones de 2 y 4 jugadores.
- Documentar qué archivos del juego toca cada cambio y su seguridad en multijugador.

---

## 3. Phase 1 — Core Features

### 3.1 Dynamic Player-Count Scaling (CORE)
El mod detecta el número de jugadores y ajusta la cantidad de enemigos grunt por encuentro.

- 1 jugador: conteo vanilla o ligero aumento.
- 2 jugadores: +15–20% enemigos.
- 3–4 jugadores: +30–40% enemigos.
- Solo aplica a enemigos grunt. **Nunca** a minibosses ni bosses.
- Se aplica al cargar la escena (sin spawning en combate).

### 3.2 Act-by-Act Progression Scaling (CORE)
La dificultad aumenta progresivamente por Acto con perfiles específicos.

- **Act 1**: ajustes sutiles.
- **Act 2**: presión táctica moderada.
- **Act 3**: alta dificultad.

### 3.3 Faction-Based AI Profiles (CORE)
Cada facción mayor tiene un perfil táctico definido.

### 3.4 Focus Fire Action (Ketheric-Style) (CORE)
Comandantes y élites pueden marcar un objetivo prioritario para que sus aliados lo ataquen durante 1-2 turnos.

### 3.5 Expanded Enemy Toolkit (CORE)
Añadir hechizos y pasivas coherentes temáticamente a los enemigos.

---

## 4. Phase 2 — Tactical Depth

- 4.1 Combat Role System (Tank, DPS, Support, Control)
- 4.2 Enemy Reaction to Player Concentration
- 4.3 XP Normalization
- 4.4 Narrative Combat Protection (no quantity scaling en bosses importantes)
- 4.5 Proportional Loot Adjustment

---

## 5. Phase 3 — New Content (Future)

- 5.1 Minibosses with Unique Mechanics
- 5.2 New Optional Encounters in Underused Zones
- 5.3 Recurring Scaled Enemy Across Acts

---

## 6. High-Impact / Low-Effort Suggestions (Quick Wins)

- 6.1 Boss Turn-1 Resistance Phase
- 6.2 Pack Tactics Passive on Grunts
- 6.3 Pre-Cast Buffs on Caster Enemies
- 6.4 Sentinel Passive on Front-Line Elites
- 6.5 Aura-Based Buff for Enemy Leaders
- 6.6 Level 20 Mod Compatibility Flag

---

## 7. Optional: Host Toggle

Permitir un modo "Quality Only" (solo mejoras de IA y calidad, sin aumento de cantidad de enemigos).

---

## 8. Summary Table

*(Aquí iría la tabla de prioridades con columnas: Feature, Phase, Complexity, Impact)*

---

**End of suggestions document.**

Cualquier duda o aclaración puede dirigirse al solicitante.