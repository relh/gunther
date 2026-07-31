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
| Abilities | Str 14, Dex 10, Con 13, Int 8, **Wis 17**, Cha 13 |
| Combat | AC 15 (chain shirt + shield), HP 9, Initiative +2, Speed 30 ft. |
| Cantrips | Guidance, Sacred Flame, Thaumaturgy, Light*, Spare the Dying* |
| Prepared | Bless, Cure Wounds, Healing Word, Guiding Bolt, Sanctuary* |

\* from Magic Initiate (Cleric), Wisdom-based; Sanctuary free once per Long Rest.
