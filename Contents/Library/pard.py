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

""" Pard marks a reset to default paragraph properties.
    When RtoX encounters pard it: 1) checks for and closes relevant open
    tags, 2) inserts a close paragraph tag, 3) inserts an open paragraph tag, and
    4) updates the tag registry. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.pard"

# Standard library imports
import json
import logging
import os


# From local application
import open_tag_check
import tag_registry_update
import working_xml_file_update
from read_log_config import logger_debug


# TODO Currently, pard does the same thing as par. But, pard should reset the
#  paragraph settings.
def pard_tag_process(debug_dir: str, tag_dict: dict, line: str):

    open_emphasis_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict)

    paragraph_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict, line=line)

    update_tag_registry(debug_dir=debug_dir)


def open_emphasis_tag_cleanup(debug_dir: str, tag_dict: dict):
    """ Check the tag registry to see whether an emphasis tag needs closing
    and close them. """
    # Check the tag registry to see whether an emphasis tag needs closing
    # and, if so, close it.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic"
    ]

    open_tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                             tag_dict=tag_dict)


def paragraph_tag_cleanup(debug_dir: str, tag_dict: dict, line: str):
    """ If the tag registry shows a closed paragraph, insert an open
    paragraph tag. If it shows an open paragraph, close it and open a new
    paragraph. """
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)

    tag_closed = "0"

    if tag_registry["paragraph"] == tag_closed:
        tag_update = tag_dict["paragraph-beg"]
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=tag_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    else:
        tag_update = tag_dict["paragraph-end"] + tag_dict["paragraph-beg"]
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=tag_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-end"] + tag_dict[
                         "paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")


def update_tag_registry(debug_dir: str, tag_open="1"):
    tag_update_dict = {"paragraph": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
