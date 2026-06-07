![Undead Patron Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-banner.svg)

<div align="center">

![Undead Patron Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-badge.svg)

</div>

---

> *You've made a pact with a creature that defies the cycle of life and death.*
> *A powerful lich. A vampire. An entity that has walked past death and come back.*
> *They know the routes past the doors of death. You're about to learn them too.*

---

## What Is the Undead Patron?

The Undead Patron is a **Warlock subclass** built around a pact with an ancient undead entity — a lich, a vampire, or another being that has transcended mortality. These patrons share their profane knowledge of death, fear, and necrotic power with those who serve their will among the living.

Where other Warlocks project raw magical force, the Undead Patron Warlock **becomes something the living fear**. From Level 3, you project terror, ignore the resistances that protect most enemies from necrotic damage, and at Level 10 become immune to necrotic damage entirely.

This is a **full progression subclass** with features at Levels 3, 6, and 10, and an expanding spell list across all odd levels through Level 9.

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Form of Dread · Undead Spells |
| 5 | Undead Spells (expanded) |
| 6 | Grave Touched |
| 7 | Undead Spells (expanded) |
| 9 | Undead Spells (expanded) |
| 10 | Necrotic Husk |

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## Level 3 Features

### 💀 Form of Dread

*The presence of your patron manifests through you — and it terrifies.*

Form of Dread grants two distinct benefits that work together:

**Fearless Form** — You have full **Immunity to the Frightened condition**. Whatever your patron might project outward, it cannot touch you inward.

**Frightful Avatar** — Once per turn, when you hit a creature with an attack roll, you can force it to make a **Wisdom saving throw** against your Spell Save DC.
- **Failure:** The target has the **Frightened** condition until the end of your next turn.

> *You become immune to the very condition you inflict. Your patron didn't just give you power — it gave you the shape of fear itself.*

---

### 📜 Undead Spells

Your pact grants you a permanently expanded spell list that grows as you level. These spells are always prepared and do not count against your Prepared Spells limit.

| WARLOCK LEVEL | SPELLS ADDED |
|---|---|
| 3 | Bane · Blindness/Deafness · Phantasmal Force · Ray of Sickness |
| 5 | Speak with Dead · Summon Undead |
| 7 | Greater Invisibility · Phantasmal Killer |
| 9 | Danse Macabre · Cloudkill |

> **10 spells total** added to your list across the full progression — a toolkit built for fear, death, and control.

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## Level 6 Features

### ☠️ Grave Touched

*Your patron's powers have a profound effect on your body and magic.*

Grave Touched is a three-part passive that fundamentally changes how your necrotic damage works:

**Arcane Necrosis** — Necrotic damage from your attacks, Warlock spells, and Warlock features **ignores Resistance** to Necrotic damage. Creatures that would normally take half damage from necrotic sources take full damage from you.

**Dreaded Necrosis** — When you deal Necrotic damage with a spell, you **cannot roll a 1** on any damage die. The floor on your necrotic output is raised permanently.

**Undead Endurance** — You don't need to sleep, and **magic cannot put you to sleep**. Immunity to the Sleep condition and any magical sleep effect.

> *At Level 6, your necrotic damage stops being ignorable. Resistance means nothing. Your minimum rolls get better. And you stop being vulnerable to one of the most common crowd-control vectors in the game.*

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## Level 10 Features

### 🦴 Necrotic Husk

*Your connection to undeath saturates your body.*

**Necrotic Resilience** — You have full **Immunity to Necrotic damage**.

This is the natural endpoint of the progression:
- Level 3: You inflict fear and project your patron's dread
- Level 6: Your necrotic damage bypasses resistance and gets a minimum floor
- Level 10: You become immune to the very damage type you specialize in

> *You are no longer simply a conduit for death. You have become something adjacent to it.*

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## 🔧 Technical Notes

This commit introduced **9 files** and **291 lines** of new implementation:

- `ClassDescriptions` — Full subclass description registered as `UndeadPatron` with Charisma as primary and spellcasting ability
- `Progressions` — Feature delivery at Levels 3, 5, 6, 7, 9, and 10 + UUID registered in the Warlock subclass selector
- `Passive.stats` — 4 new passives: `FormOfDread`, `UndeadSpells`, `GraveTouched`, `NecroticHusk`
- `english.xml` — Complete localization for all features including full description of the patron lore
- `meta.lsx` — Version bump to `144678146619211779`

Key implementation detail on **Grave Touched**:
```
Boosts: StatusImmunity(SG_Sleeping);
        IF(MainDamageTypeIs(DamageType.Necrotic)):MinimumRollResult(Damage,2);
        IgnoreResistance(Necrotic,Resistant);
```
The `MinimumRollResult(Damage,2)` ensures no damage die for necrotic spells can land on 1 — every die has a floor of 2. This applies only when the main damage type is Necrotic, so it doesn't bleed into hybrid damage spells unexpectedly.

![Undead Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/undead-patron-divider.svg)

## 🎯 Playstyle Summary

The Undead Patron is a **Charisma-based control and necrotic striker** that becomes increasingly resilient to its own damage type while making enemies more vulnerable to it.

**Your combat identity:**
- Apply **Frightened** every turn through Form of Dread — Frightened creatures have Disadvantage on attacks and can't willingly move toward you
- Blast with necrotic spells knowing Resistance does nothing from Level 6 onward
- Your necrotic damage dice never land on 1 — consistent, reliable output
- Sleep and Frightened cannot affect you — two of the most common debuff vectors in the game simply don't work on you
- At Level 10, you absorb necrotic damage entirely — enemy Warlocks, necromancers, and undead deal zero damage of their primary type to you

> *Fear up. Resistance down. Death floors raised. And at the end of it all, immunity to the thing that should have killed you.*

---

*For other Warlock subclasses, see [[Hexblade Patron]].*
*For the full Warlock class breakdown, see [[Classes]].*

← [[Classes]] · [[New Classes]] →
