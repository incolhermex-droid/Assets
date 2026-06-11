![Light Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-banner.svg)

<div align="center">

![Light Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-badge.svg)

</div>

---

> *Other Clerics pray in the dark.*
> *You are the light that makes the dark impossible.*
> *In the dark, you are not hidden. You are a target. A very bright one.*

---

## What Is the Light Domain?

The Light Domain is a **Cleric subclass** built around radiant power, sacred fire, and the divine light that burns away darkness — and everything standing in it. This is the most **offensively capable** of the core Cleric Domains, with a spell list that includes Fireball, Wall of Fire, Flame Strike, and Destructive Wave alongside its unique Channel Divinity and a reaction system — **Warding Flare** — that scales directly with your Wisdom modifier.

The 2024 rework gives the Light Domain a fixed Warding Flare scaling system that rewards Wisdom investment, a Channel Divinity that pushes undead and damages them simultaneously, and a progression that turns the Cleric into a legitimate damage dealer without sacrificing the class's identity.

![Light Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Light Domain Spells · Warding Flare · Radiance of the Dawn |
| 5 | Light Domain Spells (expanded) |
| 6 | Improved Warding Flare |
| 7 | Light Domain Spells (expanded) |
| 9 | Light Domain Spells (expanded) |

![Light Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-divider.svg)

## Level 3 Features

### 📜 Light Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Scorching Ray · See Invisibility · Burning Hands · Faerie Fire · Radiance of the Dawn |
| 5 | Daylight · Fireball |
| 7 | Guardian of Faith · Wall of Fire |
| 9 | Flame Strike · Destructive Wave |

> **10 spells total** — the most damage-focused Domain spell list in the mod. At Level 9, **Flame Strike** and **Destructive Wave** are always prepared. The Light Domain Cleric has more fire and radiant damage options than any other Cleric subclass.

---

### 🌟 Warding Flare

*They swing. You blind them. That's the whole plan.*

A **reaction interrupt** that fires when a creature you can see within 30 feet attacks you or an ally. When triggered, you impose **Disadvantage** on that attack roll — the attacker is momentarily blinded by a burst of divine radiance.

**Warding Flare charges scale with Wisdom:**

| WISDOM SCORE | CHARGES PER REST |
|---|---|
| 13 or lower | 1 |
| 14–15 | 2 |
| 16–17 | 3 |
| 18–19 | 4 |
| 20–21 | 5 |
| 22–23 | 6 |
| 24+ | 7 |

> *The higher your Wisdom, the more attacks you can negate per rest. At 20 Wisdom, you have 5 Warding Flare charges — meaning 5 attacks per rest that automatically have Disadvantage. That is not a defensive feature. That is an anti-attack system.*

**Bug fix note:** Prior to patch `5d588ca`, Warding Flare charges were not being correctly generated from the passive — the interrupt unlocked but the `ActionResource(WardingFlare)` entries were missing. This has been corrected and Wisdom scaling now works as intended.

---

### ☀️ Radiance of the Dawn — Channel Divinity

*The sun rises. Everything undead wishes it hadn't.*

Your Channel Divinity option at Level 3. Radiance of the Dawn is both a **Turn Undead effect and an area damage spell** in one action:

- Dispels magical darkness in a 30-foot radius
- Deals **2d10 + Cleric Level** radiant damage to all undead in range
- Undead must make a Constitution saving throw or be turned

> *Unlike base Turn Undead, Radiance of the Dawn always deals damage — even if the undead pass their save. You never waste the action.*

![Light Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-divider.svg)

## Level 6 Features

### ✨ Improved Warding Flare

*The flash wasn't enough? Let's try again.*

At Level 6, Warding Flare upgrades to `WardingFlare_Improved` — the same reaction now applies an additional effect beyond Disadvantage:

- The attacker takes **radiant damage** equal to your Wisdom modifier
- The Disadvantage effect remains

> *Improved Warding Flare turns a defensive reaction into a punishing one. Every attack you negate now hurts the attacker. At higher Wisdom scores with multiple charges, you're dealing meaningful radiant damage every round just from reactions.*

The interrupt system unlocks both `Interrupt_WardingFlare` and `Interrupt_WardingFlare_Improved` simultaneously at Level 6 — you choose which version fires based on your current charges and the situation.

![Light Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-divider.svg)

## 🔧 Technical Notes

This implementation spans two commits:

**Commit `b1f220f`** — Spell list implementation:
- `SpellLists.tbl` — 5 new entries: Channel Divinity list + Level 3, 5, 7, 9 spell lists
- 10 spells total distributed across 4 levels

**Commit `5d588ca`** — Warding Flare fix (Issue #53):
- `Passive.stats` — WardingFlare passive corrected with full ActionResource scaling chain
- `Passive.txt` — Generated output updated to match

The Wisdom scaling implementation:
```
ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',13)):ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',15)):ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',17)):ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',19)):ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',21)):ActionResource(WardingFlare,1,0);
IF(AbilityGreaterThan('Wisdom',23)):ActionResource(WardingFlare,1,0);
```

Each `IF` block adds 1 charge when Wisdom exceeds that threshold — they stack cumulatively, giving a minimum of 1 charge and a maximum of 7 at Wisdom 24+.

![Light Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/light-domain-divider.svg)

## 🎯 Playstyle Summary

The Light Domain is a **radiant damage dealer with a reaction-based defensive system** that rewards Wisdom investment at every level.

**Your combat identity:**
1. **Warding Flare** — every rest, negate Wisdom-modifier attacks. At 20 Wisdom, that's 5 per rest
2. **Radiance of the Dawn** — open against undead encounters with damage + turn in one action
3. **Fireball** at Level 5 — always prepared, no slot tax on a core offensive spell
4. **Improved Warding Flare** at Level 6 — reactions now deal radiant damage; defensive turns offensive
5. **Wall of Fire** at Level 7 — area denial always prepared; lock down chokepoints for free
6. **Flame Strike + Destructive Wave** at Level 9 — two of the strongest AoE spells in the game, always available

> *The Light Domain plays offensively. Your reactions protect your party. Your spell list destroys everything else.*
> *Wisdom isn't just your spellcasting stat. It's your Warding Flare budget, your Spell Save DC, and your damage output.*
> *Every point of Wisdom you invest returns value on every turn of every fight.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Life Domain]] · [[Cleric]] →
