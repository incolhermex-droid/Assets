![War Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-banner.svg)

<div align="center">

![War Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-badge.svg)

</div>

---

> *Other Clerics stay in the back.*
> *You are the front line. The shield. The sword. The answer.*
> *Your god doesn't want prayers. They want results.*

---

## What Is the War Domain?

The War Domain is a **Cleric subclass** built for one purpose: fighting. It is the most **martially capable** of all Cleric Domains — granting an extra Bonus Action attack resource, proficiency with martial weapons and heavy armor from the start, and a Level 6 passive that rewards staying in combat and landing hits.

This rework gives the War Domain a completely new resource — **War Priest Action Points** — that replenish on Short Rest, a Channel Divinity that enhances attack rolls, and a spell list that ends with **Steel Wind Strike** as an always-prepared option at Level 9.

The War Domain Cleric is the answer to "what if the Cleric just hit things?" It turns out the answer is: very effectively.

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | War Domain Spells · War Priest · Guided Strike |
| 5 | War Domain Spells (expanded) |
| 6 | War God's Blessing |
| 7 | War Domain Spells (expanded) |
| 8 | Divine Strike |
| 9 | War Domain Spells (expanded) |

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## Level 3 Features

### 📜 War Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Magic Weapon · Spiritual Weapon · Guiding Bolt · Shield of Faith · War Priest |
| 5 | Crusader's Mantle · Spirit Guardians |
| 7 | Fire Shield · Freedom of Movement |
| 9 | Hold Monster · Steel Wind Strike |

> **10 spells total** — a mix of buffs, summons, and control. **Spirit Guardians** at Level 5 and **Steel Wind Strike** at Level 9 are two of the strongest spells available to any martial caster. The War Domain Cleric has both always prepared.

---

### ⚔️ War Priest

*Your god blesses your strikes. The enemy feels it.*

A new **Bonus Action attack** powered by the `WarPriestActionPoint` resource — a dedicated action economy resource that replenishes on **Short Rest**.

- **Cost:** 1 War Priest Action Point + Bonus Action
- **Effect:** Make one weapon attack as a Bonus Action
- **Condition:** Only available if you do not already have Extra Attack active

```
Conditions: not HasPassive('ExtraAttack') 
            and not HasPassive('ExtraAttack_2')
            and not HasPassive('ExtraAttack_3')
```

> *War Priest gives you an extra attack without requiring Extra Attack. If you multiclass into a martial class and gain Extra Attack, War Priest deactivates — the system checks for it explicitly. No stacking, no exploits. Just clean martial Cleric identity.*

**War Priest Action Points scale with Wisdom:**

| WISDOM SCORE | CHARGES PER SHORT REST |
|---|---|
| 13 or lower | 1 |
| 14–15 | 2 |
| 16–17 | 3 |
| 18–19 | 4 |
| 20–21 | 5 |
| 22–23 | 6 |
| 24+ | 7 |

---

### 🎯 Guided Strike — Channel Divinity

*Your god doesn't let you miss what matters.*

Your Channel Divinity option at Level 3. When you make an attack roll, you can use your reaction to add **+10 to the roll** — turning a near-miss into a hit.

- **Cost:** 1 Channel Divinity charge + Reaction
- **Effect:** +10 bonus to one attack roll
- **Timing:** Declared after seeing the roll, before knowing if it hits

> *Guided Strike is one of the most reliable Channel Divinity options in the game. +10 to an attack roll is the difference between hitting and missing on almost any result. Use it on your highest-damage attack, or when a critical miss would waste a major resource.*

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## Level 6 Features

### 🛡️ War God's Blessing

*Your god watches every swing. They approve.*

`War_6_WarGodsBlessing` — a passive that extends your Guided Strike to **allies within 30 feet**.

When an ally within range makes an attack roll, you can use your **Reaction** to grant them the +10 bonus from Guided Strike — spending a Channel Divinity charge on their behalf.

> *War God's Blessing doubles the value of your Channel Divinity. You're no longer just boosting your own attacks — you're the party's guaranteed hit insurance. A Rogue's Sneak Attack. A Paladin's Divine Smite setup. A Fighter's Action Surge. Any of these can be turned into a guaranteed hit with your reaction.*

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## Level 8 Features

### ⚡ Divine Strike

*Every hit carries divine weight.*

At Level 8, your weapon attacks deal an extra **1d8 damage** of your deity's damage type once per turn. This is the War Domain's version of Blessed Strikes — delivered one level later but with the same core benefit.

> *Divine Strike at Level 8 means your weapon attacks permanently deal bonus damage. Combined with War Priest Bonus Action attacks and Spirit Guardians, the War Domain Cleric puts out consistent damage every round.*

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **12 files** and **398 lines** of implementation:

- `ActionResourceDefinitions` — New resource: `WarPriestActionPoint` with Short Rest replenishment
- `SpellLists.tbl` — 5 new entries: Channel Divinity list + Level 3, 5, 7, 9 spell lists
- `Target.stats` — New spell: `WarPriest` — Bonus Action attack with `EXTRA_ATTACK_WARPRIEST` status
- `Status_BOOST.stats` — `EXTRA_ATTACK_WARPRIEST` status implementation
- `Progressions.tbl` — Full progression from Level 3 to 9 + UUID registered in Cleric subclass selector
- `Passive.stats` — 2 new passives: `War_3_WarPriest` · `War_6_WarGodsBlessing`
- `english.xml` — Complete localization

Key implementation detail — **War Priest condition check**:
```
SpellProperties: IF(not HasPassive('ExtraAttack') 
                 and not HasPassive('ExtraAttack_2') 
                 and not HasPassive('ExtraAttack_3')):
                 ApplyStatus(EXTRA_ATTACK_WARPRIEST,100,1)
```
The triple Extra Attack check ensures War Priest deactivates at any level of Extra Attack progression — Fighter 5, Fighter 11, Fighter 20. Clean multiclass behavior without edge cases.

![War Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/war-domain-divider.svg)

## 🎯 Playstyle Summary

The War Domain is a **frontline martial Cleric** that fights alongside its party rather than behind it.

**Your combat identity:**
1. **War Priest** — every Short Rest, spend Wisdom-modifier Bonus Action attacks; stay in melee and use them all
2. **Guided Strike** — when a critical hit or important attack needs to land, spend Channel Divinity for +10
3. **Spirit Guardians** at Level 5 — always prepared; position yourself in melee and let it chip everything around you
4. **War God's Blessing** at Level 6 — extend your Channel Divinity to allies; be the party's hit guarantee
5. **Divine Strike** at Level 8 — every weapon hit deals bonus damage; reward for staying in melee
6. **Steel Wind Strike** at Level 9 — always prepared; teleport and hit up to 5 targets in one action

> *The War Domain doesn't ask you to choose between fighting and spellcasting.*
> *It asks you to do both. Your god expects nothing less.*
> *Short Rest recharges your War Priest points. Long Rest recharges your spells.*
> *There is no downtime. There is only the next fight.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[Trickery Domain]] →
