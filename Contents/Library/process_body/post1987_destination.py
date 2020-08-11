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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

# From standard libraries
import re

# From local application
import adjust_process_text
import control_word


def processor(debug_dir: str, parse_index: int, parse_text: str,
              line_to_parse: int, working_input_file: str,
              control_word_dict: str) -> None:
    # Test for post 3/1987 destination signal.
    test = re.search(r"(\\\*\\)([a-zA-Z]*)(\s|-|[0-9]+)+", parse_text)
    if test is not None:
        parse_text = test[0].replace("\\*", test[0])
        parse_index = parse_index + 2
        adjust_process_text.text_metric_reset(
            working_input_file=working_input_file,
            parse_index=parse_index,
            line_to_parse=line_to_parse)
        control_word.processor(
            working_input_file=working_input_file,
            debug_dir=debug_dir,
            control_word_dict=control_word_dict,
            line_to_parse=line_to_parse,
            parse_index=parse_index,
            parse_text=parse_text)
    else:
        pass
