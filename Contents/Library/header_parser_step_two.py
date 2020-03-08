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
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

"""

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.header_parser_step_two"

# From standard libraries
import json
import linecache
import os

# From local application
import split_between_characters
import table_boundaries


class HeaderParseTableController(object):

    def __init__(self, working_input_file: str, debug_dir: str) -> None:
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.header_tables_json_dict = os.path.join(
            self.debug_dir, "header_tables_dict.json")
        self.table_list_file = os.path.join(self.debug_dir,
                                            "table_list_file.json")
        self.full_tables_boundaries_list = []
        HeaderParseTableController.process_the_tables(self)

    def process_the_tables(self):
        with open(self.header_tables_json_dict) as header_tables_dict_pre:
            header_tables_dict = json.load(header_tables_dict_pre)

        header_tables_list = ["fonttbl", "filetbl", "colortbl",
                              "stylesheet", "listtables", "revtbl",
                              "rsidtable", "generator", "info"]

        for table in header_tables_list:

            table, table_start_line, table_empty = \
                HeaderParseTableController.check_for_empty_table(
                    self=HeaderParseTableController(
                        working_input_file=self.working_input_file,
                        debug_dir=self.debug_dir),
                    header_tables_dict=header_tables_dict,
                    table=table)

            table_updater = \
                HeaderParseTableController.table_emptyorfull_file_update(
                    self=HeaderParseTableController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file),
                    table=table, table_start_line=table_start_line,
                    table_empty=table_empty)

            if table_updater[table][1] is not True:

                table_boundaries_file_updater = \
                    HeaderParseTableController.find_table_boundaries(
                        self=HeaderParseTableController(
                            debug_dir=self.debug_dir,
                            working_input_file=self.working_input_file),
                        table=table, table_updater=table_updater)

                HeaderParseTableController.table_boundaries_file_update(
                    self=HeaderParseTableController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file),
                    table_boundaries_file_updater=table_boundaries_file_updater)

                HeaderParseTableController.create_empty_code_strings_dict(
                    self=HeaderParseTableController(
                        working_input_file=self.working_input_file,
                        debug_dir=self.debug_dir))

                text_to_process = HeaderParseTableController\
                    .get_table_contents_as_text_string(
                        self=HeaderParseTableController(
                            working_input_file=self.working_input_file,
                            debug_dir=self.debug_dir),
                        table_boundaries_file_updater=
                        table_boundaries_file_updater,
                        table=table)

                code_strings_list = HeaderParseTableController \
                    .get_code_strings_from_text(text_to_process=text_to_process)

                HeaderParseTableController \
                    .code_strings_file_update(
                        self=HeaderParseTableController(
                            working_input_file=self.working_input_file,
                            debug_dir=self.debug_dir),
                        table=table, code_strings_list=code_strings_list)

            else:
                pass

    def check_for_empty_table(self, table: str, header_tables_dict: dict
                              ) -> tuple:

        table_start_line = header_tables_dict[table]

        line_to_search = linecache.getline(self.working_input_file,
                                           table_start_line)

        table_start_line_index = line_to_search.index(table) + len(table)

        if line_to_search[table_start_line_index + 1] == "}" or \
                (line_to_search[table_start_line_index + 1] == " "
                 and line_to_search[table_start_line_index + 2] == "}"):
            table_empty = True
        else:
            table_empty = False

        return table, table_start_line, table_empty

    def table_emptyorfull_file_update(self, table: str, table_start_line: str,
                                      table_empty: bool):

        table_emptyorfull_file = os.path.join(
            self.debug_dir, "table_emptyorfull_dict.json")
        table_updater = {}

        table_updater.update({table: [table_start_line, table_empty]})

        with open(table_emptyorfull_file, "w+") as table_emptyorfull_file_pre:
            json.dump(table_updater, table_emptyorfull_file_pre)

        return table_updater

    def find_table_boundaries(self, table: str, table_updater):

        table_start_line = table_updater[table][0]

        table_start_line, table_first_brace, table_last_line, \
            table_last_brace = \
            table_boundaries.find_table_start_end(
                working_input_file=self.working_input_file,
                table_start_line=table_start_line, table=table)

        table_boundaries_file_updater = {table:
                                         [table_start_line,
                                          table_first_brace,
                                          table_last_line,
                                          table_last_brace]}

        return table_boundaries_file_updater

    def table_boundaries_file_update(self, table_boundaries_file_updater):

        table_boundaries_file = os.path.join(self.debug_dir,
                                             "table_boundaries.json")
        with open(table_boundaries_file, "w") as table_pre:
            json.dump(table_boundaries_file_updater, table_pre)

    def create_empty_code_strings_dict(self):

        with open(os.path.join(self.debug_dir,
                               "code_strings_file.json"),
                  "w+") as code_strings_file_empty:
            json.dump(code_strings_file_empty, "{}")

    def get_table_contents_as_text_string(
            self, table: str, table_boundaries_file_updater: dict):

        table_start_line = table_boundaries_file_updater[table][0]
        table_last_line = table_boundaries_file_updater[table][2]

        string_to_slice = ""
        controlword_line = table_start_line
        while controlword_line < table_last_line + 1:
            string_to_slice = string_to_slice + \
                              linecache.getline(self.working_input_file,
                                                controlword_line)
            controlword_line += 1

        string_to_slice = string_to_slice.replace("\n", "")
        sts_length = len(string_to_slice)
        pattern1 = "{\\" + f"{table}"
        pattern1_index = string_to_slice.find(pattern1)
        text_to_process = string_to_slice[pattern1_index:sts_length]
        text_to_process = text_to_process.replace(pattern1, "")
        pattern2 = r"[}]{2}"
        pattern2_index = text_to_process.find(pattern2)
        text_to_process = text_to_process[:pattern2_index]

        return text_to_process

    @staticmethod
    def get_code_strings_from_text(text_to_process: str):

        code_strings_list = split_between_characters.split_between(
            text_to_process=text_to_process, split_characters="}{")

        return code_strings_list

    def code_strings_file_update(self, table: str,
                                 code_strings_list: list):

        code_strings_file = os.path.join(self.debug_dir,
                                         "code_strings_file.json")

        code_strings_file_updater = {table: [code_strings_list]}

        with open(code_strings_file, "w") as code_strings_file_pre:
            json.dump(code_strings_file_updater, code_strings_file_pre)
