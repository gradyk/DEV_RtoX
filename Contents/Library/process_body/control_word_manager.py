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

""" An RTF control word is indicated by a "\" followed by a combination of
 letters (uppercase and/or lowercase) and/or numbers. Some control words
 are designated "destinations" and handled by the destination_manager.py
 module. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-16"
__name__ = "Contents.Library.process_body.control_word_manager"

# From standard libraries
import array
import importlib
import json

# From local application
import build_final_file
import dict_updater


def process_control_word(line_to_parse: int,
                         control_word_dict: str,
                         debug_dir: str,
                         control_word: str,
                         control_word_value: str) -> None:

    try:
        with open(control_word_dict, "r+") as control_word_dict_pre:
            control_word_dict = json.load(control_word_dict_pre)
            cw_func = exponential_search(
                control_word_dict=control_word_dict, val=control_word)
            importlib.import_module(cw_func[__])
            cw_func.processor(control_word_value=control_word_value)

    except KeyError:
        # If the control word is not in the dictionary,
        # add it to a missing control word file.
        cw_update = {control_word: ["", "", "null"]}
        dict_updater.json_dict_updater(
            dict_name="control_word_missing_dict.json",
            debug_dir=debug_dir,
            dict_update=cw_update)
        # Add control word that cannot be processed to build file.
        content = f'<rtfIssue line="{line_to_parse}" key="{control_word}"/>'
        build_final_file.output_style_selector(text=content)


def exponential_search(control_word_dict, val):
    if control_word_dict[0] == val:
        return 0
    index = 1
    while index < len(control_word_dict) and control_word_dict[index] <= val:
        index = index * 2
    return binary_search(array[:min(index, len(control_word_dict))], val)


def binary_search(control_word_dict, val):
    first = 0
    last = len(control_word_dict) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if control_word_dict[mid] == val:
            index = mid
        else:
            first = mid + 1
    return index
