#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.control_words_symbols.toggle"

# From standard libraries
import json
import os
import sys


def cw_func_processor(tag_info: dict) -> dict:
    # For a toggle control word, \<control_word> turns on the feature and
    # \<control_word>N turns off the feature.
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    tag_dict_file = os.path.join(dicts_dir, "xml_tags.json")
    with open(tag_dict_file, "r+") as tag_dict_file_pre:
        tag_dict_options = json.load(tag_dict_file_pre)
    tag_set = str(tag_info["tag_set"])
    tag_dict = tag_dict_options[tag_set]
    item = ""
    if tag_info["value"] == item:
        tag_info["tag_setting"] = "open"
    else:
        tag_info["tag_setting"] = "close"
    name = tag_info["name"]
    open_str_empty = tag_dict["toggle"][0]
    open_str = open_str_empty.replace("zzz", name)
    tag_info["tag_open_str"] = open_str
    tag_info["tag_close_str"] = tag_dict["toggle"][1]
    return tag_info
