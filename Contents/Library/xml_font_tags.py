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
Insert font table tag sets into appropriate places in XML working file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-21"
__name__ = "Contents.Library.xml_font_tags"

import os
from lxml import etree as et


# TODO Consider what to do with this module as part of overall font table
#  resolution.
class XMLTagSets:

    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str
                 ) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def xml_font_tags(self, fontnum, fontfamily):
        """
        Determine which font tag set to use based on user's preferences.
        """

        tag_insert = (f'\n\t#{fontnum}''{\n\tfont-style: normal;'
                      f'\n\tfont-family:'
                      f' {fontfamily};\n\tfont-size: '
                      f'12pt;\n\tfont-weight: normal;\n'
                      '\tfont-variant: normal;\n\t}\n)')

        xml_tags = [
            ["1", tag_insert, "http://www.w3.org/1999/xml", None, "rendition"],
            ["2", tag_insert, "http://www.tei-c.org/ns/1.0", "tei",
             "rendition"],
            ["3", tag_insert, "http://kennethgrady.com/ns/1.0.0", "ts",
             "revisionDesc"],
            ["4", tag_insert, "http://www.w3.org/1999/xml", None, "rendition"]
            ]

        xml_tag_set = xml_tags[int(self.xml_tag_num)][1]
        ns = xml_tags[int(self.xml_tag_num)][2]
        prefix = xml_tags[int(self.xml_tag_num)][3]
        xml_pattern_two = xml_tags[int(self.xml_tag_num)][4]

        return xml_tag_set, ns, prefix, xml_pattern_two

    def make_new_tags(self, xml_font_tags_vars):
        """
        xml_tag_set = ...vars[0], ns = ...vars[1], prefix = ...vars[2],
        xml_pattern_two = ...vars[3]
        """

        rtf_tags_file = os.path.join(self.debug_dir, "rtf_tags.xml")
        tree = et.parse(rtf_tags_file)
        root = tree.getroot()
        namespace = "{%s}" % xml_font_tags_vars[1]
        nsmapped = {xml_font_tags_vars[2]: xml_font_tags_vars[1]}
        et.SubElement(root, namespace + xml_font_tags_vars[3],
                      nsmap=nsmapped, scheme="css").text = xml_font_tags_vars[0]

        with open(os.path.join(self.debug_dir, "rtf_tags.xml"), "wb") as file:
            file.write(et.tostring(root, pretty_print=True))
