![Knowledge Domain Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-banner.svg)

<div align="center">

![Knowledge Domain Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-badge.svg)

</div>

---

> *Every mind is a library. Every secret is a door.*
> *Your god didn't give you a sword. They gave you a key.*
> *They think because you wear armor you don't understand the mind. They're wrong.*

---

## What Is the Knowledge Domain?

The Knowledge Domain is a **Cleric subclass** built around the divine gift of understanding — the ability to read minds, unravel secrets, and turn information into power. Where other Domains give Clerics weapons of destruction or shields of protection, the Knowledge Domain gives you something more dangerous: **clarity**.

This is the most **versatile and intellectually powerful** Cleric subclass in the mod. You gain Expertise in two skills at Level 3, access to some of the best psychic spells in the game, and at Level 6, a feature that fundamentally changes how your spells interact with enemy minds.

This is a **full progression subclass** with features at Levels 3, 5, 6, 7, and 9, and a spell list that includes two spells — **Mind Spike** and **Synaptic Static** — that no other Cleric Domain can access.

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 1 | Blessings of Knowledge |
| 3 | Knowledge Domain Spells · Mind Magic · Skills Expertise |
| 5 | Knowledge Domain Spells (expanded) |
| 6 | Unfettered Mind |
| 7 | Knowledge Domain Spells (expanded) |
| 9 | Knowledge Domain Spells (expanded) |

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## Level 1 Features

### 📚 Blessings of Knowledge

*Your god's first gift is understanding. Everything else follows from there.*

At Level 1, before you even choose spells, you gain proficiency in two languages and proficiency in two of the following skills: **Arcana · History · Nature · Religion**.

More importantly, you gain **Expertise** in those same two skills — doubling your proficiency bonus on those checks.

> *From Level 1, you are the party's authority on arcane, historical, natural, and religious knowledge. Not just competent — expert. Before combat even starts, you've already provided value.*

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## Level 3 Features

### 📜 Knowledge Domain Spells

Your Domain grants an expanding spell list that is **always prepared** and doesn't count against your limit:

| CLERIC LEVEL | SPELLS ADDED |
|---|---|
| 3 | Calm Emotions · Detect Thoughts · Mind Spike · Command · Sleep |
| 5 | Counterspell · Blink · Speak with Dead |
| 7 | Banishment · Confusion |
| 9 | Dominate Person · Synaptic Static |

> **12 spells total** — and two of them, **Mind Spike** and **Synaptic Static**, are exclusive to this Domain. No other Cleric subclass gets access to them as Domain spells.

**Mind Spike** (Level 2) deals psychic damage and reveals the target's location — it cuts through invisibility and hiding. **Synaptic Static** (Level 5) is a psychic explosion that impairs concentration and forces a penalty die on all subsequent ability checks. These are among the best psychic spells in the game, and the Knowledge Domain Cleric is the only Cleric who has them always prepared.

---

### 🧠 Mind Magic

*The mind is a weapon. You just learned how to aim it.*

A passive gained at Level 3 that enhances your psychic and enchantment spells. Mind Magic gives your mind-affecting spells additional potency — targets that fail their saves against your psychic effects suffer compounded consequences beyond the initial effect.

---

### 🎓 Skills Expertise

At Level 3, in addition to the skills from Blessings of Knowledge, you choose **2 additional skills** from any list and gain **Expertise** in them as well.

> *By Level 3, a Knowledge Domain Cleric can have Expertise in 4 skills. That is more skill mastery than most dedicated skill classes achieve at this level.*

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## Level 6 Features

### 👁️ Unfettered Mind

*You don't just read the battlefield. You read the people on it.*

`Knowledge_6_UnfetteredMind` — the defining Level 6 feature of the Domain.

Unfettered Mind enhances your Channel Divinity and psychic spells with a persistent mind-reading aura. When you use **Read Thoughts** (your Channel Divinity option), you can now:

- Probe the surface thoughts of a creature within 60 feet
- Force a Wisdom saving throw — on a failure, the creature is **Charmed** by you for 1 minute
- While Charmed, you can ask questions and the creature must answer them honestly
- If the creature passes the save, you can't use this feature on them again for 24 hours

> *Unfettered Mind turns information gathering into battlefield control. A Charmed creature doesn't attack you. It answers your questions. In the right encounter, this feature ends a fight without a single spell slot spent.*

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## 🔧 Technical Notes

This commit introduced **9 files** and **482 lines** of implementation:

- `SpellLists.tbl` — 7 new spell list entries for Knowledge Domain (Levels 1, 3, 5, 7, 9 + Channel Divinity list + Level 6 list)
- `Progressions.tbl` — Full progression from Level 1 to 9 + UUID `ebe18794` registered in Cleric Level 2 SubClasses list
- `Passive.stats` — 2 new passives: `Knowledge_3_MindMagic` · `Knowledge_6_UnfetteredMind`
- `Interrupt.stats` — Interrupt logic for Unfettered Mind's reaction to mind-affecting spells
- `Status_BOOST.stats` — Status effects for Mind Magic and Unfettered Mind
- `Target.stats` — New spell: `Target_MindSpike` added to the game
- `Cleric.khn` — Script integration for the Knowledge Domain's Channel Divinity logic
- `english.xml` — Complete localization for all features

Key implementation detail — **Synaptic Static cross-class addition**:
```
Bard SLevel 5 List → added Target_SynapticStatic
```
This commit also added Synaptic Static to the **Bard's Level 5 spell list** — meaning the Knowledge Domain Cleric and the Bard are now the two classes with this spell as an always-available option.

![Knowledge Domain Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/knowledge-domain-divider.svg)

## 🎯 Playstyle Summary

The Knowledge Domain is a **psychic controller and skill powerhouse** that rewards preparation, positioning, and reading the encounter before it starts.

**Your combat identity:**
1. **Out-of-combat** — your Expertise makes you the party's authority on information. You know what the enemy is, what it's immune to, and what its weaknesses are before combat starts
2. **Opening turns** — Detect Thoughts or Command to disrupt enemy action economy; Sleep against low-HP clusters; Calm Emotions to neutralize casters
3. **Mid-combat** — Mind Spike to track invisible or hiding targets; Synaptic Static at Level 9 to impair an entire cluster's concentration and action quality
4. **Channel Divinity** — Unfettered Mind to charm a priority target and extract information or remove them from the fight entirely
5. **Late game** — Dominate Person as an always-prepared option makes any humanoid a potential asset rather than a threat

> *You don't need to kill everything in the room.*
> *You need to know which ones to kill, which ones to charm, and which ones to ask nicely.*
> *With the Knowledge Domain, you know all three before initiative is even rolled.*

---

*For other Cleric Domains, see [[Cleric]].*
*For the full class list, see [[Classes]].*

← [[Grave Domain]] · [[Cleric]] →
