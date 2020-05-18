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
import re

# From local application
import control_word_functions


def destination_processor(line_to_parse: int, parse_index: int,
                          working_input_file: str,
                          control_word_func_dict: str) -> tuple:
    search_string = linecache.getline(working_input_file, line_to_parse)
    if search_string[parse_index:].find("{") is -1:
        regex = r"""[\\].+?(?=\\)"""
        matches = re.search(
            regex, search_string[parse_index:], re.MULTILINE | re.VERBOSE)
        if matches:
            end = matches.end()
            match = matches.group()
            match_split = re.findall(r"[\\][^\W\d_]+|\d+", match)
            with open(control_word_func_dict, "r") as \
                    control_word_func_dict_pre:
                control_word_func_dict_contents = json.load(
                    control_word_func_dict_pre)
                if control_word_func_dict_contents[match_split[0]] is not None:
                    # TODO: Fix .format to reduce risk
                    # Replace using string.Template
                    #
                    # Replace using CustomFormatter(string.Formatter)
                    # overwriting the get_field function and disable the
                    # access to protected attributes (all with _ at the
                    # beginning)
                    control_word_func_dict_contents[match_split[0]].format(
                        match=match_split)
                else:
                    pass
            parse_index = end
            return line_to_parse, parse_index
            pass
        else:
            pass
    else:
        pass
