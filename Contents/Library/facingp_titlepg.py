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
__name__ = "Contents.Library.facingp_titlepg"

# From standard libraries
import linecache
import re

# From local application
import file_stats


def search_for_facingp_titlepg(working_input_file: str) -> list:
    face_title = []
    cwd_list_two = {  # Spec Page 45
        "facingp": ["Coded", "", "Flag"],
        "titlepg": ["Coded", "", "Flag"]
    }
    file_stats_results = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_stats_results[1]
    for key in cwd_list_two:
        count = 0
        line = 1
        while line <= length_working_input_file:
            match = re.search(r"\\"+f"{key}", linecache.getline(
                working_input_file, line))
            if match is not None:
                face_title.append((key, line))
                count += 1
                line += 1
            else:
                line += 1
        if count > 0:
            pass
        else:
            face_title.append((key, None))

    linecache.clearcache()
    return face_title
