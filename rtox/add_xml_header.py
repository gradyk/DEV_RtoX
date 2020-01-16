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
user. Pretty-print the working xml file and write it to the output file
selected. by the user.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-09"
__name__ = "add_xml_header"

import lxml.etree as etree
import os


def add_header(debug_dir, base_script_dir, xml_tag_num, output_file):

    working_xml_file = open(os.path.join(debug_dir, "working_xml_file.xml"),
                            "w+")

    # TODO Consider moving this dict or even the whole xml_tag issue to a
    #  separate lib function.
    xml_tag_dict = {
        "1": "plainheader.xml",
        "2": "teiheader.xml",
        "3": "tpresheader.xml",
        }

    try:
        file_name = xml_tag_dict[xml_tag_num]
        insert = open(os.path.join(base_script_dir, file_name), "r")
        insert_tags = insert.read()
        working_xml_file.seek(0)
        working_xml_file.write(insert_tags)

    except TypeError:
        pass

    final_xml_file = open(os.path.join(base_script_dir, output_file), "w")

    etree.parse(working_xml_file).write(final_xml_file, encoding="utf-8")
    working_xml_file.close()
    final_xml_file.close()
