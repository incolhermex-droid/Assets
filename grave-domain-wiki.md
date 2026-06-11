![Grave Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-banner.svg)

<div align="center">

![Grave Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-badge.svg)

</div>

---

> *You don't serve death. You serve the line between life and death.*
> *That line exists for a reason. You are the reason it holds.*
> *You don't choose who lives or dies. You make sure it happens on your terms.*

---

## What Is the Grave Domain?

The Grave Domain is a **Cleric subclass** built around the idea that death is not evil — it is inevitable, sacred, and necessary. Grave Clerics don't raise undead or revel in destruction. They ensure that life ends when it should, that the dying find peace, and that those who cling to life beyond their time are **pulled back into balance**.

This is a **support and control hybrid** with a unique mechanic: **Path to the Grave** marks an enemy for doubled damage, and **Sentinel at Death's Door** protects allies from critical hits. At every level, the Grave Domain rewards positioning, timing, and reading the battlefield.

![Grave Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Grave Domain Spells · Circle of Mortality · Path to the Grave · Pull of Death |
| 5 | Grave Domain Spells (expanded) |
| 6 | Sentinel at Death's Door |
| 7 | Grave Domain Spells (expanded) |
| 9 | Grave Domain Spells (expanded) |

![Grave Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-divider.svg)

## Level 3 Features

### 📜 Grave Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit. Spells are added at Cleric levels 3, 5, 7, and 9:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Protection from Evil and Good · False Life · Lesser Restoration · Ray of Enfeeblement · Spare the Dying |
| 5 | Revivify · Vampiric Touch |
| 7 | Blight · Death Ward |
| 9 | Dispel Evil and Good · Mass Cure Wounds |

> **10 spells total** — a toolkit that spans healing, protection, debuffing, and resurrection. Every level brings something useful.

---

### ⭕ Circle of Mortality

*Life doesn't need to be generous. It just needs to be present.*

When you cast a healing spell to restore HP to a creature at **0 hit points**, you can treat any dice rolled as if they had rolled their **maximum value**.

- Applies to all healing spells
- Triggers only when the target is at exactly 0 HP
- No action cost — completely passive

> *Stabilizing a downed ally is now maximally efficient. Every healing word, every cure wounds, every spell that brings someone back from 0 hits at full power. The margin between alive and dead just got wider.*

---

### 💀 Path to the Grave

*The grave is patient. You are not.*

Channel Divinity option. As an action, you curse a creature you can see within 30 feet. Until the end of your next turn, the next hit that creature takes is treated as a **critical hit**, regardless of the actual roll.

- Trigger: Any hit against the cursed creature before the end of your next turn
- Effect: That hit automatically becomes a critical hit
- Duration: Until end of your next turn or until a hit triggers it

> *Path to the Grave turns any ally's attack into a guaranteed critical. A Rogue's Sneak Attack. A Fighter's Action Surge. A Paladin's Divine Smite. You don't deal the damage — you make sure someone else's damage counts double.*

---

### 🩸 Pull of Death

*Death pulls at the wounded. You simply give it a hand.*

A passive that scales with level:

| CLERIC LEVEL | PULL OF DEATH DAMAGE |
|---|---|
| 3–10 | 1d4 necrotic |
| 11+ | 1d6 necrotic |

When you hit a creature with a weapon attack or spell, you can trigger Pull of Death to deal additional necrotic damage. This represents the Grave Domain's constant pressure — every attack drains a little more life from those already close to death.

![Grave Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-divider.svg)

## Level 6 Features

### 🛡️ Sentinel at Death's Door

*The line holds. Not one step further.*

A new **action resource**: `SentinelAtDeathsDoor` — replenishes on rest, scaling with Wisdom modifier.

**Interrupt — Sentinel at Death's Door:**
- **Trigger:** A creature you can see within 30 feet is hit by a critical hit
- **Cost:** 1 Sentinel charge + your Reaction
- **Effect:** The critical hit becomes a **normal hit** — halving all damage and removing any critical hit bonus effects

> *Critical hits are the moments that can end a fight in one turn. A Rogue's Sneak Attack critting for 80 damage. A boss landing its legendary strike. Sentinel at Death's Door turns those moments into normal hits. The charge cost means you have to choose when to use it — but when you do, you may have just saved a life.*

The number of charges scales with your **Wisdom modifier**, rewarding investment in your primary stat.

![Grave Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-divider.svg)

## 🔧 Technical Notes

This implementation introduced **21 files** and **710 lines** across:

- `ActionResourceDefinitions` — New resource: `SentinelAtDeathsDoor`
- `LevelMapValues` — `PullOfDeath` scaling: `1d4` at Level 3, `1d6` at Level 11
- `SpellLists` — 4 spell lists (SLevel 2–5) with Domain spells assigned per level
- `Progressions` — Features delivered at Levels 3, 5, 6, 7, and 9 + UUID registered in Cleric subclass selector
- `Passive.stats` — 4 new passives: `GraveDomain_3_GraveDomainSpells` · `GraveDomain_3_CircleOfMortality` · `GraveDomain_3_PathToTheGrave` · `GraveDomain_3_PullOfDeath`
- `Interrupt.stats` — Reaction interrupt: `GraveDomain_6_SentinelAtDeathsDoor`
- `Status_BOOST.stats` — Status effects for Path to the Grave and Circle of Mortality
- `english.xml` — Complete localization for all features
- `README_Class_Cleric.MD` — Updated with Grave Domain documentation

Key implementation detail on **Circle of Mortality**:
```
IF(HasStatus('DYING',context.Target)):MaximizeHealing()
```
The maximize effect only triggers when the target has the `DYING` status — meaning exactly 0 HP. It does not apply to healing targets above 0, keeping the feature precisely scoped to its intended use case.

![Grave Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/grave-domain-divider.svg)

## 🎯 Playstyle Summary

The Grave Domain is a **battlefield controller disguised as a support Cleric**. Your core loop:

1. **Path to the Grave** — mark a priority target for guaranteed critical
2. **Signal your party** — let your Rogue, Fighter, or Paladin land the hit
3. **Circle of Mortality** — when allies drop, your healing brings them back at maximum efficiency
4. **Sentinel at Death's Door** — when a critical hit threatens to end the fight, spend a charge and negate it
5. **Pull of Death** — every attack drains a little more from enemies near their end

> *You don't need to be the one dealing damage. You need to be the one deciding who takes it, when they take it, and whether your allies survive it.*

The Grave Domain rewards players who **read the battlefield** — who to mark, when to intervene, when to let death do its work naturally.

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[Knowledge Domain]] →
