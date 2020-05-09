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
#   RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

"""
This module determines which controlword tables exist in the RTF document.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "Contents.Library.header_structure"

# Standard library imports
import json
import linecache
import os
import re

# From local application
import file_stats
import group_boundaries_no_contents


def build_header_tables_dict(working_input_file: str, debug_dir: str) -> None:
    """ Check header for existence and location of sections: <first line>,
    <font table>, <file table>, <color table>, <stylesheet>, <list table>,
    <rev table>, <rsid table>, <generator>. """
    header_tables_dict = os.path.join(debug_dir, "header_tables_dict.json")

    tables_list = [
        "fonttbl",
        "filetbl",
        "colortbl",
        "stylesheet",
        "listtables",
        "revtbl",
        "rsidtable",
        "generator",
        "info"
    ]

    file_stats_results = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_stats_results[0]

    with open(header_tables_dict, "r") as header_tables_dict_pre:
        header_tables = json.load(header_tables_dict_pre)

        line_count = 1
        while line_count < length_working_input_file + 1:
            for table in tables_list:
                line_to_read = linecache.getline(working_input_file,
                                                 line_count)
                table_search = re.search(r'{\\'+table, line_to_read)
                if table_search:
                    table_start_line = line_count
                    table_start_index = line_to_read.find(table) - 2
                    table_boundaries_info =\
                        group_boundaries_no_contents.define_boundaries_without_contents(
                            table=table,
                            working_input_file=working_input_file,
                            table_start_line=table_start_line,
                            table_start_index=table_start_index)
                    header_tables.update(table_boundaries_info)
                else:
                    pass

            line_count += 1

    with open(header_tables_dict, "w", encoding="utf-8") as \
            header_tables_dict_pre:
        json.dump(header_tables, header_tables_dict_pre, ensure_ascii=False)

    linecache.clearcache()
