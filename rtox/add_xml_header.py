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
Add a header to the working xml file based on the tag style selected by the
user. To do this, start a new file and add the appropriate header.
Next, add what is in the working_xml_file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-09"
__name__ = "add_xml_header"

# From standard libraries
import os

# From local application
import rtox.lib.open_tag_check


def add_header(debug_dir: str, base_script_dir: str, xml_tag_num: str):

    with open(os.path.join(debug_dir, "working_xml_file.xml"), "r") as \
            working_xml_file_pre:
        working_xml_file = working_xml_file_pre.read()

    tag_dict = rtox.lib.open_tag_check.TagCheck.tag_style(
        self=rtox.lib.open_tag_check.TagCheck(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num))

    # TODO There should be a default header file for each tag style.
    try:
        insert = open(os.path.join(base_script_dir+"/input", tag_dict[
            "xmlheader"]), "r")
        insert_tags = insert.read()

        with open(os.path.join(debug_dir, "new_xml_file.xml"), "w+") as \
                new_xml_file:
            new_xml_file.seek(0)
            new_xml_file.write(insert_tags)
        with open(os.path.join(debug_dir, "new_xml_file.xml"), "a") as \
                new_xml_file:
            new_xml_file.write(working_xml_file)

    except TypeError:
        # TODO A logger message should go here.
        pass
