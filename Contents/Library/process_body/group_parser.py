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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_parser"

import pprint
import re
import sys


def processor(contents_list: list, group_dict: dict):

    for ele in contents_list:
        if re.search(r"^\\", ele) is not None:
            child = {"id": ele,
                     "type": "cw"}

            group_dict["children"].append(child)
        elif re.search(r"^{", ele):
            child = {"id": ele,
                     "type": "group",
                     "children": []}

            group_dict["children"].append(child)

    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(group_dict)
    sys.exit()
