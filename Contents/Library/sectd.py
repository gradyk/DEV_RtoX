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
Sectd signifies that the section just beginning uses the same formatting as
the preceding section.
"""

# From standard library
import json
import os

# From local application
import open_tag_check


def sectd(debug_dir: str,
          xml_tag_num: str
          ) -> None:

    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
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
        open_tag_check.TagCheck.tag_check(
            self=open_tag_check.TagCheck(
                debug_dir=debug_dir,
                xml_tag_num=xml_tag_num),
            tag_dict=tag_dict,
            tag_type=item)

    with open(os.path.join(debug_dir, "tag_registry.txt")) as \
            tag_registry_sectd_pre:
        tag_registry_sectd = json.load(tag_registry_sectd_pre)
    # If a section is closed, open a section then open a paragraph.
    # 0 = status is closed, 1 = status is open
    if tag_registry_sectd["section"] == "0":
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
        # If a section is open, close it, then open a new section, then open
        # a paragraph.
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
            tag_registry_sectd_pre:
        tag_registry_sectd = json.load(tag_registry_sectd_pre)
        tag_registry_sectd_update = {"section": "1", "paragraph": "1"}
        tag_registry_sectd.update(tag_registry_sectd_update)
    with open(os.path.join(debug_dir, "tag_registry.txt"), "w") as \
            tag_registry_sectd_final:
        json.dump(tag_registry_sectd, tag_registry_sectd_final)
