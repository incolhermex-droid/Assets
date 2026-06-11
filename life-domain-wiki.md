![Life Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-banner.svg)

<div align="center">

![Life Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-badge.svg)

</div>

---

> *Your god doesn't want martyrs. They want survivors.*
> *Every ally standing at the end of the fight is a prayer answered.*
> *They fall. You decide if that's permanent.*

---

## What Is the Life Domain?

The Life Domain is the **definitive healing Cleric subclass** — rebuilt for the 2024 PHB with a complete mechanical identity from Level 1. It is the subclass that makes healing worth investing in, that makes every spell slot spent on restoration feel like it actually did something, and that makes the Cleric the most reliable life insurance policy any party can have.

This rework gives the Life Domain two new passives — **Disciple of Life** and **Blessed Healer** — and a completely new **Preserve Life** Channel Divinity with six scaling variants that distribute healing intelligently across multiple targets. This is not the passive "add 2+spell level to healing" you might remember. This is a system.

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 1 | Life Domain Spells (Bless · Cure Wounds) |
| 3 | Life Domain Spells (expanded) · Disciple of Life · Preserve Life |
| 5 | Life Domain Spells (expanded) |
| 6 | Blessed Healer |
| 7 | Life Domain Spells (expanded) |
| 9 | Life Domain Spells (expanded) |

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## Level 1 Features

### 📜 Life Domain Spells (Level 1)

The Life Domain is unique among Domains in that it grants Domain spells **from Level 1**, not Level 3:

- **Bless** — Always prepared from the moment you choose this Domain
- **Cure Wounds** — Always prepared from the moment you choose this Domain

> *Most Domains give you spells at Level 3. The Life Domain gives you two of the most useful spells in the game from character creation. Before you even have a Channel Divinity, you have more healing available than any other Cleric.*

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## Level 3 Features

### 📜 Life Domain Spells (Expanded)

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 1 | Bless · Cure Wounds |
| 3 | Aid · Lesser Restoration · Preserve Life |
| 5 | Mass Healing Word · Revivify |
| 7 | Death Ward · Guardian of Faith |
| 9 | Greater Restoration · Mass Cure Wounds |

**9 spells total** — the most healing-focused Domain spell list in the mod. At Level 9, **Greater Restoration** and **Mass Cure Wounds** are always prepared, meaning you can dedicate your prepared spell slots to damage and control without sacrificing your party's survivability.

---

### 💚 Disciple of Life

*Every spell you cast to heal costs the same. Now it returns more.*

A passive gained at Level 3 that enhances all healing spells and cantrips — and notably, **Aura of Vitality**:

```
Conditions: HealDoneGreaterThan(0) and (IsSpell() or IsCantrip()) 
            or SpellId('Target_AuraOfVitality_Activate')
```

When you cast a healing spell, Disciple of Life adds bonus healing on top of the base amount. The bonus scales with spell level — higher slots return more.

> *Disciple of Life doesn't just make your heals bigger. It makes every healing spell feel like it was worth the slot. A Cure Wounds that heals for 12 now heals for more. A Mass Cure Wounds at Level 9 becomes a full party restoration.*

---

### 🛡️ Preserve Life — Channel Divinity

*One action. Multiple allies. All at once.*

**Preserve Life** is a completely new Channel Divinity implementation with **6 variants**, each distributing a fixed healing pool across a different number of targets. The total healing pool is `5 × Cleric Level`, split mathematically:

| VARIANT | TARGETS | HEALING PER TARGET | FORMULA |
|---|---|---|---|
| Preserve Life 1 | 1 | 5 × Cleric Level | `5 * ClassLevel(Cleric)` |
| Preserve Life 2 | 2 | 2.5 × Cleric Level | `2.5 * ClassLevel(Cleric)` |
| Preserve Life 3 | 3 | ~1.67 × Cleric Level | `1.6667 * ClassLevel(Cleric)` |
| Preserve Life 4 | 4 | 1.25 × Cleric Level | `1.25 * ClassLevel(Cleric)` |
| Preserve Life 5 | 5 | 1 × Cleric Level | `ClassLevel(Cleric)` |
| Preserve Life 6 | 6 | ~0.83 × Cleric Level | `0.8333 * ClassLevel(Cleric)` |

**Critical detail:** Preserve Life only targets creatures with the **Bloodied** condition (`Blooded()`) — meaning at or below 50% HP. You cannot use it to top off healthy allies. It is a triage tool, not a maintenance heal.

> *At Cleric Level 10, Preserve Life 1 heals for 50 HP on a single target, or Preserve Life 6 heals 6 allies for ~8 HP each. The pool is the same. The distribution is your choice. In a fight where your whole party is struggling, spreading the heal wins. In a fight where one ally is about to die, concentrating it wins.*

The action costs **1 ActionPoint + 1 ChannelDivinity charge** — meaning it competes with your attack, but not with your spells.

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## Level 6 Features

### 💛 Blessed Healer

*The god of life doesn't let its own servant wither.*

When you cast a healing spell that restores HP to another creature, you also **regain HP yourself**.

`BlessedHealer` is a passive that triggers automatically — no action cost, no decision required. Every time you heal an ally with a spell, you receive healing as well.

> *Blessed Healer changes the math of playing a healer. You no longer drain yourself to keep others alive. The act of healing others sustains you. At higher levels, in long fights, this can be the difference between staying in the battle and going down.*

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **8 files** and **282 lines** of implementation:

- `SpellLists.tbl` — 6 new spell list entries (Level 1 through 9 + Channel Divinity list)
- `Progressions.tbl` — Full progression from Level 1 to 9 with spell delivery at every odd level
- `Target.stats` — Complete implementation of `Preserve Life` container spell + 6 variants (`PreserveLife_1` through `PreserveLife_6`)
- `Passive.stats` — 2 new passives: `DiscipleOfLife` · `BlessedHealer`
- `Status_BOOST.stats` — Status effects supporting Disciple of Life's bonus healing trigger
- `Global.khn` — Global script integration
- `english.xml` — Complete localization
- `dnd5.5e_Blooded.txt` — Story goal integration confirming Bloodied condition prerequisite for Preserve Life targeting

Key implementation detail — **Preserve Life targeting**:
```
TargetConditions: Character() and not Dead() and Blooded()
```
The `Blooded()` condition check means Preserve Life is **exclusively a triage tool** — it cannot be used on full-health allies. This is intentional design: the Life Domain rewards reading who needs help, not pre-healing.

![Life Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/life-domain-divider.svg)

## 🎯 Playstyle Summary

The Life Domain is a **dedicated healer** that makes every healing action return more value than any other Cleric subclass. Your core loop:

1. **Bless** from Level 1 — the single best buff in the game, always prepared
2. **Preserve Life** — when multiple allies are Bloodied, distribute the healing pool strategically across targets
3. **Disciple of Life** — every healing spell returns bonus HP automatically; never think about it, just benefit
4. **Blessed Healer** — stay alive by keeping others alive; the more you heal, the longer you last
5. **Revivify** at Level 5 — always prepared, always available; no ally needs to stay dead
6. **Greater Restoration + Mass Cure Wounds** at Level 9 — your entire Domain spell list frees up prepared slots for damage and control

> *The Life Domain doesn't make combat easier. It makes losing impossible to rush.*
> *Every ally is harder to kill. Every fall is recoverable. Every fight goes longer because you're there.*
> *That's not passive. That's the most aggressive thing a Cleric can do.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[Light Domain]] →
