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
                                       line_to_parse: int,
                                       parse_index: int,
                                       shift_text) -> tuple:
    """ Define the boundaries of an RTF table or group, while capturing
    the contents of the table or group. """
    group_info = {}
    group_contents = ""
    start_line = line_to_parse
    start_index = parse_index
    parse_text = linecache.getline(working_input_file, line_to_parse)
    parse_text = parse_text.rstrip("\n").rstrip(" ")
    length_parse_text = len(parse_text)

    if parse_index > (length_parse_text - 3):
        shift_length = length_parse_text - parse_index
        shift_text = parse_text[-shift_length]
        line_to_parse += 1
        parse_index = 0
        parse_text = linecache.getline(working_input_file, line_to_parse)
        parse_text = parse_text.rstrip("\n").rstrip(" ")
        parse_text = shift_text + parse_text
        length_parse_text = len(parse_text)
    else:
        parse_text = shift_text + parse_text
        length_parse_text = len(parse_text)
        pass

    deck = deque()

    while parse_index < length_parse_text:

        if parse_text[parse_index] == "{":
            deck.append(parse_text[parse_index])
            group_contents = group_contents + parse_text[parse_index]
            parse_index += 1
        elif parse_text[parse_index] == "}":
            deck.popleft()

            if not deck:
                group_contents = group_contents + parse_text[parse_index]
                group_end_line = line_to_parse
                group_end_index = parse_index + 1
                group_id = str(line_to_parse) + "_" + str(parse_index)
                group_info.update({group_id:
                                   [group_contents,
                                    line_to_parse,
                                    parse_index,
                                    group_end_line,
                                    group_end_index]})
                print("  BOUNDARIES 0")
                print("    ", start_line, start_index)
                print("    ", group_info[group_id][0])
                if group_end_index < length_parse_text:
                    print("    ", group_end_line, group_end_index,
                          parse_text[group_end_index])
                else:
                    print("    ", group_end_line, group_end_index)
                return group_id, group_info
            else:
                parse_index += 1
        else:
            group_contents = group_contents + parse_text[parse_index]
            parse_index += 1
            pass

    tracker = line_to_parse + 1
    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_metrics[0]

    while tracker <= length_working_input_file:
        parse_index = 0
        line_to_parse = tracker
        parse_text = linecache.getline(working_input_file, line_to_parse)
        parse_text = parse_text.rstrip("\n").rstrip(" ")
        parse_text = parse_text[parse_index:]
        length_parse_text = len(parse_text)

        while parse_index < length_parse_text:

            if parse_text[parse_index] == "{":
                deck.append(parse_text[parse_index])

            elif parse_text[parse_index] == "}":
                deck.popleft()

                if not deck:  # Means if deck becomes empty
                    group_contents = group_contents + parse_text[parse_index]
                    group_end_line = line_to_parse

                    if parse_text[parse_index] == " ":
                        group_end_index = parse_index + 2
                        parse_index += 2
                    else:
                        group_end_index = parse_index + 1
                        parse_index += 1
                    group_id = str(line_to_parse) + "_" + str(
                        parse_index)
                    group_info.update({group_id:
                                       [group_contents,
                                        line_to_parse,
                                        parse_index,
                                        group_end_line,
                                        group_end_index]})
                    print("  BOUNDARIES 1")
                    print("    ", start_line, start_index)
                    print("    ", group_info[group_id][0])
                    print("    ", group_end_line, group_end_index,
                          parse_text[group_end_index])
                    return group_id, group_info
            else:
                pass

            group_contents = group_contents + parse_text[parse_index]
            parse_index += 1

        tracker += 1

    group_end_line = line_to_parse
    group_end_index = parse_index + 1
    group_id = str(line_to_parse) + "_" + str(parse_index)
    group_info.update({group_id:
                       [group_contents,
                        line_to_parse,
                        parse_index,
                        group_end_line,
                        group_end_index]})
    print("  BOUNDARIES 2", group_info[group_id][0],
          group_end_line, group_end_index,
          parse_text[group_end_index],
          parse_text[group_end_index + 1])
    return group_id, group_info
