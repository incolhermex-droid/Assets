# Baldur's Gate 3 - Difficulty Mod  
**Design & Feature Suggestions**

**Structured Reference Document for the Mod Developer**

---

## 1. Overview & Philosophy

This document outlines feature suggestions for a new Baldur's Gate 3 difficulty mod.

The goal is **NOT** to replicate existing mods such as Relia's suite (Extra Encounters and Minibosses, More Enemies in Basic Fights, Enemies Reworked). While those mods are well-made, they cause multiplayer crashes — silent desktop drops with no error message — making them unviable for co-op sessions.

This mod follows a different, independent philosophy:

- Difficulty through **tactical intelligence**, not inflated HP or raw quantity.
- **Multiplayer stability** as a non-negotiable design constraint.
- Smart scaling based on player count and Act progression.
- Dual compatibility: must work with level cap 12 (vanilla) **and** with Level 20 mods.

---

## 2. Core Design Constraint: Multiplayer Stability

This is the single most important technical requirement. The mod must be designed from the ground up to avoid the crash pattern seen in other mods.

### Known crash triggers to avoid:
- Modifying `CombatGroupID` after a character has already died in the current combat.
- Adding or removing enemies mid-combat via script (all enemy placement must happen before combat initiation).
- Duplicate NPC spawns caused by conflicting faction tags.
- Changes to enemy stats or spells that fire as passive triggers during another player's turn in multiplayer.

### Recommended practices:
- All encounter modifications (extra enemies, stat changes, passive additions) are set at scene load, not at combat start.
- Test every encounter change in both 2-player and 4-player sessions before release.
- Document which game files each change touches and whether the change is safe in a multiplayer context.

---

## 3. Phase 1 — Core Features

These are the essential features the mod cannot ship without.

### 3.1 Dynamic Player-Count Scaling (CORE)
The mod detects the number of players in the session and adjusts grunt enemy count per encounter accordingly.

- 1 player: vanilla count, or slight increase (+1 on select hard fights).
- 2 players: +15–20% enemies per encounter.
- 3–4 players: +30–40% enemies per encounter.
- Scaling applies only to grunt-tier enemies. Minibosses and bosses are never quantity-scaled.
- Applied at scene load. No mid-combat spawning.

### 3.2 Act-by-Act Progression Scaling (CORE)
Difficulty increases progressively across Acts, with values set per encounter — not a global flat multiplier.

- **Act 1**: subtle adjustments.
- **Act 2**: moderate tactical pressure.
- **Act 3**: high difficulty.

### 3.3 Faction-Based AI Profiles (CORE)
Each major faction receives a defined tactical profile that guides how enemies prioritize targets and use their abilities.

**Examples:**
- Goblins: swarm tactics, prefer weakened targets.
- Githyanki: aggressive flanking, focus fire on squishy targets.
- Undead: relentless pressure, prioritize radiant damage dealers.
- Drow: hit-and-hide, poison-focused.
- Absolute cultists: protect casters, self-sacrifice for leaders.

### 3.4 Focus Fire Action (Ketheric-Style) (CORE)
Assign a "Focus Target" action to selected enemy commanders and elites. When used, nearby allies switch priority to the designated party member for 1–2 turns.

### 3.5 Expanded Enemy Toolkit (Spells & Passives) (CORE)
Enemies receive additional spells, actions, and passive buffs that are thematically coherent. Prioritize crowd control and debuffs over raw damage.

---

## 4. Phase 2 — Tactical Depth

### 4.1 Combat Role System Within Enemy Groups
When scaling adds enemies, the system prioritizes filling defined roles (Tank, DPS, Support, Control) before adding generic grunts.

### 4.2 Enemy Reaction to Player Concentration
Improved AI will recognize and prioritize breaking concentration on spells.

### 4.3 XP Normalization
Reduce XP gained from extra enemies to prevent over-leveling (especially important for vanilla level 12 playthroughs).

### 4.4 Narrative Combat Protection
Key story bosses (Raphael, Cazador, Ketheric, Orin, etc.) receive no quantity scaling — only quality improvements (AI + abilities).

### 4.5 Proportional Loot Adjustment
Harder encounters drop extra consumables (potions, scrolls, arrows) to compensate for increased resource drain.

---

## 5. Phase 3 — New Content (Future)

### 5.1 Minibosses with Unique Mechanics
One unique miniboss per major zone with distinctive mechanics (phase transitions, auras, priority summons, etc.).

### 5.2 New Optional Encounters
Add optional, lore-appropriate encounters in underused transition zones.

### 5.3 Recurring Scaled Enemy Across Acts
A named enemy (or enemy type) that returns in all three Acts, becoming progressively stronger and culminating as a miniboss in Act 3.

---

## 6. High-Impact / Low-Effort Suggestions (Quick Wins)

### 6.1 Boss Turn-1 Resistance Phase
Major bosses take only 25% damage on their first turn (expires at start of turn 2). Prevents round-1 nova cheese.

### 6.2 Pack Tactics Passive on Grunts
Give Pack Tactics to goblin, kobold, and similar grunt enemies.

### 6.3 Pre-Cast Buffs on Caster Enemies
Enemy casters enter combat with Mage Armor, Bless, Barkskin, etc. already active.

### 6.4 Sentinel Passive on Front-Line Elites
Gives opportunity attacks that reduce speed to 0 even on disengage.

### 6.5 Aura-Based Buff for Enemy Leaders
Commanders emit a small aura granting +1 to attacks or temporary HP to nearby allies.

### 6.6 Level 20 Mod Compatibility Flag
Automatic detection of Level 20 mods to adjust scaling and XP behavior accordingly.

---

## 7. Optional: Host Toggle

Implement a toggle (accessible by the host) with two modes:

- **Mode A (Default)**: Full mod — player-count scaling + all features.
- **Mode B (Quality Only)**: No quantity scaling. Only AI improvements, passives, pre-cast buffs, and boss mechanics.

---

## 8. Summary Table

| Feature                          | Phase              | Complexity  | Impact      |
|----------------------------------|--------------------|-------------|-------------|
| Player-count scaling             | Phase 1 — Core     | Medium      | Very High   |
| Act-by-Act progression           | Phase 1 — Core     | Medium      | Very High   |
| Faction AI profiles              | Phase 1 — Core     | Medium      | High        |
| Focus Fire action                | Phase 1 — Core     | Low         | Very High   |
| Expanded enemy toolkit           | Phase 1 — Core     | Medium      | High        |
| Combat role system               | Phase 2            | Medium      | High        |
| Concentration targeting AI       | Phase 2            | Low         | High        |
| XP normalization                 | Phase 2            | Low         | Medium      |
| Narrative fight protection       | Phase 2            | Low         | High        |
| Loot adjustment                  | Phase 2            | Low         | Medium      |
| Boss Turn-1 Resistance           | Quick Win          | Very Low    | Very High   |
| Pack Tactics on grunts           | Quick Win          | Very Low    | High        |
| Pre-cast buffs on casters        | Quick Win          | Very Low    | High        |
| Sentinel on elites               | Quick Win          | Very Low    | High        |
| Leader aura buff                 | Quick Win          | Low         | High        |
| Level 20 compatibility flag      | Quick Win          | Low         | High        |
| Minibosses w/ unique mechanics   | Phase 3 — Future   | High        | Very High   |
| New optional encounters          | Phase 3 — Future   | High        | High        |
| Recurring scaled enemy           | Phase 3 — Future   | High        | High        |

---

**End of suggestions document.**

Questions or clarifications can be directed to the requester.
