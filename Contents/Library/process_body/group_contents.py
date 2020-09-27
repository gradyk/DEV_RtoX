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
import linecache
import os
import re
from pathlib import Path

# From local applications
import build_output_file
import control_word_collections
import control_word_to_build


def processor(processing_dict: dict):
    # Temp setup for testing
    for ele in processing_dict["contents_list"]:
        if ele == "{":
            pass
        elif ele == "}":
            pass
        elif re.search(processing_dict["cw_regex"], ele):
            cw_text = "".join([i for i in ele if i.isalpha()])
            cw_value = "".join([i for i in ele if i.isdigit()])
            null_function = "null"
            try:
                cw_func = \
                    control_word_collections.processor(ele=cw_text)
                if cw_func != null_function:
                    tag_set = processing_dict["tag_set"]
                    tag_info = {
                        "func":      cw_func,
                        "cw_text":   cw_text,
                        "cw_value":  cw_value,
                        "name":      cw_text,
                        "tag_open":  "",
                        "tag_close": "",
                        "tag_set":   tag_set
                    }
                    control_word_to_build.processor(tag_info=tag_info)
                else:
                    pass
            except KeyError:
                # Add missing control word to
                # control_word_collections.csv file.
                cw_update = f'{cw_text}, Unknown, Unknown, null'
                util_dir = Path.cwd()
                csv_file = os.path.join(util_dir,
                                        "control_words_collections.csv")
                with open(csv_file, "a+") as csv_file_pre:
                    csv_file_pre.write(cw_update)
        else:
            build_output_file.processor(update_output=ele)

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
