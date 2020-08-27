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


def text_metric_reset(processing_dict: dict) -> dict:
    length = len(processing_dict["parse_text"])
    if length <= 2:
        line_to_parse_update = processing_dict["line_to_parse"] + 1
        processing_dict["line_to_parse"] = line_to_parse_update
        line = linecache.getline(processing_dict["working_input_file"],
                                 processing_dict["line_to_parse"]).rstrip("\n")
        parse_text_update = processing_dict["parse_text"] + line
        processing_dict["parse_text"] = parse_text_update
        processing_dict["parse_index"] = 0
        return processing_dict
    else:
        return processing_dict
