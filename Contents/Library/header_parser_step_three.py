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

"""  """

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
# import generator
# import para_group_table
# import rsid_table
import style_sheet_table
# import track_changes_table
# import upi_group_table


class ProcessTheTables(object):

    def __init__(self, debug_dir: str, working_input_file: str) -> None:
        self.debug_dir = debug_dir
        self.working_input_file = working_input_file

        self.ProcessTheTables = ProcessTheTables(
            debug_dir=debug_dir, working_input_file=working_input_file)

        self.analyze_table_code_strings_controller()

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
                    "fonttbl": ProcessTheTables.process_font_table,
                    "filetbl": ProcessTheTables.process_file_table,
                    "colortbl": ProcessTheTables.process_color_table,
                    "stylesheet": ProcessTheTables.process_style_sheet_table,
                    "listtable": ProcessTheTables.process_list_table,
                    "para_group":
                        ProcessTheTables.process_para_group_properties_table,
                    "track_changes":
                        ProcessTheTables.process_track_changes_table,
                    "rsid": ProcessTheTables.process_rsid_table,
                    "upi_group": ProcessTheTables.process_upi_group,
                    "generator": ProcessTheTables.process_generator
                    }

                code_function = table_parser_function_list[table]

            else:
                pass

            code_function(self=self.ProcessTheTables,
                          code_strings_to_process=code_strings_to_process)

    def process_font_table(self, code_strings_to_process: list):
        """ Process the code settings for each font number and store the
        settings in a dictionary. """

        font_table.FonttblParse(debug_dir=self.debug_dir,
                                code_strings_to_process=code_strings_to_process)

    @staticmethod
    def process_file_table(code_strings_to_process: list):
        """ Process the code settings for each file number and store the
        settings in a dictionary. """

        file_table.FiletblParse(code_strings_to_process=code_strings_to_process)

    @staticmethod
    def process_color_table(code_strings_to_process: list):
        """ Process the code settings for each color number and store the
        settings in a dictionary. """

        color_table.ColortblParse(
            code_strings_to_process=code_strings_to_process)

    def process_style_sheet_table(self, code_strings_to_process: list):
        """ Process the code settings for each style number and store the
        settings in a dictionary. """

        style_sheet_table.StyleSheetParse(
            code_strings_to_process=code_strings_to_process,
            debug_dir=self.debug_dir)

        # TODO sf_restrictions (style and formatting restrictions) is part of
        #  style sheet table

    # TODO Build modules for these tables.
    def process_list_table(self):
        # \listtable
        pass

    def process_para_group_properties_table(self):
        # \pgptbl
        pass

    def process_track_changes_table(self):
        # \*\revtbl
        pass

    def process_rsid_table(self):
        # \*\rsidtbl
        pass

    def process_upi_group(self):
        # \*\protusertbl (user protection information group)
        pass

    def process_generator(self):
        # \*\generator (emitter application stamps the doc with its name,
        # version and build number
        pass