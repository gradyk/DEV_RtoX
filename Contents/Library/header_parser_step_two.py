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
        file = os.path.join(main_dict["dicts_dir"], "tables_dict.json")
        with open(file) as function_definitions:
            table_parser_function = json.load(function_definitions)
        code_function = table_parser_function[table]["function"]
        code_function(main_dict=main_dict,
                      code_strings_to_process=code_strings_to_process)
