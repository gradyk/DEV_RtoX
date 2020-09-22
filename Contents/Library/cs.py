#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

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

""" A line which begins with the keyword {\\cs... and ends with a }
is a text line (not to be confused with {\\*\\cs ...} which marks a
character style). The "cs" stands for "character setting". The relevant
settings for XML purposes are: italic, bold, underline, strikethrough,
and small caps. RtoX also captures the text to which those settings apply. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-10"
__name__ = "Contents.Library.cs"

# Standard library imports
import linecache
import logging

# Local application imports
from control_words_symbols import emphasis
import keyword_end_alt
import tag_check
import tag_registry_update
import output_file_update
from read_log_config import logger_debug


# TODO Extend the parsing of cs styles to cover font character formatting as
#  described in spec beginning at p.78.
def determine_cs_bounds(working_input_file: str, line_to_search: int) -> str:
    """ Find the boundaries of the keyword. """

    cs_end_line = keyword_end_alt.keyword_end_alt(
        working_file=working_input_file,
        keyword_open=line_to_search)

    return cs_end_line


def cs_line_parse(line_to_read: str, working_input_file: str) -> tuple:
    """ Find the settings for each relevant variable in the keyword and
        capture the text to which those settings apply. """
    area_search = linecache.getline(working_input_file, line_to_read)

    italic = emphasis.italic(area_search=area_search)
    bold = emphasis.bold(area_search=area_search)
    underline = emphasis.underline(area_search=area_search)
    strikethrough = emphasis.strikethrough(area_search=area_search)
    small_caps = emphasis.small_caps(area_search=area_search)
    text = emphasis.text(area_search=area_search)

    cs_line_dict = {"italic": italic,
                    "bold": bold,
                    "underline": underline,
                    "strikethrough": strikethrough,
                    "small_caps": small_caps
                    }

    return cs_line_dict, text


def open_emphasis_tag_cleanup_start(tag_dict: dict, debug_dir: str) -> None:
    """ Check for open emphasis tags and close them. """
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic"
    ]

    tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                        tag_dict=tag_dict)


def insert_opening_cs_tag(cs_line_dict: dict, text: str,
                          tag_dict: dict, debug_dir: str,
                          line_to_read: str):

    list_of_tags = []
    tag_tracker = 0

    tag_closed = "0"
    tag_open = "1"

    for key in cs_line_dict:
        if cs_line_dict[key] == tag_closed:
            pass
        else:
            tag_tracker = 1
            list_of_tags.append(key)

    if tag_tracker == 1:
        tag = ""
        tag_bag = []
        # Create a string of all tags to open.
        for lot_item in list_of_tags:
            tag = tag + tag_dict[lot_item+"-beg"]
            tag_bag.append(lot_item)

            # Update the tag registry.
            content_update_dict = {lot_item: tag_open}
            tag_registry_update.processor(debug_dir=debug_dir,
                                          tag_update_dict=content_update_dict)
            try:
                if logger_debug.isEnabledFor(logging.DEBUG):
                    logger_debug.error(msg=str(tag_dict[lot_item+"-beg"] +
                                               f" {line_to_read}"))
            except AttributeError:
                logging.exception("Check setLevel for logger_debug.")

        # To the string of tags, add the cs line text. Write the string to the
        # working_xml_file.
        content_update = tag + text
        output_file_update.content_append(debug_dir, content_update)

    else:
        # If no tags need to be added, just write the text to the file.
        tag_bag = []
        content_update = text
        output_file_update.content_append(debug_dir, content_update)

    return tag_bag


def insert_closing_cs_tags(debug_dir: str, tag_dict: dict, tag_bag: list,
                           line: str):
    """ All tags opened by cs_opening_tags must be closed. This may happen
        immediately after we write the tags and text to the working_xml_file if
        the cs text line does not contain any nested tags (e.g., a footnote or
        paragraph). Or, it may happen after processing the nested lines if they
        exist. """
    tag = ""
    tag_closed = "0"

    # If the tag_bag is empty, no tags need to be closed and control should
    # be returned to the line_parser module.
    if not tag_bag:
        pass
    else:
        # If there are tags in the tag_bag, reverse the order of the tags.
        tag_bag.reverse()

        # Add a closing tag for each tag in the reversed list.
        for tag_item in tag_bag:
            tag = tag + tag_dict[tag_item+"-end"]

            # Update the tag registry.
            content_update_dict = {tag_item: tag_closed}
            tag_registry_update.processor(debug_dir=debug_dir,
                                          tag_update_dict=content_update_dict)
            try:
                if logger_debug.isEnabledFor(logging.DEBUG):
                    msg = str(f"{line} " + tag_dict[tag_item+"-end"])
                    logger_debug.error(msg)
            except AttributeError:
                logging.exception("Check setLevel for logger_debug.")

        # Add the closing tags to the working_xml_file.
        content_update = tag
        output_file_update.content_append(debug_dir, content_update)

    # Emptying the tag_bag prevents unwanted closing tags from being
    # added when there are nested tags in the cs text line.
    tag_bag.clear()
