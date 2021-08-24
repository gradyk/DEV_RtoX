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
import process_color_table
import process_file_table
import process_font_table
import process_generator
import process_info
import process_list_table
import process_pgp_table
import process_rev_table
import process_rsid_table
import process_style_sheet_table
import process_track_changes_table
import process_upi_group
import process_xmlns


def analyze_table_code_strings_controller(main_dict: dict) -> None:
    code_strings_file = os.path.join(
        main_dict["debug_dir"], "code_strings_file.json")
    header_tables_file = os.path.join(
        main_dict["debug_dir"], "header_tables_dict.json")
    with open(code_strings_file, "r") as code_strings_file_pre:
        code_strings = json.load(code_strings_file_pre)
    with open(header_tables_file, "r") as header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)
    for table in header_tables_dict:
        code_strings_to_process = code_strings[table][0]
        convert = {
            "colortbl": process_color_table.processor,
            "filetbl": process_file_table.processor,
            "fonttbl": process_font_table.processor,
            "generator": process_generator.processor,
            "info": process_info.processor,
            "listtables": process_list_table.processor,
            "pgptbl": process_pgp_table.processor,
            "revtbl": process_rev_table.processor,
            "rsidtbl": process_rsid_table.processor,
            "stylesheet": process_style_sheet_table.processor,
            "track_changes": process_track_changes_table.processor,
            "upi_group": process_upi_group.processor,
            "xmlnstbl": process_xmlns.processor
        }
        function = convert[table]
        function(main_dict=main_dict,
                 code_strings_to_process=code_strings_to_process)
