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
Sectd signifies that the section just beginning uses the same formatting as
the preceding section.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "Contents.Library.sectd"

# Standard library imports
import json
import os
import sys

# From application library
import open_tag_check
import tag_registry_update
import working_xml_file_update


def tag_insert(debug_dir: str, xml_tag_num: str, line: str):

    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # Check the tag registry to see whether an emphasis or paragraph tag needs
    # closing and, if so, close it.
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph"
    ]

    open_tag_check.TagCheck.tag_check(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num),
        tag_dict=tag_dict,
        status_list=status_list)

    # Check the tag registry for the status of a section tag. If it is
    # closed, open a new section and open a paragraph.
    tag_registry = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)
    # 0 = closed, 1 = open
    if tag_registry["section"] == "0":
        tag_update = tag_dict["section-beg"]
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=tag_update)
        sys.stdout.write(tag_dict["section-beg"] + f"{line}")
        pass
    else:
        # If a section tag is open, close it and open a new section.
        tag_update = tag_dict["section-end"] + tag_dict["section-beg"]
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=tag_update)
        sys.stdout.write(tag_dict["section-end"] +
                         tag_dict["section-beg"] + f"{line}")
        pass

    # Update tag registry.
    tag_update_dict = {"section": "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
