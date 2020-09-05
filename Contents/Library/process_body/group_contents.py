#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

# From standard libraries
import json
import linecache
import re

# From local applications
import control_word_to_build
import dict_updater
import text_to_build


def processor(processing_dict: dict):
    # Temp setup for testing
    for ele in processing_dict["contents_list"]:
        if ele == "{":
            pass
        elif ele == "}":
            pass
        elif re.search(r"^(\\[a-zA-Z\-\s0-9]*)", ele):
            with open(processing_dict["control_word_dict"], "r+") as \
                    control_word_dict_pre:
                ref_dict = json.load(control_word_dict_pre)
                cw_text = "".join([i for i in ele if i.isalpha()])
                cw_value = "".join([i for i in ele if i.isdigit()])

                null_function = "null"
                try:
                    cw_func = ref_dict[cw_text][2]
                    if cw_func != null_function:
                        control_word_to_build.processor(
                            cw_func=cw_func,
                            cw_value=cw_value,
                            processing_dict=processing_dict)
                    else:
                        pass
                except KeyError:
                    # Add missing control word to control_word_dict.json file.
                    cw_update = {cw_text: ["", "", "null"]}
                    dict_updater.json_dict_updater(
                        dict_name="control_word_dict.json",
                        debug_dir=processing_dict["dicts_dir"],
                        dict_update=cw_update)
        else:
            text_to_build.processor(text=ele)

    processing_dict = processing_dict_reset(processing_dict=processing_dict)
    return processing_dict


def processing_dict_reset(processing_dict: dict):
    line = linecache.getline(
        processing_dict["working_input_file"],
        processing_dict["line_to_parse"]).rstrip("\n").rstrip()
    length = len(line)
    if processing_dict["parse_index"] > length:
        processing_dict["line_to_parse"] += 1
        processing_dict["parse_index"] = 0
        processing_dict["parse_text"] = \
            linecache.getline(
                processing_dict["working_input_file"],
                processing_dict["line_to_parse"]).\
            rstrip("\n").rstrip()
        processing_dict["contents_string"] = ""
        processing_dict["contents_list"] = []
    else:
        processing_dict["parse_text"] = linecache.getline(
            processing_dict["working_input_file"],
            processing_dict["line_to_parse"])
        processing_dict["parse_text"] = \
            processing_dict["parse_text"].rstrip("\n").rstrip(" ")
        processing_dict["group_contents"] = ""
        processing_dict["contents_string"] = ""
        processing_dict["contents_list"] = []

    return processing_dict
