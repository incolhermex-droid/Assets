![Astral Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-banner.svg)

<div align="center">

![Astral Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-badge.svg)

</div>

---

> *Your deity does not dwell in temples or forests or seas.*
> *They dwell between things — in the space that separates one place from another.*
> *Space is not an obstacle. It's a resource. You just learned how to spend it.*

---

## What Is the Astral Domain?

The Astral Domain is a **completely original Cleric subclass** — not found in any official D&D sourcebook. It was designed from scratch for this mod, built around one concept: **control of space itself**. Where other Domains give you fire, death, trickery, or war, the Astral Domain gives you the ability to reshape the battlefield through force, displacement, and planar manipulation.

At Level 3 you gain **Create Void** — a Channel Divinity that deals force damage and pushes enemies with gravitational force — and **Planar Reach**, a dedicated action resource for spatial effects. At Level 6, **Spatial Exchange** lets you swap positions with any character on the battlefield as a Bonus Action.

This is the most **tactically unique** Cleric subclass in the mod, and one of the few features in the game built entirely around repositioning rather than damage or healing.

![Astral Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Astral Domain Spells · Create Void · Planar Reach |
| 5 | Astral Domain Spells (expanded) |
| 6 | Spatial Exchange |
| 7 | Astral Domain Spells (expanded) |
| 9 | Astral Domain Spells (expanded) |

![Astral Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-divider.svg)

## Level 3 Features

### 📜 Astral Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Blur · Guiding Bolt · Invisibility · Longstrider · Starry Wisp |
| 5 | Blink · Slow |
| 7 | Banishment · Dimension Door |
| 9 | Dispel Evil and Good · Wall of Stone |

> **9 spells total** — a toolkit built around speed, evasion, and spatial control. **Blink** at Level 5 lets you phase in and out of the Ethereal Plane. **Slow** at the same level reduces up to six creatures' speed, AC, and actions. **Dimension Door** at Level 7 lets you teleport yourself and one ally up to 500 feet. **Wall of Stone** at Level 9 creates a permanent barrier that reshapes the physical environment.

---

### 🌀 Create Void — Channel Divinity

*You open a hole in reality. Everything near it gets pulled in.*

Your Channel Divinity option at Level 3. As a Bonus Action, you create a gravitational void at a target point within range.

```
UseCosts: BonusActionPoint:1;ChannelDivinity:1
AreaRadius: 5 meters
SpellRoll: not SavingThrow(Ability.Dexterity, SourceSpellDC())
DamageType: Force
```

**On a failed Dexterity save:**
- Deal `1d8 + Cleric Level` Force damage
- Apply `Force(-4, TargetToEntity, Neutral)` — a directional push toward the void's center

**On a successful save:**
- Deal `(1d8 + Cleric Level) / 2` Force damage
- No push effect

> *Create Void scales with your Cleric level — at Level 10, every failed save deals 1d8+10 Force damage plus a knockback effect. In a corridor or near a ledge, the push effect is more valuable than the damage. This is a battlefield control tool first, a damage tool second.*

The void uses `Spiritual Weapon` sound and animation assets — the effect is visually dramatic without requiring custom assets.

---

### 🔮 Planar Reach

*The astral plane bends to your will. It takes practice.*

A new action resource — `PlanarReach` — that replenishes on rest. This resource powers the Astral Domain's spatial manipulation features and serves as the mechanical foundation for the Domain's identity.

Planar Reach charges appear on your action resource panel, giving you visible feedback on how many spatial manipulations you have available.

> *Planar Reach is the engine behind the Astral Domain. Every spatial feature costs it. Managing your charges — when to use Create Void, when to hold Planar Reach for Spatial Exchange — is the core decision space of this subclass.*

![Astral Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-divider.svg)

## Level 6 Features

### ⚡ Spatial Exchange

*Here. There. Instantly. The rules of space don't apply to you.*

The defining Level 6 feature of the Astral Domain. As a Bonus Action, you swap positions with **any character** within range — ally or enemy.

```
Using: TrickstersTransposition (base class)
TargetConditions: Character()
UseCosts: BonusActionPoint:1;ChannelDivinity:1
CastSound: Spell_Cast_Utility_MistyStep_L1to3
SpellFlags: HasVerbalComponent;IsSpell;HasHighGroundRangeExtension;RangeIgnoreVerticalThreshold
```

Key differences from `Trickster's Transposition` (the Trickery Domain's version):
- **Target:** Any `Character()` — ally or enemy, not just your duplicate
- **Range:** Extended with `RangeIgnoreVerticalThreshold` — works across elevation differences
- **Flags:** Includes `HasVerbalComponent` and `IsSpell` — it is a real spell, not a passive ability

> *Spatial Exchange is one of the most powerful repositioning tools in the mod. Swap a downed ally out of danger. Swap an enemy out of cover and into the open. Swap yourself into a better flanking position. Swap the enemy's caster into melee range of your Fighter.*
>
> *The applications are limited only by your imagination and the number of ChannelDivinity charges you have.*

![Astral Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **16 files** and **461 lines** of implementation (with 24 lines modified):

- `ActionResourceDefinitions.tbl` — New resource: `PlanarReach` (UUID `9a8fa384`, replenish on Rest, shown on panel)
- `ClassDescriptions.tbl` — Full subclass registration: UUID `0a7ae8c2`, `AstralDomain`, Wisdom primary/spellcasting, `MustPrepareSpells: True`
- `SpellLists.tbl` — 4 new spell lists: SLevel 2 (Level 3), SLevel 3 (Level 5), SLevel 4 (Level 7), SLevel 5 (Level 9)
- `Progressions.tbl` — Full progression Levels 3, 5, 6, 7, 9. UUID `0a7ae8c2` added to **front** of Cleric Level 2 SubClasses list
- `Target.stats` — 2 new spells: `CreateVoid` (full implementation) · `SpatialExchange` (extends TrickstersTransposition)
- `Passive.stats` — 4 new passives: `Astral_3_AstralDomainSpells` · `Astral_3_CreateVoid` · `Astral_3_PlanarReach` · `Astral_3_PlanarReach_Resource`
- `english.xml` — Complete localization
- `README_Class_Cleric.MD` — Updated with Astral Domain documentation

Key implementation detail — **Create Void damage formula**:
```
SpellSuccess: DealDamage(1d8+ClassLevel(Cleric),Force);
              Force(-4, TargetToEntity, Neutral, false, true);
SpellFail: DealDamage((1d8+ClassLevel(Cleric)/2),Force);
```
The `Force(-4, TargetToEntity, Neutral)` call applies directional push toward the void's center point — negative value means pull/push inward rather than outward. `false, true` parameters control whether the push ignores terrain and whether it's applied in world space.

![Astral Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/astral-domain-divider.svg)

## 🎯 Playstyle Summary

The Astral Domain is a **spatial controller** that treats the battlefield as a resource to be spent rather than a static environment to fight in.

**Your combat identity:**
1. **Create Void** — open combat by pulling clustered enemies toward a central point, dealing force damage and disrupting their positioning
2. **Astral Domain spells** — Blur for personal defense, Slow for multi-target speed reduction, Blink for tactical evasion
3. **Spatial Exchange** at Level 6 — the most flexible repositioning tool in the mod; use it every time a swap would change the fight's dynamics
4. **Dimension Door** at Level 7 — always prepared; extract yourself and an ally from any situation instantly
5. **Wall of Stone** at Level 9 — permanently reshape the physical battlefield; create corridors, seal exits, split enemy formations

> *The Astral Domain doesn't ask: "How do I deal more damage?"*
> *It asks: "Where should everyone be standing right now?"*
> *And then it moves them there.*

---

> ⚠️ **Note:** The Astral Domain is an **original creation** exclusive to this mod — it does not exist in any official D&D sourcebook. It was designed and implemented by Yoonmoonsik as a unique addition to the Cleric class.

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[Apocalypse Domain]] →
