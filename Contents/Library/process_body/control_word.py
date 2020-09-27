#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word"

# From standard libraries
import json
import logging
import os
import re
import sys
from pathlib import Path

# From local application
import adjust_process_text
import build_output_file
import control_word_collections
import control_word_to_build


def processor(processing_dict: dict) -> dict:
    # Test for control word (backslash followed by a combination of text,
    # character (optional), and numbers (optional).
    item = None
    try:
        test = re.search(processing_dict["cw_regex"], processing_dict[
            "parse_text"])
        if test is not item:
            length = test.end() - test.start()
            control_word = test[0]
            parse_index_update = processing_dict["parse_index"] + length
            processing_dict["parse_index"] = parse_index_update
            processing_dict = cw_evaluation(processing_dict=processing_dict,
                                            control_word=control_word,
                                            test=test)
        else:
            pass
    except TypeError:
        logging.exception(f"{processing_dict['line_to_parse']}:"
                          f"{processing_dict['parse_index']}--"
                          f"{processing_dict['parse_text']}")
    return processing_dict


def cw_evaluation(processing_dict: dict, control_word: str,
                  test) -> dict:
    cw_text = "".join([i for i in test[0] if i.isalpha()])
    cw_value = "".join([i for i in test[0] if i.isdigit()])
    null_function = "null"
    try:
        cw_func = \
            control_word_collections.processor(ele=cw_text)
        if cw_func != null_function:
            tag_set = processing_dict["tag_set"]
            tag_info = {
                "func":             cw_func,
                "name":             cw_text,
                "value":            cw_value,
                "tag_open_str":     "",
                "tag_close_str":    "",
                "tag_setting":      "",
                "tag_set":          tag_set
            }
            control_word_to_build.processor(tag_info=tag_info)
        else:
            pass
    except KeyError:
        # Add missing control word to control_word_collections.csv file.
        cw_update = f'{cw_text}, Unknown, Unknown, null'
        util_dir = Path.cwd()
        csv_file = os.path.join(util_dir, "control_words_collections.csv")
        with open(csv_file, "a+") as csv_file_pre:
            csv_file_pre.write(cw_update)
        # Add control word that cannot be processed to XML build file.
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        dicts_dir = os.path.join(base_dir, "Library/dicts")
        tag_dict_file = os.path.join(dicts_dir, "xml_tags.json")
        with open(tag_dict_file, "r+") as tag_dict_file_pre:
            tag_dict_options = json.load(tag_dict_file_pre)
        tag_set = processing_dict["tag_set"]
        tag_dict = tag_dict_options[tag_set]
        tag_empty = tag_dict["missing"][0]
        tag = tag_empty.replace("zzz", str(processing_dict["line_to_parse"]))
        tag = tag.replace("aaa", cw_text)
        build_output_file.processor(update_output=tag)
    parse_text_update = \
        processing_dict["parse_text"].replace(control_word, "", 1)
    processing_dict["parse_text"] = parse_text_update
    processing_dict["parse_index"] = 0
    processing_dict = adjust_process_text.processor(
        processing_dict=processing_dict)
    return processing_dict
