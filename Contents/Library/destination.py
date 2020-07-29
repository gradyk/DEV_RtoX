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
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" An RTF destination is indicated by a "\" followed by a combination of
 letters (lowercase) and/or numbers. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-16"
__name__ = "Contents.Library.destination"

# From standard libraries
import json
import linecache
import os
import re
import sys

# From local application
import control_word_functions
import working_xml_file_update


def destination_processor(line_to_parse: int, parse_index: int,
                          working_input_file: str,
                          control_word_func_dict: str,
                          debug_dir: str) -> tuple:
    parse_text = linecache.getline(working_input_file, line_to_parse)
    parse_text = parse_text.rstrip("\n").rstrip(" ")

    try:

        regex = r"""^[\\][a-z0-9]+"""
        matches = re.search(
            regex, parse_text[parse_index:],
            re.MULTILINE | re.VERBOSE)
        end = matches.end()
        match = matches.group()
        match_split = re.findall(r"[\\][^\W\d_]+|\d+", match)

        with open(control_word_func_dict, "r") as control_word_func_dict_pre:
            control_word_func_dict_contents = json.load(
                control_word_func_dict_pre)

            try:
                cw_base = control_word_func_dict_contents[match_split[0]]
                if cw_base is None:
                    pass
                else:
                    control_word_functions.DestinationFunctions(
                        match=match_split, cw_base=cw_base)

            except KeyError:
                # If the destination is not in control_word_func_dict,
                # add it to a storage file of destinations. At the end of RtoX,
                # those destinations will be added to the dict.
                key = match_split[0]
                cw_update = {key: "null"}
                base_script_dir = os.path.dirname(os.path.abspath(
                    sys.argv[0]))
                dicts_dir = os.path.join(base_script_dir, "Library/dicts")
                control_word_func_missing_keys_file = os.path.join(
                    dicts_dir, "control_word_func_missing_keys_file.json")
                with open(control_word_func_missing_keys_file) as \
                        control_word_func_missing_keys:
                    cwf_missing_keys = json.load(
                        control_word_func_missing_keys)
                    cwf_missing_keys.update(cw_update)
                with open(control_word_func_missing_keys_file, "a+",
                          encoding='utf-8') as \
                        control_word_func_missing_keys:
                    json.dump(cwf_missing_keys, control_word_func_missing_keys,
                              ensure_ascii=False)

            parse_index = parse_index + end

        print("DESTINATION", match_split[0], line_to_parse, parse_index)
        return line_to_parse, parse_index

    except TypeError:
        # Add text that cannot be processed to working_xml_file.
        regex = """^[^a-z0-9][a-z0-9]+"""
        matches = re.search(
            regex, parse_text[parse_index:],
            re.MULTILINE | re.VERBOSE)
        content = "<rtfIssue line=" + f"{line_to_parse}" + ">" \
                  + matches.group(0) + "</rtfIssue>"
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=content)
        end = matches.end()
        parse_index = parse_index + end

    return line_to_parse, parse_index
