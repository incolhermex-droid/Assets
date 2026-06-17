![Fiend Patron Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-banner.svg)

<div align="center">

![Fiend Patron Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-badge.svg)

</div>

---

> *Hell doesn't give power freely. But the terms were acceptable. To you, at least.*
> *Every enemy that falls near you feeds your patron's gift.*
> *That's not a coincidence. That's the contract working as intended.*

---

## What Is the Fiend Patron?

The Fiend Patron is a **Warlock subclass** built around a pact with a being from the Lower Planes — a Pit Fiend, a Balor, an Archdevil, or another entity of infernal power. Where the Celestial heals and the Archfey teleports, the Fiend Patron Warlock **feeds on death** — every nearby kill strengthens you, and your patron's luck occasionally bends impossible rolls in your favor.

This subclass centers on **Dark One's Blessing** — a passive that grants Temporary HP whenever an enemy dies near you — alongside **Dark One's Own Luck** (a guaranteed bonus to a critical roll once per rest) and **Fiendish Resilience** (adaptive damage resistance). Together, these features make the Fiend Patron one of the most **survivable** Warlock subclasses, sustained directly by combat itself.

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Fiend Spells · Dark One's Blessing |
| 6 | Dark One's Own Luck |
| 10 | Fiendish Resilience |

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## Level 3 Features

### 📜 Fiend Spells

Your Patron grants an always-prepared spell list that doesn't count against your Pact Magic limit — themed around fire, darkness, and infernal destruction.

---

### 🔥 Dark One's Blessing

*Something dies nearby. You feel stronger. Don't think about why too hard.*

Your signature Level 3 feature — a **reaction interrupt** that triggers automatically:

```
Interrupt_DarkOnesBlessings
Trigger: OnDeath (Nearby scope, 3 meters / 10 ft)
Condition: Dead character is an enemy AND within range of observer
Effect: ApplyStatus(OBSERVER_OBSERVER, DARK_ONES_BLESSING, 100, -1)
Temporary HP: Charisma modifier + Warlock level
```

**Critical bug fix (commit `a490212`):** The original implementation incorrectly applied the Temporary HP boost to `SELF` — meaning the **dead enemy** received the buff instead of the observing Warlock. This was corrected so the status correctly targets `OBSERVER_OBSERVER`, ensuring the Warlock who witnessed the kill is the one who gains Temporary HP.

> *Dark One's Blessing means every enemy that dies within 10 feet of you makes you tankier. In a fight against multiple weak enemies, this can stack significant Temporary HP before the encounter even reaches its midpoint. The closer you fight, the more you benefit — this is a Fiend Patron that wants to be near the action, not behind it.*

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## Level 6 Features

### 🎲 Dark One's Own Luck

*The void tilts in your favor. Don't ask why.*

Once per rest, when you make an ability check or saving throw, you can add **1d10** to the roll **after seeing the initial result**.

> *Dark One's Own Luck is a guaranteed safety net — declared after the dice lands, so you only use it when you know it's needed. A failed Concentration save becomes a success. A narrow miss on a Death saving throw becomes a stabilization. One use per rest means it has to count.*

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## Level 10 Features

### 🛡️ Fiendish Resilience

*Something from beyond is watching over you. The sensation is unsettling.*

Choose one damage type after completing a rest. You gain **Resistance to that damage type** until your next rest.

> *Fiendish Resilience is adaptive armor based on prediction. Walking into a dragon's lair? Choose its breath damage type. Heading into an undead crypt? Choose Necrotic. The Fiend Patron rewards scouting and planning — choose correctly and an entire encounter becomes half as dangerous.*

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## 🔧 Technical Notes

The Dark One's Blessing fix (commit `a490212`) is a clean example of targeting precision in status application:

**Before the fix:**
```
OnDeath trigger → ApplyStatus(SELF, DARK_ONES_BLESSING, 100, -1)
```
`SELF` in an `OnDeath` interrupt context refers to the **dying entity**, not the observer. This meant the buff was applied to a corpse — functionally wasted.

**After the fix:**
```
OnDeath trigger → ApplyStatus(OBSERVER_OBSERVER, DARK_ONES_BLESSING, 100, -1)
```
`OBSERVER_OBSERVER` correctly targets the entity that is observing the death event — the Warlock with the Dark One's Blessing passive. The fix required understanding the distinction between the event's "self" (the dying creature) and the "observer" (the Warlock watching it die) within the interrupt's context scope.

This fix (along with whitespace corrections to two related `OnApplyFunctors` blocks) was bundled into the same commit that also added the **Eldritch Hex** system to the Great Old One Patron — both changes touched the same `Status_BOOST.stats` file.

![Fiend Patron Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/fiend-patron-divider.svg)

## 🎯 Playstyle Summary

The Fiend Patron is a **sustain-through-combat Warlock** that grows tankier the longer a fight against multiple enemies continues.

**Your combat identity:**
1. **Position aggressively** — Dark One's Blessing only triggers within 10 feet of enemy deaths; staying at range means missing the buff
2. **Eldritch Blast + Agonizing Blast/Repelling Blast** — your primary damage tool, same as any Warlock
3. **Dark One's Blessing** — passive Temporary HP accumulation as enemies fall around you
4. **Dark One's Own Luck** at Level 6 — save it for the roll that actually matters
5. **Fiendish Resilience** at Level 10 — predict the encounter's primary damage type and resist it for the whole rest period

> *The Fiend Patron doesn't need careful resource management to survive.*
> *It needs enemies to die near it. The deal handles the rest.*

---

*For other Warlock Patrons, see [[Warlock]].*
*For the full class list, see [[Classes]].*

← [[Archfey Patron]] · [[Great Old One Patron]] →
