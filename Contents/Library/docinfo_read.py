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
Each RTF file, after the header section, may have an "info" section that
captures metadata about the document. This module controls the processing of
the "info" section.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-29"
__name__ = "Contents.Library.docinfo_read"

# From standard libraries
import json
import os
import re

# From local applications
import header_parser_step_two
import split_between_characters


class InfoParseController(object):

    def __init__(self,
                 working_input_file: str,
                 debug_dir: str,
                 table_start_line: int,
                 table_start_index: int,
                 table: str):
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.table_start_line = table_start_line
        self.table_start_index = table_start_index
        self.table = table

    def process_info_section(self) -> None:

        info_parse_controller = InfoParseController(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir,
            table_start_line=self.table_start_line,
            table_start_index=self.table_start_index,
            table=self.table)

        header_tables_file = os.path.join(self.debug_dir,
                                          "header_tables_dict.json")

        with open(header_tables_file) as header_tables_dict:
            header_tables = json.load(header_tables_dict)
        info_table_boundaries = header_tables["info"]

        text_to_process = InfoParseController.get_info_section_contents(
            self=info_parse_controller,
            info_table_boundaries=info_table_boundaries,
            working_input_file=self.working_input_file)

        info_code_strings_list = InfoParseController.get_info_strings_from_text(
            text_to_process=text_to_process)

        InfoParseController.info_code_strings_file_update(
            self=info_parse_controller,
            info_code_strings_list=info_code_strings_list)

    def get_info_section_contents(self, info_table_boundaries: dict,
                                  working_input_file: str) -> str:
        """ Extract the contents of the info table. """
        text_to_process = header_parser_step_two.\
            get_table_contents_as_text_string(
                table=self.table,
                table_boundaries=info_table_boundaries,
                working_input_file=working_input_file)

        return text_to_process

    @staticmethod
    def get_info_strings_from_text(text_to_process: str) -> list:
        """ Break the info table contents into separate code strings. """
        info_code_strings_list = split_between_characters.split_between(
            text_to_process=text_to_process,
            split_characters="}{")

        return info_code_strings_list

    def info_code_strings_file_update(self, info_code_strings_list: list) \
            -> None:
        """ Store the info table code strings in a file. """
        info_code_strings_file = os.path.join(self.debug_dir,
                                              "info_code_strings_file.json")

        info_code_strings_file_updater = {self.table: [info_code_strings_list]}

        with open(info_code_strings_file, "w") as info_code_strings_file_pre:
            json.dump(info_code_strings_file_updater,
                      info_code_strings_file_pre)


class ProcessTheInfoCodes(object):

    def __init__(self, debug_dir: str) -> None:
        self.debug_dir = debug_dir

        with open(os.path.join(
                self.debug_dir, "info_code_strings_file.json"), "r") as \
                info_codes_file_pre:
            self.info_codes_file = json.load(info_codes_file_pre)

        self.info_code_string = self.extract_info_code_string()
        self.parse_info_code_string()

    def extract_info_code_string(self) -> str:
        """ Pull the info code strings out of the file one at a time. """
        for info_code in self.info_codes_file:
            info_code_string = self.info_codes_file[info_code]

            return info_code_string

    def parse_info_code_string(self):
        """ Parse each code string. """
        info_part_list = [
                "title",
                "subject",
                "author",
                "manager",
                "company",
                "operator",
                "category",
                "comment",
                "doccomm",
                "hlinkbase",
                "version",
                "edmins",
                "nofpages",
                "nofwords",
                "nofchars",
                "nofcharsws",
                "vern",
                "keywords"
            ]

        for info_part in info_part_list:

            info_part_contents = GetPartContents.extract_info_part_contents(
                self=GetPartContents(info_code_string=self.info_code_string),
                info_part=info_part)

            info_part_updater = {info_part: info_part_contents}

            ProcessTheInfoCodes.update_info_file(
                self=ProcessTheInfoCodes(debug_dir=self.debug_dir),
                info_part_updater=info_part_updater)

    def parse_time_components(self):

        time_part_list = [
            "creatim",
            "revtim",
            "printim",
            "buptim"
        ]

        for time_part in time_part_list:
            info_part_updater = {}
            try:
                test = re.search(time_part, self.info_code_string)
                if test is None:
                    info_part_updater = {time_part: {"yr":  0, "mo": 0, "dy": 0,
                                                     "hr":  0, "min": 0,
                                                     "sec": 0}}
                else:
                    time_string = test[0].replace("{\\"+time_part,
                                                  "").replace("}", "")
                    time_string_list = time_string.split("\\")
                    for time_item in time_string_list:
                        info_part_updater = GetPartContents.\
                            extract_time_part_contents(time_item=time_item)
            except TypeError:
                info_part_updater = {time_part: {"yr": 0, "mo": 0, "dy": 0,
                                                 "hr": 0, "min": 0, "sec": 0}}

            ProcessTheInfoCodes.update_info_file(
                self=ProcessTheInfoCodes(debug_dir=self.debug_dir),
                info_part_updater=info_part_updater)

    def update_info_file(self, info_part_updater: dict) -> None:

        with open(os.path.join(self.debug_dir, "info_codes_file.json"), "w+") \
                as info_codes_file_pre:
            json.dump(info_part_updater, info_codes_file_pre)


class GetPartContents(object):

    def __init__(self, info_code_string: str) -> None:
        self.info_code_string = info_code_string

    def extract_info_part_contents(self, info_part) -> str:
        """ For each part in the info table, extract the contents. """
        try:
            test = re.search(info_part, self.info_code_string)
            if test is None:
                result = "None"
                return result
            else:
                pattern = r'\s(\w+|\s|\W)+'
                info_text = re.search(pattern, self.info_code_string)
                if info_text:
                    pre_result = info_text[0].rstrip()
                    result = pre_result[:-1]
                    return result
                else:
                    result = "None"
                    return result
        except TypeError:
            result = "None"
            return result

    @staticmethod
    def extract_time_part_contents(time_item) -> dict:
        """ For each time part in the info table, extract the contents. """
        info_part_updater = {}
        time_data_list = ["yr", "mo", "dy", "hr", "min", "sec"]

        for item in time_data_list:

            if re.search(r"\\"+item, time_item) is None:
                item_value = 0
            else:
                item_value = time_item.replace('\\'+item, "")

            info_part_updater = info_part_updater.update({item: item_value})

        return info_part_updater
