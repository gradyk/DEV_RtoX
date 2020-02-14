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
Insert file table tag sets into appropriate place in the XML working file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-13"
__name__ = "Contents.Library.xml_file_tags"

import os
from lxml import etree as et


# TODO Consider what to do with this module as part of overall file table
#  resolution.
class XMLTagSets:

    def __init__(self, debug_dir, xml_tag_num):
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def file_tags(self):
        """
        Record a tag about the file table.
        """

        tag_insert = ("""
            \n
            \t\t\t\tp.normal = {}\n
            \n""")

        xml_tag_list = [
            ["1", tag_insert, "http://www.w3.org/1999/xml", None, "rendFormat"],
            ["2", tag_insert, "http://www.tei-c.org/ns/1.0", "tei",
             "rendition"],
            ["3", tag_insert, "http://kennethgrady.com/ns/1.0.0", "ts",
             "rendition"],
            ["4", tag_insert, "http://www.w3.org/1999/xml", None, "rendFormat"]
        ]

        xml_tags = xml_tag_list[int(self.xml_tag_num)][1]
        ns = xml_tag_list[int(self.xml_tag_num)][2]
        prefix = xml_tag_list[int(self.xml_tag_num)][3]
        xml_pattern_two = xml_tag_list[int(self.xml_tag_num)][4]

        return xml_tags, ns, prefix, xml_pattern_two

    def tags_to_db(self, xml_tags, xml_pattern_two, ns, prefix):

        rtf_tags_file = os.path.join(self.debug_dir, "rtf_tags.xml")
        tree = et.parse(rtf_tags_file)
        root = tree.getroot()
        namespace = "{%s}" % ns
        nsmapped = {prefix: ns}
        et.SubElement(root, namespace + xml_pattern_two,
                      nsmap=nsmapped, scheme="css").text = xml_tags

        with open(os.path.join(self.debug_dir, "rtf_tags.xml"), "wb") as file:
            file.write(et.tostring(root, pretty_print=True))
