#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
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

""" This module checks for open tags using a list (status_list). If any tags on
the list are open, they are closed by inserting closing tags into the
working_xml_file. The tag_registry is updated. These steps are performed by
open_tag_check. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-07"
__name__ = "Contents.Library.tag_closer"

# From local application
import tag_check
import tag_set_file


def tag_closer(debug_dir: str, tag_set: int):

    status_list = [
        "italic",
        "bold",
        "underline",
        "strikethrough",
        "small_caps",
        "paragraph",
        "section"
    ]

    tag_dict = tag_set_file.tag_dict_selection(tag_set=tag_set)

    tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                        tag_dict=tag_dict)
