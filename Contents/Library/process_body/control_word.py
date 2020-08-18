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
import backslash_text
import build_final_file
import check_parse_text
import dict_updater


def processor(working_input_file: str, debug_dir: str,
              control_word_dict: str, parse_text: str,
              line_to_parse: int, parse_index: int,
              num_lines: int) -> None:
    # Test for control symbol (backslash followed by single, non-alphabetic
    # character other than an asterisk).
    # TODO Amend regex so that this processor does not capture \\*
    item = None
    try:
        test = re.search(r"^(\\)[^A-Za-z0-9]?", parse_text)
        if test is not item:
            control_word = test[0]
            parse_index = parse_index + len(control_word)
            control_word = control_word.replace("\\*", "").rstrip()
            try:
                with open(control_word_dict, "r+") as control_word_dict_pre:
                    ref_dict = json.load(control_word_dict_pre)
                    cs_func = ref_dict[control_word]
                    importlib.import_module(cs_func[2])
                    cs_func.processor()
                    parse_text, line_to_parse, parse_index = \
                        adjust_process_text.text_metric_reset(
                            working_input_file=working_input_file,
                            parse_index=parse_index,
                            line_to_parse=line_to_parse)
                    check_parse_text.check_string_manager(
                        working_input_file=working_input_file,
                        debug_dir=debug_dir,
                        control_word_dict=control_word_dict,
                        parse_text=parse_text,
                        line_to_parse=line_to_parse,
                        parse_index=parse_index,
                        num_lines=num_lines)

            except KeyError:
                # Add missing control symbol to missing control symbol file.
                cw_update = {control_word: ["", "", "null"]}
                dict_updater.json_dict_updater(
                    dict_name="control_word_missing_dict.json",
                    debug_dir=debug_dir,
                    dict_update=cw_update)
                # Add control symbol that cannot be processed to build file.
                open_tag = f'<ts:rtfIssue line="{line_to_parse}" ' \
                           f'key="{control_word}"/>'
                text = ""
                close_tag = ""
                build_final_file.processor(open_tag=open_tag,
                                           text=text,
                                           close_tag=close_tag)
                parse_text, line_to_parse, parse_index = \
                    adjust_process_text.text_metric_reset(
                        working_input_file=working_input_file,
                        parse_index=parse_index,
                        line_to_parse=line_to_parse)
                check_parse_text.check_string_manager(
                        working_input_file=working_input_file,
                        debug_dir=debug_dir,
                        control_word_dict=control_word_dict,
                        parse_text=parse_text,
                        line_to_parse=line_to_parse,
                        parse_index=parse_index,
                        num_lines=num_lines)
        else:
            backslash_text.processor(
                working_input_file=working_input_file,
                debug_dir=debug_dir, line_to_parse=line_to_parse,
                parse_index=parse_index, parse_text=parse_text,
                control_word_dict=control_word_dict)
            pass
    except TypeError:
        logging.exception("_______")
