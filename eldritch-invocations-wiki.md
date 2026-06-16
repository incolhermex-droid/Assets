![Eldritch Invocations Banner](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-banner.svg)

<div align="center">

![Eldritch Invocations Badge](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-badge.svg)

</div>

---

> *The pact gives you power. The invocations decide what you do with it.*
> *Every Warlock has Eldritch Blast. Not every Warlock has the same Eldritch Blast.*
> *Choose carefully. These choices define what kind of Warlock you are.*

---

## What Are Eldritch Invocations?

Eldritch Invocations are **permanent magical abilities** that the Warlock gains starting at **Level 1** — earlier than any other class gets their defining features. They are not spells. They don't cost spell slots. They are passive enhancements, active abilities, and identity-defining choices that stack and compound as you level.

In the 2024 PHB rework, **Pact Boons** (Blade, Chain, Tome) are now part of the Invocation system — chosen at Level 1 alongside your first Invocation rather than as a separate Level 3 feature. This means the Warlock's identity is locked in from the first level of play.

Every Warlock selects **1 Invocation at Level 1**, then gains additional choices at Levels 2, 5, 7, 9, and 12. The pool grows with each level — higher-level Invocations require minimum Warlock levels to access.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## Invocation Unlock Schedule

| WARLOCK LEVEL | INVOCATIONS UNLOCKED |
|---|---|
| **1** | Pact Boons + Level 1 pool |
| **2** | Level 2 pool (new choices available) |
| **5** | Level 5 pool (new choices available) |
| **7** | Level 7 pool (new choices available) |
| **9** | Level 9 pool (new choices available) |
| **12** | Level 12 pool — final tier |

> *The key change from the base game: at Level 1, you already choose a Pact Boon AND an Invocation. By Level 2, you have three choices active. The Warlock's full identity is present from the very first session.*

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 🔮 Level 1 Invocations

*Available from character creation. The foundation of your Warlock.*

### Pact Boons

**Pact of the Blade** (`PactOfTheBlade_Hex`)
Summon a magical pact weapon as a Bonus Action. The weapon uses **Charisma** for attack and damage rolls. Counts as a Warlock spell attack for all relevant features. Synergizes with **Thirsting Blade** (Level 5) for Extra Attack.

**Pact of the Chain** (`PactOfTheChain`)
Gain access to a powerful familiar beyond the standard Find Familiar options. Your familiar can Attack on your command, using your spell attack modifier. The Chain familiar has unique abilities unavailable to standard familiars.

**Pact of the Tome** (`PactOfTheTome`)
Gain a Book of Shadows granting **three additional cantrips** from any class list. These cantrips use Charisma as their spellcasting ability regardless of original class.

---

### General Invocations (Level 1)

**Armor of Shadows** (`ArmorOfShadows`)
Cast *Mage Armor* on yourself at will — no spell slot required. Your base AC becomes 13 + Dexterity modifier without needing physical armor.

**Beast Speech** (`BeastSpeech`)
Cast *Speak with Animals* at will. Communicate with beasts freely without spending a spell slot.

**Beguiling Influence** (`BeguilingInfluence`)
Gain proficiency in **Deception** and **Persuasion**. Your patron's influence makes you naturally compelling and deceptive.

**Eldritch Mind** (`EldritchMind`)
Gain **Advantage on Concentration saving throws**. Essential for any Warlock who relies on concentration spells in melee range.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## ⚡ Level 2 Invocations

*Available from Level 2. These define your combat style.*

**Agonizing Blast** (`AgonizingBlast`)
Add your **Charisma modifier** to the damage of every Eldritch Blast beam. At 20 Charisma, every beam deals +5 damage. With 2-4 beams at higher levels, this is the single most impactful Invocation for damage output.

**Devil's Sight** (`DevilsSight`)
See normally in magical and non-magical **darkness** up to 120 feet. Pairs devastatingly with *Darkness* spell — you fight normally, enemies are effectively blind.

