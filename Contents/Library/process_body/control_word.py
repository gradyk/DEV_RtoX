#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word"

# From standard libraries
import importlib
import json
import logging
import re

# From local application
import adjust_process_text
import build_final_file
import check_parse_text
import check_text
import dict_updater


def processor(processing_dict: dict) -> None:
    # Test for control symbol (backslash followed by single, non-alphabetic
    # character other than an asterisk).
    item = None
    null_function = "null"
    try:
        # TODO Amend regex so that this processor does not capture \\*
        test = re.search(r"^^(\\[a-zA-Z\-0-9]+)", processing_dict["parse_text"])
        if test is not item:
            control_word = test[0]
            length = test.end() - test.start()
            parse_index_update = processing_dict["parse_index"] + length
            processing_dict["parse_index"] = parse_index_update

            with open(processing_dict["control_word_dict"], "r+") as \
                    control_word_dict_pre:
                ref_dict = json.load(control_word_dict_pre)
                control_word_text = "".join([i for i in test[0] if
                                             i.isalpha()])
                control_word_value = "".join(
                    [i for i in test[0] if i.isdigit()])

                try:
                    cw_func = ref_dict[control_word_text][2]
                except KeyError:
                    # Add missing control word to control_word_dict.json
                    # file.
                    cw_update = {control_word_text: ["", "", "null"]}
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
                        processing_dict["parse_text"].replace(control_word, "")
                    processing_dict["parse_text"] = parse_text_update
                    processing_dict["parse_index"] = 0

                    print(control_word_text)
                    processing_dict = adjust_process_text.text_metric_reset(
                        processing_dict=processing_dict)
                    check_parse_text.check_string_manager(
                        processing_dict=processing_dict)

                if cw_func != null_function:
                    print(control_word_text)
                    control_word_to_tag(cw_func=cw_func,
                                        control_word_value=control_word_value)

                    parse_text_update = \
                        processing_dict["parse_text"].replace(control_word, "")
                    processing_dict["parse_text"] = parse_text_update
                    processing_dict["parse_index"] = 0

                    processing_dict = adjust_process_text.text_metric_reset(
                            processing_dict=processing_dict)
                    check_parse_text.check_string_manager(
                        processing_dict=processing_dict)
                else:
                    print(control_word_text)

                    parse_text_update = processing_dict[
                        "parse_text"].replace(control_word, "")
                    processing_dict["parse_text"] = parse_text_update
                    processing_dict["parse_index"] = 0

                    processing_dict = \
                        adjust_process_text.text_metric_reset(
                            processing_dict=processing_dict)
                    check_parse_text.check_string_manager(
                        processing_dict=processing_dict)

        else:
            check_text.processor(processing_dict=processing_dict)
            pass
    except TypeError:
        logging.exception(f"{processing_dict['line_to_parse']}:"
                          f"{processing_dict['parse_index']}--"
                          f"{processing_dict['parse_text']}")


def control_word_to_tag(cw_func, control_word_value: str):
    # THIS DOESN'T WORK-E.G. I.PY DOESN'T EVAL, ETC.
    # importlib.import_module(cw_func)
    # cw_func.processor(control_word_value)
    # ABOVE TWO LINES DON'T WORK
    print(cw_func, "--", control_word_value)
