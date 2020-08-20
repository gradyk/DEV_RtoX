#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

#
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

""" The main body of an RTF document has four components assembled in a
variety of combinations: control symbols, groups containing destinations that
can be ignored, destinations that must be processed (within or outside of
groups), and groups (which also contain pieces of the core text of the
original document). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.doc_parser"

# From standard libraries
import json
import linecache
import os
import re
import sys

# From local application
import process_body.control_word_manager
import contents_group_parse
import process_body.group
import Contents.Library.slash_star
import output_file_update


class MainDocDirector:
    def __init__(self,
                 working_input_file: str,
                 debug_dir: str,
                 control_word_dict: str,
                 shift_text="") -> None:
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.control_word_dict = control_word_dict
        self.parse_index = 0
        self.line_to_parse = 0
        self.shift_text = shift_text
        self.parse_text = 0
        self.length_parse_text = 0
        self.reset_line_to_parse = self.line_to_parse
        self.header_table_file = os.path.join(self.debug_dir,
                                              "../../debugdir/header_tables_dict.json")
        self.main_doc_dir = ()
        self.cw_lead = {}

    # https://softwareengineering.stackexchange.com/questions/182093/
    # why-store-a-function-inside-a-python-dictionary/182095

    def parse_controller(self):
        self.main_doc_dir = MainDocDirector(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir,
            control_word_dict=self.control_word_dict,
            shift_text=self.shift_text)

        self.cw_lead = {
            "{\\*": MainDocDirector.bracket_slash_star(self=self.main_doc_dir),
            "\\":   MainDocDirector.destination(self=self.main_doc_dir),
            '{':    MainDocDirector.group(self=self.main_doc_dir),
            '}':    MainDocDirector.closer(self=self.main_doc_dir),
            ' ':    MainDocDirector.blank_space(self=self.main_doc_dir),
        }

        MainDocDirector.retrieve_parse_start_point(self=self.main_doc_dir)
        MainDocDirector.load_tag_registry(self=self.main_doc_dir)

        self.parse_text, self.length_parse_text = \
            MainDocDirector.set_parse_text(
                self=self.main_doc_dir)

        while self.parse_index <= (self.length_parse_text - 1):
            self.parse_index, self.line_to_parse, self.shift_text = \
                MainDocDirector.set_parse_index(
                    self=self.main_doc_dir)

            character = self.parse_text[self.parse_index]
            character_plus_one = self.parse_text[self.parse_index+1]
            character_plus_two = self.parse_text[self.parse_index+2]
            init_chrs = character + character_plus_one + character_plus_two

            try:
                self.cw_lead[init_chrs[0]]()
            except (KeyError, ):
                self.line_to_parse, self.parse_index = \
                    MainDocDirector.contents(
                        self=self.main_doc_dir)

            if self.reset_line_to_parse != self.line_to_parse:
                self.line_to_parse = self.reset_line_to_parse
                break
            else:
                pass

            self.shift_text = ""

    def retrieve_parse_start_point(self) -> None:

        with open(self.header_table_file, "r") as header_table_dict_pre:
            header_table_dict = json.load(header_table_dict_pre)
        self.line_to_parse = header_table_dict["info"][2]
        self.parse_index = header_table_dict["info"][3]

    def load_tag_registry(self):
        base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        dicts_dir = os.path.join(base_script_dir, "Library/dicts")
        opening_registry_file = os.path.join(dicts_dir,
                                             "../dicts/opening_tag_registry_dict.json")
        tag_registry_file = os.path.join(self.debug_dir,
                                         "../../debugdir/tag_registry.json")
        with open(opening_registry_file) as orf:
            orf_copy = json.load(orf)
        with open(tag_registry_file) as trf:
            trf_ready = orf_copy.copy()
            json.dump(trf_ready, trf)

    def set_parse_text(self) -> tuple:
        parse_text = linecache.getline(self.working_input_file,
                                       self.line_to_parse)
        parse_text = parse_text.rstrip("\n").rstrip(" ")
        parse_text = self.shift_text + parse_text
        length_parse_text = len(parse_text)
        return parse_text, length_parse_text

    def set_parse_index(self):
        if self.parse_index > (self.length_parse_text - 3):
            shift_length = self.length_parse_text - self.parse_index
            self.shift_text = self.parse_text-shift_length
            self.line_to_parse += 1
            self.parse_index = 0
        else:
            pass
        return self.parse_index, self.line_to_parse, self.shift_text

    def blank_space(self) -> tuple:
        self.parse_index += 1
        return self.line_to_parse, self.parse_index

    def bracket_slash_star(self) -> tuple:
        self.line_to_parse, self.parse_index \
            = Contents.Library.slash_star.slash_star_processor(
                working_input_file=self.working_input_file,
                parse_index=self.parse_index,
                line_to_parse=self.line_to_parse,
                shift_text=self.shift_text)

        if self.reset_line_to_parse > self.line_to_parse:
            self.line_to_parse = self.reset_line_to_parse
        else:
            pass

        self.reset_line_to_parse, self.line_to_parse = \
            MainDocDirector.reset_parse_line(self=self.main_doc_dir)
        return self.line_to_parse, self.parse_index

    def closer(self) -> None:
        self.parse_index += 1
        self.reset_line_to_parse, self.line_to_parse = \
            MainDocDirector.reset_parse_line(self=self.main_doc_dir)

    def contents(self) -> tuple:
        try:
            parse_text = linecache.getline(self.working_input_file,
                                           self.line_to_parse)
            parse_text = parse_text.rstrip("\n").rstrip(" ")
            regex = r"^((?!\}|\\).)*"
            matches = re.search(regex, parse_text[self.parse_index:])
            output_file_update.content_append(
                debug_dir=self.debug_dir,
                content_update=matches.group(0))
            end = matches.end()
            self.parse_index = self.parse_index + end
            return self.line_to_parse, self.parse_index
        except TypeError:
            # TODO Replace next line
            print("STRING DOES NOT MATCH", self.line_to_parse, self.parse_index)
            return self.line_to_parse, self.parse_index

    def destination(self) -> tuple:
        self.line_to_parse, self.parse_index = \
            process_body.control_word_manager.destination_processor(
                line_to_parse=self.line_to_parse,
                parse_index=self.parse_index,
                working_input_file=self.working_input_file,
                control_word_dict=self.control_word_dict,
                debug_dir=self.debug_dir)
        self.reset_line_to_parse, self.line_to_parse = \
            MainDocDirector.reset_parse_line(self=self.main_doc_dir)
        return self.line_to_parse, self.parse_index

    def group(self) -> tuple:
        group_id, group_info, reset_line_to_parse, self.parse_index = \
            process_body.group.group_processor(
                line_to_parse=self.line_to_parse,
                parse_index=self.parse_index,
                working_input_file=self.working_input_file,
                shift_text=self.shift_text)

        contents_group_parse.contents_group_processor(
            debug_dir=self.debug_dir,
            group_id=group_id, group_info=group_info,
            control_word_dict=self.control_word_dict)
        return reset_line_to_parse, self.parse_index

    def reset_parse_line(self) -> tuple:
        if self.parse_index >= self.length_parse_text:
            self.reset_line_to_parse = self.line_to_parse + 1
            self.parse_index = 0
        else:
            pass
        return self.reset_line_to_parse, self.line_to_parse