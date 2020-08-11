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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

""" Method to update the tag registry after tag openings or closings. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-06"
__name__ = "Contents.Library.tag_registry_update"

# From standard libraries
import json
import os
# import sys


def tag_registry_update(debug_dir: str, content_update_dict: dict) -> None:

    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")

    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)
        tag_registry.update(content_update_dict)

    # TODO change the next line into a logger.
    # sys.stdout.write(str(tag_registry))
    with open(tag_registry_file, "w+", encoding='utf-8') as tag_registry_pre:
        json.dump(tag_registry, tag_registry_pre, ensure_ascii=False)
