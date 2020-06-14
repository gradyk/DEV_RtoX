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
Updates the working_xml_file by inserting new tags from other modules.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-07"
__name__ = "Contents.Library.working_xml_file_update"

# From standard libraries
import os


def tag_append(debug_dir: str, tag_update: str):
    # TODO Change tag_append to content_append (here and wherever this
    #  function is called.

    working_xml_file = os.path.join(debug_dir, "working_xml_file.xml")

    with open(working_xml_file, "r") as xml_file_pre:
        xml_file = xml_file_pre.read()
        xml_file_update = xml_file + tag_update

    with open(working_xml_file, "w") as xml_file_pre:
        xml_file_pre.write(xml_file_update)
