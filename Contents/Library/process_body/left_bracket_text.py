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
__name__ = "Contents.Library.process_body.left_bracket_text"

# From standard libraries
import logging
import re

# From local application
import adjust_process_text
import build_final_file
import check_parse_text
import control_word


def processor(parse_text: str, line_to_parse: int, parse_index: int,
              group_dict: dict,
              working_input_file: str, debug_dir: str,
              control_word_dict: str, num_lines: int) -> None:
    # Test for left bracket character as part of text.
    item = None
    try:
        test = re.search(r"^({)", parse_text)
        if test is not item:
            open_tag = ""
            text = "{"
            close_tag = ""
            build_final_file.processor(open_tag=open_tag,
                                       text=text,
                                       close_tag=close_tag)

            parse_text = parse_text.replace(test[0], "")
            parse_index = 0

            parse_text, line_to_parse, parse_index = \
                adjust_process_text.text_metric_reset(
                    working_input_file=working_input_file,
                    parse_index=parse_index,
                    line_to_parse=line_to_parse,
                    parse_text=parse_text)
            check_parse_text.check_string_manager(
                parse_text=parse_text,
                line_to_parse=line_to_parse,
                parse_index=parse_index, working_input_file=working_input_file,
                debug_dir=debug_dir, control_word_dict=control_word_dict,
                num_lines=num_lines, group_dict=group_dict)
        else:
            control_word.processor(
                parse_text=parse_text,
                line_to_parse=line_to_parse,
                parse_index=parse_index, working_input_file=working_input_file,
                debug_dir=debug_dir, control_word_dict=control_word_dict,
                num_lines=num_lines,
                group_dict=group_dict)
            pass
    except TypeError:
        logging.exception(f"Left_bracket_test: {line_to_parse}:{parse_index}"
                          f"--{parse_text}")
        pass
