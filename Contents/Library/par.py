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
Par marks the end of a paragraph. It does not include any other coding. The
necessary steps are: 1) determine user's tag style preference, 2) check for and
close relevant open tags, 3) close the paragraph tag, 4) insert an open
paragraph tag, 5) write the tags to the working xml file.
"""

# Standard library imports
import json
import os
import sys

# From local application
import open_tag_check
import tag_registry_update
import working_xml_file_update


def tag_insert(debug_dir: str, xml_tag_num: str, line: str):
    """

    """
    # Determine tag style based on user's preference.
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # Check the tag registry to see whether an emphasis tag needs closing
    # and, if so, close it.
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

    # Check the status of the paragraph tag. It if is closed then
    # open it.
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)
    # 0 = closed, 1 = open
    if tag_registry["paragraph"] == "0":
        tag_update = tag_dict["paragraph-beg"]
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=tag_update)
        sys.stdout.write(tag_dict["paragraph-beg"] + f"{line}")
        pass
    else:
        # If it is open, close it and open a new paragraph (pard marks the
        # end of a paragraph and, presumptively, the beginning of a new
        # paragraph).
        tag_update = tag_dict["paragraph-end"] + tag_dict["paragraph-beg"]
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=tag_update)
        sys.stdout.write(tag_dict["paragraph-end"] + tag_dict[
                         "paragraph-beg"] + f"{line}")
        pass

    # Update the tag registry.
    tag_update_dict = {"paragraph": "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)
