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

""" Parse text and settings in the RTF file wrapped by the footnote keyword ({
\\footnote ...}). """

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


def footnote_process_controller_start(working_input_file: str,
                                      line_to_search: str,
                                      debug_dir: str, tag_dict: dict,
                                      line: str) -> None:

    determine_footnote_bounds(working_input_file=working_input_file,
                              line_to_search=line_to_search)

    open_emphasis_tag_cleanup_start(debug_dir=debug_dir, tag_dict=tag_dict)

    insert_opening_footnote_tag(debug_dir=debug_dir, tag_dict=tag_dict,
                                line=line)

    update_tag_registry_start(debug_dir=debug_dir)


def determine_footnote_bounds(working_input_file: str,
                              line_to_search: str) -> str:
    """ A footnote is bounded by an opening brace and keyword ({\\footnote)
        and a closing brace (}). The opening is easy to identify. The closing
        can be determined by counting opening and closing braces until the count
        matches. """
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


def open_emphasis_tag_cleanup_start(debug_dir: str, tag_dict: dict) -> None:
    """ Check for open tags that need to be closed and close them. Insert the
    opening footnote tag. Update the tag_registry after inserting tags. """
    # TODO At least in TPRES, a footnote can be embedded in a paragraph or at
    #  the end of a paragraph. If embedded, the paragraph tag should not be
    #  closed before the footnote or opened after it. See also header.
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


def insert_opening_footnote_tag(debug_dir: str, tag_dict: dict,
                                line: str) -> None:
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


def update_tag_registry_start(debug_dir: str):
    tag_open = "1"
    tag_update_dict = {"footnote": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)


def footnote_process_controller_end(debug_dir: str, tag_dict: dict,
                                    line: str) -> None:

    open_emphasis_tag_cleanup_end(debug_dir=debug_dir, tag_dict=tag_dict)

    insert_closing_footnote_tag(debug_dir=debug_dir, tag_dict=tag_dict,
                                line=line)

    update_tag_registry_end(debug_dir=debug_dir)


def open_emphasis_tag_cleanup_end(debug_dir: str, tag_dict: dict) -> None:
    """ Check for open tags and close them. Insert the closing footnote tag.
        Updated the tag registry. """
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


def insert_closing_footnote_tag(debug_dir: str, tag_dict: dict,
                                line: str) -> None:

    tag_update = tag_dict["footnote-end"]

    working_xml_file_update.tag_append(debug_dir=debug_dir,
                                       tag_update=tag_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(f"({line})" + tag_dict["footnote-end"])
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")


def update_tag_registry_end(debug_dir: str, tag_closed="0") -> None:
    tag_update_dict = {"footnote": tag_closed}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
