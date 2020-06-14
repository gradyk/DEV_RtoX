import re
import os
import sys
import csv


def keydefs_translate():
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))

    keydefs_list = os.path.join(base_script_dir, "TEICombinedList.csv")

    base_string = "core: item note q quote said sp stage "\
                  "corpus: particDesc setting settingDesc "\
                  "drama: castList epilogue performance prologue set view "\
                  "figures: cell figure "\
                  "header: abstract application availability cRefPattern " \
                  "calendar change correction correspAction correspContext " \
                  "correspDesc editionStmt editorialDecl encodingDesc " \
                  "handNote hyphenation interpretation langUsage licence " \
                  "normalization prefixDef projectDesc publicationStmt " \
                  "punctuation quotation refsDecl samplingDecl scriptNote " \
                  "segmentation seriesStmt sourceDesc stdVals styleDefDecl "\
                  "msdescription: accMat acquisition additions binding " \
                  "bindingDesc collation condition custEvent custodialHist " \
                  "decoDesc decoNote filiation foliation handDesc history " \
                  "layout layoutDesc msContents msDesc msFrag msItem " \
                  "msItemStruct msPart musicNotation objectDesc origin " \
                  "physDesc provenance recordHist scriptDesc seal sealDesc " \
                  "signatures source summary support supportDesc surrogates " \
                  "typeDesc typeNote "\
                  "namesdates: climate event langKnowledge listRelation nym " \
                  "object occupation org person personGrp persona place " \
                  "population state terrain trait "\
                  "spoken: broadcast equipment recording recordingStmt " \
                  "scriptStmt transcriptionDesc "\
                  "tagdocs: exemplum remarks specGrp "\
                  "textcrit: lem rdg "\
                  "textstructure: argument back body div div1 div2 div3 div4 " \
                  "div5 div6 div7 epigraph front postscript "\
                  "transcr: metamark "\
                  "verse: metDecl"

    old_string = re.sub(r"[^[a-zA-Z]]", " ", base_string).split()

    new_string = ""

    keydefs_dict = {}

    with open(keydefs_list, "r") as keydefs_pre:
        csv_reader = csv.reader(keydefs_pre, delimiter=',')
        for row in csv_reader:
            keydefs_dict_update = {row[0]: row[1]}
            keydefs_dict.update(keydefs_dict_update)

    for entry in old_string:

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
            new_term = f' <xref keyref=\"' + f'{tpres_key_term}\">' + f"{pre}" \
                       f'{tpres_key_term}' + f'{post}' + '</xref>'
            new_string = new_string + new_term
            pre = ""
            post = ""
        except KeyError:
            fixed_entry = fixed_entry.replace(".", "-")
            new_term = f' <xref keyref=\"' + f'{fixed_entry}\">' + f'{pre}' + \
                       f'{fixed_entry}' + f'{post}' + f'</xref><!-- TODO Fix ' \
                                                      f'-->'
            new_string = new_string + new_term

    print(new_string)


if __name__ == "__main__":
    keydefs_translate()
