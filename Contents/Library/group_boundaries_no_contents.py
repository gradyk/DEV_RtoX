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

"""
Module that identifies and returns the start line and index, and end line and
index, for RTF tables or groups.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.group_boundaries_no_contents"

# From standard libraries
import linecache
from collections import deque

# From application libraries
import file_stats


def define_boundaries_without_contents(table: str, working_input_file: str,
                                       table_start_line: int,
                                       table_start_index: int) -> dict:
    """ Define the boundaries of an RTF table or group, without capturing
    the contents of the table or group. """
    table_boundaries_info = {}
    group_start_line = table_start_line
    search_line = table_start_line
    string_to_search = linecache.getline(working_input_file, search_line)
    string_to_search = string_to_search.replace("\n", "")

    deck = deque()
    length_string_to_search = len(string_to_search)
    index = table_start_index
    group_start_index = table_start_index

    while index < length_string_to_search:

        if string_to_search[index] == "{":
            deck.append(string_to_search[index])
            index += 1
        elif string_to_search[index] == "}":
            deck.popleft()
            index += 1

            if not deck:  # mMeans if deck becomes empty
                group_end_line = search_line
                group_end_index = index
                table_boundaries_info.update({table: [group_start_line,
                                                      group_start_index,
                                                      group_end_line,
                                                      group_end_index]})
                return table_boundaries_info
        else:
            index += 1
            pass

    index = 0
    search_line += 1
    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_metrics[0]

    while search_line <= length_working_input_file:
        string_to_search = linecache.getline(working_input_file, search_line)
        string_to_search = string_to_search.replace("\n", "")
        length_string_to_search = len(string_to_search)
        string_to_search = string_to_search[index:length_string_to_search]

        while index < length_string_to_search:

            if string_to_search[index] == "{":
                deck.append(string_to_search[index])
                index += 1
            elif string_to_search[index] == "}":
                deck.popleft()
                index += 1

                if not deck:  # Means if deck becomes empty
                    group_end_line = search_line
                    group_end_index = index
                    table_boundaries_info.update({table:
                                                  [group_start_line,
                                                   group_start_index,
                                                   group_end_line,
                                                   group_end_index]})
                    return table_boundaries_info
            else:
                index += 1
                pass

        search_line += 1
        index = 0

    group_end_line = search_line
    group_end_index = index
    table_boundaries_info.update({table:
                                  [group_start_line,
                                   group_start_index,
                                   group_end_line,
                                   group_end_index]})

    return table_boundaries_info
