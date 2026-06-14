![Open Hand Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-banner.svg)

<div align="center">

![Open Hand Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-badge.svg)

</div>

---

> *The open hand does not strike blindly. It chooses exactly what it takes.*
> *Prone. Pushed. Unable to react. You don't deal the most damage in the room.*
> *You decide who does — and who can't stop them.*

---

## What Is the Way of the Open Hand?

The Way of the Open Hand is the **definitive control Monk subclass**. Where other traditions add elements, weapons, or healing, the Open Hand adds **consequences** to every unarmed strike. Your Flurry of Blows becomes a toolkit — knock prone, push away, or strip reactions — and everything else in the subclass builds on that foundation.

This rework gives the Open Hand three distinct Flurry variants at Level 3, a Wisdom-scaling heal at Level 6, and at Level 11 a passive that makes Step of the Wind completely free. It is the subclass that rewards knowing exactly where every enemy should be standing.

![Open Hand Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Open Hand Technique |
| 6 | Wholeness of Body |
| 11 | Fleet Step |

![Open Hand Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-divider.svg)

## Level 3 Features

### 👊 Open Hand Technique

*Every strike of your Flurry means something. You choose what.*

When you use **Flurry of Blows**, each hit can apply one of three effects. You choose which variant to use before the Flurry:

**Knock** — `OpenHandTechnique_Knock`
The target must make a **Dexterity saving throw** against your Ki save DC. On failure: knocked **Prone**.

> *Prone targets are attacked with Advantage from melee. A Rogue's Sneak Attack. A Fighter's Great Weapon. A Paladin's Divine Smite. You don't set up the kill — you set up whoever does it best.*

**Push** — `OpenHandTechnique_Push`
The target must make a **Strength saving throw** against your Ki save DC. On failure: pushed back with `Force(5, EntityForward, Neutral)` — 5 meters directly away from you.

> *Push creates distance, breaks grapples, removes enemies from advantage positions, and sends targets off ledges. The terrain does the rest.*

**No Reactions** — `OpenHandTechnique_NoReactions`
The target is inflicted with `OPEN_HAND_NO_REACTIONS` — they **cannot use reactions** until the start of your next turn.

> *No Reactions removes opportunity attacks, Counterspell, Shield, and any other reaction the enemy was planning to use. In the right moment — before a critical spell or a flanking repositioning — this is worth more than the damage.*

![Open Hand Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-divider.svg)

## Level 6 Features

### 💚 Wholeness of Body

*The body heals itself. You just had to learn how to ask.*

Once per **Short Rest**, as a Bonus Action, restore HP equal to:
`Martial Arts die + Wisdom modifier`

The heal scales with Wisdom — the same scaling pattern as Warding Flare charges and Preserve Life:

| WISDOM SCORE | HEAL AMOUNT (at Monk 6, d8 Martial Arts) |
|---|---|
| 14 | 1d8 + 2 |
| 16 | 1d8 + 3 |
| 18 | 1d8 + 4 |
| 20 | 1d8 + 5 |

> *Wholeness of Body is not a combat-changing heal. It is sustainability — the difference between entering the next fight at 40% HP and entering it at 70%. It refreshes on Short Rest, meaning you can use it every encounter.*

![Open Hand Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-divider.svg)

## Level 11 Features

### 💨 Fleet Step

*Step of the Wind is no longer a choice. It's a given.*

At Level 11, **Step of the Wind no longer costs a Bonus Action**. You can Disengage or Dash as part of your movement without spending your Bonus Action — freeing it for Flurry of Blows, Patient Defense, or class features.

> *Fleet Step fundamentally changes your action economy at Level 11. You used to choose between movement and Flurry. Now you have both. Every turn.*

![Open Hand Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/open-hand-divider.svg)

## 🎯 Playstyle Summary

The Way of the Open Hand is a **battlefield controller** that turns every Flurry of Blows into a positioning tool.

**Your combat loop:**
1. Attack with your Action — land hits, apply Stunning Strike when Ki allows
2. Flurry of Blows — choose your technique based on the fight: Knock for advantage setup, Push for terrain control, No Reactions before a critical play
3. Wholeness of Body on Short Rest — sustain through multiple encounters
4. Fleet Step at Level 11 — move freely, Disengage freely, Flurry freely

> *The Open Hand Monk doesn't ask: "How much damage did I deal?"*
> *It asks: "How much damage did my positioning enable?"*

---

*For the full Monk class breakdown, see [[Monk]].*
*For other Monastic Traditions, see [[Way of Mercy]] · [[Way of the Four Elements]] · [[Way of the Kensei]].*

← [[Monk]] · [[Way of Mercy]] →