**Eldritch Spear** (`EldritchSpear`)
Eldritch Blast's range increases to **300 feet**. The longest-range cantrip attack in the mod.

**Mask of Many Faces** (`MaskOfManyFaces`)
Cast *Disguise Self* at will — no spell slot required. Unlimited disguises for social and infiltration scenarios.

**Otherworldly Leap** (`OtherworldlyLeap`)
Cast *Jump* on yourself at will — no spell slot required. Your jump distance triples.

**Repelling Blast** (`RepellingBlast`)
When Eldritch Blast hits, push the target **10 feet** away from you. With multiple beams, this can push a target up to **40 feet** in one cast. Combined with ledges or environmental hazards, this is one of the most powerful control tools in the game.

> **Note on Repelling Blast interactions:** This invocation also interacts with *Thunderclap* — if the target is Large or smaller, `Force(3)` knockback applies on hit. And with the reworked *True Strike* (`TrueStrike_Ranged`), Repelling Blast triggers on the ranged attack variant as well.

**Thief of Five Fates** (`ThiefOfFiveFates`)
Cast *Bane* once per rest without expending a spell slot. Three targets roll saving throws with a -1d4 penalty on all future rolls for 1 minute.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 🌑 Level 5 Invocations

*Requires Warlock Level 5. These are the power-defining picks.*

**Thirsting Blade** (`ThirstingBlade`)
When you take the Attack action with your **Pact of the Blade weapon**, you can attack **twice** instead of once. This is Extra Attack for Blade Warlocks — essential for any melee build.

> *Thirsting Blade is implemented with three variants: `ThirstingBlade_Check` (validates Pact of Blade), `ThirstingBlade_Blade` (grants Extra Attack), `ThirstingBlade_Tome` (grants tome-based variant). The system ensures it only activates with a valid Pact weapon.*

**Eldritch Smite** (`EldritchSmite`)
When you hit with your Pact weapon, you can expend a Warlock spell slot to deal extra force damage and knock the target **Prone**. The damage scales with slot level.

**Investment of the Chain Master** (`InvestmentOfTheChainMaster`)
Your **Pact of the Chain** familiar gains significant power boosts — enhanced AC, attack bonuses, and new action options. Transforms the familiar from a utility tool into a genuine combat asset.

**Gift of the Depths** (`GiftOfTheDepths`)
Gain a **swimming speed** equal to your walking speed and the ability to breathe underwater. Cast *Water Breathing* once per rest without a spell slot.

**Book of Ancient Secrets** (`BookOfAncientSecrets`)
Cast any **ritual spell** from any class list without a spell slot, as long as you have the spell written in your Book of Shadows. Dramatically expands your out-of-combat utility.

**Mire the Mind** (`MireTheMind`)
Cast *Slow* once per rest using a spell slot. Six creatures reduced to half speed, -2 AC, -2 Dexterity saves, and limited actions for 1 minute.

**One with Shadows** (`OneWithShadows`)
When in **dim light or darkness**, become **Invisible** as an Action. The invisibility breaks if you move or take an action. Pairs with Devil's Sight for ambush potential.

**Sign of Ill Omen** (`SignOfIllOmen`)
Cast *Bestow Curse* once per rest using a Warlock spell slot. A powerful debuff that imposes Disadvantage or deals extra necrotic damage for up to 1 minute.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 👁️ Level 7 Invocations

*Requires Warlock Level 7.*

**Dreadful Word** (`DreadfulWord`)
Cast *Confusion* once per rest using a spell slot. Up to 8 creatures in a 10-foot radius act erratically for 1 minute — attacking allies, moving randomly, or doing nothing.

**Sculptor of Flesh** (`SculptorOfFlesh`)
Cast *Polymorph* once per rest using a spell slot. Transform a creature into a harmless beast — or yourself into something more useful for the current situation.

**Whispers of the Grave** (`WhispersOfTheGrave`)
Cast *Speak with Dead* at will — no spell slot required. Unlimited conversations with corpses for information gathering.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 💀 Level 9 Invocations

