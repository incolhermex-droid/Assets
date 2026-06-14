![Mercy Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-banner.svg)

<div align="center">

![Mercy Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-badge.svg)

</div>

---

> *Mercy is not weakness. It is precision.*
> *The same hands that end a life can save one.*
> *The same knowledge of anatomy that kills can heal.*
> *That's not contradiction. That's mastery.*

---

## What Is the Way of Mercy?

The Way of Mercy is a **Monk subclass** built around duality — the same Ki that drives your strikes into enemies can be redirected to restore allies. The Mercy Monk is a **support-striker hybrid** that deals necrotic damage with every unarmed hit through Hand of Harm, heals with Hand of Healing at the same cost, and at Level 11 gains a full Flurry of Healing and Harm that turns a single Bonus Action into a triage + damage sequence.

This is the only Monk subclass in the mod that **actively supports allies** without sacrificing martial capability. The cost is Ki — always Ki — but the return on that Ki is uniquely flexible.

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## Class Features

### Progression Overview

| LEVEL | FEATURE |
|---|---|
| 3 | Hand of Harm · Hand of Healing · Implements of Mercy |
| 6 | Physician's Touch |
| 11 | Flurry of Healing and Harm |

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## Level 3 Features

### ☠️ Hand of Harm

*You know exactly where it hurts. You use that knowledge.*

When you hit a creature with an **unarmed strike**, you can spend **1 Ki Point** to deal additional **Necrotic damage** equal to `Martial Arts die + Wisdom modifier`.

Additionally, on a **critical hit**, Hand of Harm automatically applies the **POISONED** condition to the target.

> *Hand of Harm turns every unarmed strike into a necrotic drain. The Wisdom scaling means that Wisdom investment — already valuable for Ki save DC and AC — also increases your damage output. At 20 Wisdom, every Hand of Harm adds +5 necrotic on top of the Martial Arts die.*

---

### 💚 Hand of Healing

*The body wants to heal. You just remind it how.*

When you use the **Help action** or touch a willing creature, you can spend **1 Ki Point** to restore HP equal to `Martial Arts die + Wisdom modifier`.

> *Hand of Healing costs the same as Hand of Harm — 1 Ki Point — and returns the same amount: Martial Arts die + Wisdom modifier. The Mercy Monk's core identity is that this cost is identical. You choose every Ki point: harm or heal.*

---

### 🎭 Implements of Mercy

*You know what you're doing. You look like you know what you're doing.*

Gain proficiency in **Insight** and **Medicine** skills. Additionally gain proficiency with the **Herbalism Kit**.

> *Implements of Mercy makes you the party's medical authority. Medicine checks to stabilize downed allies, Insight to read enemies and NPCs, and Herbalism Kit for crafting healing items. The Mercy Monk is valuable outside of combat.*

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## Level 6 Features

### 🩺 Physician's Touch

*You've graduated from basic anatomy.*

Physician's Touch expands both Hand of Harm and Hand of Healing:

**Hand of Healing upgrade** — when you use Hand of Healing, it also **removes one of the following conditions** from the target:
- Poisoned
- Diseased
- Paralyzed
- Blinded

**Hand of Harm upgrade** — when you use Hand of Harm, it automatically applies the **POISONED** condition (previously only triggered on critical hits).

> *At Level 6, every Hand of Harm Poisons on hit — no critical required. And every Hand of Healing becomes a condition cleanse alongside the HP restore. The Mercy Monk becomes a full triage unit: remove conditions, restore HP, and deal necrotic damage all in the same combat sequence.*

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## Level 11 Features

### ⚡ Flurry of Healing and Harm

*Both. At the same time. This is what training looks like.*

Once per **Long Rest**, as a Bonus Action, you can use one of two options:

**Flurry of Healing** — Spend **2 Ki Points**: make two Hand of Healing touches as a Bonus Action, each restoring `Martial Arts die + Wisdom modifier` HP without spending additional Ki per touch.

**Flurry of Harm** — Spend **2 Ki Points**: trigger `HandOfHarmTurn` — a sequence of Hand of Harm applications as part of your Flurry of Blows, each dealing `Martial Arts die + Wisdom modifier` Necrotic + POISONED.

> *Flurry of Healing and Harm is the Level 11 payoff for the entire subclass. In one Bonus Action:*
> *— Two allies healed and condition-cleansed, or*
> *— Multiple enemies taking necrotic damage and being Poisoned.*
>
> *The once-per-Long-Rest limitation makes it a meaningful choice rather than a passive bonus. When you use it, it matters.*

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## 🔧 Technical Notes

The Mercy Monk implementation uses a Wisdom-scaling pattern identical to Warding Flare and Wholeness of Body:

```
Boosts: ActionResource(HandOfHarm,1,0);
IF(AbilityGreaterThan('Wisdom',13)):ActionResource(HandOfHarm,1,0);
IF(AbilityGreaterThan('Wisdom',15)):ActionResource(HandOfHarm,1,0);
...
```

Hand of Harm and Hand of Healing share the same damage/heal formula:
```
DealDamage(MartialArts+WisdomModifier, Necrotic)  // Harm
Heal(MartialArts+WisdomModifier)                   // Healing
```

The `FlurryOfHealingAndHarm` resource is flagged `LimitedUse:1` with Long Rest replenishment — strictly once per Long Rest regardless of Ki pool size.

![Mercy Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/mercy-divider.svg)

## 🎯 Playstyle Summary

The Way of Mercy is a **Ki-economy hybrid** that gives you genuine flexibility every combat turn.

**Your combat loop:**
1. **Attack** — standard unarmed strikes with Stunning Strike available
2. **Hand of Harm** — spend 1 Ki on a hit for Necrotic + Poison (guaranteed after Level 6)
3. **Flurry of Blows** — 2-3 unarmed strikes as Bonus Action
4. **Hand of Healing** — when allies need it, spend 1 Ki to heal + cleanse conditions
5. **Flurry of Healing and Harm** — once per Long Rest, triage multiple allies or devastate clustered enemies

> *The Mercy Monk never has a "wrong" Ki spend. Harm or heal — both are right. Which one is right depends on who needs it most.*

---

*For the full Monk class breakdown, see [[Monk]].*
*For other Monastic Traditions, see [[Way of the Open Hand]] · [[Way of the Four Elements]] · [[Way of the Kensei]].*

← [[Way of the Open Hand]] · [[Way of the Four Elements]] →
