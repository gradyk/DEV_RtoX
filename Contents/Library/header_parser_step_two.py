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

"""  """

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


def process_the_tables(debug_dir: str, working_input_file: str):

    header_tables_dict = os.path.join(debug_dir, "header_tables_dict.json")

    with open(header_tables_dict) as header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)

    for header_table in header_tables_dict:

        table, table_start_line, table_empty = check_for_empty_table(
                header_tables_dict=header_tables_dict,
                table=header_table, working_input_file=working_input_file)

        table_updater = table_emptyorfull_file_update(
                table=table, table_start_line=table_start_line,
                table_empty=table_empty, debug_dir=debug_dir)

        if table_updater[table][1] is not True:

            table_boundaries_file_updater = find_table_boundaries(
                    table=table, table_updater=table_updater,
                    working_input_file=working_input_file)

            table_boundaries_file_update(
                table_boundaries_file_updater=table_boundaries_file_updater,
                debug_dir=debug_dir)

            text_to_process = get_table_contents_as_text_string(
                working_input_file=working_input_file,
                table_boundaries_file_updater=table_boundaries_file_updater,
                table=table)

            code_strings_list = get_code_strings_from_text(
                text_to_process=text_to_process)

            code_strings_file_update(
                table=table, code_strings_list=code_strings_list,
                debug_dir=debug_dir)

        else:
            pass


def check_for_empty_table(table: str, header_tables_dict: dict,
                          working_input_file: str) -> tuple:

    table_start_line = header_tables_dict[table]

    line_to_search = linecache.getline(working_input_file, table_start_line)

    table_start_line_index = line_to_search.index(table) + len(table)

    if line_to_search[table_start_line_index + 1] == "}" or \
            (line_to_search[table_start_line_index + 1] == " "
             and line_to_search[table_start_line_index + 2] == "}"):
        table_empty = True
    else:
        table_empty = False

    return table, table_start_line, table_empty


def table_emptyorfull_file_update(table: str, table_start_line: str,
                                  table_empty: bool, debug_dir: str,):

    table_emptyorfull_file = os.path.join(
        debug_dir, "table_emptyorfull_dict.json")
    table_updater = {}

    table_updater.update({table: [table_start_line, table_empty]})

    with open(table_emptyorfull_file, "w+") as table_emptyorfull_file_pre:
        json.dump(table_updater, table_emptyorfull_file_pre)

    return table_updater


def find_table_boundaries(table: str, table_updater: dict,
                          working_input_file: str):

    table_start_line = table_updater[table][0]

    table_start_line, table_first_brace, table_last_line, \
        table_last_brace = \
        table_boundaries.find_table_start_end(
            working_input_file=working_input_file,
            table_start_line=table_start_line, table=table)

    table_boundaries_file_updater = {table:
                                     [table_start_line,
                                      table_first_brace,
                                      table_last_line,
                                      table_last_brace]}

    return table_boundaries_file_updater


def table_boundaries_file_update(table_boundaries_file_updater: dict,
                                 debug_dir: str):

    table_boundaries_file = os.path.join(debug_dir,
                                         "table_boundaries.json")
    with open(table_boundaries_file, "w") as table_pre:
        json.dump(table_boundaries_file_updater, table_pre)


def get_table_contents_as_text_string(
        table: str, table_boundaries_file_updater: dict,
        working_input_file: str):

    table_start_line = table_boundaries_file_updater[table][0]
    table_last_line = table_boundaries_file_updater[table][2]

    string_to_slice = ""
    controlword_line = table_start_line
    while controlword_line < table_last_line + 1:
        string_to_slice = string_to_slice + \
                          linecache.getline(working_input_file,
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


def get_code_strings_from_text(text_to_process: str):

    code_strings_list = split_between_characters.split_between(
        text_to_process=text_to_process, split_characters="}{")

    return code_strings_list


def code_strings_file_update(table: str, debug_dir: str,
                             code_strings_list: list):

    code_strings_file = os.path.join(debug_dir,
                                     "code_strings_file.json")

    code_strings_file_updater = {table: [code_strings_list]}

    with open(code_strings_file, "w") as code_strings_file_pre:
        json.dump(code_strings_file_updater, code_strings_file_pre)
