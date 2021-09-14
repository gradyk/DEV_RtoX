#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

from typing import Tuple


def processor(main_dict: dict, temp_dict: dict) -> Tuple[dict, dict]:
    # If parse_text has only 1 character, increase parse_text by adding
    # the next string from working_input_file.
    if temp_dict["text_length"] == 1:
        temp_dict["line"] += 1
        new_text = main_dict["working_input_file"][temp_dict["line"]]
        temp_dict["parse_text"] = temp_dict["parse_text"] + new_text
        main_dict["parse_text"] = temp_dict["parse_text"]
        main_dict["group_end_line"] = temp_dict["line"]
        temp_dict["text_length"] = len(temp_dict["parse_text"])
        temp_dict["end_index"] = 0
    else:
        pass
    return main_dict, temp_dict
