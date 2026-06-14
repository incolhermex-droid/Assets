![Kensei Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-banner.svg)

<div align="center">

![Kensei Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-badge.svg)

</div>

---

> *Most monks abandon weapons. You mastered them.*
> *The sword is not a tool you use. It is an extension of what you already are.*
> *The sword is not separate from the monk. It is the monk, extended.*

---

## What Is the Way of the Kensei?

The Way of the Kensei is a **Monk subclass** built around weapon mastery — the philosophy that a chosen weapon, trained to perfection, is as much a part of the monk as any unarmed strike. Where other traditions abandon weapons entirely, the Kensei designates specific weapons as **Kensei weapons** and builds an entire combat identity around them.

This rework implements the Kensei fully: **Kensei Weapons** at Level 3 with Agile Parry and Kensei's Shot, **Magic Kensei Weapons and Deft Strike** at Level 6, and **Sharpen the Blade** at Level 11 — a Ki-powered weapon enchantment that applies a stacking accuracy and damage bonus to your Kensei weapon for 10 turns.

The Kensei is the Monk subclass for players who want to fight with a blade and still feel like a Monk.

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Kensei Weapons · Agile Parry · Kensei's Shot |
| 6 | Magic Kensei Weapons · Deft Strike |
| 11 | Sharpen the Blade |

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## Level 3 Features

### ⚔️ Kensei Weapons

*These weapons are not separate from your training. They are your training.*

At Level 3, you designate specific weapons as your **Kensei weapons**. These weapons gain the following benefits:
- You can use **Dexterity** instead of Strength for attack and damage rolls
- They are considered **Monk weapons** for all class features
- They benefit from Kensei-specific abilities unavailable to other weapons

Compatible weapon types for Kensei designation:
`Dagger · Longsword · Rapier · Scimitar · Shortsword · Sickle`

> *The Kensei weapon list covers the primary one-handed precision weapons. A Rapier Kensei and a Longsword Kensei have meaningfully different damage profiles — d8 vs d8, but with different reach and mastery properties.*

---

### 🛡️ Agile Parry

*The weapon is also a shield. You just had to learn to use it that way.*

When you make an **unarmed strike** as part of the Attack action while holding a Kensei weapon, you gain **+2 AC** until the start of your next turn.

> *Agile Parry rewards mixing unarmed strikes and weapon attacks — a natural part of the Kensei's combat style. Every turn you mix both, you get the AC bonus. It is passive and automatic as long as you play to the subclass's identity.*

---

### 🏹 Kensei's Shot

*Distance is not an obstacle. It's just a longer reach.*

As a **Bonus Action** while holding a **bow**, you can add your **Martial Arts die** to the next ranged weapon attack you make this turn.

```
UseCosts: BonusActionPoint:1
TargetConditions: (equipped bow)
ApplyStatus: KENSEIS_SHOT
```

> *Kensei's Shot bridges the gap between melee and ranged combat. A Kensei carrying a bow as a secondary weapon can use a Bonus Action to enhance their next arrow before switching to melee — or open with a boosted ranged attack before closing distance.*

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## Level 6 Features

### ✨ Magic Kensei Weapons

Your Kensei weapons are now treated as **magical** for the purpose of overcoming resistance and immunity to non-magical damage. This is the Kensei equivalent of Ki-Empowered Strikes — applied specifically to your designated weapons.

> *At Level 6, your Kensei weapon bypasses the resistances that non-magical weapons cannot. Combined with Ki-Empowered Strikes (which covers unarmed), a Level 6+ Kensei is fully equipped against resistant enemies regardless of which attack type they use.*

---

### 🗡️ Deft Strike

*The weapon does more than you let it show.*

An **interrupt** that triggers `OnCastHit` — when you hit with your Kensei weapon:

```
UseCosts: KiPoint:1;DeftStrike:1
Interrupt trigger: OnCastHit with Kensei weapon
Effect: DealDamage(MartialArts, weapon damage type)
```

Spend **1 Ki Point** when you hit to deal **additional damage equal to your Martial Arts die** in your weapon's damage type.

