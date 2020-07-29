import re
import os
import sys
import csv


def keydefs_translate():
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))

    keydefs_list = os.path.join(base_script_dir, "TEICombinedList.csv")
    delete_list = os.path.join(base_script_dir, "delete_list.csv")
    new_string = ""

    container = 1
    attribute = 0
    schema = 0

    base_string = "analysis: c cl interp interpGrp m pc phr s span spanGrp w " \
                  "certainty: certainty precision respons " \
                  "core: abbr add address binaryObject cb choice cit corr " \
                  "date del distinct email emph expan foreign gap gb gloss " \
                  "graphic hi index lb measure measureGrp media mentioned " \
                  "milestone name note num orig pb ptr q quote ref reg rs " \
                  "said sic soCalled term time title unclear unit " \
                  "dictionaries: lang oRef pRef " \
                  "figures: figure formula notatedMusic " \
                  "gaiji: g " \
                  "header: idno " \
                  "iso-fs: fLib fs fvLib " \
                  "linking: alt altGrp anchor join joinGrp link linkGrp seg " \
                  "timeline " \
                  "msdescription: catchwords depth dim dimensions height " \
                  "heraldry locus locusGrp material objectType origDate " \
                  "origPlace secFol signatures stamp watermark width " \
                  "namesdates: addName affiliation bloc climate country " \
                  "district forename genName geo geogFeat geogName location " \
                  "nameLink objectName offset orgName persName placeName " \
                  "population region roleName settlement state surname " \
                  "terrain trait " \
                  "spoken: incident kinesic pause shift vocal writing " \
                  "tagdocs: att code gi ident specDesc specList tag val " \
                  "textcrit: app witDetail " \
                  "textstructure: floatingText " \
                  "transcr: addSpan am damage damageSpan delSpan ex fw " \
                  "handShift listTranspose metamark mod redo restore retrace " \
                  "secl space subst substJoin supplied surplus undo " \
                  "verse: caesura rhyme " \
                  "character data " \

    if container == 1:
        new_string = container_translate(base_string=base_string,
                                         keydefs_list=keydefs_list,
                                         delete_list=delete_list)
    elif attribute == 1:
        new_string = attribute_translate(base_string=base_string,
                                         keydefs_list=keydefs_list,
                                         delete_list=delete_list)

    elif schema == 1:
        new_string = schema_translate(base_string=base_string,
                                      keydefs_list=keydefs_list,
                                      delete_list=delete_list)

    else:
        print("You forgot to set container, attribute, or schema!")

    print(new_string)


def container_translate(base_string: str, keydefs_list: str, delete_list: str):
    old_string = re.sub(r"[^[a-zA-Z]]", " ", base_string).split()

    new_string = ""
    keydefs_dict = {}

    module_list = [
        "analysis:",
        "briefing:",  # New in TPRES
        "certainty:",
        "citing:",  # New in TPRES
        "core:",
        "corpus:",
        "dictionaries:",
        "drama:",
        "figures:",
        "gaiji:",
        "header:",
        "iso-fs:",
        "linking:",
        "msdescription:",
        "namesdates:",
        "nets:",
        "spoken:",
        "tagdocs:",
        "tei:",
        "textcrit:",
        "textstructure:",
        "transcr:",
        "verse:"
    ]

    with open(keydefs_list, "r") as keydefs_pre:
        csv_reader = csv.reader(keydefs_pre, delimiter=',', dialect="excel")
        for row in csv_reader:
            if row == 0:
                row += 1
            else:
                keydefs_dict_update = {row[0]: row[1]}
                keydefs_dict.update(keydefs_dict_update)

    for entry in old_string:
        status = 0
        dropped = 0

        if status == 0:

            for module in module_list:
                mod_entry = entry.strip("[").strip("]")
                if mod_entry == module:
                    new_term = f'\n<b>' + f'{module}</b>'
                    new_string = new_string + new_term
                    status = 1
                else:
                    pass
        else:
            pass

        if status != 1:
            cw_open = re.search(r"\[[a-zA-Z.]+", entry)
            if cw_open:
                pre = "["
                fixed_entry = cw_open[0].strip("[")
            else:
                pre = ""
                fixed_entry = entry

            cw_close = re.search(r"[a-zA-Z.]+\]", fixed_entry)
            if cw_close:
                post = "]"
                fixed_entry = cw_close[0].strip("]")
            else:
                post = ""

            try:
                tpres_key_term = keydefs_dict[fixed_entry]
                tpres_key_term = tpres_key_term.replace(".", "-")
                new_term = f' <xref keyref=\"' + f'{tpres_key_term}\">' + \
                           f"{pre}" \
                           f'{tpres_key_term}' + f'{post}' + '</xref>'
                new_string = new_string + new_term
                pre = ""
                post = ""
            except KeyError:
                with open(delete_list) as delete_list_pre:
                    delete_reader = csv.reader(delete_list_pre, delimiter=',',
                                               dialect="excel")
                    for row in delete_reader:
                        if row == 0:
                            row += 1
                        else:
                            if fixed_entry == row[0]:
                                fixed_entry = fixed_entry.replace(".", "-")
                                new_term = f' <xref keyref=\"' + \
                                           f'{fixed_entry}\">' + f'{pre}' + \
                                           f'{fixed_entry}' + f'{post}' + \
                                           f'</xref><!-- DROPPED -->'
                                new_string = new_string + new_term
                                dropped = 1
                            else:
                                pass
                if dropped == 0:
                    fixed_entry = fixed_entry.replace(".", "-")
                    new_term = f' <xref keyref=\"' + f'{fixed_entry}\">' + \
                               f'{pre}' + \
                               f'{fixed_entry}' + f'{post}' + \
                               f'</xref><!-- TODO Fix ' \
                               f'-->'
                    new_string = new_string + new_term
                else:
                    dropped = 0
                    pass
        else:
            pass
    new_string = new_string.lstrip("\n")
    return new_string


