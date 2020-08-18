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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

# BASED ON USER'S SELECTION, GO TO LATEX OR XML FILE BUILDER AND ADD TEXT

# From standard libraries
import os
import sys


def processor(open_tag: str, close_tag: str, text: str) -> None:
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_script_dir, "debugdir")
    output_file_base = os.path.join(debug_dir, "output_file.xml")

    with open(output_file_base, "r") as output_file_pre:
        output_file = output_file_pre.read()
        update_list = [open_tag, text, close_tag]
        content_update = ''.join(update_list)
        output_file_updated = output_file + content_update

    with open(output_file_base, "w") as output_file_pre:
        output_file_pre.write(output_file_updated)
