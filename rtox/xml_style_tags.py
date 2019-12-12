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
__name__ = "xml_style_tags"

import os
from lxml import etree as et


class XMLTagSets:

    def __init__(
                 self,
                 debug_dir,
                 xml_tag_num,
                 code,
                 additive,
                 para_next,
                 bold,
                 italic,
                 underline,
                 small_caps,
                 strikethrough,
                 style_name
                 ):
        self.__debug_dir = debug_dir
        self.__xml_tag_num = xml_tag_num
        self.__code = code
        self.__additive = additive
        self.__para_next = para_next
        self.__bold = bold
        self.__italic = italic
        self.__underline = underline
        self.__small_caps = small_caps
        self.__strikethrough = strikethrough
        self.__style_name = style_name

    def xml_style_tags(self):
        """
        Determine which font tag set to use based on user's preferences.
        """

        if self.__xml_tag_num == "1":
            tag_vars = XMLTagSets.plain_xml(
                self=XMLTagSets(
                    debug_dir=self.__debug_dir,
                    xml_tag_num=self.__xml_tag_num,
                    code=self.__code,
                    additive=self.__additive,
                    para_next=self.__para_next,
                    bold=self.__bold,
                    italic=self.__italic,
                    underline=self.__underline,
                    small_caps=self.__small_caps,
                    strikethrough=self.__strikethrough,
                    style_name=self.__style_name))
            xml_tag_set_pass = tag_vars[0]
            xml_pattern_pass = tag_vars[1]
            xml_pattern_two_pass = tag_vars[2]
            ns_pass = tag_vars[3]
            prefix_pass = tag_vars[4]

        elif self.__xml_tag_num == "2":
            tag_vars = XMLTagSets.tei_xml(
                self=XMLTagSets(
                    debug_dir=self.__debug_dir,
                    xml_tag_num=self.__xml_tag_num,
                    code=self.__code,
                    additive=self.__additive,
                    para_next=self.__para_next,
                    bold=self.__bold,
                    italic=self.__italic,
                    underline=self.__underline,
                    small_caps=self.__small_caps,
                    strikethrough=self.__strikethrough,
                    style_name=self.__style_name))
            xml_tag_set_pass = tag_vars[0]
            xml_pattern_pass = tag_vars[1]
            xml_pattern_two_pass = tag_vars[2]
            ns_pass = tag_vars[3]
            prefix_pass = tag_vars[4]

        elif self.__xml_tag_num == "3":
            tag_vars = XMLTagSets.tpres_xml(
                self=XMLTagSets(
                    debug_dir=self.__debug_dir,
                    xml_tag_num=self.__xml_tag_num,
                    code=self.__code,
                    additive=self.__additive,
                    para_next=self.__para_next,
                    bold=self.__bold,
                    italic=self.__italic,
                    underline=self.__underline,
                    small_caps=self.__small_caps,
                    strikethrough=self.__strikethrough,
                    style_name=self.__style_name))
            xml_tag_set_pass = tag_vars[0]
            xml_pattern_pass = tag_vars[1]
            xml_pattern_two_pass = tag_vars[2]
            ns_pass = tag_vars[3]
            prefix_pass = tag_vars[4]

        else:
            tag_vars = XMLTagSets.plain_xml(
                self=XMLTagSets(
                    debug_dir=self.__debug_dir,
                    xml_tag_num=self.__xml_tag_num,
                    code=self.__code,
                    additive=self.__additive,
                    para_next=self.__para_next,
                    bold=self.__bold,
                    italic=self.__italic,
                    underline=self.__underline,
                    small_caps=self.__small_caps,
                    strikethrough=self.__strikethrough,
                    style_name=self.__style_name))
            xml_tag_set_pass = tag_vars[0]
            xml_pattern_pass = tag_vars[1]
            xml_pattern_two_pass = tag_vars[2]
            ns_pass = tag_vars[3]
            prefix_pass = tag_vars[4]

        XMLTagSets.make_new_tags(
            self=XMLTagSets(
                debug_dir=self.__debug_dir,
                xml_tag_num=self.__xml_tag_num,
                code=self.__code,
                additive=self.__additive,
                para_next=self.__para_next,
                bold=self.__bold,
                italic=self.__italic,
                underline=self.__underline,
                small_caps=self.__small_caps,
                strikethrough=self.__strikethrough,
                style_name=self.__style_name),
            xml_tag_set=xml_tag_set_pass,
            xml_pattern_two=xml_pattern_two_pass,
            ns=ns_pass,
            prefix=prefix_pass)

    def plain_xml(self):
        """
        Tag set for plain xml.
        :return: xml_tag_set: tags to wrap font codes
        :return: xml_pattern:
        :return: xml_pattern_two:
        :return: ns: namespace
        """
        xml_tag_set = (
            f'\n\t\t\t#{self.__code}'
            ' {\n'
            f'\t\t\t\tadditive: {self.__additive};\n'
            f'\t\t\t\tpara_next: {self.__para_next};\n'
            f'\t\t\t\tbold: {self.__bold};\n'
            f'\t\t\t\titalic: {self.__italic};\n'
            f'\t\t\t\tunderline: {self.__underline};\n'
            f'\t\t\t\tsmall_caps: {self.__small_caps};\n'
            f'\t\t\t\tstrikethrough: {self.__strikethrough}\n'
            f'\t\t\t\tstyle_name: {self.__style_name}\n'
            '\t\t\t}'
            f'\n'
        )
        prefix = None
        ns = "http://www.w3.org/1999/xml"
        xml_pattern = "p"
        xml_pattern_two = "rendition"
        return xml_tag_set, xml_pattern, xml_pattern_two, ns, prefix

    def tei_xml(self):
        """
        Tag set for TEI. See plain_xml for returns.
        """
        xml_tag_set = (
            f'\n\t\t\t#{self.__code}'
            ' {\n'
            f'\t\t\t\tadditive: {self.__additive};\n'
            f'\t\t\t\tpara_next: {self.__para_next};\n'
            f'\t\t\t\tbold: {self.__bold};\n'
            f'\t\t\t\titalic: {self.__italic};\n'
            f'\t\t\t\tunderline: {self.__underline};\n'
            f'\t\t\t\tsmall_caps: {self.__small_caps};\n'
            f'\t\t\t\tstrikethrough: {self.__strikethrough}\n'
            f'\t\t\t\tstyle_name: {self.__style_name}\n'
            '\t\t\t}'
            f'\n'
        )
        prefix = "tei"
        ns = "http://www.tei-c.org/ns/1.0"
        xml_pattern = "p"
        xml_pattern_two = "rendition"
        return xml_tag_set, xml_pattern, xml_pattern_two, ns, prefix

    def tpres_xml(self):
        """
        Tag set for TPRES. See plain_xml for returns.
        """
        xml_tag_set = (
            f'\n\t\t\t#{self.__code}'
            ' {\n'
            f'\t\t\t\tadditive: {self.__additive};\n'
            f'\t\t\t\tpara_next: {self.__para_next};\n'
            f'\t\t\t\tbold: {self.__bold};\n'
            f'\t\t\t\titalic: {self.__italic};\n'
            f'\t\t\t\tunderline: {self.__underline};\n'
            f'\t\t\t\tsmall_caps: {self.__small_caps};\n'
            f'\t\t\t\tstrikethrough: {self.__strikethrough}\n'
            f'\t\t\t\tstyle_name: {self.__style_name}\n'
            '\t\t\t}'
            f'\n'
        )
        prefix = "ts"
        ns = "http://kennethgrady.com/ns/1.0.0"
        xml_pattern = "revisionDesc"
        xml_pattern_two = "rendFormat"
        return xml_tag_set, xml_pattern, xml_pattern_two, ns, prefix

    def make_new_tags(self, xml_tag_set, xml_pattern_two, ns, prefix):

        rtf_tags_file = os.path.join(self.__debug_dir, "rtf_tags.xml")
        tree = et.parse(rtf_tags_file)
        root = tree.getroot()
        namespace = "{%s}" % ns
        nsmapped = {prefix: ns}
        et.SubElement(root, namespace + xml_pattern_two,
                      nsmap=nsmapped, scheme="css").text = xml_tag_set

        with open(os.path.join(self.__debug_dir, "rtf_tags.xml"), "wb") as file:
            file.write(et.tostring(root, pretty_print=True))
