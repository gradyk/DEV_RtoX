#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
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

import json
import os

import input_file_prep
import rtf_codes_file_prep
from opening_tag_registry_dict import opening_tag_registry_dict


def initiate_working_files(xml_tag_num: str, debug_dir: str,
                           input_file_name: str, base_script_dir: str) -> str:

    create_working_tag_registry(debug_dir=debug_dir)

    create_header_table_dict(debug_dir=debug_dir)

    create_rtf_file_codes_file(debug_dir=debug_dir)

    create_empty_code_strings_dict(debug_dir=debug_dir)

    create_empty_info_code_strings_file(debug_dir=debug_dir)

    create_font_file(debug_dir=debug_dir)

    create_style_file(debug_dir=debug_dir)

    create_working_xml_file(xml_tag_num=xml_tag_num, debug_dir=debug_dir)

    working_input_file_pass = create_working_input_file(
        debug_dir=debug_dir, input_file_name=input_file_name,
        base_script_dir=base_script_dir)

    return working_input_file_pass


def create_working_tag_registry(debug_dir: str) -> None:
    """ Dictionary for tracking open and closed XML tags. """
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file, "w", encoding='utf-8') as \
            tag_registry:
        json.dump(opening_tag_registry_dict, tag_registry)


def create_header_table_dict(debug_dir: str) -> None:
    """ Dictionary for storing which tables are in the RTF file header
        and the line number on which each table starts. """
    header_tables_dict = os.path.join(debug_dir,
                                      "header_tables_dict.json")
    with open(header_tables_dict, "w+", encoding="utf-8") as \
            header_tables:
        json.dump({}, header_tables)


def create_rtf_file_codes_file(debug_dir: str) -> None:
    """  """
    rtf_file_codes = os.path.join(debug_dir, "rtf_file_codes.json")
    with open(rtf_file_codes, "w+") as rtf_file_codes_prep:
        json.dump([], rtf_file_codes_prep)


def create_empty_info_code_strings_file(debug_dir: str) -> None:
    """ File to hold code strings from the info table. """
    info_code_strings = os.path.join(debug_dir, "info_code_strings_file.json")
    with open(info_code_strings, "w+") as info_code_strings_file_empty:
        json.dump({}, info_code_strings_file_empty)


def create_empty_code_strings_dict(debug_dir: str) -> None:
    """ File to hold code strings from a table. """
    code_strings_file = os.path.join(debug_dir, "code_strings_file.json")
    with open(code_strings_file, "w+") as code_strings_file_empty:
        json.dump({}, code_strings_file_empty)


def create_font_file(debug_dir: str) -> None:
    """ File to hold code strings from the font table. """
    font_file = os.path.join(debug_dir, "font_file.json")
    with open(font_file, "w+") as font_file_pre:
        json.dump([], font_file_pre)


def create_style_file(debug_dir: str) -> None:
    """ File to hold code strings from the style table. """
    style_file = os.path.join(debug_dir, "style_file.json")
    with open(style_file, "w+") as style_file_pre:
        json.dump([], style_file_pre)


def create_working_xml_file(xml_tag_num: str, debug_dir: str) -> None:
    """ XML file to hold tags during processing. """
    rtf_codes_file_prep.RTFCodesPrep.rtf_codes_to_xml_prep(
        self=rtf_codes_file_prep.RTFCodesPrep(
            debug_dir=debug_dir, xml_tag_num=xml_tag_num))


def create_working_input_file(input_file_name: str, debug_dir: str,
                              base_script_dir: str) -> str:
    """ Copy of the input file for use during processing. """
    working_input_file = input_file_prep.InputPrep.input_file_prep(
        input_file_prep.InputPrep(input_file_name=input_file_name,
                                  debug_dir=debug_dir,
                                  base_script_dir=base_script_dir))

    return working_input_file
