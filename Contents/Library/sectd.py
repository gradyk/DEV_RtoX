#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Sectd signifies that the section just beginning uses the same formatting as
the preceding section.
"""

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
import open_tag_check
import tag_registry_update
import tag_style
import working_xml_file_update
from read_log_config import logger_debug


def tag_insert(debug_dir: str, xml_tag_num: str, line: str):

    # Determine tag style based on user's preference.
    tag_dict = tag_style.tag_dict_selection(xml_tag_num=xml_tag_num)

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

    open_tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                             tag_dict=tag_dict)

    # Check the tag registry for the status of a section tag. If it is
    # closed, open a new section and open a paragraph.
    tag_registry = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)

    tag_closed = "0"
    tag_open = "1"

    if tag_registry["section"] == tag_closed:
        tag_update = tag_dict["section-beg"]
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=tag_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["section-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    else:
        # If a section tag is open, close it and open a new section.
        tag_update = tag_dict["section-end"] + tag_dict["section-beg"]
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=tag_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["section-end"] +
                          tag_dict["section-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    # Update tag registry.
    tag_update_dict = {"section": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
