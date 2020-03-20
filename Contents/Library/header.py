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

""" Parse text and settings in the RTF file wrapped by the header keyword ({
\\header ...}). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "Contents.Library.header"

# From standard libraries
import linecache
import logging

# From local application
import open_tag_check
import tag_registry_update
import working_xml_file_update
from read_log_config import logger_debug


def determine_header_bounds(working_input_file: str,
                            line_to_search: int) -> str:
    """ A header is bounded by an opening brace and keyword ({\\header)
        and a closing brace (}). The opening is easy to identify. The closing
        can be determined by counting opening and closing braces until the count
        matches. """
    left_brace = 0
    right_brace = 0
    header_end_line = "0"
    while header_end_line == "0":
        search_text = linecache.getline(working_input_file, line_to_search)
        for character in search_text:
            if character == "{":
                left_brace += 1
            elif character == "}":
                right_brace += 1
            else:
                pass
            if left_brace == right_brace:
                header_end_line = line_to_search
            else:
                pass
        line_to_search += 1

    linecache.clearcache()
    return header_end_line


def open_emphasis_tag_cleanup_start(debug_dir: str, tag_dict: dict):
    """ Check for open tags and close them. Insert the opening
    header tag. Update the tag_registry. """
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


def insert_opening_header_tag(debug_dir: str, tag_dict: dict,
                              line_to_read: str) -> None:
    tag_update = tag_dict["header-beg"]

    working_xml_file_update.tag_append(debug_dir=debug_dir,
                                       tag_update=tag_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            logger_debug.error(msg=str(tag_dict["header-beg"] +
                                       f"{line_to_read}"))
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")


def update_tag_registry_start(debug_dir: str, tag_open="1") -> None:
    tag_update_dict = {"header": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)


def header_process_controller_end(debug_dir: str, tag_dict: dict,
                                  line: str) -> None:

    open_emphasis_tag_cleanup_end(debug_dir=debug_dir, tag_dict=tag_dict)

    insert_closing_header_tag(debug_dir=debug_dir, tag_dict=tag_dict,
                              line=line)

    update_tag_registry_end(debug_dir=debug_dir)


def open_emphasis_tag_cleanup_end(debug_dir: str, tag_dict: dict) -> None:
    """ Check for open tags and close them. """
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


def insert_closing_header_tag(debug_dir: str, tag_dict: dict,
                              line: str) -> None:
    # TODO At least in TPRES, a header may be embedded in a paragraph or fall
    #  at the end or beginning of a paragraph. See also footnote.
    """ Insert the header closing tag. Note that a header ending is
        different than a footnote ending. Headers are separate blocks and need
        a paragraph opening tag afterwards. """
    tag_update = tag_dict["header-end"] + tag_dict["paragraph-beg"]

    working_xml_file_update.tag_append(debug_dir=debug_dir,
                                       tag_update=tag_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(tag_dict["header-end"] +
                      tag_dict["paragraph-beg"] + f"{line}")
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")


def update_tag_registry_end(debug_dir: str, tag_closed="0",
                            tag_open="1") -> None:
    tag_update_dict = {"header": tag_closed, "paragraph": tag_open}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
