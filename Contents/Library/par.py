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
Par marks the end of a paragraph. It does not include any other coding. The
necessary steps are: 1) determine user's tag style preference, 2) check for and
close relevant open tags, 3) close the paragraph tag, 4) insert an open
paragraph tag, 5) write the tags to the working xml file.
"""

# Standard library imports
import json
import os

# From local application
import open_tag_check


def tag_insert(debug_dir, xml_tag_num):

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
        "italic"
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

    # Check the status of the paragraph tag. It if is closed then
    # open it.
    with open(os.path.join(debug_dir, "tag_registry.txt")) as \
            tag_registry_par_pre:
        tag_registry_par_tag_check = json.load(tag_registry_par_pre)
    # 0 = status is closed, 1 = status is open
    if tag_registry_par_tag_check["paragraph"] == "0":
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
                wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + tag_dict["paragraph-beg"]
        with open(os.path.join(debug_dir, "working_xml_file.xml"), "w") as \
                wxf_pre:
            wxf_pre.write(wxf)
        pass
    else:
        # If it is open, close it and open a new paragraph (par marks the
        # end of a paragraph and, presumptively, the beginning of a new
        # paragraph).
        with open(os.path.join(debug_dir, "working_xml_file.xml"),
                  "r") as wxf_pre:
            wxf = wxf_pre.read()
            wxf = wxf + tag_dict["paragraph-end"] + "\n" + tag_dict[
                "paragraph-beg"]
        with open(os.path.join(debug_dir, "working_xml_file.xml"),
                  "w") as wxf_pre:
            wxf_pre.write(wxf)
        pass

    # Update the tag registry.
    with open(os.path.join(debug_dir, "tag_registry.txt")) as \
            tag_registry_par_pre:
        tag_registry_par = json.load(tag_registry_par_pre)
        tag_registry_par_update = {"paragraph": "1"}
        tag_registry_par.update(tag_registry_par_update)
    with open(os.path.join(debug_dir, "tag_registry.txt"), "w") as \
            tag_registry_par_final:
        json.dump(tag_registry_par, tag_registry_par_final)
