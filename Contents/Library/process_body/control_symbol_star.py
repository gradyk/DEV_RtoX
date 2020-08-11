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

""" In RTF, a "{\\*" combination (remembering two slashes appears as only
one slash in an RTF file whereas in a Python file the first slash is an
escape symbol) indicates a destination group that RtoX can ignore. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-16"
__name__ = "Contents.Library.process_body.control_symbol_star"

# From standard libraries
import process_body.group_boundaries_capture_contents


def processor(working_input_file: str, parse_index: int,
              line_to_parse: int, debug_dir: str) -> tuple:
    # {group_id:
    #  [group_contents,
    #   group_start_line,
    #   group_start_index,
    #   group_end_line,
    #   group_end_index]}

    group_id, group_info \
        = process_body.group_boundaries_capture_contents \
        .define_boundaries_capture_contents(
            working_input_file=working_input_file,
            line_to_parse=line_to_parse,
            parse_index=parse_index,
            debug_dir=debug_dir)

    # NEED TO REDO NEXT LINES AND CHANGE RETURN
    line_to_parse = group_info[group_id][3]
    parse_index = group_info[group_id][4]

    return line_to_parse, parse_index
