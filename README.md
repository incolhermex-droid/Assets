# 🎨 DnD 5.5e All-in-One BEYOND — Documentation & Visual Identity

> A complete documentation system and visual identity built from scratch for the [DnD 5.5e All-in-One BEYOND](https://mod.io/g/baldursgate3/m/dnd55e) mod for Baldur's Gate 3 — one of the most comprehensive ruleset overhaul mods on the platform.

---

## 👤 About This Repository

This repository is the original source of the **wiki structure, technical documentation, and SVG visual identity** for the DnD 5.5e All-in-One BEYOND mod, authored and maintained by **[@incolhermex-droid](https://github.com/incolhermex-droid)** — Social Communicator & Journalist, and Spanish localization lead for the mod.

What started as a translation role grew into a full documentation initiative: reading the mod's actual commit history and source code, translating technical implementation details into clear player-facing explanations, and designing a consistent visual system to support it — all without the mod's author requesting it. The wiki pages, class breakdowns, subclass deep-dives, and every banner in this repository were built page by page, commit by commit, over **100+ commits** of iterative work.

This repo serves as the permanent, timestamped record of that work.

---

## 📚 What's Inside

| CATEGORY | CONTENTS |
|---|---|
| **Wiki Pages** | Full `.md` breakdowns for every documented class and subclass — Cleric (8 Domains), Warlock (6 Patrons + Eldritch Invocations), Monk (4 Traditions), Gunslinger (3 Archetypes), and more |
| **Banners** | 25+ custom SVG banners, one per class/subclass, each with a unique color identity matching its thematic role |
| **Badges & Dividers** | Matching badge and divider SVGs for consistent visual structure across every wiki page |
| **Mod Descriptions** | Full mod.io/Nexus description (`dnd55e_FINAL.md`) and plain-text in-game mod manager description (`dnd55e_INGAME.txt`) |
| **Class Suggestion Docs** | Standalone `.md` proposals for Gunslinger and Illrigger class documentation |

Every wiki `.md` file in this repository was written by directly reading the mod's GitHub commit diffs — actual `.stats`, `.khn`, and localization file changes — and translating that implementation into structured, readable documentation with technical accuracy notes for advanced users.

---

## 📁 Repository Structure

```
Assets/
├── banners/                          ← Legacy section-divider banners (mod.io description)
│   ├── 01_header.svg
│   ├── 02_core_rules.svg
│   └── ... (13 total)
│
├── [class]-banner.svg                ← Wiki page banner, one per class/subclass
├── [class]-badge.svg                 ← Matching badge
├── [class]-divider.svg               ← Matching section divider
├── [class]-wiki.md                   ← Full wiki page content
│
├── dnd55e_FINAL(Mod.io and Nexus).md ← Full rich-text mod description
├── dnd55e_INGAME.txt                 ← Plain-text in-game description
└── README.md
```

---

## 🧩 Classes & Subclasses Documented

<details>
<summary><strong>📋 Click to expand the full documentation index</strong></summary>

### Cleric
- General class breakdown
- Apocalypse Domain · Astral Domain (original, mod-exclusive) · Grave Domain · Knowledge Domain · Life Domain · Light Domain · Trickery Domain · War Domain

### Warlock
- General class breakdown
- Archfey Patron · Celestial Patron · Fiend Patron · Great Old One Patron · Hexblade Patron · Undead Patron
- Eldritch Invocations (full system breakdown, 20+ invocations)

### Monk
- General class breakdown
- Way of the Open Hand · Way of Mercy · Way of the Four Elements · Way of the Kensei

### Gunslinger *(original class)*
- General class breakdown
- High Roller · Spellslinger · White Hat

### Other Systems
- Spell Scroll Restrictions (full class-by-spell breakdown)
- Creatures (Monster Manual 2024 conversions)

</details>

Each page includes: feature breakdowns by level, exact mechanical formulas pulled from source code, technical implementation notes, and a playstyle summary written for players evaluating the build.

---

## 🔗 Usage

All banners are standalone SVG files — lightweight, scalable, no external dependencies.

```markdown
![banner name](https://raw.githubusercontent.com/incolhermex-droid/Assets/main/[filename].svg)
```

> Replace `main` with a specific commit hash for a permanent permalink to a frozen version.

---

## 🎨 Visual Identity System

Every class and subclass has a distinct color identity, designed to be immediately recognizable while maintaining a consistent layout structure (ornamental corners, gradient borders, stat rows, and italicized taglines) across the entire collection:

| THEME | EXAMPLES |
|---|---|
| Divine gold | Cleric, Light Domain |
| Crimson/blood | War Domain, Apocalypse Domain |
| Void purple | Warlock, Hexblade Patron, Eldritch Invocations |
| Cosmic green | Great Old One Patron |
| Corpse green | Undead Patron |
| Fey emerald | Archfey Patron |
| Hellfire orange | Fiend Patron |
| Steel/frost | Way of the Kensei, White Hat |

---

## 🔧 Maintenance Notes

- Banners are SVG — no quality loss at any resolution.
- Each wiki `.md` is self-contained and cross-links to related pages.
- To update a banner: replace the `.svg` file directly; GitHub raw links update automatically.

---

## 🔗 Related Links

- **Mod page:** [mod.io/g/baldursgate3/m/dnd55e](https://mod.io/g/baldursgate3/m/dnd55e)
- **Mod repository:** [github.com/Yoonmoonsik/dnd55e](https://github.com/Yoonmoonsik/dnd55e)
- **Original mod author:** [Yoonmoonsik](https://github.com/Yoonmoonsik)

---

## ✍️ Author

Documentation, wiki structure, and visual design by **[@incolhermex-droid](https://github.com/incolhermex-droid)** — Social Communicator & Journalist, Spanish localization lead for DnD 5.5e All-in-One BEYOND.

*All commit history in this repository reflects the original authorship and timeline of this documentation work.*