def attribute_translate(base_string: str, keydefs_list: str, delete_list: str):
    old_string = re.sub(r"[^[a-zA-Z]]", " ", base_string).split()
    new_string = ""
    keydefs_dict = {}

    with open(keydefs_list, "r") as keydefs_pre:
        csv_reader = csv.reader(keydefs_pre, delimiter=',', dialect="excel")
        for row in csv_reader:
            if row == 0:
                row += 1
            else:
                keydefs_dict_update = {row[0]: row[1]}
                keydefs_dict.update(keydefs_dict_update)

    return new_string


def schema_translate(base_string: str, keydefs_list: str, delete_list: str):
    old_string = re.sub(r"[^[a-zA-Z]]", ", ", base_string).split()
    new_string = ""
    keydefs_dict = {}

    with open(keydefs_list, "r") as keydefs_pre:
        csv_reader = csv.reader(keydefs_pre, delimiter=',', dialect="excel")
        for row in csv_reader:
            if row == 0:
                row += 1
            else:
                keydefs_dict_update = {row[0]: row[1]}
                keydefs_dict.update(keydefs_dict_update)

    for entry in old_string:
        dropped = 0
        entry = entry.strip(", ")

        cw_open = re.search(r"\([a-zA-Z.]+", entry)
        if cw_open:
            pre = "("
            fixed_entry = cw_open[0].strip("(")
        else:
            pre = ""
            fixed_entry = entry

        cw_divider = re.search(r"\s\|\s", fixed_entry)
        if cw_divider:
            divider = "|"
            fixed_entry = cw_divider[0].strip(" | ")
        else:
            divider = ""

        cw_close = re.search(r"[a-zA-Z.]+\)", fixed_entry)
        if cw_close:
            post = ")"
            fixed_entry = cw_close[0].strip(")")
        else:
            post = ""

        try:
            tpres_key_term = keydefs_dict[fixed_entry]
            tpres_key_term = tpres_key_term.replace(".", "-")
            new_term = f'\t<xref keyref=\"' + f'{tpres_key_term}\">' + \
                       f"{pre}" \
                       f'{tpres_key_term}' + f'{divider}' + \
                       f'{post}' + '</xref>,\n'
            new_string = new_string + new_term
            pre = ""
            post = ""
        except KeyError:
            with open(delete_list) as delete_list_pre:
                delete_reader = csv.reader(delete_list_pre, delimiter=',',
                                           dialect="excel")
                for row in delete_reader:
                    if row == 0:
                        row += 1
                    else:
                        if fixed_entry == row[0]:
                            fixed_entry = fixed_entry.replace(".", "-")
                            new_term = f' <xref keyref=\"' + \
                                       f'{fixed_entry}\">' + f'{pre}' + \
                                       f'{fixed_entry}' + f'{post}' + \
                                       f'</xref><!-- DROPPED -->'
                            new_string = new_string + new_term
                            dropped = 1
                        else:
                            pass
            if dropped == 0:
                fixed_entry = fixed_entry.replace(".", "-")
                new_term = f'\t<xref keyref=\"' + f'{fixed_entry}\">' + \
                           f'{pre}' + \
                           f'{fixed_entry}' + f'{divider}' + \
                           f'{post}' + \
                           f'</xref>,<!-- TODO Fix -->\n'
                new_string = new_string + new_term
            else:
                dropped = 0
                pass

    return new_string


if __name__ == "__main__":
    keydefs_translate()
