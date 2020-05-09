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

""" """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.docinfo_parser"

# From standard libraries
import json
import os

# From local applications
import docinfo_read


def process_docinfo(debug_dir: str, working_input_file: str):
    """ Parse the info section of document and save the information in a
    dictionary. """
    with open(os.path.join(debug_dir, "header_tables_dict.json")) as \
            header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)

        table_start_line = header_tables_dict["info"][0]
        table_start_index = header_tables_dict["info"][1]

        docinfo_read.InfoParseController.process_info_section(
            self=docinfo_read.InfoParseController(
                debug_dir=debug_dir,
                table_start_line=table_start_line,
                table_start_index=table_start_index,
                table="info",
                working_input_file=working_input_file))
