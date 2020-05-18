#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
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

""" An RTF control symbol is indicated by a "\" followed by a single,
non-alphabetic character. They do not have delimiters (no space before
the next command). They often indicate a specific character, e.g.,
if the "\" is followed by a ~ it means non-breaking space. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-16"
__name__ = "Contents.Library.control_symbol"

# From standard libraries
import json
import linecache
import re


def control_symbol_processor(line_to_parse: int, parse_index: int,
                             working_input_file: str,
                             control_word_func_dict: str) -> tuple:
    search_string = linecache.getline(working_input_file, line_to_parse)
    if search_string[parse_index:].find("{") == -1:
        regex = r"""[\\]([^a-zA-Z0-9])+?(?!=\s)"""
        matches = re.search(
            regex, search_string[parse_index:], re.MULTILINE | re.VERBOSE)
        if matches:
            end = matches.end()
            match = matches.group()
            with open(control_word_func_dict, "r") as \
                    control_word_func_dict_pre:
                control_word_func_dict_contents = json.load(
                    control_word_func_dict_pre)
                if control_word_func_dict_contents[match]:
                    # TODO: Fix .format to reduce risk
                    # Replace using string.Template
                    #
                    # Replace using CustomFormatter(string.Formatter)
                    # overwriting the get_field function and disable the
                    # access to protected attributes (all with _ at the
                    # beginning)
                    control_word_func_dict_contents[match].format(match=match)
                else:
                    pass
            parse_index = end
            return line_to_parse, parse_index
            pass
        else:
            pass
    else:
        pass
