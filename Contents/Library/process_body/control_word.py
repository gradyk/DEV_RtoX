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
import adjust_process_text
import control_word_manager


def processor(debug_dir: str, parse_index: int, parse_text: str,
              line_to_parse: int, working_input_file: str,
              control_word_dict: str) -> None:
    # Test for control word: \\LetterSequence<Delimiter>
    test = re.search(r"(\\)([a-zA-Z]*)(\s|-|[0-9]+)+", parse_text[0:])
    if test is not None:
        control_word = "".join([i for i in test[0] if i.isalpha()])
        control_word_value = "".join([i for i in test[0] if i.isdigit()])
        parse_index = parse_index + test.end()
        control_word_manager.process_control_word(
            control_word=control_word,
            control_word_value=control_word_value,
            control_word_dict=control_word_dict,
            debug_dir=debug_dir,
            line_to_parse=line_to_parse)
        adjust_process_text.text_metric_reset(
            parse_index=parse_index,
            line_to_parse=line_to_parse,
            working_input_file=working_input_file)
    else:
        pass
