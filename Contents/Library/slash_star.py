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
__name__ = "Contents.Library.slash_star"

# From standard libraries
import Contents.Library.group_boundaries_no_contents


def slash_star_processor(working_input_file: str, parse_index: int,
                         line_to_parse: int) -> tuple:
    table_boundaries_info \
        = Contents.Library.group_boundaries_no_contents \
        .define_boundaries_without_contents(
            table=str(line_to_parse) + "_" + str(parse_index),
            working_input_file=working_input_file,
            table_start_line=line_to_parse,
            table_start_index=parse_index)
    entry = str(line_to_parse) + "_" + str(parse_index)
    line_to_parse = table_boundaries_info[entry][2]
    parse_index = table_boundaries_info[entry][3]
    return line_to_parse, parse_index
