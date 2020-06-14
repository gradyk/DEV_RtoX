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

import os


def single_line_rtf_file():
    base_script_dir = '/Users/gradyke/Documents/DEV_RtoX/Contents'
    debug_dir = os.path.join(base_script_dir, "debugdir")

    with open(os.path.join(debug_dir, "working_input_file.txt"), "r") as \
            input_file_pre:
        input_file = input_file_pre.read()
        input_file = input_file.replace("\n", "")

    with open(os.path.join(debug_dir, "working_input_single_line.txt"),
              "w+") as single_line_input_file_pre:
        single_line_input_file_pre.write(input_file)


if __name__ == "__main__":
    single_line_rtf_file()
