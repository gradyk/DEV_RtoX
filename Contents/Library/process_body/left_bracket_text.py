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

# From standard libraries
import re

# From local application
import build_final_file


def processor(debug_dir: str, parse_index: int, parse_text: str,
              line_to_parse: int, working_input_file: str) -> None:
    # Test for left bracket character as part of text.
    test = re.search(r"\\{", parse_text[0:2])
    if test is not None:
        text = "{"
        parse_index = parse_index + test.end()
        build_final_file.output_style_selector(text=text)
    else:
        pass
