#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pypdf>=4"]
# ///
"""Render a character JSON onto the official D&D 2024 fillable character sheet.

Usage:
    uv run fill_sheet.py gunther.json
    # or: pip install pypdf && python3 fill_sheet.py gunther.json

Writes <Name>-character-sheet.pdf next to the JSON file.
"""
import argparse
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, TextStringObject

TEMPLATE = Path(__file__).parent / "template" / "character-sheet.pdf"

# Field names in the official WotC fillable PDF (2024 sheet, 670D3898000001 EN).
ABILITY_FIELDS = {
    #                 modifier   score     save      save-prof checkbox
    "strength":     ("Text21", "Text64", "Text91", "Check Box37"),
    "dexterity":    ("Text22", "Text66", "Text87", "Check Box33"),
    "constitution": ("Text24", "Text67", "Text86", "Check Box32"),
    "intelligence": ("Text20", "Text63", "Text69", "Check Box4"),
    "wisdom":       ("Text23", "Text65", "Text75", "Check Box21"),
    "charisma":     ("Text25", "Text68", "Text81", "Check Box26"),
}
SKILL_FIELDS = {
    #                  bonus      prof checkbox
    "athletics":       ("Text92", "Check Box38"),
    "acrobatics":      ("Text88", "Check Box34"),
    "sleight_of_hand": ("Text89", "Check Box35"),
    "stealth":         ("Text90", "Check Box36"),
    "arcana":          ("Text70", "Check Box16"),
    "history":         ("Text71", "Check Box17"),
    "investigation":   ("Text72", "Check Box19"),
    "nature":          ("Text73", "Check Box20"),
    "religion":        ("Text74", "Check Box18"),
    "animal_handling": ("Text76", "Check Box22"),
    "insight":         ("Text77", "Check Box23"),
    "medicine":        ("Text78", "Check Box25"),
    "perception":      ("Text79", "Check Box31"),
    "survival":        ("Text80", "Check Box24"),
    "deception":       ("Text82", "Check Box27"),
    "intimidation":    ("Text83", "Check Box28"),
    "performance":     ("Text84", "Check Box30"),
    "persuasion":      ("Text85", "Check Box29"),
}
# Weapon table rows: (name, atk, damage, notes)
WEAPON_ROWS = [
    ("Text30", "Text31", "Text32", "Text33"),
    ("Text34", "Text35", "Text36", "Text37"),
    ("Text38", "Text39", "Text40", "Text41"),
    ("Text42", "Text43", "Text44", "Text45"),
    ("Text46", "Text47", "Text48", "Text49"),
    ("Text50", "Text51", "Text52", "Text53"),
]
# Spell table notes column, rows 0-29 (level/name/time/range are Text105-109 kids).
SPELL_NOTES = [
    "Text108", "Text208", "Text209", "Text210", "Text211", "Text212", "Text213",
    "Text214", "Text215", "Text216", "Text217", "Text218", "Text219", "Text220",
    "Text221", "Text222", "Text223", "Text224", "Text225", "Text227", "Text228",
    "Text229", "Text230", "Text244", "Text231", "Text232", "Text233", "Text234",
    "Text235", "Text236",
]
# Narrow boxes need smaller type to avoid clipping.
FONT_OVERRIDES_P1 = {"Text28": 9, "Text32": 8, "Text33": 8, "Text35": 8,
                     "Text36": 8, "Text37": 8, "Text40": 8, "Text41": 8,
                     "Text44": 8, "Text45": 8, "Text48": 8, "Text49": 8,
                     "Text52": 8, "Text53": 8}
FONT_OVERRIDES_P2 = {f"Text107.{i}": 8 for i in range(30)}
FONT_OVERRIDES_P2.update({n: 7 for n in SPELL_NOTES})
# Long prose boxes: appearance, backstory & personality, equipment
FONT_OVERRIDES_P2.update({"Text96": 8, "Text97": 7, "Text99": 8})


