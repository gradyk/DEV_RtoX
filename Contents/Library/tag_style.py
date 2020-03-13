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

""" The user can express a preference for XML tag style, which dictates the XML
tag dictionary used. Without a preference, the program defaults to XML plain.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-16"
__name__ = "Contents.Library.tag_style"

# From standard libraries
import importlib


def tag_dict_selection(xml_tag_num: str):
    """ Import an XML tag dictionary based on user XML tag style preference. """
    # Possible XML tag dictionaries.
    options = {
        "1": "xml_tag_dict",
        "2": "tei_tag_dict",
        "3": "tpres_tag_dict",
    }

    try:
        value = options[xml_tag_num]
        xtags = importlib.import_module("Contents.Library.dicts.xml_tags")
        tag_dict_pre = {value: getattr(xtags, value)}
        tag_dict = tag_dict_pre[value]
    except (TypeError, SyntaxError):
        raise ("You did not express a tag style preference. "
               "Plain XML will be used.")

    return tag_dict
