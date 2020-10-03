#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
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

"""
Finds the end of the {\\cs line.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.keyword_end_alt"

# From standard library
import linecache


# TODO Compare this to footnote_end_alt: they seem to be the same. Why can't
#  footnote_end_alt be replace by this generic function? (the return would be
#  changed to keyword_end_line)
def keyword_end_alt(working_file: str, keyword_open: int) -> str:

    search_line = keyword_open

    left_brace = 0
    right_brace = 0
    cs_end_line = "0"
    while cs_end_line == "0":
        search_text = linecache.getline(working_file, search_line)
        for elem in search_text:
            if elem == "{":
                left_brace += 1
            elif elem == "}":
                right_brace += 1
            if left_brace == right_brace:
                cs_end_line = search_line
            else:
                pass
        search_line += 1

    linecache.clearcache()
    return cs_end_line
