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
import linecache
import os
import sys

# From local application
import file_stats
from process_body import check_parse_text


class MainDocManager(object):
    def __init__(self,
                 working_input_file: str,
                 debug_dir: str,
                 control_word_dict: str) -> None:
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.control_word_dict = control_word_dict
        self.length_parse_text = 0
        self.header_table_file = os.path.join(
            self.debug_dir, "header_tables_dict.json")

    def body_parse_manager(self) -> None:
        main_doc_dir = MainDocManager(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir,
            control_word_dict=self.control_word_dict)

        MainDocManager.load_tag_registry(self=main_doc_dir)
        parse_text, line_to_parse, parse_index = \
            MainDocManager.parse_starting_point(self=main_doc_dir)

        num_lines = file_stats.processor(
            working_input_file=self.working_input_file)

        group_data_file = os.path.join(self.debug_dir, "group_data_file.json")
        with open(group_data_file, "r+") as gdf_pre:
            group_data = json.load(gdf_pre)
            group_start = {"id":       "root",
                           "type":     "group",
                           "children": []}
            group_data.update(group_start)
            gdf_pre.seek(0)
            json.dump(group_data, gdf_pre)

        check_parse_text.check_string_manager(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir,
            control_word_dict=self.control_word_dict,
            parse_text=parse_text,
            line_to_parse=line_to_parse,
            parse_index=parse_index,
            num_lines=num_lines,
            group_dict=group_data)

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
            line_to_parse = header_table["info"][2]
            parse_index = header_table["info"][3]
        parse_text, line_to_parse, parse_index = \
            MainDocManager.set_process_text(
                self=MainDocManager(
                    working_input_file=self.working_input_file,
                    debug_dir=self.debug_dir,
                    control_word_dict=self.control_word_dict),
                parse_index=parse_index,
                line_to_parse=line_to_parse)
        return parse_text, line_to_parse, parse_index

    def set_process_text(self, parse_index: int, line_to_parse: int) -> tuple:
        line = linecache.getline(self.working_input_file, line_to_parse).rstrip(
            "\n")
        line = line[parse_index:]
        length = len(line)
        if parse_index > length - 2:
            parse_text = line[parse_index:] + \
                         linecache.getline(self.working_input_file,
                                           line_to_parse + 1).rstrip("\n")
            line_to_parse += 1
            parse_index = 0
            return parse_text, line_to_parse, parse_index
        else:
            parse_text = line
            parse_index = 0
            return parse_text, line_to_parse, parse_index
            pass

    def closer(self):
        pass

    def blank_space(self):
        pass
