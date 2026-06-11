![Apocalypse Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-banner.svg)

<div align="center">

![Apocalypse Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-badge.svg)

</div>

---

> *Other Clerics pray for peace. For healing. For guidance.*
> *You received a vision of the end — and you said yes.*
> *They didn't ask for salvation. They asked for an ending. You deliver.*

---

## What Is the Apocalypse Domain?

The Apocalypse Domain is a **Cleric subclass** built around one idea: total annihilation. Where other Domains give Clerics tools to support, control, or protect, the Apocalypse Domain gives you a countdown — and everything in its path gets erased.

This is the most **offensive Cleric subclass in the mod**. Your spell list is a catalog of destruction. Your Channel Divinity locks enemies in place. Your Level 6 feature turns death into a chain reaction. You are not here to keep anyone alive. You are here to make sure nothing is left standing.

This is a **full progression subclass** with features at Levels 3, 5, 6, 7, and 9, and one of the most aggressive expanded spell lists in the entire class roster.

![Apocalypse Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Apocalypse Domain Spells · Visions of Annihilation · Doom Song |
| 5 | Apocalypse Domain Spells (expanded) |
| 6 | All Will Be Dust |
| 7 | Apocalypse Domain Spells (expanded) |
| 9 | Apocalypse Domain Spells (expanded) |

![Apocalypse Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-divider.svg)

## Level 3 Features

### 📜 Apocalypse Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit. Every spell on this list is a weapon:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Darkness · Hellish Rebuke · Phantasmal Force · Thunderwave |
| 5 | Hunger of Hadar · Fear |
| 7 | Blight · Ice Storm |
| 9 | Cloudkill · Insect Plague |

> **10 spells of pure destruction** — darkness, terror, poison, ice, and plague. From Level 3, you have tools that most Clerics never see. From Level 9, you're dropping Cloudkill and Insect Plague as always-prepared options.

---

### 👁️ Visions of Annihilation

*The apocalypse isn't coming. You're showing them what it looks like.*

A new action resource — `VisionsOfAnnihilation` — that replenishes on rest. This resource powers your Channel Divinity and other Apocalypse features, representing the overwhelming psychic weight of the end you've witnessed.

---

### 🎵 Doom Song

*You open your mouth and what comes out isn't words. It's the sound of everything ending.*

Your **Channel Divinity** option at Level 3. Doom Song projects the apocalyptic visions burned into your mind outward, locking enemies in place with pure terror and dread.

- **Trigger:** Use Channel Divinity as an action
- **Effect:** Creatures in range that fail their saving throw are **paralyzed** or **restrained** by visions of annihilation — they see how they die, and for a moment, they believe it
- **Save:** Wisdom against your Spell Save DC

> *Most Channel Divinity options are support tools. Doom Song is a lockdown. In the right encounter, it ends a fight before it starts.*

![Apocalypse Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-divider.svg)

## Level 6 Features

### 💀 All Will Be Dust

*Every death feeds the next one. That's not a threat. That's cosmology.*

The defining feature of the Apocalypse Domain — and one of the most powerful Level 6 features in the mod.

When a creature **dies within range**, `AllWillBeDust` triggers automatically:
- The death releases a pulse of annihilation energy
- Nearby creatures take damage and may be pushed, frightened, or debilitated
- The effect chains — if the pulse kills another creature, it triggers again

> *All Will Be Dust turns a battlefield into a cascade. One kill becomes two. Two becomes four. In a fight with clustered enemies, this feature can clear a room by itself. The apocalypse isn't a single event — it's a sequence. And it starts with the first body.*

This passive is **always active** — no charges, no action cost, no decisions. It simply fires every time something near you dies.

![Apocalypse Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **18 files** and **709 lines** of implementation:

- `ActionResourceDefinitions` — New resource: `VisionsOfAnnihilation`
- `SpellLists` — 4 spell lists (SLevel 2–5) with Domain spells at Levels 3, 5, 7, and 9
- `Progressions` — Features delivered at Levels 3, 5, 6, 7, and 9 + UUID `4d7bc9f4` registered in Cleric subclass selector
- `Passive.stats` — 3 new passives: `Apocalypse_3_VisionsOfAnnihilation` · `Apocalypse_3_DoomSong` · `Apocalypse_6_AllWillBeDust`
- `Status_BOOST.stats` — Status effects for Doom Song's lockdown conditions
- `Spell_Target.stats` — Targeting logic for Doom Song's area
- `english.xml` — Complete localization for all features
- `README_Class_Cleric.MD` — Updated with Apocalypse Domain documentation

Key implementation detail on the **subclass registration**:
```
SubClasses: 4d7bc9f4-526f-4902-b9a2-b31577203d02 (ApocalypseDomain)
            added to the Cleric Level 2 progression SubClasses list
```
The Apocalypse Domain UUID was inserted at the **front** of the SubClasses list — meaning it appears first in the subclass selection screen at character creation.

![Apocalypse Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/apocalypse-domain-divider.svg)

## 🎯 Playstyle Summary

The Apocalypse Domain is a **pure offense Cleric** with a chain-reaction passive that rewards aggressive positioning and kill sequencing.

**Your combat identity:**
1. Open with **Doom Song** — lock down clustered enemies before they can act
2. Blast with Domain spells — Hunger of Hadar at Level 5 creates a zone of terror and blindness, Fear at the same level pushes enemies into your kill zone
3. Land the first kill — **All Will Be Dust** fires and the cascade begins
4. Control the sequence — position yourself so each death triggers the next
5. At Level 9, drop **Cloudkill** or **Insect Plague** into a locked-down cluster and watch All Will Be Dust chain through the aftermath

> *Other Clerics ask: "How do I keep my party alive?"*
> *You ask: "How many of them can I kill before my turn ends?"*
>
> *The answer is: more than they expected.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Cleric]] · [[Grave Domain]] →
