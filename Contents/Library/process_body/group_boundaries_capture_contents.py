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
__name__ = "Contents.Library.process_body.group_boundaries_capture_contents"

# From standard libraries
import linecache
from collections import deque

# From local application
import adjust_process_text


def define_boundaries_capture_contents(working_input_file: str,
                                       line_to_parse: int,
                                       parse_index: int) -> tuple:
    """ Define the boundaries of an RTF table or group, while capturing
    the contents of the table or group. """
    group_contents = ""
    parse_text = linecache.getline(working_input_file, line_to_parse)
    parse_text = parse_text.rstrip("\n").rstrip(" ")
    working_index = parse_index

    if working_index > (len(parse_text) - 2):
        parse_text, line_to_parse, working_index = \
            adjust_process_text.text_metric_reset(
                working_input_file=working_input_file,
                line_to_parse=line_to_parse,
                parse_index=working_index)
    else:
        pass

    deck = deque()

    while working_index < len(parse_text):

        if parse_text[working_index] == "{":
            deck.append(parse_text[working_index])
            group_contents = group_contents + parse_text[working_index]
            working_index += 1
        elif parse_text[working_index] == "}":
            group_contents = group_contents + parse_text[working_index]
            deck.popleft()

            if not deck:  # If deck is empty ...
                group_end_line = line_to_parse
                group_end_index = working_index + 1
                key_list = [str(line_to_parse), "_", str(parse_index)]
                key = ''.join(key_list)
                group_info = {key:
                              [group_contents,
                               line_to_parse,
                               parse_index,
                               group_end_line,
                               group_end_index]}
                return group_info, key
            else:
                working_index += 1
        else:
            group_contents = group_contents + parse_text[working_index]
            working_index += 1
            pass

    tracker = line_to_parse + 1

    working_index = 0
    line_to_parse = tracker
    parse_text = linecache.getline(working_input_file, line_to_parse)
    parse_text = parse_text.rstrip("\n").rstrip(" ")
    parse_text = parse_text[working_index:]

    while working_index < len(parse_text):

        if parse_text[working_index] == "{":
            deck.append(parse_text[parse_index])

        elif parse_text[working_index] == "}":
            group_contents = group_contents + parse_text[working_index]
            deck.popleft()

            if not deck:  # If deck is empty ...
                group_end_line = line_to_parse

                if parse_text[working_index] == " ":
                    group_end_index = working_index + 2
                    working_index += 2
                else:
                    group_end_index = working_index + 1
                    working_index += 1
                key_list = [str(line_to_parse), "_", str(parse_index)]
                key = ''.join(key_list)
                group_info = {key:
                              [group_contents,
                               line_to_parse,
                               parse_index,
                               group_end_line,
                               group_end_index]}

                return group_info, key
        else:
            pass

        group_contents = group_contents + parse_text[working_index]
        working_index += 1

    tracker += 1

    group_end_line = line_to_parse
    group_end_index = working_index + 1
    key_list = [str(line_to_parse), "_", str(parse_index)]
    key = "".join(key_list)
    group_info = {key:
                  [group_contents,
                   line_to_parse,
                   parse_index,
                   group_end_line,
                   group_end_index]}

    return group_info, key
