![Archfey Patron Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-banner.svg)

<div align="center">

![Archfey Patron Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-badge.svg)

</div>

---

> *The fey don't lie. They just make the truth look like something else entirely.*
> *Your patron is ancient, powerful, and utterly unconcerned with your survival.*
> *What it gave you was not a gift. It was a loan. The interest is interesting.*

---

## What Is the Archfey Patron?

The Archfey Patron is a **Warlock subclass** built around a pact with a powerful being from the Feywild — a Summer Queen, an Archdruid of the Green, or another ancient fey entity that bends reality through charm, fear, and the beauty of terrible things.

Where other Warlocks project raw magical force or cursed energy, the Archfey Patron Warlock moves. **Steps of the Fey** at Level 3 is a Misty Step-based system with four variants — teleport and taunt, teleport and terrify, teleport and refresh allies, or teleport and vanish. At Level 6, **Misty Escape** gives you a reaction teleport when you take damage. At Level 10, **Beguiling Defenses** protects you from charm effects and lets you turn them back on attackers.

The Archfey is the most **mobile** Warlock subclass and the most **fey** in identity — every feature involves teleportation, glamour, or the unsettling beauty of fey magic.

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Archfey Spells · Steps of the Fey |
| 6 | Misty Escape |
| 10 | Beguiling Defenses |

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## Level 3 Features

### 📜 Archfey Spells

Your Patron grants an always-prepared spell list that doesn't count against your Pact Magic limit. *(Spell list entries referenced from the mod's spell list implementation.)*

---

### 🌿 Steps of the Fey

*Where you were. Where you are now. The space between is none of your concern.*

Your defining Level 3 feature. You gain charges of the `MistyStep` action resource, powering a choice of four teleportation variants as a **Bonus Action**. Each variant teleports you to a target location and applies an additional effect.

**Steps of the Fey charges scale with Charisma:**

| CHARISMA SCORE | CHARGES PER REST |
|---|---|
| 13 or lower | 1 |
| 14–15 | 2 |
| 16–17 | 3 |
| 18–19 | 4 |
| 20–21 | 5 |
| 22–23 | 6 |
| 24+ | 7 |

---

#### 🗡️ Taunting Step
*You arrive somewhere new and make your presence immediately known.*

```
UseCosts: BonusActionPoint:1;MistyStep:1
SpellProperties: GROUND:TeleportSource()
OriginSpellProperties: GROUND:CreateExplosion(Projectile_TauntingStep)
SpellFlags: HasHighGroundRangeExtension;RangeIgnoreVerticalThreshold
```

- Teleport to target location
- Launch `Projectile_TauntingStep` from origin point — enemies at the origin who fail a **Wisdom save** gain `GOADING_ATTACK` for 2 turns
- Works across elevation differences

> *Taunting Step is a hit-and-run control tool. Teleport away from a melee threat, apply Goading Attack from your origin point to lock them onto you, then deal with them on your terms.*

---

#### 💀 Dreadful Step
*You arrive. Something behind you arrives worse.*

```
Using: TauntingStep (base class)
OriginSpellProperties: GROUND:CreateExplosion(Projectile_DreadfulStep)
```

- Teleport to target location
- Launch `Projectile_DreadfulStep` from origin — enemies who fail the Wisdom save take **2d10 Psychic damage** in addition to `GOADING_ATTACK`

> *Dreadful Step is the damage variant of Taunting Step. Same teleport, same Wisdom save — but failure now costs 2d10 Psychic as well as the Goading condition. Use this when the taunt isn't enough by itself.*

---

#### 🌱 Refreshing Step
*You arrive somewhere new. Your allies feel better about it.*

```
SpellProperties: GROUND:TeleportSource();ApplyStatus(REFRESHING_STEP,100,-1);ApplyStatus(SELF,REFRESHING_STEP,100,-1)
AreaRadius: 3 (allies in 3m of destination)
AoEConditions: Ally()
```

- Teleport to target location
- Apply `REFRESHING_STEP` to yourself and all allies within **3 meters of your destination**
- Duration: Indefinite (until removed)

> *Refreshing Step is a support-oriented teleport. Position yourself near your party and apply a beneficial status to everyone in range as part of the movement. No action cost beyond the Bonus Action and one MistyStep charge.*

---

#### 👻 Disappearing Step
*You arrive. Then you don't.*

```
Using: RefreshingStep (base class)
SpellProperties: GROUND:TeleportSource();ApplyStatus(SELF,INVISIBILITY,100,2)
```

