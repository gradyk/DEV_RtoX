#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

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

""" Sectd marks a reset to default section properties.
When RtoX encounters sectd it: 1) checks for and closes relevant open
tags, 2) inserts a close section tag, 3) inserts an
open paragraph tag, and 4) updates the tag registry. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "Contents.Library.sectd"

# Standard library imports
import json
import logging
import os

# From application library
import tag_check
import tag_registry_update
import output_file_update
from read_log_config import logger_debug


def sectd_tag_process(debug_dir: str, tag_dict: dict, line: str):

    open_emphasis_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict)

    section_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict, line=line)

    update_tag_registry(debug_dir=debug_dir)


def open_emphasis_tag_cleanup(debug_dir: str, tag_dict: dict):

    # Check the tag registry to see whether an emphasis or paragraph tag needs
    # closing and, if so, close it.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph"
    ]

    tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                        tag_dict=tag_dict)


def section_tag_cleanup(debug_dir: str, tag_dict: dict, line: str):
    """ If the tag registry shows a closed section, insert an open
        section tag and an open paragraph tag. If it shows an open section,
        close it and open a new section and a new paragraph. """
    tag_registry = os.path.join(debug_dir, "../../debugdir/tag_registry.json")
    with open(tag_registry) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)

    tag_closed = "0"

    if tag_registry["section"] == tag_closed:
        content_update = tag_dict["section-beg"]
        output_file_update.content_append(debug_dir=debug_dir,
                                      content_update=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["section-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    else:
        # If a section tag is open, close it and open a new section.
        content_update = tag_dict["section-end"] + tag_dict["section-beg"]
        output_file_update.content_append(debug_dir=debug_dir,
                                      content_update=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["section-end"] +
                          tag_dict["section-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")


def update_tag_registry(debug_dir: str, tag_open="1"):
    content_update_dict = {"section": tag_open}
    tag_registry_update.processor(tag_info, )
