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
Sect marks the end of a section. It does not include any other coding. The
necessary steps are: (1) insert and end of section tag, and (2) insert a
beginning of section tag.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "sect"

# Standard library imports
import json
import os

# From application library
import rtox.lib.open_tag_check


# TODO Tags inserted need to vary depending on user tag style choice.
def tag_insert(debug_dir: str, xml_tag_num: str):

    # Determine tag style based on user's preference.
    tag_dict = rtox.lib.open_tag_check.TagCheck.tag_style(
        self=rtox.lib.open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph",
        "section"
    ]

    # Check the tag registry to see whether an emphasis tag needs closing
    # and, if so, close it.
    for item in status_list:
        rtox.lib.open_tag_check.TagCheck.tag_check(
            self=rtox.lib.open_tag_check.TagCheck(
                debug_dir=debug_dir,
                xml_tag_num=xml_tag_num),
            tag_dict=tag_dict,
            tag_type=item)

    # Check the tag registry for the status of a section tag. If it is
    # closed, open a new section and open a paragraph.
    with open(os.path.join(debug_dir, "tag_registry.txt")) as \
            tag_registry_sect_pre:
        tag_registry_sect = json.load(tag_registry_sect_pre)
    # 0 = status is closed, 1 = status is open
    if tag_registry_sect["section"] == "0":
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
                wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + "\n" + tag_dict["section-beg"] + \
                "\n\t" + tag_dict["paragraph-beg"]
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "w") as \
                wxf_pre:
            wxf_pre.write(wxf)
        pass
    else:
        # If a section tag is open, close it, open a new section and open a
        # paragraph.
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
                wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + tag_dict["section-end"] + "\n" + tag_dict[
                "section-beg"] + "\n\t" + tag_dict["paragraph-beg"]
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "w") as \
                wxf_pre:
            wxf_pre.write(wxf)
            pass

    # Update tag registry.
    with open(os.path.join(debug_dir, "tag_registry.txt")) as \
            tag_registry_sect_pre:
        tag_registry_sect = json.load(tag_registry_sect_pre)
        tag_registry_sect_update = {"section": "1", "paragraph": "1"}
        tag_registry_sect.update(tag_registry_sect_update)
    with open(os.path.join(debug_dir, "tag_registry.txt"), "w") as \
            tag_registry_sect_final:
        json.dump(tag_registry_sect, tag_registry_sect_final)
