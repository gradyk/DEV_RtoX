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
import json
import linecache
import os
import re

# From local application
import open_tag_check


def pard(working_file: str,
         line_to_read: str,
         styles_status_list: list,
         xml_tag_num: str,
         debug_dir: str
         ) -> None:

    # Search the pard line for the paragraph style code (\\sX). If no such
    # code exists, use the default paragraph style.
    search_area = linecache.getline(working_file, line_to_read)
    match = re.search(r"\\s[0-9]+", search_area)
    if match is None:
        set_style = "s56"
    else:
        set_style = match[0].replace("\\", "")

    # Search the styles_status_list (compiled from the style_sheet_table) for
    # that paragraph style code. Return a dictionary (pard_style) with the
    # settings for the paragraph style code (set_style).
    style_catalogue = {}
    b = {}

    code_set = [i for i in styles_status_list if set_style in i]
    for a, b in code_set:
        style_catalogue.setdefault(a, b)
    pard_style = dict(b)

    # Parse the settings of the pard line.
    # TODO any need for code, additive, style_name, style_next_paragraph?
    italic = PardParse.italic(self=PardParse(pard_style=pard_style))
    bold = PardParse.bold(self=PardParse(pard_style=pard_style))
    underline = PardParse.underline(self=PardParse(pard_style=pard_style))
    strikethrough = PardParse.strikethrough(self=PardParse(
        pard_style=pard_style))
    small_caps = PardParse.small_caps(self=PardParse(pard_style=pard_style))

    settings_dict = {
        "italic":           italic,
        "bold":             bold,
        "underline":        underline,
        "strikethrough":    strikethrough,
        "small_caps":       small_caps
    }

    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # Use the xml tag dictionary to create xml tags based on the pard line
    # settings.
    tag = ""
    for key in settings_dict:
        if settings_dict[key] > "0":
            # Create tag.
            tag = tag_dict[key+"-beg"]
            # Update tag registry.
            with open(os.path.join(debug_dir, "tag_registry.txt")) as \
                    tag_registry_pard_pre:
                tag_registry_pard = json.load(tag_registry_pard_pre)
                trd_pard_update = {key: "1"}
                tag_registry_pard.update(trd_pard_update)
            with open(os.path.join(debug_dir, "tag_registry.txt"), "w") as \
                    tag_registry_pard_final:
                json.dump(tag_registry_pard, tag_registry_pard_final)
        else:
            pass

    # Check the tag registry to see whether an emphasis tag needs closing
    # and, if so, close it.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph"
    ]

    for item in status_list:
        open_tag_check.TagCheck.tag_check(
            self=open_tag_check.TagCheck(
                debug_dir=debug_dir,
                xml_tag_num=xml_tag_num),
            tag_dict=tag_dict,
            tag_type=item)

    # Insert the tags to close open tags and then the tags for the next
    # paragraph. Write those tags to the working xml file.
    with open(os.path.join(debug_dir, "working_xml_file.xml"),
              "r") as wxf_pre:
        wxf = wxf_pre.read()
        wxf = wxf + tag + tag_dict["paragraph-beg"]
    with open(os.path.join(debug_dir, "working_xml_file.xml"),
              "w") as wxf_pre:
        wxf_pre.write(wxf)

    # Update the tag registry.
    with open(os.path.join(debug_dir, "tag_registry.txt")) as trd_pard_pre:
        trd_pard = json.load(trd_pard_pre)
        trd_update = {"paragraph": "1"}
        trd_pard.update(trd_update)
    with open(os.path.join(debug_dir, "tag_registry.txt"), "w") as \
            trd_pard_final:
        json.dump(trd_pard, trd_pard_final)

        
class PardParse:

    # TODO Collapse this to a for loop that runs through the style types and
    #  builds a dictionary of results.

    def __init__(self,
                 pard_style: dict) -> None:
        self.pard_style = pard_style

    def italic(self):
        try:
            italic_value = str(self.pard_style["italic"])
            return italic_value
        except TypeError:
            italic_value = "0"
            return italic_value

    def bold(self):
        try:
            bold_value = str(self.pard_style["bold"])
            return bold_value
        except TypeError:
            bold_value = "0"
            return bold_value
        
    def underline(self):
        try:
            underline_value = str(self.pard_style["underline"])
            return underline_value
        except TypeError:
            underline_value = "0"
            return underline_value
        
    def strikethrough(self):
        try:
            strikethrough_value = str(self.pard_style["strikethrough"])
            return strikethrough_value
        except TypeError:
            strikethrough_value = "0"
            return strikethrough_value
        
    def small_caps(self):
        try:
            small_caps_value = str(self.pard_style["small_caps"])
            return small_caps_value
        except TypeError:
            small_caps_value = "0"
            return small_caps_value

    linecache.clearcache()
