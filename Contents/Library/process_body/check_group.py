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
import group_boundaries_capture_contents
import group_contents


def processor(debug_dir: str, parse_index: int, parse_text: str,
              line_to_parse: int, working_input_file: str) -> None:

    test = re.search(r"{", parse_text)
    if test is not None:

        group_info = group_boundaries_capture_contents. \
            define_boundaries_capture_contents(
                working_input_file=working_input_file,
                line_to_parse=line_to_parse,
                parse_index=parse_index)

        group_contents.processor_settings(group_info=group_info)

    else:
        pass
