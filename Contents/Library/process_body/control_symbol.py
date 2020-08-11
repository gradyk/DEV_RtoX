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

# From standard libraries
import importlib
import json
import os
import re
import sys

# From local application
import build_final_file
import dict_updater


def processor(parse_text: str, debug_dir: str, line_to_parse: int) -> None:
    # Test for control symbol (backslash followed by single, non-alphabetic
    # character) other than control symbol star.
    # TODO Amend regex so that this processor does not capture \\*
    test = re.search(r"(\\)[^A-Za-z0-9]?", parse_text[0:2])
    if test is not None:
        control_symbol_manager_processor(control_symbol=test[0],
                                         debug_dir=debug_dir,
                                         line_to_parse=line_to_parse)
    else:
        pass


def control_symbol_manager_processor(control_symbol: str, line_to_parse: int,
                                     debug_dir: str):
    # A control symbol consists of a backslash followed by a single,
    # non-alphanumeric character. The control symbol with an asterisk is a
    # special case handled by control_symbol_star.py.
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    dicts_dir = os.path.join(base_script_dir, "Library/dicts")
    control_symbol_dict = os.path.join(dicts_dir, "control_symbol_dict.json")

    try:
        with open(control_symbol_dict, "r+") as control_symbol_dict_pre:
            ref_dict = json.load(control_symbol_dict_pre)
            cs_func = ref_dict[control_symbol]
            importlib.import_module(cs_func[2])
            cs_func.processor()

    except KeyError:
        # If the control symbol is not in the dictionary,
        # add it to a missing control symbol file.
        cs_update = {control_symbol: ["", "", "null"]}
        dict_updater.json_dict_updater(
            dict_name="control_symbol_missing_dict.json",
            debug_dir=debug_dir,
            dict_update=cs_update)
        # Add control symbol that cannot be processed to build file.
        content = f'<rtfIssue line="{line_to_parse}" key="{control_symbol}"/>'
        build_final_file.output_style_selector(text=content)
