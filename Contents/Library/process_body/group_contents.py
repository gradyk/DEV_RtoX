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
import os
import re
from pathlib import Path
from typing import Any

# From local applications
import build_output_file
import control_word_to_build


def gc_processor(main_dict: dict, collections_dict: dict) -> Any:
    # Temp setup for testing
    for ele in main_dict["contents_list"]:
        if ele == "{":
            pass
        elif ele == "}":
            pass
        elif re.search(main_dict["cw_regex"], ele):
            cw_text = "".join([i for i in ele if i.isalpha()])
            cw_value = "".join([i for i in ele if i.isdigit()])
            null_function = "null"
            try:
                cw_func = collections_dict[cw_text]
                if cw_func != null_function:
                    tag_set = main_dict["tag_set"]
                    tag_info = {
                        "func":      cw_func,
                        "cw_text":   cw_text,
                        "cw_value":  cw_value,
                        "name":      cw_text,
                        "tag_open":  "",
                        "tag_close": "",
                        "tag_set":   tag_set
                    }
                    main_dict = control_word_to_build.cwtb_processor(
                        tag_info=tag_info, main_dict=main_dict)
                else:
                    pass
            except KeyError:
                # Add missing control word to control_word_collections.csv file.
                cw_update = f'{cw_text}, Unknown, Unknown, null'
                util_dir = Path.cwd()
                csv_file = os.path.join(util_dir,
                                        "control_words_collections.csv")
                with open(csv_file, "a+") as csv_file_pre:
                    csv_file_pre.write(cw_update)
        else:
            build_output_file.bof_processor(update_output=ele,
                                            main_dict=main_dict)
    main_dict = processing_dict_reset(main_dict=main_dict)
    return main_dict


def processing_dict_reset(main_dict: dict) -> dict:
    working_input_file = main_dict["working_input_file"]
    line = working_input_file[main_dict["line_to_parse"]].rstrip()
    length = len(line)
    if main_dict["parse_index"] > length:
        main_dict["line_to_parse"] += 1
        main_dict["parse_index"] = 0
        main_dict["parse_text"] = \
            working_input_file[main_dict["line_to_parse"]].rstrip()
        main_dict["contents_string"] = ""
        main_dict["contents_list"] = []
    else:
        main_dict["parse_text"] = working_input_file[main_dict["line_to_parse"]]
        main_dict["parse_text"] = main_dict["parse_text"].rstrip(" ")
        main_dict["group_contents"] = ""
        main_dict["contents_string"] = ""
        main_dict["contents_list"] = []
    return main_dict
