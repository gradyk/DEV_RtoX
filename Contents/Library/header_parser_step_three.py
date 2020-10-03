#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

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
import information_group
# import para_group_table
# import rsid_table
import style_sheet_table
# import track_changes_table
# import upi_group_table


class ProcessTheTables(object):

    def __init__(self, main_dict: dict) -> None:
        self.main_dict = main_dict
        self.debug_dir = main_dict["control_info"]["debug_dir"]
        self.working_input_file = main_dict["control_info"]["working_file_name"]

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
                    "generator": ProcessTheTables.process_generator,
                    "info": ProcessTheTables.process_info
                    }

                code_function = table_parser_function_list[table]

            else:
                pass

            code_function(self=ProcessTheTables(main_dict=self.main_dict),
                          code_strings_to_process=code_strings_to_process)

    def process_font_table(self, code_strings_to_process: list):
        """ Process the code settings for each font number and store the
        settings in a dictionary. """
        font_table.FonttblParse.trim_fonttbl(
            self=font_table.FonttblParse(
                code_strings_to_process=code_strings_to_process,
                debug_dir=self.debug_dir))
        font_table.FonttblParse.remove_code_strings(
            self=font_table.FonttblParse(
                code_strings_to_process=code_strings_to_process,
                debug_dir=self.debug_dir))
        font_table.FonttblParse.parse_code_strings(
            self=font_table.FonttblParse(
                debug_dir=self.debug_dir,
                code_strings_to_process=code_strings_to_process))

    @staticmethod
    def process_file_table(code_strings_to_process: list):
        """ Process the code settings for each file number and store the
        settings in a dictionary. """
        file_table.FiletblParse(code_strings_to_process=code_strings_to_process)

    def process_color_table(self, code_strings_to_process: list):
        """ Process the code settings for each color number and store the
        settings in a dictionary. """
        color_table.ColortblParse.trim_colortbl(
            self=color_table.ColortblParse(
                code_strings_to_process=code_strings_to_process,
                main_dict=self.main_dict))
        code_strings_list = color_table.ColortblParse\
            .parse_code_strings_to_process(
                self=color_table.ColortblParse(
                    code_strings_to_process=code_strings_to_process,
                    main_dict=self.main_dict))
        color_table.ColortblParse.parse_code_strings(
            self=color_table.ColortblParse(
                code_strings_to_process=code_strings_to_process,
                main_dict=self.main_dict), code_string_list=code_strings_list)

    def process_style_sheet_table(self, code_strings_to_process: list):
        """ Process the code settings for each style number and store the
        settings in a dictionary. """
        code_strings_to_process = \
            style_sheet_table.StyleSheetParse.trim_stylesheet(
                self=style_sheet_table.StyleSheetParse(
                    code_strings_to_process=code_strings_to_process,
                    main_dict=self.main_dict))
        code_strings_to_process = \
            style_sheet_table.StyleSheetParse.update_code_strings(
                self=style_sheet_table.StyleSheetParse(
                    code_strings_to_process=code_strings_to_process,
                    main_dict=self.main_dict))
        style_sheet_table.StyleSheetParse.parse_code_strings(
            self=style_sheet_table.StyleSheetParse(
                code_strings_to_process=code_strings_to_process,
                main_dict=self.main_dict))

        # TODO sf_restrictions (style and formatting restrictions) is part of
        #  style sheet table

    # TODO Build modules for these tables.
    def process_list_table(self, code_strings_to_process: list):
        # \listtable
        pass

    def process_para_group_properties_table(self,
                                            code_strings_to_process: list):
        # \pgptbl
        pass

    def process_track_changes_table(self, code_strings_to_process: list):
        # \*\revtbl
        pass

    def process_rsid_table(self, code_strings_to_process: list):
        # \*\rsidtbl
        pass

    def process_upi_group(self, code_strings_to_process: list):
        # \*\protusertbl (user protection information group)
        pass

    def process_generator(self, code_strings_to_process: list):
        # \*\generator (emitter application stamps the doc with its name,
        # version and build number
        pass

    def process_info(self, code_strings_to_process: list):
        information_group.InfoGrpParse.process_code_strings(
            self=information_group.InfoGrpParse(
                main_dict=self.main_dict,
                code_strings_to_process=code_strings_to_process))
