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
Pard signifies that the paragraph just beginning uses the same formatting as
the preceding paragraph.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "pard"


# From standard library
import importlib
import linecache
import os
import re


def pard(working_file: str,
         line_to_read: str,
         styles_status_list: list,
         xml_tag_num: str,
         debug_dir: str
         ) -> None:

    # Search the pard line for the paragraph style code (\\sX).
    search_area = linecache.getline(working_file, line_to_read)
    match = re.search(r"\\s[0-9]+", search_area)
    if match is None:
        set_style = "s56"
    else:
        set_style = match[0].replace("\\", "")

    # Search the styles_status_list for that paragraph style code. If no such
    # code exists, use the default paragraph style. Return a dictionary (
    # di_b) with the settings for the paragraph style code.
    di = {}
    b = {}

    code_set = [i for i in styles_status_list if set_style in i]
    for a, b in code_set:
        di.setdefault(a, b)
    di_b = dict(b)

    # Parse the settings.
    # TODO any need for code, additive, style_name, style_next_paragraph?
    italic = PardParse.italic(self=PardParse(di_b=di_b))
    bold = PardParse.bold(self=PardParse(di_b=di_b))
    underline = PardParse.underline(self=PardParse(di_b=di_b))
    strikethrough = PardParse.strikethrough(self=PardParse(di_b=di_b))
    small_caps = PardParse.small_caps(self=PardParse(di_b=di_b))

    # Possible xml tag dictionaries.
    # TODO consolidate all the xml tag dictionary decisions in one file so it
    #  is easier to add nex dictionaries.
    options = {
        "1": "xml_tag_dict",
        "2": "tei_tag_dict",
        "3": "tpres_tag_dict",
    }

    # Import xml tag dictionary based on user xml tag style preference.
    if options[xml_tag_num]:
        value = options[xml_tag_num]
        xtags = importlib.import_module("rtox.dictionaries.xml_tags")
        tag_dict_pre = {value: getattr(xtags, value)}
        tag_dict = tag_dict_pre[value]
    else:
        from rtox.dictionaries.xml_tags import xml_tag_dict as tag_dict

    tag = ""
    # Use the results to create xml tags.
    if italic > "0":
        tag = tag_dict["italic-beg"]
    else:
        pass

    if bold > "0":
        tag = tag + tag_dict["bold-beg"]
    else:
        pass

    if underline > "0":
        tag = tag + tag_dict["underline-beg"]
    else:
        pass

    if strikethrough > "0":
        tag = tag + tag_dict["strikethrough-beg"]
    else:
        pass

    if small_caps > "0":
        tag = tag + tag_dict["smallcaps-beg"]
    else:
        pass

    with open(os.path.join(debug_dir, "working_xml_file.xml"),
              "a") as wxf_pre:
        wxf_pre.write(tag)

        
class PardParse:
    def __init__(self,
                 di_b: dict) -> None:
        self.di_b = di_b

    def italic(self):
        """

        """
        try:
            italic_value = str(self.di_b["italic"])
            return italic_value
        except TypeError:
            italic_value = "0"
            return italic_value

    def bold(self):
        """

        """
        try:
            bold_value = str(self.di_b["bold"])
            return bold_value
        except TypeError:
            bold_value = "0"
            return bold_value
        
    def underline(self):
        """

        """
        try:
            underline_value = str(self.di_b["underline"])
            return underline_value
        except TypeError:
            underline_value = "0"
            return underline_value
        
    def strikethrough(self):
        """

        """
        try:
            strikethrough_value = str(self.di_b["strikethrough"])
            return strikethrough_value
        except TypeError:
            strikethrough_value = "0"
            return strikethrough_value
        
    def small_caps(self):
        """

        """
        try:
            small_caps_value = str(self.di_b["small_caps"])
            return small_caps_value
        except TypeError:
            small_caps_value = "0"
            return small_caps_value

    linecache.clearcache()
