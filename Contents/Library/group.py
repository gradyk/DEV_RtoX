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
import Contents.Library.doc_group_parse
import Contents.Library.group_boundaries_capture_contents


def group_processor(parse_index: int, line_to_parse: int,
                    working_input_file: str,
                    debug_dir: str, control_word_func_dict: str):

    group_start_index = parse_index

    group_info = Contents.Library. \
        group_boundaries_capture_contents. \
        define_boundaries_capture_contents(
            working_input_file=working_input_file,
            group_start_line=line_to_parse,
            group_start_index=group_start_index)

    line_to_parse, parse_index = \
        Contents.Library.doc_group_parse.group_parse_processor(
            group_info=group_info, debug_dir=debug_dir,
            control_word_func_dict=control_word_func_dict,
            line_to_parse=line_to_parse, parse_index=parse_index,
            working_input_file=working_input_file)

    return line_to_parse, parse_index
