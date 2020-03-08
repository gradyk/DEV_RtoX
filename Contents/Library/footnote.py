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
Parse text and settings in the RTF file wrapped by the footnote keyword ({
\\footnote ...}).
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-18"
__name__ = "Contents.Library.footnote"

# Standard library imports
import linecache
import logging

# From local application
import open_tag_check
import tag_registry_update
import working_xml_file_update
from read_log_config import logger_debug


def footnote_bounds(working_input_file: str, line_to_search: str) -> str:
    """
    A footnote is bounded by an opening brace and keyword ({\\footnote)
    and a closing brace (}). The opening is easy to identify. The closing can
    be determined by counting opening and closing braces until the count
    matches.
    """
    left_brace = 0
    right_brace = 0
    footnote_end_line = "0"
    while footnote_end_line == "0":
        line_to_search = linecache.getline(working_input_file, line_to_search)
        for character in line_to_search:
            if character == "{":
                left_brace += 1
            elif character == "}":
                right_brace += 1
            else:
                pass

            if left_brace == right_brace:
                footnote_end_line = line_to_search
            else:
                pass

        line_to_search += 1

    linecache.clearcache()
    return footnote_end_line


def footnote_start(debug_dir: str, tag_dict: dict, line: str):
    """
    Before inserting an opening XML tag for a footnote, check for open tags
    that need to be closed and (if any) close them. Insert the opening
    footnote tag. Update the tag_registry after inserting tags.
    """
    # TODO At least in TPRES, a footnote can be embedded in a paragraph or at
    #  the end of a paragraph. If embedded, the paragraph tag should not be
    #  closed before the footnote or opened after it. See also header.
    # Check for and close open tags.
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

    # Add the opening footnote tag.
    tag_update = tag_dict["footnote-beg"]

    working_xml_file_update.tag_append(debug_dir=debug_dir,
                                       tag_update=tag_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(tag_dict["footnote-beg"] + f"{line}")
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")

    # Update the tag registry.
    tag_open = "1"
    tag_update_dict = {"footnote": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)


def footnote_end(debug_dir: str, tag_dict: dict, line: str):
    """
    Before inserting a closing XML tag for a footnote, check for open tags
    and (if any) close them. Insert the closing footnote tag. Updated the
    tag registry.
    """
    # TODO Should that tag_dict be determined at the outset and passed as a
    #  variable?
    # Check for and close open tags.
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

    # Add the closing footnote tag.
    tag_update = tag_dict["footnote-end"]

    working_xml_file_update.tag_append(debug_dir=debug_dir,
                                       tag_update=tag_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(f"({line})" + tag_dict["footnote-end"])
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")

    # Update the tag registry.
    tag_closed = "0"
    tag_update_dict = {"footnote": tag_closed}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
