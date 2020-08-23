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

import linecache


def text_metric_reset(working_input_file: str, parse_index: int,
                      line_to_parse: int, parse_text: str) -> tuple:
    length = len(parse_text)
    if length <= 2:
        line_to_parse += 1
        line = linecache.getline(working_input_file, line_to_parse).rstrip("\n")
        parse_text = parse_text + line
        parse_index = 0
        return parse_text, line_to_parse, parse_index
    else:
        # parse_text = parse_text[parse_index:]
        # parse_index = 0
        return parse_text, line_to_parse, parse_index
