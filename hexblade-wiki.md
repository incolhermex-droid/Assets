![Hexblade Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-banner.svg)

<div align="center">

![Hexblade Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-badge.svg)

</div>

---

> *The Hexblade is not a spellcaster who learned to fight.*
> *It is a weapon that learned to think.*
> *The sword chose you. Now make your enemies regret it.*

---

## What Is the Hexblade?

The Hexblade is a **Warlock subclass** built around a pact with a powerful entity from the Shadowfell — a sentient weapon of immense power. Where other Warlocks blast enemies from range, the Hexblade steps into melee, applies **Hex**, and turns every attack into a layered curse that dismantles whatever stands in front of it.

This rework gives the Hexblade a complete mechanical identity centered on a new resource: **Hexblade Manifest** — a pool of charges scaled directly to your Charisma modifier that changes how Hex works at its core.

This is no longer a subclass that frontloads one good feature. It has a full progression from Level 3 to Level 10 with meaningful choices at every step.

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Hexblade Spells · Hexblade Manifest · Draining Slash · Harrowing Blade · Stymying Mark |
| 6 | Life Stealer · Hungering Hex |
| 10 | Armor of Hexes |

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## Level 3 Features

### ⚔️ Hexblade Spells

Your pact grants you expanded spell access from Level 3. These spells are always prepared and do not count against your Prepared Spells limit.

At Level 3, your expanded list includes: `Hex` · `Shield` · `Arcane Vigor` · `Wrathful Smite`

> **Key change:** Hex can now be cast by consuming a **Hexblade Manifest** charge instead of a spell slot. If you have a Manifest charge available, Hex costs nothing from your Pact Magic.

---

### 🌑 Hexblade Manifest

*The shadow of your patron flows through you, sharpening your curse into something tangible.*

A new action resource that regenerates on rest. The number of charges you receive scales directly with your **Charisma modifier**:

| CHARISMA SCORE | MANIFEST CHARGES |
|---|---|
| 13 or lower | 1 |
| 14–15 | 2 |
| 16–17 | 3 |
| 18–19 | 4 |
| 20–21 | 5 |
| 22–23 | 6 |
| 24+ | 7 |

This makes **Charisma investment directly rewarding** — not just for spell DCs and attack rolls, but for the frequency of your core class loop.

---

### 🗡️ Hexblade's Mark Effects — Choose Your Style

At Level 3, you gain access to three **toggleable passive effects** that all trigger on attack against a **Hexed target**. Only one can be active at a time — this is a combat decision, not a passive bonus.

#### Draining Slash *(Default On)*
When you hit a Hexed target, force a **Constitution saving throw** against your Spell Save DC.
- **Failure:** The target is inflicted with `DRAINING_SLASH` — a debilitating status that reduces their effectiveness.

*Use this when you need to lock down a dangerous enemy quickly. Constitution saves are generally strong, which makes landing this feel earned.*

---

#### Harrowing Blade
When you hit a Hexed target, force a **Wisdom saving throw** against your Spell Save DC.
- **Failure:** The target is inflicted with `HARROWING_BLADE`.
- **Additionally:** If you attack a target that does **not** have Hex on them, you still deal **1d6 necrotic damage** as your blade hungers.

*The backup damage on non-Hexed targets makes Harrowing Blade excellent in multi-target fights where your Hex hasn't reached everyone yet.*

---

#### Stymying Mark
When you hit a Hexed target, apply `STYMYING_MARK` — a status that impairs their ability to act effectively.

*More control-focused than the other two. Use this when battlefield control matters more than raw punishment.*

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## Level 6 Features

### 🩸 Life Stealer

*Your weapon doesn't just wound. It takes.*

When you miss an attack against a **Hexed target**, the miss is not wasted — your blade still draws from the shadow bond.

- Trigger: `OnAttack` where the result is a **miss** and the target has Hex
- Effect: Deal necrotic damage to the target regardless of the miss

> *Missing stopped being a dead turn. The Hex persists. The drain continues.*

---

### 💀 Hungering Hex *(Hidden Passive)*

*When a Hexed enemy falls, the shadow feeds you.*

- Trigger: When a **Hexed character** is reduced to 0 HP by your damage
- Effect: Regain **1d8 + Charisma modifier** hit points instantly

This passive is hidden — it works automatically in the background without cluttering your hotbar. It rewards focusing your Hex on priority targets and finishing them yourself.

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## Level 10 Features

### 🛡️ Armor of Hexes

*The same shadow that curses your enemies now shields you.*

Armor of Hexes introduces a **second Charisma-scaled resource** — the `ArmorOfHexes` pool — and a powerful **reaction interrupt**:

**Interrupt — Armor of Hexes:**
- **Trigger:** You take damage while **you yourself** are under a Hex-adjacent status (`HasHexStatusReverse`)
- **Cost:** 1 ArmorOfHexes charge + your Reaction
- **Effect:** Reduce incoming damage by **2d8 + Charisma modifier**

The number of `ArmorOfHexes` charges scales identically to Hexblade Manifest:

| CHARISMA SCORE | ARMOR CHARGES |
|---|---|
| 13 or lower | 1 |
| 14–15 | 2 |
| 16–17 | 3 |
| 18–19 | 4 |
| 20–21 | 5 |
| 22–23 | 6 |
| 24+ | 7 |

> *At high Charisma, Armor of Hexes can absorb enormous amounts of damage over the course of a long fight. This is a melee subclass that can now survive being in melee.*

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## 🔧 Technical Notes

This rework introduced **16 new files** and **447 lines** of implementation across:

- `ActionResourceDefinitions` — Two new action resources: `HexbladeManifest` and `ArmorOfHexes`
- `Progressions` — Features assigned at Level 3, 6, and 10
- `Passive.stats` — 8 new passives implementing the full feature set
- `Interrupt.stats` — New reaction interrupt for Armor of Hexes
- `SpellLists` — Removed `HexbladesCurse` from Level 2 spell list (replaced by the new system)
- `Status_BOOST.stats` — Status effects for DRAINING_SLASH, HARROWING_BLADE, STYMYING_MARK
- `Warlock.khn` — Script-level integration

> The toggle system (`ToggleGroup: Hexblade_3_DrainingSlash`) ensures only one Mark Effect is active at a time — this is enforced at the engine level, not through UI tricks.

![Hexblade Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/hexblade-divider.svg)

## 🎯 Playstyle Summary

The Hexblade is a **Charisma-first melee striker** with strong curse-based debuffs and surprising survivability at later levels.

**Your combat loop:**
1. Apply **Hex** — consuming a Manifest charge instead of a spell slot
2. Choose your **Mark Effect** toggle based on the fight
3. Attack. Let the curse work.
4. If you miss at Level 6+, **Life Stealer** ensures the turn wasn't wasted
5. When a Hexed target drops, **Hungering Hex** refuels you for the next one
6. At Level 10, use your **Reaction** to absorb punishment and stay in the fight

> *The more Charisma you stack, the more Hex you cast. The more you cast, the more you drain. The more you drain, the longer you survive. Everything feeds everything.*

---

*For other Warlock subclasses, see [[New Classes]].*
*For the full Warlock class breakdown, see [[Classes]].*

← [[Classes]] · [[New Classes]] →
