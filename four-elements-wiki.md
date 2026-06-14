![Four Elements Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-banner.svg)

<div align="center">

![Four Elements Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-badge.svg)

</div>

---

> *You didn't choose an element. You became all of them.*
> *Acid. Cold. Fire. Lightning. Thunder.*
> *The world has five ways to destroy something. You wear all five.*

---

## What Is the Way of the Four Elements?

The Way of the Four Elements is a **Monk subclass** built around elemental attunement — choosing an elemental aura that reshapes your combat presence and dealing elemental damage with every strike. This rework gives the Four Elements Monk a completely new **VFX system** with distinct visual effects for each of the five elements, a scaling elemental burst at Level 6, and expanded elemental spells at Level 11.

This is the most **visually dramatic** Monk subclass in the mod, and one of the most unique mechanically — your attunement choice at Level 3 defines your elemental identity for the rest of the subclass's progression.

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Elemental Attunement (5 auras) |
| 6 | Elemental Burst |
| 11 | Elemental Disciplines (expanded) |

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## Level 3 Features

### 🔥 Elemental Attunement

*Pick your element. Become it.*

At Level 3, choose one of five elemental attunements. Your choice grants a persistent **elemental aura** with unique VFX and adds elemental damage to your unarmed strikes and monk weapon attacks.

Each attunement has been given completely new visual effects in the VFX update commit — distinct particle systems, color palettes, and animation timings for each element.

| ATTUNEMENT | DAMAGE TYPE | VFX |
|---|---|---|
| **Acid** | Acid | Green corrosive particles, dissolving effect |
| **Cold** | Cold | Blue-white frost wisps, crystalline shards |
| **Fire** | Fire | Orange-red flame trails, ember cascade |
| **Lightning** | Lightning | Yellow-white arc sparks, electric discharge |
| **Thunder** | Thunder | Purple-grey shockwave pulses, concussive rings |

> *The attunement is permanent once chosen. Your entire subclass identity flows from this decision. A Fire Monk and a Lightning Monk play very differently in terms of which enemies they're effective against.*

Each attunement adds the corresponding damage type to your unarmed strikes — synergizing with **Ki-Empowered Strikes** (which ignores Bludgeoning resistance) to create a character that bypasses multiple resistance categories simultaneously.

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## Level 6 Features

### 💥 Elemental Burst

*You've been holding it in. Time to let it out.*

Spend **2 Ki Points** as an Action to release a burst of your attuned element in an area centered on you.

- **Area:** 3-meter radius around you
- **Damage:** Scales with Monk level
- **Type:** Matches your elemental attunement
- **Save:** Dexterity against your Ki save DC — half damage on success

> *Elemental Burst is a radius AoE that uses your own position as the center. It rewards fighting in melee where the Four Elements Monk naturally operates. Surround yourself with enemies and detonate.*

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## Level 11 Features

### ✨ Elemental Disciplines (Expanded)

At Level 11, your elemental mastery expands with new disciplines that apply your element in broader ways — area effects, sustained auras, and interactions with the environment.

> *The specific disciplines available depend on your chosen attunement. Each element gains unique Level 11 options that no other attunement shares.*

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## 🔧 Technical Notes

The VFX update (commit `5ec9dd2`) was specifically focused on visual polish for this subclass:

- 5 distinct particle systems implemented — one per element
- Updated icon assets for all elemental attunement abilities
- Animation timing adjusted for each element's visual identity:
  - Fire: fast, erratic, orange-red cascade
  - Ice: slow, crystalline, blue-white formation
  - Lightning: instant flash, arc discharge
  - Thunder: radial pulse, concussive ring
  - Acid: dripping, dissolving, green corrosion

The underlying mechanical implementation uses a single `ElementalAttunement` passive that checks which attunement is active and routes damage type accordingly — clean, scalable architecture that allows new elements to be added without restructuring the entire system.

![Four Elements Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/four-elements-divider.svg)

## 🎯 Playstyle Summary

The Way of the Four Elements is an **elemental striker** that fights in melee while projecting elemental energy outward.

**Your combat loop:**
1. Choose your position carefully — you want to be surrounded for Elemental Burst
2. Attack with unarmed strikes — your attunement adds elemental damage to every hit
3. Flurry of Blows — 2-3 additional hits all carrying elemental damage
4. **Stunning Strike** — still your most powerful Ki spend at Level 5
5. **Elemental Burst** at Level 6 — when 3+ enemies are in range, 2 Ki for area damage
6. Level 11 disciplines — broaden your elemental toolkit with new applications

> *The Four Elements Monk is the subclass that looks the most dramatic on the battlefield.*
> *The VFX alone make it worth trying. The elemental damage on every strike makes it worth keeping.*

---

> ⚠️ **Element choice is permanent.** Choose carefully at character creation — your entire subclass scales around your attunement.

---

*For the full Monk class breakdown, see [[Monk]].*
*For other Monastic Traditions, see [[Way of the Open Hand]] · [[Way of Mercy]] · [[Way of the Kensei]].*

← [[Way of Mercy]] · [[Way of the Kensei]] →
