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
import os
import sys

# From local application
import adjust_process_text
from process_body import check_parse_text


class MainDocManager(object):
    def __init__(self,
                 working_input_file: str,
                 debug_dir: str,
                 control_word_dict: str) -> None:
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.control_word_dict = control_word_dict
        self.parse_index = 0
        self.line_to_parse = 0
        self.parse_text = ""
        self.length_parse_text = 0
        self.header_table_file = os.path.join(
        self.debug_dir, "header_tables_dict.json")

    def body_parse_manager(self) -> None:
        main_doc_dir = MainDocManager(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir,
            control_word_dict=self.control_word_dict)

        MainDocManager.load_tag_registry(self=main_doc_dir)
        self.parse_text, self.line_to_parse, self.parse_index = \
            MainDocManager.parse_starting_point(self=main_doc_dir)

        check_parse_text.CheckString.check_string_manager(
            self=check_parse_text.CheckString(
                working_input_file=self.working_input_file,
                debug_dir=self.debug_dir,
                control_word_dict=self.control_word_dict,
                parse_text=self.parse_text,
                line_to_parse=self.line_to_parse,
                parse_index=self.parse_index))

    def load_tag_registry(self) -> None:
        base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        dicts_dir = os.path.join(base_script_dir, "Library/dicts")
        opening_registry_file = os.path.join(
            dicts_dir, "opening_tag_registry_dict.json")
        tag_registry_file = os.path.join(
            self.debug_dir, "tag_registry.json")
        with open(tag_registry_file, "w+") as trf:
            with open(opening_registry_file) as orf_pre:
                orf = json.load(orf_pre)
                tag_registry = orf.copy()
                json.dump(tag_registry, trf, indent=4)

    def parse_starting_point(self) -> tuple:
        with open(self.header_table_file) as htf_pre:
            header_table = json.load(htf_pre)
        self.line_to_parse = header_table["info"][2]
        self.parse_index = header_table["info"][3]
        self.parse_text, self.line_to_parse, self.parse_index = \
            adjust_process_text.text_metric_reset(
                working_input_file=self.working_input_file,
                parse_index=self.parse_index,
                line_to_parse=self.line_to_parse)
        return self.parse_text, self.line_to_parse, self.parse_index

    def closer(self):
        pass

    def blank_space(self):
        pass
