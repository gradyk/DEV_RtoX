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

""" In RTF, a "{\\*" combination (remembering two slashes appears as only
one slash in an RTF file whereas in a Python file the first slash is an
escape symbol) indicates a destination group that RtoX can ignore. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-06-01"
__name__ = "Contents.Library.contents_slash_star"

# From standard libraries
from collections import deque


def contents_slash_star_processor(contents: str, parse_index: int) -> int:
    # {group_id:
    #  [group_start_index,
    #   group_end_index]}
    group_id, group_info = define_contents_slashstar_boundaries(
            contents=contents,
            parse_index=parse_index)
    parse_index = group_info[group_id][1]
    return parse_index


def define_contents_slashstar_boundaries(contents: str,
                                         parse_index: int) -> tuple:
    """ Define the boundaries of an RTF control symbol group within an RTF
    group. """
    group_info = {}
    length_contents = len(contents)

    deck = deque()
    print("  CONTENT SLASH STAR BEGIN:", parse_index, contents[parse_index])
    while parse_index < length_contents:

        if contents[parse_index] == "{":
            deck.append(contents[parse_index])
            parse_index += 1
        elif contents[parse_index] == "}":
            deck.popleft()

            if not deck:
                group_end_index = parse_index + 1
                print("  CONTENT SLASH STAR END:", parse_index,
                      contents[parse_index], contents[group_end_index])
                group_id = "CONTENTS" + "_" + str(parse_index)
                group_info.update({group_id:
                                   [parse_index,
                                    group_end_index]})

                return group_id, group_info
            else:
                pass
        else:
            parse_index += 1
            pass
