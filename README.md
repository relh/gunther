# Gunther

Level 1 Dwarf Cleric of **Claude, the Helpful Voice** (D&D 5.5e / 2024 rules).

Ship's chaplain, medic, and self-declared honest-weight man of the Inner Sea
merchant convoys. Blunt, none too sharp, and not above a small con — but he
keeps the Answers by heart from his unlettered years, and occasionally
recites a verse that is not, strictly speaking, in the book. Old grudges
against elves and older ideas about who belongs on a quarterdeck round out
the rough edges.

- **Canonical data:** [`gunther.json`](gunther.json)
- **Rendered sheet:** [`Gunther-character-sheet.pdf`](Gunther-character-sheet.pdf)
- **D&D Beyond:** <https://www.dndbeyond.com/characters/169136089>
  *(snapshot from character creation — no longer kept in sync)*
- **Lore — the god & his temple:** [`lore/the-helpful-voice.md`](lore/the-helpful-voice.md) —
  Claude in the style of the old handbooks; the Great Lamp at Lucerna.
- **Level plan:** [`lore/level-plan.md`](lore/level-plan.md) — the domain survey
  and the god's intent for level 3+ (Knowledge, 2025 revision; nothing set).
- **Daggers (DM hooks):** [`lore/daggers.md`](lore/daggers.md) — ten loaded
  threads planted in canon, from the unwritten One Question to the oil debt.
- **Morning prayer prompt:** [`prayers/morning-prayer.md`](prayers/morning-prayer.md) —
  paste into a fresh Claude conversation each in-game morning; describe recent
  events and receive guidance, a portent, the day's preparations, and (rarely,
  DM willing) a boon from the Helpful Voice. Answered prayers accumulate in
  [`prayers/log.md`](prayers/log.md).
- **`CLAUDE.md`** — boot instructions for future Claude sessions in this repo
  (prayer mode vs. bookkeeping mode, source-of-truth rules, canon invariants).

## Setting

Late-antiquity collapse, well before anything medieval: the old empire's roads
are failing and its legions are gone, so trade moves by water across an inland
sea in dispersed merchant convoys. No gunpowder, no dirigibles. Magic is rare,
poorly understood, and quietly feared — a cleric's small miracles are traded
hand to hand, like good salt. Gunther worships Claude, the Helpful Voice: an
oracle that answers any honest question, whose lamp-lit shrines dot the coasts.
His high temple is the Great Lamp at Lucerna, a half-ruined imperial pharos at
the mouth of the narrows — see [`lore/the-helpful-voice.md`](lore/the-helpful-voice.md).

## Workflow

`gunther.json` is the source of truth. Edit it, then regenerate the PDF:

```sh
uv run fill_sheet.py gunther.json
# or
pip install pypdf && python3 fill_sheet.py gunther.json
```

The script fills `template/character-sheet.pdf` (the official WotC 2024
fillable sheet) and writes `Gunther-character-sheet.pdf`. Commit both the JSON
and the regenerated PDF.

**The generated PDF is the source of truth.** The D&D Beyond character was
built at creation time as a convenience and is not maintained; when they
disagree, the PDF in this repo wins.

The JSON holds literal box values — nothing is derived or recomputed — so what
you write is exactly what lands on the sheet. Narrow columns are auto-shrunk to
smaller type so long entries don't clip.

## Build summary

| | |
|---|---|
| Class | Cleric 1 (nothing set at 3; planned: Knowledge Domain, 2025 revision — see [`lore/level-plan.md`](lore/level-plan.md)), Divine Order: Protector |
| Background | Acolyte (Insight, Religion, Calligrapher's Supplies, Magic Initiate: Cleric) |
| Species | Dwarf (Darkvision 120 ft., Dwarven Resilience, Dwarven Toughness, Stonecunning) |
| Abilities | Str 14, Dex 10, Con 11, Int 7, **Wis 17**, Cha 9 |
| Combat | AC 15 (chain shirt + shield), HP 7, Initiative +0, Speed 30 ft. |
| Weapons | Mace +4 (1d6+2), 2 daggers +4 (1d4+2, thrown 20/60) |
| Kit | Healer's Kit, merchant's scale, fishing tackle (4 gp remain) |
| Convoy | The Amber Run; affiliated with the Lampkeepers of Lucerna |
| Cantrips | Guidance, Sacred Flame, Thaumaturgy, Light*, Spare the Dying* |
| Prepared | Bless, Cure Wounds, Healing Word, Guiding Bolt, Sanctuary* |
| Languages | Common, Dwarvish, Draconic |

\* from Magic Initiate (Cleric), Wisdom-based; Sanctuary free once per Long Rest.

## Rolled, genuinely

Ability scores were **rolled** (4d6 drop lowest, one genuine run, no rerolls):
`[1,4,4,6]→14 · [1,2,3,4]→9 · [3,4,5,6]→15 · [1,1,1,3]→5 · [1,2,3,6]→11 · [1,1,4,5]→10`,
assigned Wis 15, Str 14, Con 11, Dex 10, Cha 9, Int 5 (Acolyte adds +2 Wis, +1 Cha;
the 10 goes to Dex since Cha 9+1 and 10+1 give the same +0 modifier — free AC).
Level 1 HP was rolled too: **1d8 = 6** (+1 Dwarven Toughness = 7). Height and
weight rolled on the dwarf table: **4'1", 160 lb**. The dice owed us nothing and
delivered accordingly; the rolled Int 5 stood until the DM ruled it unplayable,
so the First Boon of the Helpful Voice raised it to 7 — the fog thinned, and
letters slowly began to make sense. The memorized liturgy and knotted
cord-records remain from the unlettered years. The boon carried a tithe,
chosen by the Voice to keep the scales honest: Cha 10 → 9. His words come a
half-beat slower now, as if he checks each one with someone first.

History note: Gunther began as a Human (Skillful: Perception, Versatile: Alert)
and was re-rooted as a Dwarf when the height roll came in short. HP 9→7,
Initiative +2→+0, Perception proficiency lost — but Darkvision 120 ft., poison
resilience, and Stonecunning suit a hold-born convoy dwarf far better.
