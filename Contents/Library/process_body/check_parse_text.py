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

# From local application
import check_group
import post1987_destination
import control_word
import control_symbol
import backslash_text
import left_bracket_text
import check_text


class CheckString(object):
    def __init__(self,
                 working_input_file: str,
                 debug_dir: str,
                 control_word_dict: str,
                 parse_text: str,
                 line_to_parse: int,
                 parse_index: int):
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.control_word_dict = control_word_dict
        self.parse_text = parse_text
        self.line_to_parse = line_to_parse
        self.parse_index = parse_index

    def check_string_manager(self):

        check_group.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text)
        post1987_destination.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text,
            control_word_dict=self.control_word_dict)
        control_symbol.processor(parse_text=self.parse_text,
                                 debug_dir=self.debug_dir,
                                 line_to_parse=self.line_to_parse)
        backslash_text.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text)
        left_bracket_text.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text)
        control_word.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text,
            control_word_dict=self.control_word_dict)
        check_text.processor(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir, line_to_parse=self.line_to_parse,
            parse_index=self.parse_index, parse_text=self.parse_text)
