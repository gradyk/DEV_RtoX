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
#   RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

"""
Module that breaks down RTF tables into separated groups for parsing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.table_boundaries"

# From standard libraries
import linecache


def find_table_start_end(table: str, working_input_file: str,
                         table_start_line: str):
    """ Finding definitions within a table is a three-step process. First,
    find the entirety of the text within the table. Second, break the text
    into major table groups (e.g., font, color). Third, parse each
    table group. """

    line_to_search = table_start_line

    table_last_line = 0
    table_last_brace = 0
    left_brace_count = 0
    right_brace_count = 0

    startint_string = linecache.getline(working_input_file, line_to_search)
    line_length = len(startint_string)

    table_first_brace = startint_string.find(table) - 2
    string_to_search = startint_string[table_first_brace:line_length]

    while table_last_brace == 0:

        for character in string_to_search:
            if character == "{":
                left_brace_count += 1
            elif character == "}":
                right_brace_count += 1
            if left_brace_count == right_brace_count:
                table_last_line = line_to_search
                table_last_brace = string_to_search.index(
                    character)
            else:
                pass
        line_to_search += 1
        string_to_search = linecache.getline(working_input_file, line_to_search)

    return table_start_line,  table_first_brace, table_last_line, \
        table_last_brace
