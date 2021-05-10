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
import dict_updater
import header_structure
import split_between_characters


def process_the_tables(main_dict: dict) -> None:
    header_structure.build_header_tables_dict(main_dict=main_dict)

    header_tables_file = os.path.join(main_dict["debug_dir"],
                                      "header_tables_dict.json")

    with open(header_tables_file) as header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)
        for header_table in header_tables_dict:
            table_boundaries = header_tables_dict[header_table]
            text_to_process = get_table_contents_as_text_string(
                working_input_file=main_dict["working_input_file"],
                table_boundaries=table_boundaries)
            code_strings_list = split_between_characters.split_between(
                text_to_process=text_to_process, split_characters="}{")
            code_strings_file_update(
                main_dict=main_dict, code_strings_list=code_strings_list,
                header_table=header_table)


def get_table_contents_as_text_string(table_boundaries: dict,
                                      working_input_file: list):
    # PROBLEM: This doesn't work when everything in the group is on the same
    # line. Need a solution for 1) everything on the same line, and 2)
    # everything on 2 or more lines.
    table_start_line = table_boundaries[0]
    table_last_line = table_boundaries[2]
    controlword_line = table_start_line
    initial_string = working_input_file[controlword_line]
    string_to_slice = initial_string[table_boundaries[1]:]
    if table_start_line == table_last_line:
        text_to_process = working_input_file[controlword_line][
            table_boundaries[1]:table_boundaries[3]]
    else:
        controlword_line += 1
        while controlword_line < table_last_line:
            string_list = \
                [string_to_slice, working_input_file[controlword_line]]
            string_to_slice = ''.join(string_list)
            controlword_line += 1
        last_string = working_input_file[controlword_line]
        last_string = last_string[:table_boundaries[3]]
        text_list = [string_to_slice, last_string]
        text_to_process = ''.join(text_list)
    return text_to_process


def code_strings_file_update(header_table: str, main_dict: dict,
                             code_strings_list: list):
    code_strings_file_updater = {header_table: [code_strings_list]}
    dict_updater.json_dict_updater(
        dict_name="code_strings_file.json", main_dict=main_dict,
        dict_update=code_strings_file_updater)
