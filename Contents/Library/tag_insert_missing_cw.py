#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Insert a tag in the XML file showing the control word that could not be
processed. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.tag_insert_missing_cw"

# From standard libraries
import json
import os


# From local application
import build_output_file


def ti_processor(main_dict: dict, cw_text: str) -> None:
    tag_dict_file = os.path.join(main_dict["dicts_dir"], "xml_tags.json")
    with open(tag_dict_file, "r+") as tag_dict_file_pre:
        tag_dict_options = json.load(tag_dict_file_pre)
    tag_set = str(main_dict["tag_set"])
    tag_dict = tag_dict_options[tag_set]
    tag_empty = tag_dict["missing"][0]
    tag = tag_empty.replace("zzz", str(main_dict["line_to_parse"]))
    tag = tag.replace("aaa", cw_text)
    build_output_file.processor(update_output=tag, main_dict=main_dict)
