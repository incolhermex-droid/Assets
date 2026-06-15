![Great Old One Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-banner.svg)

<div align="center">

![Great Old One Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-badge.svg)

</div>

---

> *Most patrons are powerful. Archfey. Fiends. Celestials.*
> *Your patron is older than the concept of power.*
> *It noticed you first. That's the part they never mention.*

---

## What Is the Great Old One Patron?

The Great Old One Patron is a **Warlock subclass** built around a pact with an entity of incomprehensible age and alien intelligence — Cthulhu, an Elder Brain, an Aboleth of cosmic proportions, or something that doesn't have a name because nothing survived the encounter to give it one.

Where other Warlocks fight with fire, shadow, or radiant light, the Great Old One Patron Warlock **unravels the minds of enemies**. **Eldritch Hex** at Level 10 lets you choose which ability score to debilitate — imposing Disadvantage on all checks and saving throws for that stat. **Entropic Ward** gives you a reaction slot-burning ward that neutralizes attacks. **Thought Shield** makes you resistant to psychic damage and reflects it back at attackers.

This is the most **mind-focused, debilitation-oriented** Warlock subclass in the mod.

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Great Old One Spells · Dark One's Own Luck · Fiendish Resilience |
| 6 | Entropic Ward |
| 10 | Thought Shield · Eldritch Hex · Hex (always prepared) |

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## Level 3 Features

### 📜 Great Old One Spells

Your Patron grants an always-prepared spell list that doesn't count against your Pact Magic limit. *(Spell list entries from mod implementation.)*

---

### 🎲 Dark One's Own Luck

*The void tilts in your favor. Don't ask why.*

`DarkOnesOwnLuck` — once per rest, when you make an ability check or saving throw, you can add **1d10** to the roll after seeing the initial result.

> *Dark One's Own Luck is the Great Old One's signature gift — a guaranteed +1 to +10 on any check or save, declared after the dice hits the table. It turns near-misses into successes and failed saves into narrow victories.*

---

### 🛡️ Fiendish Resilience

*Something from beyond the stars is watching over you. The sensation is unsettling.*

`FiendishResilience` — choose one damage type after completing a rest. You gain **Resistance to that damage type** until your next rest.

> *Fiendish Resilience is adaptive armor — you choose what to resist based on what you expect to face. Fire for the dragon encounter. Psychic for the mindflayer. Cold for the undead dungeon. It rewards planning and pays off when the encounter matches your prediction.*

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## Level 6 Features

### ⚡ Entropic Ward

*They aimed at you. The cosmos disagreed.*

`EntropicWard` — a **reaction interrupt** with three variants, each costing a Warlock Spell Slot of the corresponding level:

```
Interrupt_EntropicWard   (base)
Interrupt_EntropicWard_3 — Cost: ReactionActionPoint:1;WarlockSpellSlot:1:3
Interrupt_EntropicWard_4 — Cost: ReactionActionPoint:1;WarlockSpellSlot:1:4
Interrupt_EntropicWard_5 — Cost: ReactionActionPoint:1;WarlockSpellSlot:1:5
```

- **Trigger:** A creature makes an attack roll against you
- **Cost:** Your Reaction + one Warlock Pact Magic slot (Level 3, 4, or 5)
- **Effect:** The attack is made with **Disadvantage**
- **On Miss:** You gain **Advantage** on your next attack roll against that creature

> *Entropic Ward is expensive — it costs a Pact Magic slot, which are precious. But the payoff is significant: Disadvantage on an incoming attack, and if it misses, Advantage on your next attack. Against high-accuracy enemies, spending a slot to negate a likely hit is a sound trade.*
>
> *The three slot levels (3/4/5) let you choose how much investment you make — though the effect is identical regardless of slot level.*

The passive `EntropicWard` unlocks all four interrupts simultaneously:
```
Boosts: UnlockInterrupt(Interrupt_EntropicWard);
        UnlockInterrupt(Interrupt_EntropicWard_3);
        UnlockInterrupt(Interrupt_EntropicWard_4);
        UnlockInterrupt(Interrupt_EntropicWard_5);
        ActionResource(Interrupt_EntropicWard_Charge,1,0)
```

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## Level 10 Features

### 🧠 Thought Shield

*They tried to reach your mind. They found something else in there.*

`Thought_Shield_Psychic_Resistance` — a permanent passive with two distinct effects:

```
Boosts: Resistance(Psychic,Resistant);
        RedirectDamage(1,,Psychic,true)
```

**Effect 1 — Psychic Resistance:** You have Resistance to Psychic damage — all psychic damage taken is halved.

**Effect 2 — Psychic Reflection:** When you take Psychic damage, **1 point of that damage** is redirected back to the attacker.

> *Thought Shield makes the Great Old One Patron Warlock the hardest target for psychic attacks in the game. Mindflayers, Intellect Devourers, psionic enemies — all deal halved damage and take reflected damage in return. The reflection is 1 point per hit, not per session — meaningful in fights with many psychic hits.*

