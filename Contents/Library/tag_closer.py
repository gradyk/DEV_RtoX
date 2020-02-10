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
__date__ = "2020-02-07"
__name__ = "tag_closer"

# From standard libraries
import os

# From local application
import open_tag_check


def tag_closer(debug_dir: str, xml_tag_num: str):

    status_list = [
        "italic",
        "bold",
        "underline",
        "strikethrough",
        "small_caps",
        "paragraph",
        "section"
    ]

    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(debug_dir=debug_dir,
                                     xml_tag_num=xml_tag_num))

    open_tag_check.TagCheck.tag_check(
        self=open_tag_check.TagCheck(debug_dir=debug_dir,
                                     xml_tag_num=xml_tag_num),
        status_list=status_list,
        tag_dict=tag_dict)

    with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
            xml_file_pre:
        xml_file = xml_file_pre.read()
    with open(os.path.join(debug_dir, "new_xml_file.xml"), "w") as final_xml:
        final_xml.write(xml_file)
