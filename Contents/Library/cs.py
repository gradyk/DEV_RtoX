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
import os
import sys

# Local application imports
import emphasis
import keyword_end_alt
import open_tag_check
import tag_registry_update


def cs_bounds(working_file: str, line_to_read: str) -> str:
    """
    Start with the line that includes the keyword "{\\cs..." find the end of
    the text line (marked by a closing brace "}").
    """
    cs_end_line = keyword_end_alt.keyword_end_alt(
            working_file=working_file,
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

    working_xml_file = os.path.join(debug_dir, "working_xml_file.xml")

    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # Check the tag registry to see whether any emphasis tags need closing.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic"
    ]

    open_tag_check.TagCheck.tag_check(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num),
        tag_dict=tag_dict,
        status_list=status_list)

    # From the cs line, create a list (list_of_tags) of emphasis tags which
    # need to be added to the working_xml_file. Add those tags to the file
    # and to a tag_bag.
    list_of_tags = []
    tag_tracker = 0
    # 0 = closed, 1 = open
    for key in cs_line_dict:
        if cs_line_dict[key] == "0":
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
            tag_update_dict = {lot_item: "1"}
            tag_registry_update.tag_registry_update(
                debug_dir=debug_dir,
                tag_update_dict=tag_update_dict)
            sys.stdout.write(tag_dict[lot_item+"-beg"] + f"{line}")

        # To that list of tags, add the cs line text and write to the
        # working_xml_file: contents of the file, plus the tag string,
        # plus the text.
        with open(working_xml_file, "r") as wxf_pre:
            wxf = wxf_pre.read() + tag + text
        with open(working_xml_file, "w") as wxf_pre:
            wxf_pre.write(wxf)

    else:
        # If no tags needed to be added, just add the cs line text and write
        # to the working_xml_file: contents of the file plus the text.
        tag_bag = []
        with open(working_xml_file, "r") as wxf_pre:
            wxf = wxf_pre.read() + text
        with open(working_xml_file, "w") as wxf_pre:
            wxf_pre.write(wxf)

    return tag_bag, tag_dict


def cs_closing_tags(debug_dir: str, tag_dict: str, tag_bag: list, line: str):
    """
    All tags opened by cs_opening_tags must be closed. This may happen
    immediately after we write the tags and text to the working_xml_file if
    the cs text line does not contain any nested tags (e.g., a footnote or
    paragraph). Or, it may happen after processing the nested lines if they
    exist.
    """
    working_xml_file = os.path.join(debug_dir, "working_xml_file.xml")
    tag = ""

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
            tag_update_dict = {tag_item: "0"}
            tag_registry_update.tag_registry_update(
                debug_dir=debug_dir,
                tag_update_dict=tag_update_dict)
            sys.stdout.write(f"{line}" + tag_dict[tag_item+"-end"])

        # Add the closing tags to the working_xml_file.
        with open(working_xml_file, "r") as wxf_pre:
            wxf = wxf_pre.read() + tag
        with open(working_xml_file, "w") as wxf_pre:
            wxf_pre.write(wxf)

    # Empty the tag_bag (this step prevents unwanted closing tags from being
    # added when there are nested tags in the cs text line).
    tag_bag.clear()
