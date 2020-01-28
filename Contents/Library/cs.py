#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
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

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
In an RTF file, a line which begins with the keyword {\\cs... is a text line.
The "cs" stands for "character setting". The relevant settings for XML
purposes are: italic, bold, underline, strikethrough, and small caps. We also
need to capture the text at the end of the line, to which those settings apply.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-10"
__name__ = "cs"

# Standard library imports
import os

# Local application imports
import emphasis
import keyword_end_alt
import open_tag_check


def cs_line_boundaries(working_file: str, line_to_read: str) -> str:
    """
    Find the end of the text line.
    """
    text_line = keyword_end_alt.keyword_end_alt(
            working_file=working_file,
            keyword_open=line_to_read)

    return text_line


def cs_line_parse(text_line: str) -> tuple:
    """
    Find the settings for each relevant variable and capture the text to
    which those settings apply.
    """
    italic = emphasis.italic(area_search=text_line)
    bold = emphasis.bold(area_search=text_line)
    underline = emphasis.underline(area_search=text_line)
    strikethrough = emphasis.strikethrough(area_search=text_line)
    small_caps = emphasis.small_caps(area_search=text_line)
    text = emphasis.text(area_search=text_line)

    cs_line_dict = {"italic": italic,
                    "bold": bold,
                    "underline": underline,
                    "strikethrough": strikethrough,
                    "small_caps": small_caps
                    }

    return cs_line_dict, text


def cs_tag_write(cs_line_dict: dict, text: str,
                 xml_tag_num: str, debug_dir: str):
    """
    Determine what style tags to use. Check for relevant open tags and close
    them. Based on the settings in the "cs" (text) line, write to the working
    xml file the tags needed to implement those settings. Then, write the
    text \to which those settings apply.
    """

    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # Relevant tags to check to see if they are open and if so close them.
    status_list = [
        "italic",
        "bold",
        "underline",
        "strikethrough",
        "small_caps"
    ]

    # Check the tag registry to see whether an emphasis tag needs closing.
    for item in status_list:
        open_tag_check.TagCheck.tag_check(
            self=open_tag_check.TagCheck(
                debug_dir=debug_dir,
                xml_tag_num=xml_tag_num),
            tag_dict=tag_dict,
            tag_type=item)

    # Add xml tags to working xml file that reflect settings of current
    # text line. As appropriate, update text line status dictionary.
    list_of_tags = []
    tag_tracker = 0
    for key in cs_line_dict:
        if cs_line_dict[key] == "0":  # Means no tags need to be opened.
            pass
        else:
            tag_tracker = 1  # Means at least one tag should be opened.
            list_of_tags.append(key)

    if tag_tracker == 1:
        tag = ""
        # Open all necessary tags.
        for item in list_of_tags:
            tag = tag + tag_dict[item+"-beg"]

        # To that list of tags, add the cs line text.
        tag = tag + text

        # Reverse the list of tags to open.
        list_of_tags.reverse()

        # Add a closing tag for each item in the reversed list.
        for item in list_of_tags:
            tag = tag + tag_dict[item+"-end"]

        # Add the tags plus text to the working xml file.
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
                wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + tag
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "w") as \
                wxf_pre:
            wxf_pre.write(wxf)

    else:
        # If no tags needed to be added, just add the text to the file.
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
                wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + text
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "w") as \
                wxf_pre:
            wxf_pre.write(wxf)
