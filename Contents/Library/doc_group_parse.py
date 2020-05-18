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

""" An RTF group is bound by a "{" and a "}". The group may include
groups, destinations, and destinations that can be ignored "\\*\\". This
processor handles each component of a group. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-05-09"
__name__ = "Contents.Library.doc_group_parse"

# From standard library
import re

# From local application
import Contents.Library.destination
import Contents.Library.group_boundaries_capture_contents
import Contents.Library.slash_star
import working_xml_file_update


def group_parse_processor(group_info: dict, working_input_file: str,
                          line_to_parse: int, parse_index: int,
                          control_word_func_dict: str, debug_dir: str):

    for key in group_info:
        group_contents = group_info[key][0]
        # {group_id:
        #      [group_contents,
        #       group_start_line,
        #       group_start_index,
        #       group_end_line,
        #       group_end_index]}
        if group_contents[0] == "{" and group_contents[1] == "\\" and \
                group_contents[2] == "*":

            line_to_parse, parse_index \
                = Contents.Library.slash_star.slash_star_processor(
                    working_input_file=working_input_file,
                    parse_index=parse_index,
                    line_to_parse=line_to_parse)
            pass

        elif group_contents[0] is "\\":
            line_to_parse, parse_index = \
                Contents.Library.destination.destination_processor(
                    line_to_parse=line_to_parse,
                    parse_index=parse_index,
                    working_input_file=working_input_file,
                    control_word_func_dict=control_word_func_dict)
            pass

        elif group_contents[0] is " " and group_contents[1] is not "\\" and \
                group_contents[1] is not "}" and group_contents[1] is not "{":
            regex = r"\s+(\w+|\s|\W)+(?<!})"
            match = re.search(regex, group_contents)
            if match:
                working_xml_file_update.tag_append(
                    debug_dir=debug_dir,
                    tag_update=match.group(0))
            parse_index += 1
            pass

        elif group_contents[0] is "{":
            parse_index += 1
            pass

        else:
            parse_index += 1
            pass

    return line_to_parse, parse_index
