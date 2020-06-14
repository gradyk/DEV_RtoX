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

""" An RTF group is enclosed by braces: {}. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-16"
__name__ = "Contents.Library.group"

# From application library
import Contents.Library.group_boundaries_capture_contents


def group_processor(parse_index: int, line_to_parse: int,
                    working_input_file: str,
                    shift_text: str) -> tuple:
    print("GROUP BEGIN:")
    group_start_index = parse_index
    group_id, group_info = Contents.Library. \
        group_boundaries_capture_contents. \
        define_boundaries_capture_contents(
            working_input_file=working_input_file,
            line_to_parse=line_to_parse,
            parse_index=group_start_index,
            shift_text=shift_text)
    print("GROUP END")
    reset_line_to_parse = group_info[group_id][3]  # group_end_line
    parse_index = group_info[group_id][4]  # group_end_index

    return group_id, group_info, reset_line_to_parse, parse_index
