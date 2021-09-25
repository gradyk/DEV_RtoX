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


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    # For a toggle control word, \<control_word> turns on the feature and
    # \<control_word>N turns off the feature.
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.
    item = ""
    if tag_info["cw_value"] == item:
        tag_info["tag_status"] = "open"
    else:
        tag_info["tag_status"] = "close"
    open_str_empty = main_dict["tags"]["toggle_emph"][0]
    open_str = open_str_empty.replace("zzz", tag_info["name"])
    tag_info["tag_open_str"] = open_str
    tag_info["tag_close_str"] = main_dict["tags"]["toggle_emph"][1]
    return tag_info, main_dict
