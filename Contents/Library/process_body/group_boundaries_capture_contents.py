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
import build_group_contents_list


def define_boundaries_capture_contents(processing_dict: dict) -> None:
    """ Define the boundaries of an RTF table or group, while capturing
    the contents of the table or group. """
    processing_dict["group_contents"] = ""
    deck = deque()
    working_index = processing_dict["parse_index"]
    decklength = 1
    boundary_master(
        decklength=decklength, deck=deck,
        processing_dict=processing_dict,
        working_index=working_index)


def boundary_master(decklength: int, working_index: int,
                    processing_dict: dict, deck):
    while decklength != 0:

        processing_dict, decklength = boundary_test(
            working_index=working_index, deck=deck,
            processing_dict=processing_dict,
            decklength=decklength)

        processing_dict["line_to_parse"] = processing_dict["line_to_parse"] + 1
        processing_dict["parse_index"] = processing_dict["group_end_index"]

    build_group_contents_list.pre_process(
        processing_dict=processing_dict)


def boundary_test(processing_dict: dict, working_index: int, deck,
                  decklength: int) -> tuple:
    processing_dict["parse_text"] = linecache.getline(
        processing_dict["working_input_file"], processing_dict["line_to_parse"])
    processing_dict["parse_text"] = \
        processing_dict["parse_text"].rstrip("\n").rstrip(" ")
    processing_dict["parse_text"] = \
        processing_dict["parse_text"][working_index:]
    length = len(processing_dict["parse_text"])

    if working_index > length - 2:
        processing_dict = adjust_process_text.text_metric_reset(
            processing_dict=processing_dict)
    else:
        pass

    while working_index < length:

        if processing_dict["parse_text"][working_index] == "{":
            deck.append(processing_dict["parse_text"][working_index])
            processing_dict["group_contents"] = \
                processing_dict["group_contents"] + \
                processing_dict["parse_text"][working_index]
            working_index += 1
            decklength = len(deck)
        elif processing_dict["parse_text"][working_index] == "}":
            processing_dict["group_contents"] = \
                processing_dict["group_contents"] + \
                processing_dict["parse_text"][working_index]
            deck.popleft()

            decklength = len(deck)
            if decklength == 0:  # If deck is empty ...
                processing_dict["group_end_line"] = \
                    processing_dict["line_to_parse"]
                processing_dict["group_end_index"] = working_index + 1
                boundary_master(decklength=decklength, deck=deck,
                                processing_dict=processing_dict,
                                working_index=working_index)
            else:
                working_index += 1
        else:
            processing_dict["group_contents"] = \
                processing_dict["group_contents"] + \
                processing_dict["parse_text"][working_index]
            working_index += 1
            pass
    return processing_dict, decklength
