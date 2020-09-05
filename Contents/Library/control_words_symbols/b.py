#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def tagger(processing_dict: dict, cw_value: str) -> list:
    # \b turns on bold; \b0 (or any other number) turns off bold
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.
    item = ""
    tag_num = processing_dict["tag_set"]
    if cw_value == item:
        tag_options = {
            1: "",
            2: "",
            3: ["bold", "tagon", '<ts:hiText rend="bold">']
        }
        tag = tag_options[tag_num]
    else:
        tag_options = {
            1: "",
            2: "",
            3: ["bold", "tagoff", '</ts:hiText>']
        }
        tag = tag_options[tag_num]
    return tag
