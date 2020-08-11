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

""" Headers and footers have the following format;
    <hdrftr>        '{' <hdrctl> <pap>+ '}' <hdrftr>?
    <hdrctl>        \\header | \\footer | \\headerderl | \\headerr |
                    \\headerf | \\footer | \\footerr | \\footerf
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.header_cwd"

# From standard libraries


# From local applications
import facingp_titlepg


header_cwd_list = {  # Spec Page 45
    "\\header": ["Coded", "Header on all pages.", "Destination"],
    "\\headerl": ["Coded", "Header on left pages only.", "Destination"],
    "\\headerr": ["Coded", "Header on right pages only.", "Destination"],
    "\\headerf": ["Coded", "Header on first page only.", "Destination"],
}

def header_control(working_input_file: str):
    face_title = facingp_titlepg.search_for_facingp_titlepg(
        working_input_file=working_input_file)

    for item in face_title:
        if item[0] == "facingp" and item[1] is None:

        elif



if facingp, then headerl, headerr, footerl, footerr
if no facingp, then header, footer
if titlepg, the headerf, footerf

if titlepg and facingpg,

if no titlepg and no facingpg, then header, footer

if Section 1 has titlepg and headerf or footerf
    and if Section 2 does not have titlepg, then
    headerf/footerf will not appear. But, if Section 3
    does have titlepg, headerf/footerf will reappear.

