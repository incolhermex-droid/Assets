# Baldur's Gate 3 - Difficulty Mod  
**Design & Feature Suggestions**

**Structured Reference Document for the Mod Developer**

---

## 1. Overview & Philosophy

This document outlines feature suggestions for a new Baldur's Gate 3 difficulty mod.

Philosophy:

- Difficulty through **tactical intelligence**, and better HP (HP PLUS).
- **Multiplayer stability**.
- Smart scaling based on player count and Act progression: More attacks, and one additional action; for example, if an enemy attacked twice, now they will attack three times and have an additional action, optionally 3 meters more movement and perhaps some extra passive ability.
- Dual compatibility: must work with level cap 12 (vanilla) **and** with Level 20 mods.

---

## 2. Phase 1 — Core Features

These are the essential features.

### 2.1 Dynamic Player-Count Scaling (CORE)
The mod detects the number of players in the session and adjusts grunt enemy count per encounter accordingly.

- 1 player: vanilla count, or slight increase (+1 on select hard fights).
- 2 players: +15–20% enemies per encounter.
- 3–4 players: +30–40% enemies per encounter.
- Scaling applies only to grunt-tier enemies. Minibosses and bosses are never quantity-scaled.
- Applied at scene load. No mid-combat spawning.

### 2.2 Act-by-Act Progression Scaling (CORE)
Difficulty increases progressively across Acts, with values set per encounter — not a global flat multiplier.

- **Act 1**: subtle adjustments.
- **Act 2**: moderate tactical pressure.
- **Act 3**: high difficulty.

### 2.3 Faction-Based AI Profiles (CORE)
Each major faction receives a defined tactical profile that guides how enemies prioritize targets and use their abilities.

**Examples:**
- Goblins: swarm tactics, prefer weakened targets.
- Githyanki: aggressive flanking, focus fire on squishy targets.
- Undead: relentless pressure, prioritize radiant damage dealers.
- Drow: hit-and-hide, poison-focused.
- Absolute cultists: protect casters, self-sacrifice for leaders.

### 2.4 Focus Fire Action (Ketheric-Style) (CORE)
Assign a "Focus Target" (Focus target is a Ketheric Thorm ability; it may be possible to copy and use it on multiple bosses or enemies that have groups of companions.) action to selected enemy commanders and elites. When used, nearby allies switch priority to the designated party member for 1–2 turns.

### 2.5 Expanded Enemy Toolkit (Spells & Passives) (CORE)
Enemies receive additional spells, actions, and passive buffs that are thematically coherent. Prioritize crowd control and debuffs over raw damage.

---

## 3. Phase 2 — Tactical Depth

### 3.1 Combat Role System Within Enemy Groups
When scaling adds enemies, the system prioritizes filling defined roles (Tank, DPS, Support, Control) before adding generic grunts: For example, in a group of enemies, one might have more health, another has melee attack passives, another has save passives and spell difficulty class, etc

### 3.2 Enemy Reaction to Player Concentration
Improved AI will recognize and prioritize breaking concentration on spells.

### 3.3 XP Normalization
Reduce XP gained from extra enemies to prevent over-leveling (especially important for vanilla level 12 playthroughs).

### 3.4 Narrative Combat Protection
Key story bosses (Raphael, Cazador, Ketheric, Orin, etc.) hp scaling, more attacks (effect of the speed potion or simply extra attacks), Reduced damage on the first turn, If it casts spells, it can cast 2 instead of 1.

### 3.5 Proportional Loot Adjustment
Harder encounters drop extra consumables (potions, scrolls, arrows) to compensate for increased resource drain.

---

## 4. Phase 3 — New Content (Future)

### 4.1 Minibosses with Unique Mechanics
One unique miniboss per major zone with distinctive mechanics (phase transitions, auras, priority summons, etc.).

### 4.2 New Optional Encounters
Add optional, lore-appropriate encounters in underused transition zones.

### 4.3 Recurring Scaled Enemy Across Acts
A named enemy (or enemy type) that returns in all three Acts, becoming progressively stronger and culminating as a miniboss in Act 3.

---

## 5. High-Impact / Low-Effort Suggestions (Quick Wins)

### 5.1 Boss Turn-1 Resistance Phase
Major bosses take only 25% damage on their first turn (expires at start of turn 2). Prevents round-1 nova cheese.

### 5.2 Pack Tactics Passive on Grunts
Give Pack Tactics to goblin, kobold, and similar grunt enemies.

### 5.3 Pre-Cast Buffs on Caster Enemies
Enemy casters enter combat with Mage Armor, Bless, Barkskin, etc. already active (This can be done by giving these enemies permanent conditions).

### 5.4 Sentinel Passive on Front-Line Elites
Gives opportunity attacks that reduce speed to 0 even on disengage.

### 5.5 Aura-Based Buff for Enemy Leaders
Commanders emit a small aura granting +1 to attacks or temporary HP to nearby allies.

### 5.6 Level 20 Mod Compatibility Flag
Automatic detection of Level 20 mods to adjust scaling and XP behavior accordingly (This may be difficult, I don't know if it will be possible).

---

## 6. Optional: Host Toggle

Implement a toggle (accessible by the host) with two modes:

- **Mode A (Default)**: Full mod — player-count scaling + all features.
- **Mode B (Quality Only)**: No quantity scaling. Only AI improvements, passives, pre-cast buffs, and boss mechanics.

---

## 7. Summary Table

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