*Requires Warlock Level 9.*

**Lifedrinker** (`Lifedrinker`)
When you hit with your Pact weapon, deal additional **Necrotic damage** equal to your Charisma modifier. Passive, always active, no resource cost. The highest sustained damage passive for Blade Warlocks.

**Gift of the Protectors** (`GiftOfTheProtectors`)
When an ally drops to 0 HP, they instead drop to **1 HP** — once per rest. Passive life insurance for the entire party.

**Minions of Chaos** (`MinionsOfChaos`)
Cast *Conjure Elemental* once per rest using a spell slot. Summon a powerful elemental to fight alongside you for 1 hour.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## ⚔️ Level 12 Invocations

*Requires Warlock Level 12. The final tier.*

**Devouring Blade** (`DevouringBlade`)
The pinnacle Blade Warlock Invocation. Enhances your Pact weapon attacks with additional effects — the weapon literally consumes what it strikes, dealing enhanced damage and applying debilitating conditions.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 🔧 Technical Notes

The Invocation system was completely restructured in commit `0f63458` — a **unified PassiveList pool** replaces the old level-gated separate lists:

**Before:** Separate passive lists per level tier (Level 2 pool, Level 5 pool, etc.) with `MergedInto` chains.

**After:** A single master pool `ab56f79f` ("5.5 Warlock invocations 12") that contains **all invocations simultaneously**. The `SelectPassives` call at each level pulls from this unified pool, and the game filters by prerequisites internally.

```
Level 1: SelectPassives(8d8ac513, 1, WarlockInvocations)  — 1 pick from full pool
Level 2: SelectPassives(ab56f79f, 2, WarlockInvocations)  — 2 picks from master pool
Level 5: SelectPassives(ab56f79f, 2, WarlockInvocations)  — 2 more picks
Level 7: SelectPassives(ab56f79f, 1, WarlockInvocations)  — 1 more pick
Level 9: SelectPassives(ab56f79f, 1, WarlockInvocations)  — 1 more pick
Level 12: (DevouringBlade available in pool)
```

Additionally, **Magical Cunning** (`Shout_MagicalCunning`) was added as a spell at Level 2 via a new spell list entry — giving it a proper UI presence rather than being a hidden passive.

The **Pact Boon** was removed from the Level 3 `SelectPassives(PactBoon)` selector and moved into the Level 1 Invocation pool — meaning Pact Boon is now selected at Level 1 as part of your first Invocation choice.

![Eldritch Invocations Divider](https://raw.githubusercontent.com/incolhermex-droid/Assets/refs/heads/main/eldritch-invocations-divider.svg)

## 🎯 Build Recommendations

**Eldritch Blast Builds:**
- `Agonizing Blast` + `Repelling Blast` — the classic combination. Every beam pushes and deals Charisma-scaled bonus damage.
- Add `Devil's Sight` + cast *Darkness* on yourself — you're untouchable in the cloud.
- Add `Eldritch Spear` for 300-foot range — snipe from safety.

**Blade Pact Builds:**
- `PactOfTheBlade` + `ThirstingBlade` (Level 5) + `Lifedrinker` (Level 9) — the complete martial Warlock kit.
- Add `Eldritch Smite` for burst damage and knockdown.
- `DevouringBlade` at Level 12 is the payoff.

**Utility Builds:**
- `PactOfTheTome` + `BookOfAncientSecrets` — ritual casting from any class list.
- `ArmorOfShadows` + `OneWithShadows` — free AC and free invisibility in darkness.
- `BeguilingInfluence` + `MaskOfManyFaces` — the ultimate social infiltrator.

---

*For the full Warlock class breakdown, see [[Warlock]].*
*For Patron-specific features, see [[Archfey Patron]] · [[Celestial Patron]] · [[Fiend Patron]] · [[Great Old One Patron]] · [[Hexblade Patron]] · [[Undead Patron]].*

← [[Warlock]] · [[Archfey Patron]] →
