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

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_parse_text"

# From standard libraries
import sys

# From local application
import check_group
import control_word
import backslash_text
import left_bracket_text
import check_text


def check_string_manager(working_input_file: str, debug_dir: str,
                         control_word_dict: str, parse_text: str,
                         line_to_parse: int, parse_index: int,
                         num_lines: int) -> None:

    csm_dict = {"working_input_file": working_input_file,
                "debug_dir": debug_dir,
                "control_word_dict": control_word_dict,
                "parse_text": parse_text,
                "line_to_parse": line_to_parse,
                "parse_index": parse_index,
                "num_lines": num_lines}

    if line_to_parse > num_lines:
        sys.exit()
    else:
        # Checks for an RTF group.
        check_group.processor(**csm_dict)
        # Checks for a backslash that should be treated as text.
        backslash_text.processor(**csm_dict)
        # Checks for a left bracket that should be treated as text.
        left_bracket_text.processor(**csm_dict)
        # Checks for a control word or destination.
        control_word.processor(**csm_dict)
        # Checks for text.
        check_text.processor(**csm_dict)
