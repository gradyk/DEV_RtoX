#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.control_words_symbols.toggle_emph"

# From standard libraries
from typing import Tuple

import build_output_file


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    # For a toggle control word, \<control_word> turns on the feature and
    # \<control_word>N turns off the feature.
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.

    # main_dict["cw_text"] == "open" & tag_info["cw_value"] == ""
    #   do nothing
    # main_dict["cw_text"] == "open" & tag_info["cw_value"] != ""
    #   insert tag_close_str, change main_dict["cw_text"] to "closed"
    # main_dict["cw_text"] == "closed" & tag_info["cw_value"] == ""
    #   insert tag_open_str, change main_dict["cw_text"] to "open"
    # main_dict["cw_text"] == "closed" & tag_info["cw_value"] != ""
    #   do nothing

    item = ""
    cw_text = tag_info["cw_text"]
    if main_dict[cw_text] == "open" and tag_info["cw_value"] == item:
        open_str_empty = main_dict["tags"]["toggle_emph"][0]
        open_str = open_str_empty.replace("zzz", tag_info["cw_text"])
        main_dict["update_output"] = main_dict["tags"]["toggle_emph"][1] + \
            open_str
        print("1")
    elif main_dict[cw_text] == "open" and tag_info["cw_value"] != "":
        main_dict[cw_text] = "closed"
        main_dict["update_output"] = main_dict["tags"]["toggle_emph"][1]
        main_dict["tag_queue"].append(main_dict["tag_queue"][-1])
        print("2")
    elif main_dict[cw_text] == "closed" and tag_info["cw_value"] == "":
        main_dict[cw_text] = "open"
        open_str_empty = main_dict["tags"]["toggle_emph"][0]
        open_str = open_str_empty.replace("zzz", tag_info["cw_text"])
        main_dict["update_output"] = open_str
        main_dict["tag_queue"].append(main_dict["tags"]["toggle_emph"][1])
        print("3")
    else:
        main_dict["update_output"] = ""
        print("4")
    build_output_file.processor(main_dict=main_dict)
    return tag_info, main_dict