> *Deft Strike is a Ki sink that rewards hit confirmation — you only spend the Ki when the attack lands. At Monk Level 6-10 (d8 Martial Arts), this adds 1d8 of your weapon's damage type on a confirmed hit. Efficient and precise — exactly what the Kensei should be.*

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## Level 11 Features

### 🌟 Sharpen the Blade

*The blade remembers every cut. You remind it.*

As a **Bonus Action**, spend **1-3 Ki Points** to apply `SHARPEN_THE_BLADE` to your Kensei weapon for **10 turns**.

```
UseCosts: BonusActionPoint:1;KiPoint:1 (up to 3)
Duration: 10 turns
Target: Must be wielding a valid Kensei weapon
Valid weapons: Dagger · Longsword · Rapier · Scimitar · Shortsword · Sickle
```

The number of Ki Points spent determines the bonus:
- **1 Ki:** +1 to attack rolls and damage rolls
- **2 Ki:** +2 to attack rolls and damage rolls
- **3 Ki:** +3 to attack rolls and damage rolls

> *Sharpen the Blade is a pre-combat buff that rewards planning. Spending 3 Ki before a major encounter gives your Kensei weapon +3 to hit and +3 to damage for 10 full turns. At high levels where accuracy and damage matter most, this is a meaningful accuracy investment.*
>
> *10 turns covers most combat encounters entirely. Use it at the start of a boss fight and forget about it until it expires.*

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## 🔧 Technical Notes

The Kensei implementation (commit `2ddc2d6`) introduced **22 files** and **678 lines**:

- `ActionResourceDefinitions` — New resource: `DeftStrike` (replenish per turn, enables interrupt)
- `Progressions` — Features at Levels 3, 6, 11 + UUID registered in Monk subclass selector
- `Passive.stats` — 5 new passives: `Kensei_3_KenseiWeapons` · `Kensei_3_AgileParry` · `Kensei_3_KenseisShot` · `Kensei_6_MagicKenseiWeapons` · `Kensei_6_DeftStrike`
- `Target.stats` — `KenseisShot` spell + `SharpenTheBlade` spell (3 variants for 1/2/3 Ki)
- `Status_BOOST.stats` — `KENSEIS_SHOT` · `SHARPEN_THE_BLADE` · `AGILE_PARRY` status effects
- `Interrupt.stats` — `DeftStrike` interrupt triggered on `OnCastHit`
- `english.xml` — Complete localization

Key implementation detail — **Sharpen the Blade weapon check**:
```
Conditions: (HasWeaponInMainHand('Dagger') or HasWeaponInMainHand('Longsword') 
             or HasWeaponInMainHand('Rapier') or HasWeaponInMainHand('Scimitar')
             or HasWeaponInMainHand('Shortsword') or HasWeaponInMainHand('Sickle'))
```
Sharpen the Blade explicitly checks for valid weapon types in main hand — you cannot use it with improvised weapons or non-Kensei weapon types, enforcing the subclass's thematic identity.

![Kensei Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/kensei-divider.svg)

## 🎯 Playstyle Summary

The Way of the Kensei is a **precision weapon striker** that combines the Monk's action economy with weapon-enhanced accuracy and damage.

**Your combat loop:**
1. **Pre-combat** — Sharpen the Blade for +1 to +3 attack/damage (3 Ki for maximum)
2. **Attack action** — lead with a Kensei weapon strike + one unarmed strike to trigger Agile Parry (+2 AC)
3. **Deft Strike** — when a hit lands, spend 1 Ki for bonus Martial Arts die damage
4. **Flurry of Blows** — mix unarmed and weapon strikes
5. **Stunning Strike** — still available and still devastating; save Ki for it
6. **Kensei's Shot** — when range is needed, Bonus Action to boost next arrow

> *The Kensei is the most equipment-dependent Monk — but also the one that gets the most out of a good weapon.*
> *Find your weapon. Designate it. Sharpen it. And use it until there's nothing left to cut.*

---

*For the full Monk class breakdown, see [[Monk]].*
*For other Monastic Traditions, see [[Way of the Open Hand]] · [[Way of Mercy]] · [[Way of the Four Elements]].*

← [[Way of the Four Elements]] · [[Monk]] →
