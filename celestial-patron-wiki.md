![Celestial Patron Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-banner.svg)

<div align="center">

![Celestial Patron Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-badge.svg)

</div>

---

> *Most Warlocks make deals with things that dwell in darkness.*
> *You made yours with something that burns.*
> *Your patron shines. You are what it shines through.*

---

## What Is the Celestial Patron?

The Celestial Patron is a **Warlock subclass** built around a pact with a powerful being from the Upper Planes — a solar, a ki-rin, a unicorn, or another radiant entity. Where other Warlocks wield darkness, necrotic energy, or eldritch horror, the Celestial Patron Warlock channels **healing light and radiant power**.

This is the only Warlock subclass in the mod with a dedicated healing resource: **Healing Light** — a pool of charges that scales with your Warlock level and lets you heal allies or yourself as a Bonus Action. At Level 6, **Radiant Soul** adds your Charisma modifier to radiant damage. At Level 10, **Celestial Resilience** applies a protective status to allies around you once per Short Rest.

The Celestial Patron is the answer to "can a Warlock support a party?" The answer is yes — without sacrificing the class's identity.

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Celestial Spells · Healing Light (4 charges) |
| 4 | +1 Healing Light charge |
| 5 | Celestial Spells (expanded) · +1 Healing Light charge |
| 6 | Radiant Soul · +1 Healing Light charge |
| 7 | Celestial Spells (expanded) · +1 Healing Light charge |
| 8 | +1 Healing Light charge |
| 9 | Celestial Spells (expanded) · +1 Healing Light charge |
| 10 | Celestial Resilience · +1 Healing Light charge |
| 11 | +1 Healing Light charge |
| 12 | +1 Healing Light charge |

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## Level 3 Features

### 📜 Celestial Spells

Your Patron grants an expanding spell list that is **always prepared** and doesn't count against your Pact Magic limit:

| WARLOCK LEVEL | SPELLS ADDED |
|---|---|
| 3 | Light · Sacred Flame · Cure Wounds · Guiding Bolt · Aid · Lesser Restoration |
| 5 | Daylight · Revivify |
| 7 | Guardian of Faith · Wall of Fire |
| 9 | Greater Restoration |

> **7 spells total** — a healing and radiant toolkit that no other Warlock Patron provides. **Revivify** at Level 5 means you always have resurrection available. **Greater Restoration** at Level 9 is one of the most powerful condition-clearing spells in the game.

---

### 💛 Healing Light

*Your patron's radiance flows through you. Spend it wisely.*

A new action resource — `HealingLight` — that starts at **4 charges** at Level 3 and gains **1 additional charge per Warlock level** thereafter, reaching a maximum of **12 charges** at Level 12.

As a **Bonus Action**, spend **1+ Healing Light charges** to restore HP to a creature you can see within 60 feet:
- Each charge restores **1d6 HP**
- You can spend multiple charges in one use for more healing
- You can use it on yourself

```
ActionResource: HealingLight
ReplenishType: Rest
Starting charges: 4 (Level 3) +1 per level from Level 4
```

> *Healing Light is the most efficient healing resource in the mod relative to action cost — it costs a Bonus Action, not an Action, and it scales continuously with your level. At Level 12, you have 12d6 of healing available per rest, distributed however you choose.*
>
> *The resource panel shows your current charges, making triage decisions visible and explicit.*

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## Level 6 Features

### ☀️ Radiant Soul

*You've spent enough time in your patron's light that some of it stuck.*

`Celestial_6_RadiantSoul` — a passive that adds your **Charisma modifier** to the damage of:
- Radiant spells
- Fire spells
- Healing spells that restore HP

> *Radiant Soul stacks Charisma into every radiant spell you cast. Sacred Flame, Guiding Bolt, Wall of Fire — all gain your Charisma modifier as bonus damage. Since Charisma is already your spellcasting ability and primary stat, this is pure additive value with no extra investment required.*

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## Level 10 Features

### 🌟 Celestial Resilience

*Your patron wraps your allies in starlight. It doesn't ask permission.*

`Celestial_10_CelestialResilience` — usable once per **Short Rest** as an Action. Applies `CELESTIAL_RESILIENCE` status to all allies within **9 meters**.

```
Cooldown: OncePerShortRest
AreaRadius: 9
TargetConditions: Ally() and not Dead()
SpellProperties: ApplyStatus(CELESTIAL_RESILIENCE,100,-1)
```

> *Celestial Resilience is a protective AoE buff that covers your entire nearby party in one action. The status persists until removed — it is not a time-limited effect. Short Rest replenishment means you can use it once between encounters, making it reliable pre-combat preparation for every fight.*

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## 🔧 Technical Notes

This commit introduced **14 files** and **439 lines** of implementation:

- `ActionResourceDefinitions` — New resource: `HealingLight` (`NameFS: HealingLight`, `ReplenishType: Rest`, `ShowOnActionResourcePanel: True`)
- `ClassDescriptions` — UUID `1e077f6b` registered as `Celestial` subclass, Charisma primary/spellcasting, `LearningStrategy: AllChildren`
- `SpellLists` — 4 spell lists (SLevel 2–5) with Celestial spells at Levels 3, 5, 7, 9
- `Progressions` — Full progression Levels 3–12 with `HealingLight` charge increments at every level. UUID `1e077f6b` added to Warlock Level 2 SubClasses list
- `Target.stats` — `CelestialResilience` spell implementation (AoE Shout-type, `OncePerShortRest`)
- `Passive.stats` — `Celestial_3_CelestialSpells` · `Celestial_3_HealingLight` · `Celestial_6_RadiantSoul` · `Celestial_10_CelestialResilience`
- `Status_BOOST.stats` — `CELESTIAL_RESILIENCE` status effect definition
- `Warlock.khn` — Script integration for Healing Light usage logic
- `english.xml` — Complete localization

Key implementation detail — **Healing Light charge scaling**:
```
Level 3:  ActionResource(HealingLight,4,0)
Level 4:  ActionResource(HealingLight,1,0)
Level 5:  ActionResource(HealingLight,1,0)
...continuing +1 per level through Level 12
```
Each level adds exactly 1 charge via a separate `Boosts` entry — clean and explicit scaling that makes the resource predictable at every level.

![Celestial Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/celestial-patron-divider.svg)

## 🎯 Playstyle Summary

The Celestial Patron is a **radiant support Warlock** that brings healing and protective utility without abandoning offensive capability.

**Your combat identity:**
1. **Healing Light** — every Short Rest you have a pool of Bonus Action heals; use them when allies drop, not preemptively
2. **Sacred Flame + Guiding Bolt** — always prepared radiant damage options boosted by Radiant Soul at Level 6
3. **Eldritch Blast** — your primary damage cantrip, enhanced by Invocations as normal
4. **Revivify** — always prepared from Level 5; no ally needs to stay down
5. **Celestial Resilience** — pre-combat buff to your whole party, once per Short Rest
6. **Greater Restoration** — always prepared at Level 9; the most powerful condition-cleanse in the game

> *The Celestial Patron doesn't ask you to choose between dealing damage and supporting allies.*
> *It gives you both — and a Bonus Action economy to use them at the same time.*
> *Your patron is a being of light. You fight like it.*

---

*For other Warlock Patrons, see [[Warlock]].*
*For the full class list, see [[Classes]].*

← [[Warlock]] · [[Archfey Patron]] →
