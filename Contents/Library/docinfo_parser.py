
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


class DocinfoParse(object):

    def __init__(self,
                 debug_dir: str,
                 working_input_file: str):
        self.debug_dir = debug_dir
        self.working_input_file = working_input_file

    def process_docinfo(self):
        """ Parse the info section of document and save the information in a
        dictionary. """
        table = "info"
        with open(os.path.join(self.debug_dir, "header_tables_dict.json")) as \
                header_tables_dict_pre:
            header_tables_dict = json.load(header_tables_dict_pre)

        if table in header_tables_dict.keys():

            line_to_check = header_tables_dict[table]

            docinfo_read.InfoParseController.process_info_section(
                self=docinfo_read.InfoParseController(
                    debug_dir=self.debug_dir,
                    line_to_read=line_to_check,
                    table=table,
                    working_input_file=self.working_input_file))

        else:
            pass
