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
In an RTF file, a line which begins with the keyword {\\cs... and ends with a }
is a text line. The "cs" stands for "character setting". The relevant
settings for XML purposes are: italic, bold, underline, strikethrough,
and small caps. We also need to capture the text at the end of the line,
to which those settings apply.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-10"
__name__ = "Contents.Library.cs"

# Standard library imports
import linecache
import logging
import sys

# Local application imports
import emphasis
import keyword_end_alt
import open_tag_check
import tag_registry_update
import tag_style
import working_xml_file_update
from read_log_config import logger_debug


def cs_bounds(working_file: str, line_to_read: str) -> str:
    """
    Start with the line that includes the keyword "{\\cs..." find the end of
    the text line (marked by a closing brace "}").
    """
    cs_end_line = keyword_end_alt.keyword_end_alt(working_file=working_file,
                                                  keyword_open=line_to_read)

    return cs_end_line


def cs_line_parse(line_to_read: str, working_file: str) -> tuple:
    """
    Find the settings for each relevant variable and capture the text to
    which those settings apply.
    """
    area_search = linecache.getline(working_file, line_to_read)

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


def cs_opening_tags(cs_line_dict: dict, text: str,
                    xml_tag_num: str, debug_dir: str,
                    line: str):
    """
    Determine what tag_dict (style tags) to use based on the user's
    preference. Check for open cs tags (e.g., an open italic tag) and close
    them. Based on the settings in the cs (text) line, write to the
    working_xml_file the tags implementing those settings. Store the types
    of tags (e.g., italic, bold) in the tag_bag. Then, write to the
    working_xml_file any text in the cs line to which those settings apply.
    """

    # Determine tag style based on user's preference.
    tag_dict = tag_style.tag_dict_selection(xml_tag_num=xml_tag_num)

    # Check the tag registry to see whether any emphasis tags need closing.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic"
    ]

    open_tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                             tag_dict=tag_dict)

    # From the cs line, create a list (list_of_tags) of emphasis tags which
    # need to be added to the working_xml_file. Add those tags to the file
    # and to a tag_bag.
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
            tag_update_dict = {lot_item: tag_open}
            tag_registry_update.tag_registry_update(
                debug_dir=debug_dir,
                tag_update_dict=tag_update_dict)
            try:
                if logger_debug.isEnabledFor(logging.DEBUG):
                    msg = str(tag_dict[lot_item+"-beg"] + f" {line}")
                    logger_debug.error(msg)
            except AttributeError:
                logging.exception("Check setLevel for logger_debug.")

        # To that list of tags, add the cs line text and write to the
        # working_xml_file: contents of the file, plus the tag string,
        # plus the text.
        tag_update = tag + text
        working_xml_file_update.tag_append(debug_dir, tag_update)

    else:
        # If no tags need to be added, just add the cs line text and write
        # to the working_xml_file: contents of the file plus the text.
        tag_bag = []
        tag_update = text
        working_xml_file_update.tag_append(debug_dir, tag_update)

    return tag_bag, tag_dict


def cs_closing_tags(debug_dir: str, tag_dict: str, tag_bag: list, line: str):
    """
    All tags opened by cs_opening_tags must be closed. This may happen
    immediately after we write the tags and text to the working_xml_file if
    the cs text line does not contain any nested tags (e.g., a footnote or
    paragraph). Or, it may happen after processing the nested lines if they
    exist.
    """
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
            tag_update_dict = {tag_item: tag_closed}
            tag_registry_update.tag_registry_update(
                debug_dir=debug_dir,
                tag_update_dict=tag_update_dict)
            try:
                if logger_debug.isEnabledFor(logging.DEBUG):
                    msg = str(f"{line} " + tag_dict[tag_item+"-end"])
                    logger_debug.error(msg)
            except AttributeError:
                logging.exception("Check setLevel for logger_debug.")

        # Add the closing tags to the working_xml_file.
        tag_update = tag
        working_xml_file_update.tag_append(debug_dir, tag_update)

    # Empty the tag_bag (this step prevents unwanted closing tags from being
    # added when there are nested tags in the cs text line).
    tag_bag.clear()
