#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.header_parser_step_two"

# From standard libraries
import json
import os

# From local application
import color_table
import file_table
import font_table
# import generator
import information_group
import pgp_table
import rsid_table
import style_sheet_table
# import track_changes_table
# import upi_group_table
import xml_namespace_table


class ProcessTheTables(object):

    def __init__(self, main_dict: dict) -> None:
        self.main_dict = main_dict
        self.debug_dir = main_dict["debug_dir"]
        self.working_input_file = main_dict["working_file_name"]

    def analyze_table_code_strings_controller(self):
        code_strings_file = os.path.join(self.debug_dir,
                                         "code_strings_file.json")
        header_tables_file = os.path.join(self.debug_dir,
                                          "header_tables_dict.json")
        with open(code_strings_file, "r") as code_strings_file_pre:
            code_strings = json.load(code_strings_file_pre)

        with open(header_tables_file, "r") as header_tables_dict_pre:
            header_tables_dict = json.load(header_tables_dict_pre)

        for table in header_tables_dict:
            code_strings_to_process = code_strings[table][0]
            # Note: All RTF tables using table in the control word abbreviate
            # it "tbl" with the exception of "listable" which does not
            # abbreviate table.
            table_parser_function_list = {
                "colortbl": ProcessTheTables.process_color_table,
                "filetbl": ProcessTheTables.process_file_table,
                "fonttbl": ProcessTheTables.process_font_table,
                "generator": ProcessTheTables.process_generator,
                "info": ProcessTheTables.process_info,
                "listtable": ProcessTheTables.process_list_table,
                "pgptbl":
                    ProcessTheTables.process_pgp_table,
                "rsidtbl": ProcessTheTables.process_rsid_table,
                "stylesheet": ProcessTheTables.process_style_sheet_table,
                "track_changes":
                    ProcessTheTables.process_track_changes_table,
                "upi_group": ProcessTheTables.process_upi_group,
                "xmlnstbl": ProcessTheTables.process_xmlns,
                }

            code_function = table_parser_function_list[table]

            code_function(self=ProcessTheTables(main_dict=self.main_dict),
                          code_strings_to_process=code_strings_to_process)

    def process_font_table(self, code_strings_to_process: list):
        """ Process the code settings for each font number and store the
        settings in a dictionary. """
        font_table.FonttblParse.trim_fonttbl(
            self=font_table.FonttblParse(
                code_strings_to_process=code_strings_to_process,
                main_dict=self.main_dict))
        font_table.FonttblParse.remove_code_strings(
            self=font_table.FonttblParse(
                code_strings_to_process=code_strings_to_process,
                main_dict=self.main_dict))
        font_table.FonttblParse.parse_code_strings(
            self=font_table.FonttblParse(
                main_dict=self.main_dict,
                code_strings_to_process=code_strings_to_process))

    @staticmethod
    def process_file_table(code_strings_to_process: list):
        """ Process the code settings for each file number and store the
        settings in a dictionary. """
        file_table.FiletblParse(code_strings_to_process=code_strings_to_process)

    def process_color_table(self, code_strings_to_process: list):
        """ Process the code settings for each color number and store the
        settings in a dictionary. """
        code_strings_list = color_table.trim_colortbl(
            code_strings=code_strings_to_process)
        code_strings_list = color_table.split_code_strings(
            code_strings_list=code_strings_list)
        color_table.parse_code_strings(
            code_strings_list=code_strings_list, main_dict=self.main_dict)

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

    # TODO Build modules for table functions still missing modules.
    def process_list_table(self, code_strings_to_process: list):
        # \listtable
        pass

    def process_pgp_table(self, code_strings_to_process: list):
        code_strings_to_process = pgp_table.trim_pgptbl(
            code_strings_to_process=code_strings_to_process)
        pgp_table.parse_pgp_string(
            main_dict=self.main_dict,
            code_strings_to_process=code_strings_to_process)

    def process_track_changes_table(self, code_strings_to_process: list):
        # \*\revtbl
        pass

    def process_rsid_table(self, code_strings_to_process: list):
        new_code_string = rsid_table.trim_rsidtbl(
            code_strings_to_process=code_strings_to_process)
        rsid_table.parse_rsid_string(
            main_dict=self.main_dict,
            code_string=new_code_string)

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

    def process_xmlns(self, code_strings_to_process: list):
        xml_namespace_table.trim_xmlnstbl(
            code_strings_to_process=code_strings_to_process)
        xml_namespace_table.parse_namespace(
            main_dict=self.main_dict,
            code_strings_to_process=code_strings_to_process)
