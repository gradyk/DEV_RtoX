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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-18"
__name__ = "footnote"

# Standard library imports
import linecache
import os
import sys

# From local application
import open_tag_check
import tag_registry_update


def footnote_bounds(working_file: str, search_line: str) -> str:
    """

    """
    leftb = 0
    rightb = 0
    footnote_end_line = "0"
    while footnote_end_line == "0":
        line_to_search = linecache.getline(working_file, search_line)
        for elem in line_to_search:
            if elem == "{":
                leftb += 1
            elif elem == "}":
                rightb += 1
            if leftb == rightb:
                footnote_end_line = search_line
            else:
                pass
        search_line += 1

    linecache.clearcache()
    return footnote_end_line


def footnote_start(debug_dir: str, xml_tag_num: str, line: str):
    """

    """
    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(debug_dir=debug_dir,
                                     xml_tag_num=xml_tag_num))

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

    with open(os.path.join(debug_dir, "new_xml_file.xml"), "w") as xml_file:
        xml_file.write(tag_dict["footnote-beg"])
        sys.stdout.write(tag_dict["footnote-beg"] + f"{line}")

    # Update the tag registry.
    tag_update_dict = {"footnote": "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)


def footnote_end(debug_dir: str, xml_tag_num: str, line: str):
    """

    """
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
        "paragraph"
    ]

    open_tag_check.TagCheck.tag_check(
        self=open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num),
        tag_dict=tag_dict,
        status_list=status_list)

    with open(os.path.join(debug_dir, "working_xml_file.xml"),
              "a") as wxf_pre:
        wxf_pre.write(tag_dict["footnote-end"] + tag_dict["paragraph-beg"])
        sys.stdout.write(tag_dict["footnote-end"] +
                         tag_dict["paragraph-beg"] + f"({line})")

    # Update the tag registry.
    tag_update_dict = {"footnote": "0", "paragraph": "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, tag_update_dict=tag_update_dict)