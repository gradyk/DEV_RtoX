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

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2030-03-19"
__name__ = "Contents.Library.create_files"

import os
import json

# From application library
import Contents.Library.input_file_prep
import rtf_codes_file_prep


def initiate_working_files(xml_tag_num: str, debug_dir: str,
                           input_file_name: str, base_script_dir: str) -> str:

    create_working_xml_file(xml_tag_num=xml_tag_num, debug_dir=debug_dir)

    create_dict_files(base_script_dir=base_script_dir)

    working_input_file = create_working_input_file(
        debug_dir=debug_dir, input_file_name=input_file_name,
        base_script_dir=base_script_dir)
    return working_input_file


def create_working_xml_file(xml_tag_num: str, debug_dir: str) -> None:
    """ XML file to hold tags during processing. """
    rtf_codes_file_prep.RTFCodesPrep.rtf_codes_to_xml_prep(
        self=rtf_codes_file_prep.RTFCodesPrep(
            debug_dir=debug_dir, xml_tag_num=xml_tag_num))


def create_dict_files(base_script_dir: str) -> None:
    dict_library = (
        "header_tables_dict.json",
        "rtf_file_codes.json",
        "code_strings_file.json",
        "table_emptyorfull_dict.json",
        "font_table_file.json",
        "color_table_file.json",
        "style_sheet_table_file.json",
        "control_word_info_dict.json",
        "control_word_func_dict.json"
    )

    for file in dict_library:
        dict_dir = os.path.join(base_script_dir, "debugdir")
        dict_path = os.path.join(dict_dir, file)
        with open(dict_path, "w+") as open_dict:
            json.dump({}, open_dict)


def create_working_input_file(input_file_name: str, debug_dir: str,
                              base_script_dir: str) -> str:
    """ Copy of the input file for use during processing. """
    working_input_file = Contents.Library.input_file_prep.input_file_prep(
        input_file_name=input_file_name,
        debug_dir=debug_dir,
        base_script_dir=base_script_dir)
    return working_input_file