---

### 👁️ Eldritch Hex

*You look into their mind and pick which part to break.*

`GreatOldOne_10_EldritchHex` — the defining Level 10 feature. When you apply **Hex** to a target, you choose one of six **Eldritch Hex variants** to inflict alongside it:

| VARIANT | STATUS | EFFECT |
|---|---|---|
| **Eldritch Hex: Strength** | `ELDRITCH_HEX_STRENGTH` | Disadvantage on all Strength checks AND Strength saves |
| **Eldritch Hex: Dexterity** | `ELDRITCH_HEX_DEXTERITY` | Disadvantage on all Dexterity checks AND Dexterity saves |
| **Eldritch Hex: Constitution** | `ELDRITCH_HEX_CONSTITUTION` | Disadvantage on all Constitution checks AND Constitution saves |
| **Eldritch Hex: Intelligence** | `ELDRITCH_HEX_INTELLIGENCE` | Disadvantage on all Intelligence checks AND Intelligence saves |
| **Eldritch Hex: Wisdom** | `ELDRITCH_HEX_WISDOM` | Disadvantage on all Wisdom checks AND Wisdom saves |
| **Eldritch Hex: Charisma** | `ELDRITCH_HEX_CHARISMA` | Disadvantage on all Charisma checks AND Charisma saves |

Additionally at Level 10, **Hex** is added to your always-prepared spell list via a dedicated spell list entry — meaning you never need to use a spell prepared slot on it.

> *Eldritch Hex is a surgical debilitation tool. Every variant targets both ability checks AND saving throws for that stat — not one or the other, both.*
>
> *Constitution Hex: the enemy has Disadvantage on Concentration saves. Your party's spells last longer.*
> *Wisdom Hex: Disadvantage on Perception, Insight, and Wisdom saves. Charm and Fear effects become dramatically more reliable.*
> *Strength Hex: Disadvantage on Athletics and Strength saves. Grapples fail. Shoves fail.*
>
> *Choose based on the enemy. Every fight has a right answer.*

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## 🔧 Technical Notes

This commit (b337c55) introduced **14 files** and **349 additions, 62 modifications**:

- `SpellLists.tbl` — New entry: "Warlock The Great Old One Level 10" — adds `Target_Hex` to always-prepared list
- `Progressions.tbl` — Level 10 updated: replaced `Thought_Shield_Psychic_Reflection` with `GreatOldOne_10_EldritchHex` + `AddSpells` selector for Hex spell list
- `Interrupt.stats` — 3 new interrupts: `Interrupt_EntropicWard_3/4/5` (extending base EntropicWard, each with different slot cost)
- `Passive.stats` — 5 new passives: `DarkOnesOwnLuck` · `FiendishResilience` · `EntropicWard` · `GreatOldOne_10_EldritchHex` · `Thought_Shield_Psychic_Resistance`
- `Status_BOOST.stats` — 6 new status effects: `ELDRITCH_HEX_STRENGTH/DEXTERITY/CONSTITUTION/INTELLIGENCE/WISDOM/CHARISMA`
- `Status_BOOST.stats` — 2 bug fixes: removed leading whitespace from `OnApplyFunctors` in Dark One's Blessing statuses
- `english.xml` — Complete localization

Key implementation detail — **Eldritch Hex status structure:**
```
ELDRITCH_HEX_STRENGTH:
  Boosts: Disadvantage(Ability, Strength);Disadvantage(SavingThrow, Strength)

ELDRITCH_HEX_CONSTITUTION:
  Boosts: Disadvantage(Ability, Constitution);Disadvantage(SavingThrow, Constitution)
```
Each variant applies **two separate Disadvantage boosts** — one for ability checks, one for saving throws. This means the debilitation is complete: no roll using that ability score is exempt.

![Great Old One Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/great-old-one-divider.svg)

## 🎯 Playstyle Summary

The Great Old One Patron is a **psychic debilitator** that wins by making enemies less capable rather than by dealing direct damage.

**Your combat identity:**
1. **Hex** — always prepared at Level 10; the foundation of your kit
2. **Eldritch Hex** — choose your variant based on the enemy's key stat; Constitution for casters, Strength for melee, Wisdom for smart enemies
3. **Dark One's Own Luck** — once per rest safety net for critical ability checks or saves
4. **Fiendish Resilience** — pre-combat damage type resistance based on what you expect
5. **Entropic Ward** — expensive but decisive when a hit would cost too much; Disadvantage on the attack + Advantage on your next
6. **Thought Shield** — passive psychic resistance + reflection; mindflayer encounters become trivially easier

> *The Great Old One Patron doesn't ask: "How much damage can I deal?"*
> *It asks: "What can my enemy no longer do?"*
> *By Level 10, the answer is: whatever stat you chose. Completely.*

---

*For other Warlock Patrons, see [[Warlock]].*
*For the full class list, see [[Classes]].*

← [[Warlock]] · [[Hexblade Patron]] →
