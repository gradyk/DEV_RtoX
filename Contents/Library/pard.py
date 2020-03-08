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
Pard indicates the paragraph just starting has the same styling as the
previous paragraph. The necessary steps are: 1) determine user's tag style
preference, 2) check for and close relevant open tags, 3) close the paragraph
tag, 4) insert an open paragraph tag, 5) write the tags to the working xml file.
"""

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


def tag_insert(debug_dir: str, tag_dict: dict, line: str):
    """

    """
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

    # Check the status of the paragraph tag. It if is closed then
    # open it.
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)

    tag_closed = "0"
    tag_open = "1"

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
        # If it is open, close it and open a new paragraph (pard marks the
        # end of a paragraph and, presumptively, the beginning of a new
        # paragraph).
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

    # Update the tag registry.
    tag_update_dict = {"paragraph": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
