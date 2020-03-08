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
#   RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
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
__name__ = "Contents.Library.header_parser_step_three"

# From standard libraries
import json
import os

# From local application
import color_table
import file_table
import font_table
# import para_group_table
# import rsid_table
# import sf_restrictions_table
import style_sheet_table
# import track_changes_table
# import upi_group_table


class ProcessTheTables(object):

    def __init__(self, debug_dir: str, working_input_file: str) -> None:
        self.debug_dir = debug_dir
        self.working_input_file = working_input_file
        self.ProcessTheTables = ProcessTheTables(
            debug_dir=debug_dir, working_input_file=working_input_file)

        ProcessTheTables.analyze_table_code_strings_controller(self)

    def analyze_table_code_strings_controller(self):

        code_strings_file = os.path.join(self.debug_dir,
                                         "code_strings_file.json")
        with open(code_strings_file, "r") as code_strings_file_pre:
            code_strings = json.load(code_strings_file_pre)

        table_info_file = os.path.join(self.debug_dir,
                                       "table_emptyorfull_dict.json")
        with open(table_info_file, "r") as table_info_file_pre:
            table_info = json.load(table_info_file_pre)

        code_function = ""
        code_strings_to_process = ""

        for table in table_info:
            if table_info[table][1] is not True:
                code_strings_to_process = code_strings[table][0]

                table_parser_function_list = {
                    "fonttbl": ProcessTheTables.font_table_parser,
                    "filetbl": ProcessTheTables.file_table_parser,
                    "colortbl": ProcessTheTables.color_table_parser,
                    "stylesheet": ProcessTheTables.style_sheet_table_parser,
                    "rsid": ProcessTheTables.process_rsid_table,
                    "sf_restrictions":
                        ProcessTheTables.process_sf_restrictions_table,
                    "track_changes":
                        ProcessTheTables.process_track_changes_table,
                    "upi_group": ProcessTheTables.process_upi_group,
                    "para_groups": ProcessTheTables.process_para_group_table}

                code_function = table_parser_function_list[table]

            else:
                pass

            code_function(self=self.ProcessTheTables,
                          code_strings_to_process=code_strings_to_process)

    def font_table_parser(self, code_strings_to_process: list):
        """ Process the code settings for each font number and store the
        settings in a dictionary. """

        font_table.FonttblParse(debug_dir=self.debug_dir,
                                code_strings_to_process=code_strings_to_process)

    @staticmethod
    def file_table_parser(code_strings_to_process: list):
        """ Process the code settings for each file number and store the
        settings in a dictionary. """

        file_table.FiletblParse(code_strings_to_process=code_strings_to_process)

    @staticmethod
    def color_table_parser(code_strings_to_process: list):
        """ Process the code settings for each color number and store the
        settings in a dictionary. """

        color_table.ColortblParse(
            code_strings_to_process=code_strings_to_process)

    def style_sheet_table_parser(self, code_strings_to_process: list):
        """ Process the code settings for each style number and store the
        settings in a dictionary. """

        style_sheet_table.StyleSheetParse(
            code_strings_to_process=code_strings_to_process,
            debug_dir=self.debug_dir)

    # TODO Put these in the proper order and complete the modules.
    def process_rsid_table(self):
        pass

    def process_sf_restrictions_table(self):
        pass

    def process_track_changes_table(self):
        pass

    def process_upi_group(self):
        pass

    def process_para_group_table(self):
        pass
