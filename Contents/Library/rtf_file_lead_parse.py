#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Process the RTF file control words that precede the table definitions,
capturing codes in the rtf_file_codes dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-10"
__name__ = "Contents.Library.first_line"

# From standard libraries
import json
import logging
import os
import re

# From local application
from read_log_config import logger_basic
from read_log_config import logger_debug


def check_for_opening_brace(main_dict: dict) -> dict:
    """ Check the working_input_file for an opening brace. """
    working_input_file = main_dict["working_input_file"]
    if working_input_file[0][1] == "{":
        pass
    else:
        working_input_file = main_dict["working_input_file"]
        first_line_list = ["{", working_input_file[0]]
        new_first_line = ''.join(first_line_list)
        working_input_file[0] = new_first_line
        main_dict["working_input_file"] = working_input_file
    return main_dict


def code_process(main_dict: dict) -> list:
    """ Test for the existence of each pretable controlword and,
    if present, capture the code. """
    pretable_controlword_replacementtext_list = [
        "rtf[0-9]+",
        "ansi",
        "ansicpg[0-9]+",
        "upr",
        "uc[0-9]+",
        "deflang[0-9]+",
        "deflangfe[0-9]+",
        "deff[0-9]+",
        "adeff[0-9]+",
        "stshfdbch[0-9]+",
        "stshfloch[0-9]+",
        "stshfhich[0-9]+",
        "stshfbi[0-9]+",
        "([a-z]+deflang[a-z]+)",
        "themelang[0-9]+",
        "themelangfe[0-9]+",
        "themelangcs[0-9]+",
    ]
    rtf_file_codes_update = []
    working_input_file = main_dict["working_input_file"]
    line_to_search = working_input_file[0]
    for item in pretable_controlword_replacementtext_list:
        try:
            code_match = re.search(rf'\\{item}', line_to_search)
            code_text = "".join([i for i in code_match[0] if i.isalpha()])
            code_value = "".join([i for i in code_match[0] if i.isdigit()])
            rtf_file_codes_update.append((code_text, code_value))
        except TypeError:
            if logger_basic.isEnabledFor(logging.INFO):
                logger_basic.info(f"No {item} code.")

    return rtf_file_codes_update


def update_rtf_file_codes_list(rtf_file_codes_update: list,
                               main_dict: dict) -> None:
    """ Update the rtf_file_codes dictionary with codes extracted from
    pretable control words. """
    rtf_file_codes_file = os.path.join(main_dict["debug_dir"],
                                       "rtf_file_codes.json")
    with open(rtf_file_codes_file, "r+") as rtf_file_codes_file_pre:
        rtf_file_codes = json.load(rtf_file_codes_file_pre)
        rtf_file_codes.update(rtf_file_codes_update)
        rtf_file_codes_file_pre.seek(0)
        json.dump(rtf_file_codes, rtf_file_codes_file_pre, indent=4)
    # Used for debugging purposes.
    if logger_debug.isEnabledFor(logging.ERROR):
        logger_debug.debug(msg=str(rtf_file_codes))
