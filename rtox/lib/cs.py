#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2019. Kenneth A. Grady
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
import importlib
import os

# Local application imports
import rtox.lib.keyword_end_alt
import rtox.lib.emphasis


def cs_line_boundaries(working_file: str, line_to_read: str) -> str:
    """
    Find the end of the text line.
    """

    text_line = rtox.lib.keyword_end_alt.keyword_end_alt(
            working_file=working_file,
            keyword_open=line_to_read)

    return text_line


def cs_line_parse(text_line: str) -> tuple:
    """
    Find the settings for each relevant variable and capture the text to
    which those settings apply.
    """
    italic = rtox.lib.emphasis.italic(area_search=text_line)
    bold = rtox.lib.emphasis.bold(area_search=text_line)
    underline = rtox.lib.emphasis.underline(area_search=text_line)
    strikethrough = rtox.lib.emphasis.strikethrough(area_search=text_line)
    small_caps = rtox.lib.emphasis.small_caps(area_search=text_line)
    text = rtox.lib.emphasis.text(area_search=text_line)

    cs_line_dict = {"italic": italic, "bold": bold, "underline": underline,
                    "strikethrough": strikethrough, "small_caps": small_caps
                    }

    return cs_line_dict, text


def cs_tag_write(cs_line_dict: dict, text: str, cs_status_dict: dict,
                 xml_tag_num: str, debug_dir: str):
    """
    Based on the settings in the "cs" (text) line, write to the working xml
    file the tags needed to implement those settings. Then, write the text
    to which those settings apply.
    """

    # Possible xml tag dictionaries.
    options = {
        "1": "xml_tag_dict",
        "2": "tei_tag_dict",
        "3": "tpres_tag_dict",
    }

    tag_dict = {}

    # Import xml tag dictionary based on user xml tag style preference.
    if options[xml_tag_num]:
        value = options[xml_tag_num]
        function_call = "from rtox.dictionaries.xml_tags import " + \
                        value + " as tag_dict"
        importlib.import_module(function_call)
    else:
        from rtox.dictionaries.xml_tags import xml_tag_dict as tag_dict

    # Add xml tags to working xml file that reflect settings of current
    # text line. As appropriate, update text line status dictionary.
    for key in cs_line_dict:
        cs_status_dict_value = cs_status_dict[key]
        if cs_line_dict[key] == cs_status_dict_value:
            pass
        elif cs_line_dict[key] >= 1 and cs_status_dict_value < 1:
            with open(os.path.join(debug_dir, "working_xml_file.xml"),
                      "a") as wxf_pre:
                wxf_pre.write(tag_dict[key+"_beg"])

        elif cs_line_dict[key] < 1 and cs_status_dict_value >= 1:
            with open(os.path.join(debug_dir, "working_xml_file.xml"),
                      "a") as wxf_pre:
                wxf_pre.write(tag_dict[key+"_end"])

        update_dict = {key: cs_line_dict[key]}
        cs_status_dict.update(update_dict)

    with open(os.path.join(debug_dir, "working_xml_file.xml"),
              "a") as wxf_pre:
        wxf_pre.write(tag_dict[text])
