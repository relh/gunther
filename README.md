# Gunther

Level 1 Human Cleric of **Claude, god of helpful answers** (D&D 5.5e / 2024 rules).

Lay archivist of the Temple of the Helpful Voice. Relentlessly helpful, honest to
a fault, admits uncertainty freely, and occasionally cites scripture that does
not, strictly speaking, exist.

- **Canonical data:** [`gunther.json`](gunther.json)
- **Rendered sheet:** [`Gunther-character-sheet.pdf`](Gunther-character-sheet.pdf)
- **D&D Beyond:** <https://www.dndbeyond.com/characters/169136089>

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

The JSON holds literal box values — nothing is derived or recomputed — so what
you write is exactly what lands on the sheet. Narrow columns are auto-shrunk to
smaller type so long entries don't clip.

## Build summary

| | |
|---|---|
| Class | Cleric 1 (subclass at level 3), Divine Order: Protector |
| Background | Acolyte (Insight, Religion, Calligrapher's Supplies, Magic Initiate: Cleric) |
| Species | Human (Skillful: Perception, Versatile: Alert) |
| Abilities | Str 14, Dex 10, Con 11, Int 5, **Wis 17**, Cha 10 |
| Combat | AC 15 (chain shirt + shield), HP 6, Initiative +2, Speed 30 ft. |
| Cantrips | Guidance, Sacred Flame, Thaumaturgy, Light*, Spare the Dying* |
| Prepared | Bless, Cure Wounds, Healing Word, Guiding Bolt, Sanctuary* |

\* from Magic Initiate (Cleric), Wisdom-based; Sanctuary free once per Long Rest.

Ability scores were **rolled** (4d6 drop lowest, one genuine run, no rerolls):
`[1,4,4,6]→14 · [1,2,3,4]→9 · [3,4,5,6]→15 · [1,1,1,3]→5 · [1,2,3,6]→11 · [1,1,4,5]→10`,
assigned Wis 15, Str 14, Con 11, Dex 10, Cha 9, Int 5 (Acolyte adds +2 Wis, +1 Cha;
the 10 goes to Dex since Cha 9+1 and 10+1 give the same +0 modifier — free AC).
Level 1 HP was likewise rolled: **1d8 = 6**. Height/weight rolled too: 5'6", 150 lb. The dice owed us nothing and delivered
accordingly; Gunther's Int 5 is now canon.