def build_fields(c: dict) -> tuple[dict, dict]:
    ident, combat = c["identity"], c["combat"]
    p1 = {
        "Text1": c["name"],
        "Text6": ident["background"], "Text7": ident["class"],
        "Text8": ident["species"], "Text9": ident["subclass"],
        "Text11": ident["level"], "Text12": ident["xp"],
        "Text13": combat["armor_class"],
        "Text14": combat["hp_current"], "Text15": combat["hp_temp"],
        "Text16": combat["hp_max"],
        "Text17": combat["hit_dice_max"], "Text18": combat["hit_dice_spent"],
        "Text19": combat["proficiency_bonus"],
        "Text26": combat["initiative"], "Text27": combat["speed"],
        "Text28": combat["size"], "Text29": combat["passive_perception"],
        "Text54": c["class_features"][0], "Text55": c["class_features"][1],
        "Text57": c["species_traits"], "Text58": c["feats"],
        "Text59": c["training"]["weapons"], "Text60": c["training"]["tools"],
    }
    checks = {"Check Box3": combat["shield"], "Check Box11": combat["heroic_inspiration"]}
    armor = c["training"]["armor"]
    checks.update({"Check Box13": armor["light"], "Check Box14": armor["medium"],
                   "Check Box15": armor["heavy"], "Check Box12": armor["shields"]})
    for key, (f_mod, f_score, f_save, f_prof) in ABILITY_FIELDS.items():
        a = c["abilities"][key]
        p1.update({f_mod: a["modifier"], f_score: a["score"], f_save: a["save"]})
        checks[f_prof] = a["save_prof"]
    for key, (f_bonus, f_prof) in SKILL_FIELDS.items():
        s = c["skills"][key]
        p1[f_bonus] = s["bonus"]
        checks[f_prof] = s["prof"]
    for row, w in zip(WEAPON_ROWS, c["weapons"]):
        p1.update(dict(zip(row, (w["name"], w["atk"], w["damage"], w["notes"]))))
    p1.update({k: ("/Yes" if v else "/Off") for k, v in checks.items()})

    sc = c["spellcasting"]
    p2 = {
        "Text111": sc["ability"], "Text93": sc["modifier"],
        "Text94": sc["save_dc"], "Text95": sc["attack_bonus"],
        "Text112": sc["slots_level_1"],
        "Text96": c["appearance"],
        "Text97": c.get("backstory_sheet") or c["backstory"],
        "Text100": ident["alignment"], "Text98": c["languages"],
        "Text99": c["equipment"],
        "Text226": c["coins"]["cp"], "Text267": c["coins"]["sp"],
        "Text268": c["coins"]["ep"], "Text269": c["coins"]["gp"],
        "Text270": c["coins"]["pp"],
    }
    for i, sp in enumerate(c["spells"][:30]):
        p2[f"Text105.{i}"] = sp["level"]
        p2[f"Text106.{i}"] = sp["name"]
        p2[f"Text107.{i}"] = sp["time"]
        p2[f"Text109.{i}"] = sp["range"]
        p2[SPELL_NOTES[i]] = sp["notes"]
    return p1, p2


def apply_font_overrides(page, overrides: dict) -> None:
    for annot in page.get("/Annots", []):
        obj = annot.get_object()
        name = obj.get("/T")
        parent = obj.get("/Parent")
        parent_name = parent.get_object().get("/T") if parent else None
        qualified = f"{parent_name}.{name}" if parent_name and name is not None else name
        size = overrides.get(qualified) or overrides.get(name)
        if size:
            obj[NameObject("/DA")] = TextStringObject(f"/Helv {size} Tf 0 g")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("json_path", type=Path)
    ap.add_argument("-o", "--output", type=Path, default=None)
    args = ap.parse_args()

    character = json.loads(args.json_path.read_text())
    out = args.output or args.json_path.parent / f"{character['name']}-character-sheet.pdf"

    writer = PdfWriter()
    writer.append(PdfReader(TEMPLATE))
    apply_font_overrides(writer.pages[0], FONT_OVERRIDES_P1)
    apply_font_overrides(writer.pages[1], FONT_OVERRIDES_P2)
    p1, p2 = build_fields(character)
    writer.update_page_form_field_values(writer.pages[0], p1)
    writer.update_page_form_field_values(writer.pages[1], p2)
    writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)
    with open(out, "wb") as fh:
        writer.write(fh)
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