- Teleport to target location
- Apply **INVISIBILITY** to yourself for **2 turns**
- No AoE effect — self only

> *Disappearing Step is your escape hatch. Teleport to safety and vanish for 2 turns. Enemies lose track of you immediately. Use it when you need to reset a bad position or buy time for a critical spell.*

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## Level 6 Features

### 🌀 Misty Escape

*They hit you. You're somewhere else now. The timeline is confused.*

`Archfey_6_MistyEscape` — a **reaction interrupt** that triggers when you take damage.

- **Trigger:** You take damage from any source
- **Cost:** Reaction
- **Effect:** Immediately teleport up to 60 feet to an unoccupied space you can see

> *Misty Escape turns incoming damage into a repositioning opportunity. The moment you're hit, you can be somewhere else — before the rest of the attack sequence resolves. Combined with Disappearing Step's Invisibility, an Archfey Warlock who is threatened can teleport away and vanish in the same round.*

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## Level 10 Features

### 🛡️ Beguiling Defenses

*They tried to charm you. Quaint.*

`Archfey_10_BeguilingDefenses` with hidden resource `BeguilingDefenses` (MaxValue: 1, Rest replenishment).

- **Passive:** You are **immune to the Charmed condition**
- **Active (Once per Rest):** When a creature attempts to charm you and fails, you can use your reaction to turn the charm back — the creature is now Charmed by you instead

```
ActionResource: BeguilingDefenses
MaxValue: 1
ReplenishType: Rest
IsHidden: True
```

> *Beguiling Defenses gives you complete immunity to the condition your patron is most associated with — and once per rest, turns a failed charm attempt into a weapon. An enemy Enchantment Wizard who tries to charm you just accidentally gave you control of them for the rest of the encounter.*

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## 🔧 Technical Notes

This commit (21f51d5) introduced **16 files and 434 lines**:

- `ActionResourceDefinitions` — `__WARLOCK__` separator marker + `BeguilingDefenses` resource (UUID `cf7ca2a2`, hidden, MaxValue 1, Rest)
- `Progressions` — Level 3 passives: `Archfey_3_ArchfeySpells;Archfey_3_StepsOfTheFey;Archfey_3_StepsOfTheFey_Resource` / Level 6: `Archfey_6_MistyEscape` / Level 10: `Archfey_10_BeguilingDefenses`
- `Projectile.stats` — `TauntingStep` + `DreadfulStep` projectiles (launched from origin point via `CreateExplosion`)
- `Target.stats` — `RefreshingStep` + `DisappearingStep` target spells
- `Teleportation.stats` — `TauntingStep` + `DreadfulStep` teleportation spells (full implementations)
- `Interrupt.stats` — `Archfey_6_MistyEscape` reaction interrupt
- `Passive.stats` — All Archfey passives
- `Status_INVISIBLE.stats` — Invisibility status variant for Disappearing Step
- `english.xml` — Complete localization

Key implementation detail — **four-variant structure:**

The Steps of the Fey system uses two inheritance chains:
```
TauntingStep (Teleportation) → DreadfulStep (extends, adds 2d10 Psychic)
RefreshingStep (Target) → DisappearingStep (extends, removes AoE, adds Invisibility to self)
```
This means only two full spell implementations are needed — the other two extend them with minimal overrides. Clean and maintainable.

![Archfey Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/archfey-patron-divider.svg)

## 🎯 Playstyle Summary

The Archfey Patron is a **mobile controller** that fights through positioning, charm immunity, and the constant threat of disappearing.

**Your combat identity:**
1. **Steps of the Fey** — every Bonus Action is a teleport with a combat effect; choose your variant based on the fight
2. **Taunting/Dreadful Step** — when you need to lock an enemy down or deal psychic damage from your origin point
3. **Refreshing Step** — when your party is clustered, teleport into them and buff everyone
4. **Disappearing Step** — when you need to vanish, this is your instant exit
5. **Misty Escape** — when you take a hit, teleport away before the next one
6. **Beguiling Defenses** — immune to Charm; once per rest, reflect it back

> *The Archfey Patron doesn't fight in one place.*
> *It fights everywhere — and nowhere — at once.*
> *Your patron gave you the ability to be somewhere else at a moment's notice.*
> *Use it. Constantly.*

---

*For other Warlock Patrons, see [[Warlock]].*
*For the full class list, see [[Classes]].*

← [[Celestial Patron]] · [[Warlock]] →
