#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word"

# From standard libraries
import logging
import re

# From local application
import adjust_process_text
import control_word_to_build
import csv_modifier
import tag_insert_missing_cw
from typing import Any


def cw_processor(main_dict: dict, collections_dict: dict) -> tuple:
    # Test for control word (backslash followed by a combination of text,
    # character (optional), and numbers (optional).
    cw_regex = main_dict["cw_regex"]
    parse_index = main_dict["parse_index"]
    item = None
    try:
        test = re.search(cw_regex, main_dict["parse_text"])
        if test is not item:
            length = test.end() - test.start()
            control_word = test[0]
            parse_index = parse_index + length
            main_dict["parse_index"] = parse_index
            main_dict, collections_dict = cw_evaluation(
                main_dict=main_dict,
                test=test[0], collections_dict=collections_dict)
            main_dict["parse_text"] = \
                main_dict["parse_text"].replace(control_word, "", 1).lstrip()
            main_dict["parse_index"] = 0
            main_dict = adjust_process_text.apt_processor(main_dict=main_dict)
        else:
            pass
    except TypeError:
        logging.exception(f"{main_dict['line_to_parse']}:"
                          f"{main_dict['parse_index']}--"
                          f"{main_dict['parse_text']}")
    return main_dict, collections_dict


def cw_evaluation(main_dict: dict, test: Any, collections_dict: dict) -> tuple:
    cw_text = "".join([i for i in test if i.isalpha()])
    cw_value = "".join([i for i in test if i.isdigit()])
    null_function = "null"
    try:
        cw_func = collections_dict[cw_text]
        if cw_func != null_function:
            tag_set = main_dict["tag_set"]
            tag_info = {
                "func":             cw_func,
                "name":             cw_text,
                "value":            cw_value,
                "tag_open_str":     "",
                "tag_close_str":    "",
                "tag_setting":      "",
                "tag_set":          tag_set
            }
            main_dict = control_word_to_build.cwtb_processor(
                tag_info=tag_info, main_dict=main_dict)
        else:
            pass
    except KeyError:
        # Add missing control word to control_words_collections.csv file.
        collections_dict = csv_modifier.csvm_processor(
            main_dict=main_dict, cw_text=cw_text,
            collections_dict=collections_dict)
        # Add control word that cannot be processed to XML build file.
        tag_insert_missing_cw.ti_processor(main_dict=main_dict, cw_text=cw_text)
    return main_dict, collections_dict
