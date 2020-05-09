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

"""
Prepare the input file for processing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "Contents.Library.input_file_prep"

# From standard libraries
import os

# From local application
import convert_1252_to_unicode


class InputPrep:

    def __init__(self,
                 input_file_name: str,
                 debug_dir: str,
                 base_script_dir: str
                 ):
        self.input_file = input_file_name
        self.debug_dir = debug_dir
        self.base_script_dir = base_script_dir

    def input_file_prep(self):
        """
        Copy the input_file to a working file called
        "working_input_file.data" in the debug directory. Create a working
        xml file where tags will be placed and insert a header section.
        """

        # Copy input file to working_input_file.data in debugdir.
        with open(os.path.join(self.base_script_dir, self.input_file)) as \
                input_file_copy:
            read_file = input_file_copy.read()

        with open(os.path.join(self.debug_dir, "working_input_file_pre.txt"),
                  "w+") as working_rtf_file_pre:
            working_rtf_file_pre.write(read_file)

        # TODO this should be more flexible allowing for other code pages as
        #  the starting point.
        # Convert from MS1252 code page to unicode.
        convert_1252_to_unicode.convert_ms1252(
            debug_dir=self.debug_dir)

        working_rtf_file = os.path.join(self.debug_dir,
                                        "working_input_file.txt")

        # Create the file in which the XML tags and text will be
        # added as the conversion progresses.
        working_xml_file = open(os.path.join(self.debug_dir,
                                "working_xml_file.xml"), "w+")

        working_xml_file.close()

        return working_rtf_file
