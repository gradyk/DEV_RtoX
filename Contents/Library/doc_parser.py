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
__date__ = "2019-12-21"
__name__ = "Contents.Library.doc_parser"

# From standard libraries
import json
import linecache
import os

# From local application
import Contents.Library.group_boundaries_capture_contents
import Contents.Library.group_boundaries_no_contents
# import Contents.Library.group_parse
# import Contents.Library.controlword_parse
import file_stats


def main_doc_parser(working_input_file: str, debug_dir: str):
    header_table_file = os.path.join(debug_dir, "header_tables_dict.json")
    with open(header_table_file, "r") as header_table_dict_pre:
        header_table_dict = json.load(header_table_dict_pre)

    line_to_parse = header_table_dict["info"][2]
    start_index = header_table_dict["info"][3] + 1

    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)

    length_working_input_file = file_metrics[0]

    while line_to_parse < (length_working_input_file + 1):

        parse_text = linecache.getline(working_input_file, line_to_parse)
        length_parse_text = len(parse_text)
        parse_index = start_index
        group_info = {}

        while parse_index <= length_parse_text:
            # Ignore RTF controls that begin with {\*\
            if parse_text[parse_index] == "{" and parse_text[
                    parse_index + 1] == "\\" and \
                    parse_text[parse_index + 2] == "*":

                table_boundaries_info \
                    = Contents.Library.group_boundaries_no_contents\
                    .define_boundaries_without_contents(
                        table=str(line_to_parse) + "_" + str(parse_index),
                        working_input_file=working_input_file,
                        table_start_line=line_to_parse,
                        table_start_index=parse_index)

                # MOVE THE LINE_TO_PARSE TO GROUP_END_LINE AND THE
                # PARSE_INDEX TO GROUP_END_INDEX + 1
                pass

            elif parse_text[parse_index] == "\\":
                # FIND THE END OF \\________
                # MOVE THE PARSE INDEX TO THE END OF \\_____ + 1
                pass

            # elif [SYMBOL??]

            else:
                group_start_index = parse_index
                group_info = Contents.Library.\
                    group_boundaries_capture_contents.\
                    define_boundaries_capture_contents(
                        working_input_file=working_input_file,
                        group_start_line=line_to_parse,
                        group_start_index=group_start_index)

            #         Contents.Library.group_parse.____________(
            #             group_info=group_info)

                print(group_info)

            parse_index += 1

    line_to_parse += 1
