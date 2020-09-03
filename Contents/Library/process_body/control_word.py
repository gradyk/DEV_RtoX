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
import re

# From local application
import adjust_process_text
import build_final_file
import dict_updater


def processor(processing_dict: dict) -> dict:
    # Test for control word (backslash followed by a combination of text,
    # character (optional), and numbers (optional).
    item = None
    try:
        test = re.search(r"^(\\[a-zA-Z\-\s0-9]*)", processing_dict[
            "parse_text"])
        if test is not item:
            control_word = test[0]
            length = test.end() - test.start()
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


def cw_evaluation(processing_dict: dict, control_word: str, test) -> dict:
    with open(processing_dict["control_word_dict"], "r+") as \
            control_word_dict_pre:
        ref_dict = json.load(control_word_dict_pre)
        cw_text = "".join([i for i in test[0] if i.isalpha()])
        cw_value = "".join([i for i in test[0] if i.isdigit()])

        null_function = "null"
        try:
            cw_func = ref_dict[cw_text][2]
            if cw_func != null_function:
                control_word_to_tag(cw_func=cw_func,
                                    cw_value=cw_value,
                                    processing_dict=processing_dict)
            else:
                pass

        except KeyError:
            # Add missing control word to control_word_dict.json
            # file.
            cw_update = {cw_text: ["", "", "null"]}
            dict_updater.json_dict_updater(
                dict_name="control_word_dict.json",
                debug_dir=processing_dict["dicts_dir"],
                dict_update=cw_update)
            # Add control word that cannot be processed to build
            # file.
            open_tag = f'<ts:rtfIssue line="' \
                       f'{processing_dict["line_to_parse"]}" ' \
                       f'key="{control_word}"/>'
            text = ""
            close_tag = ""
            build_final_file.processor(open_tag=open_tag,
                                       text=text,
                                       close_tag=close_tag)

        parse_text_update = \
            processing_dict["parse_text"].replace(control_word, "", 1)
        processing_dict["parse_text"] = parse_text_update
        processing_dict["parse_index"] = 0
        processing_dict = adjust_process_text.text_metric_reset(
            processing_dict=processing_dict)
        return processing_dict


def control_word_to_tag(cw_func, cw_value: str, processing_dict: dict):
    # THIS DOESN'T WORK-E.G. I.PY DOESN'T EVAL, ETC.
    # importlib.import_module(cw_func)
    # cw_func.processor(cw_value=cw_value, processing_dict=processing_dict)
    # ABOVE TWO LINES DON'T WORK
    print(cw_func, "--", cw_value, f'tag_set: {processing_dict["tag_set"]}')
