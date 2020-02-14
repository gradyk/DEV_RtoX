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
Insert style table tag sets into appropriate places in XML working file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-21"
__name__ = "Contents.Library.xml_style_tags"

import os
from lxml import etree as et


# TODO Consider what to do with this module as part of overall style table
#  resolution.
class XMLTagSets:

    def __init__(self,
                 debug_dir: str,
                 code: str,
                 set_styles_vars: list) -> None:
        self.debug_dir = debug_dir
        self.code = code
        self.set_styles_vars = set_styles_vars

    def xml_style_tags(self):

        # These assignments were done to help readability.
        code = self.set_styles_vars[0]
        italic = self.set_styles_vars[1]
        bold = self.set_styles_vars[2]
        underline = self.set_styles_vars[3]
        strikethrough = self.set_styles_vars[4]
        small_caps = self.set_styles_vars[5]
        additive = self.set_styles_vars[6]
        style_name = self.set_styles_vars[7]
        style_next_paragraph = self.set_styles_vars[8]

        tag_insert = (f'n\t\t\t#{code}''{\n\t\t\t\titalic: 'f'{italic};\n'
                      f'\t\t\t\tbold: {bold};\n\t\t\t\tunderline: '
                      f'{underline};\n\t\t\t\tstrikethrough: '
                      f'{strikethrough}\n\t\t\t\tsmall_caps: {small_caps};\n'
                      f'\t\t\t\t\tadditive: {additive};\n\t\t\t\tstyle_name:'
                      f' {style_name}\n'
                      f'\t\t\t\tstyle_next_paragraph: '
                      f'{style_next_paragraph};''\n\t\t\t}\n'
                      )

        xml_tags = [
            ["1", tag_insert, "http://www.w3.org/1999/xml", None, "p",
                "rendition"],
            ["2", tag_insert, "http://www.tei-c.org/ns/1.0", "tei", "p",
                "rendition"],
            ["3", tag_insert, "http://kennethgrady.com/ns/1.0.0", "ts",
                "revisionDesc", "rendFormat"],
            ["4", tag_insert, "http://www.w3.org/1999/xml", None, "p",
                "rendition"]
            ]

        return xml_tags

    def make_new_tags(self, xml_tags, xml_pattern_two, ns, prefix):

        rtf_tags_file = os.path.join(self.debug_dir, "rtf_tags.xml")
        tree = et.parse(rtf_tags_file)
        root = tree.getroot()
        namespace = "{%s}" % ns
        nsmapped = {prefix: ns}
        et.SubElement(root, namespace + xml_pattern_two,
                      nsmap=nsmapped, scheme="css").text = xml_tags

        with open(os.path.join(self.debug_dir, "rtf_tags.xml"), "wb") as file:
            file.write(et.tostring(root, pretty_print=True))
