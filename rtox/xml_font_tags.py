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
__name__ = "xml_font_tags"

import os
from lxml import etree as Et


class XMLTagSets:

    def __init__(
                 self,
                 debug_dir,
                 xml_tag_num,
                 fontnum,
                 fontfamily
                 ):
        self.__debug_dir = debug_dir
        self.__xml_tag_num = xml_tag_num
        self.__fontnum = fontnum
        self.__fontfamily = fontfamily

    def xml_font_tags(self):
        """

        :return:
        """

        if self.__xml_tag_num == "1":
            xml_tag_set = (
                f'\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{self.__fontfamily}";\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "p"
            xml_pattern_two = "rendition"

        elif self.__xml_tag_num == "2":
            xml_tag_set = (
                f'\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{self.__fontfamily}";\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}\n'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "tei:p"
            xml_pattern_two = "rendition"

        elif self.__xml_tag_num == "3":
            xml_tag_set = (
                f'\n\t\t\t\t\t#{self.__fontnum}'
                ' {\n'
                f'\t\t\t\t\t\tfont-style: normal;\n'
                f'\t\t\t\t\t\tfontfamily: "{self.__fontfamily};"\n'
                f'\t\t\t\t\t\tfont-size: 12pt;\n'
                f'\t\t\t\t\t\tfont-weight: normal;\n'
                f'\t\t\t\t\t\tfont-variant: normal;\n'
                '\t\t\t\t\t}\n'
            )
            xml_pattern = "ts:pPrebody"
            xml_pattern_two = "rendFormat"

        else:
            xml_tag_set = (
                f'\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{self.__fontfamily}";\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "p"
            xml_pattern_two = "rendition"

        file = open(os.path.join(self.__debug_dir,
                                 "working_xml_file.xml"), "r", encoding="UTF-8")
        file_too = file.read()

        tree = Et.XML(file_too)

        for xml_pattern in tree.xpath(
                'ts:tpresHeader/ts:encodingDesc/ts:tagsDecl/ts:pPrebody[1]',
                namespaces={"ts": "http://kennethgrady.com/ns/1.0.0"}):
            parent = xml_pattern.getparent()

            ns = "{http://kennethgrady.com/ns/1.0.0}"
            new_tag = Et.SubElement(parent, ns + xml_pattern_two, scheme="css")
            new_tag.text = xml_tag_set

            parent.insert(parent.index(xml_pattern), new_tag)

        with open(os.path.join(self.__debug_dir, "working_xml_file.xml"),
                  "wb") as xfile_two:

            xfile_two.write(Et.tostring(tree, pretty_print=True))
