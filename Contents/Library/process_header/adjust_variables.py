#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


def processor(temp_dict: dict) -> dict:
    temp_dict["deck_length"] = len(temp_dict["deck"])
    temp_dict["parse_text"] = temp_dict["parse_text"][1:]
    temp_dict["end_index"] += 1
    temp_dict["text_length"] -= 1
    return temp_dict
