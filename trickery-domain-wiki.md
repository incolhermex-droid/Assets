![Trickery Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-banner.svg)

<div align="center">

![Trickery Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-badge.svg)

</div>

---

> *Your god is a liar. A cheat. A divine trickster who finds rules amusing and breaking them amusing.*
> *They chose you for exactly that reason.*
> *Which one is real? That's the point. They can't know either.*

---

## What Is the Trickery Domain?

The Trickery Domain is a **Cleric subclass** built around deception, illusion, and positional control. It is the most **mobile and elusive** of all Cleric Domains — creating illusions that enemies can't ignore, buffing allies to disappear into shadows, and at Level 6, teleporting between itself and its duplicate in a single Bonus Action.

This rework gives the Trickery Domain a fully implemented **Invoke Duplicity** Channel Divinity, a stealth buff in **Blessing of the Trickster**, and a Level 6 feature — **Trickster's Transposition** — that allows instant positional swaps with the duplicate once per turn. The spell list covers invisibility, fear, charm, confusion, and at Level 9, Dominate Person and Seeming.

The Trickery Domain is the only Cleric subclass that rewards **moving around the battlefield** rather than holding a position.

![Trickery Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Trickery Domain Spells · Blessing of the Trickster · Invoke Duplicity |
| 5 | Trickery Domain Spells (expanded) |
| 6 | Trickster's Transposition · Cloak of Shadows |
| 7 | Trickery Domain Spells (expanded) |
| 9 | Trickery Domain Spells (expanded) |

![Trickery Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-divider.svg)

## Level 3 Features

### 📜 Trickery Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Invisibility · Pass Without Trace · Charm Person · Disguise Self |
| 5 | Fear · Hypnotic Pattern |
| 7 | Confusion · Dimension Door |
| 9 | Dominate Person · Seeming |

> **10 spells total** — a toolkit built entirely around deception and control. **Pass Without Trace** at Level 3 gives your whole party +10 to Stealth checks. **Hypnotic Pattern** at Level 5 is one of the strongest crowd control spells in the game. At Level 9, **Seeming** lets your entire party change appearance, and **Dominate Person** turns any humanoid into a temporary asset.

---

### 🌑 Blessing of the Trickster

*The shadows want you. Let them have you — for now.*

A buff spell that grants one willing ally **Advantage on Dexterity (Stealth) checks** for 1 hour.

- Range: 9 meters
- Duration: 1 hour (concentration)
- Flagged as `Invisible` — the casting is subtle and doesn't reveal your position

> *Blessing of the Trickster is the best stealth buff in the game for a single target. Combined with Pass Without Trace on the whole party, your designated scout becomes effectively undetectable. Reconnaissance, ambushes, bypassing encounters entirely — this is where the Trickery Domain earns its name before a single attack roll is made.*

---

### 🪞 Invoke Duplicity — Channel Divinity

*Two of you. One of them is fake. Neither of them is safe.*

Your Channel Divinity option at Level 3. As a Bonus Action, you create a perfect illusory duplicate of yourself at a point you can see within range.

```
UseCosts: BonusActionPoint:1;ChannelDivinity:1
SpellFlags: CannotTargetItems;CannotTargetCharacter
```

The duplicate:
- Appears at a location you choose within 9 meters
- Is **flagged as an illusion** — enemies may attempt to identify it, but it looks identical to you
- Persists until you dismiss it, move too far, or it is destroyed
- Enables **Trickster's Transposition** at Level 6

> *Invoke Duplicity costs your Bonus Action and one Channel Divinity charge — a meaningful investment. What you get in return is a second presence on the battlefield that enemies must account for. Every attack directed at the duplicate is an attack not directed at you or your allies.*

The `MinorIllusion` character definition removes all damage resistances from the duplicate — it has **no resistances inherited from you**. A creature that destroys the duplicate does so cleanly, without benefiting from your defensive traits.

![Trickery Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-divider.svg)

## Level 6 Features

### 🌀 Trickster's Transposition

*Here. Now there. The enemy blinks and you're somewhere else entirely.*

Once per turn, you can **swap positions** with your Invoke Duplicity duplicate as a Bonus Action.

```
Cooldown: OncePerTurn
SpellProperties: TARGET:SwapPlaces();
TargetConditions: Tagged('ACT1_HAG_ILLUSION')
SpellFlags: Invisible;Temporary
```

- **Cost:** Bonus Action
- **Effect:** Instantly teleport to the duplicate's position; the duplicate moves to where you were
- **Cooldown:** Once per turn
- **Sound:** Uses Shadow Step monk animations — the swap is visually and audibly subtle

> *Trickster's Transposition is one of the most unique mobility tools in the mod. It's not a teleport — it's a **swap**. Your duplicate stays in play. You're now somewhere else. The enemy's target just moved. Their flanking position is compromised. Their melee range is gone.*
>
> *Used correctly, you can place the duplicate in melee with an enemy, take your turn safely at range, then swap to the duplicate's position to flank — all in the same round.*

---

### 🌑 Cloak of Shadows

*Sometimes the best trick is simply not being there.*

Gained at Level 6 via a dedicated spell list entry. Cloak of Shadows lets you cast **Invisibility** on yourself as an action without expending a spell slot — once per rest.

> *Cloak of Shadows is your get-out-of-danger tool. When things go wrong, when you're targeted, when the battlefield position is untenable — disappear. The Trickery Domain always has an exit.*

![Trickery Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **10 files** and **371 lines** of implementation:

- `ActionResourceDefinitions.tbl` — Two new entries: `New_Stat_1` (internal Cleric tag) and `WardingFlare` resource definition
- `SpellLists.tbl` — 6 new lists: Channel Divinity list · Level 3 · Level 5 · Level 6 (Cloak of Shadows) · Level 7 · Level 9
- `Progressions.tbl` — Full progression Levels 1–9, with spell delivery at Levels 3, 5, 6, 7, 9 and `Trickery_3_InvokeDuplicity` passive at Level 3 + `Trickery_6_TrickstersTransposition` at Level 6
- `Target.stats` — 3 new spells: `BlessingOfTheTrickster` · `InvokeDuplicity` · `TrickstersTransposition`
- `Character.stats` — `MinorIllusion` character definition with all damage resistances cleared
- `Passive.stats` — Passive entries for Invoke Duplicity and Trickster's Transposition
- `Interrupt.stats` — Interrupt logic for the transposition swap
- `Status_BOOST.stats` — Status effects supporting the duplicate's behavior
- `english.xml` — Complete localization

Key implementation detail — **Trickster's Transposition target condition**:
```
TargetConditions: Tagged('ACT1_HAG_ILLUSION')
```
The duplicate is tagged with `ACT1_HAG_ILLUSION` — the same tag used by hag illusions in Act 1. This is a clever reuse of existing engine infrastructure to identify illusory duplicates without creating a new tag system.

![Trickery Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/trickery-domain-divider.svg)

## 🎯 Playstyle Summary

The Trickery Domain is a **mobile illusionist** that wins fights by controlling information — what the enemy sees, where you are, and what they think they can hit.

**Your combat identity:**
1. **Pre-combat** — Blessing of the Trickster on your scout + Pass Without Trace on the party; approach the encounter without being detected
2. **Opening** — Invoke Duplicity as your Bonus Action to place a duplicate in a dangerous position while you stay safe
3. **Turn sequence** — cast control spells (Charm Person, Hypnotic Pattern, Confusion) from a protected position while enemies engage your duplicate
4. **Trickster's Transposition** — once per turn, swap with the duplicate to reposition; escape danger, reach a new angle, or simply confuse the enemy's targeting
5. **Cloak of Shadows** — when things go wrong, go invisible and reset the position
6. **Dominate Person** at Level 9 — always prepared; turn the most dangerous humanoid in the room into a temporary ally

> *The Trickery Domain doesn't win fights by being stronger than the enemy.*
> *It wins by making the enemy fight something that isn't there — until it's too late.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[War Domain]] →
