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

""" The main body of an RTF document has four components assembled in a
variety of combinations: control symbols, destinations that can be ignored,
destinations that must be processed, and groups. This module acts as a
switchboard, sending the program to the correct module to process each
component. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.doc_parser"

# From standard libraries
import json
import linecache
import os
import re

# From local application
import Contents.Library.control_symbol
import Contents.Library.destination
import file_stats
import Contents.Library.group
import Contents.Library.group_boundaries_capture_contents
import Contents.Library.group_boundaries_no_contents
import Contents.Library.slash_star
import working_xml_file_update


def main_doc_parser(working_input_file: str, debug_dir: str,
                    control_word_func_dict: str):
    header_table_file = os.path.join(debug_dir, "header_tables_dict.json")
    with open(header_table_file, "r") as header_table_dict_pre:
        header_table_dict = json.load(header_table_dict_pre)

    line_to_parse = header_table_dict["info"][2]
    start_index = header_table_dict["info"][3]

    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)

    length_working_input_file = file_metrics[0]

    while line_to_parse < (length_working_input_file + 1):

        parse_text = linecache.getline(working_input_file, line_to_parse)
        length_parse_text = len(parse_text)
        parse_index = start_index

        while parse_index <= length_parse_text:
            # Ignore RTF controls that begin with {\*
            if parse_text[parse_index] == "{" and parse_text[
                    parse_index + 1] == "\\" and \
                    parse_text[parse_index + 2] == "*":

                line_to_parse, parse_index\
                    = Contents.Library.slash_star.slash_star_processor(
                        working_input_file=working_input_file,
                        parse_index=parse_index,
                        line_to_parse=line_to_parse)
                pass

            # Slash plus non-alphabetic character means control symbol.
            elif parse_text[parse_index] == "\\" and parse_text[
                    parse_index + 1].isalnum() is False:
                line_to_parse, parse_index = \
                    Contents.Library.control_symbol.control_symbol_processor(
                        working_input_file=working_input_file,
                        line_to_parse=line_to_parse,
                        parse_index=parse_index,
                        control_word_func_dict=control_word_func_dict)
                pass

            # Slash plus alphabetic character means destination.
            elif parse_text[parse_index] == "\\":
                line_to_parse, parse_index = \
                    Contents.Library.destination.destination_processor(
                        line_to_parse=line_to_parse,
                        parse_index=parse_index,
                        working_input_file=working_input_file,
                        control_word_func_dict=control_word_func_dict)
                pass

            # Left brace means beginning of a group.
            elif parse_text[parse_index] == "{":
                line_to_parse, parse_index = \
                    Contents.Library.group.group_processor(
                        line_to_parse=line_to_parse,
                        parse_index=parse_index,
                        working_input_file=working_input_file,
                        debug_dir=debug_dir,
                        control_word_func_dict=control_word_func_dict)
                pass

            # Space means (1) delimiter followed by text, or (2) advance parse
            # index by one.
            else:
                if parse_text[parse_index] is " " and \
                        parse_text[parse_index+1] is not "\\" and \
                        parse_text[parse_index+1] is not "}" and \
                        parse_text[parse_index+1] is not "{":
                    regex = r"\s+(\w+|\s|\W)+(?<!})"
                    match = re.search(regex, parse_text[parse_index:])
                    if match:
                        working_xml_file_update.tag_append(
                            debug_dir=debug_dir,
                            tag_update=match.group(0))
                else:
                    parse_index = cleanup_processor(parse_index=parse_index)
                pass


def cleanup_processor(parse_index: int) -> int:
    """ This is a fail-safe function. """
    parse_index += 1
    return parse_index
    pass
