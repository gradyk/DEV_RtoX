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

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.group_boundaries_capture_contents"

# From standard libraries
import linecache
from collections import deque

# From local application
import file_stats


def define_boundaries_capture_contents(working_input_file: str,
                                       group_start_line: int,
                                       group_start_index: int) -> dict:
    """ Define the boundaries of an RTF table or group, while capturing
    the contents of the table or group. """
    group_info = {}
    group_contents = ""
    search_line = group_start_line
    string_to_search = linecache.getline(working_input_file, search_line)
    string_to_search = string_to_search.replace("\n", "")

    deck = deque()
    length_string_to_search = len(string_to_search)
    index = group_start_index

    while index < length_string_to_search:

        if string_to_search[index] == "{":
            deck.append(string_to_search[index])
            group_contents = group_contents + string_to_search[index]
            index += 1
        elif string_to_search[index] == "}":
            deck.popleft()
            group_contents = group_contents + string_to_search[index]
            index += 1

            if not deck:
                group_end_line = search_line
                group_end_index = index
                group_id = str(group_start_line) + "_" + str(group_start_index)
                group_info.update({group_id:
                                   [group_contents,
                                    group_start_line,
                                    group_start_index,
                                    group_end_line,
                                    group_end_index]})

                return group_info
        else:
            group_contents = group_contents + string_to_search[index]
            index += 1
            pass

    tracker = search_line + 1
    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_metrics[0]

    while tracker <= length_working_input_file:
        index = 0
        search_line = tracker
        string_to_search = linecache.getline(working_input_file, search_line)
        string_to_search = string_to_search.replace("\n", "")
        string_to_search = string_to_search[index:]
        length_string_to_search = len(string_to_search)

        while index < length_string_to_search:

            if string_to_search[index] == "{":
                deck.append(string_to_search[index])

            elif string_to_search[index] == "}":
                deck.popleft()

                if not deck:  # Means if deck becomes empty
                    group_end_line = search_line
                    group_end_index = index
                    group_contents = group_contents + string_to_search[0:index]
                    group_id = str(group_start_line) + "_" + str(
                        group_start_index)
                    group_info.update({group_id:
                                       [group_contents,
                                        group_start_line,
                                        group_start_index,
                                        group_end_line,
                                        group_end_index]})
                    return group_info
            else:
                pass

            group_contents = group_contents + string_to_search[index]
            index += 1

        tracker += 1

    group_end_line = search_line
    group_end_index = index
    group_id = str(group_start_line) + "_" + str(group_start_index)
    group_info.update({group_id:
                       [group_contents,
                        group_start_line,
                        group_start_index,
                        group_end_line,
                        group_end_index]})

    return group_info
