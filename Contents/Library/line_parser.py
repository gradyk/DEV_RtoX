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
Each keyword "line" (which may consist of several lines in the RTF input
file) must be parsed to extract settings and text.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-08"
__name__ = "line_parser"

# From local application.
import cs
import header
import footnote
import par
import pard
import sect
import sectd


class Parser:
    # TODO Do pard and sectd need opening and closing functions and setting
    #  parsings?
    """
    The line parser calls a function (or, in the case of the cs, footnote,
    and header keywords a beginning and closing function) to parse the
    settings and text for the keyword.
    """
    def __init__(self,
                 keyword_linenumber_list: list,
                 line_to_read: str,
                 working_file: str,
                 debug_dir: str,
                 xml_tag_num: str) -> None:
        self.keyword_linenumber_list = keyword_linenumber_list
        self.line_to_read = line_to_read
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    @staticmethod
    def cs_open_process(working_file: str, line_to_read: str, xml_tag_num: str,
                        debug_dir: str):

        cs_line_dict, text = cs.cs_line_parse(
            working_file=working_file,
            line_to_read=line_to_read)

        tag_bag, tag_dict = cs.cs_opening_tags(cs_line_dict=cs_line_dict,
                                               text=text,
                                               xml_tag_num=xml_tag_num,
                                               debug_dir=debug_dir,
                                               line=line_to_read)
        return tag_bag, tag_dict

    @staticmethod
    def cs_close_process(debug_dir: str, tag_bag: list, tag_dict: str,
                         line_to_read: str):
        cs.cs_closing_tags(debug_dir=debug_dir, tag_bag=tag_bag,
                           tag_dict=tag_dict, line=line_to_read)

    @staticmethod
    def footnote_beg_process(debug_dir: str, xml_tag_num: str,
                             line_to_read: str):
        footnote.footnote_start(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                                line=line_to_read)

    @staticmethod
    def footnote_end_process(debug_dir: str, xml_tag_num: str,
                             line_to_read: str):
        footnote.footnote_end(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                              line=line_to_read)

    @staticmethod
    def header_beg_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        header.header_start(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                            line=line_to_read)

    @staticmethod
    def header_end_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        header.header_end(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                          line=line_to_read)

    @staticmethod
    def par_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        par.tag_insert(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                       line=line_to_read)

    @staticmethod
    def pard_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        pard.tag_insert(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                        line=line_to_read)

    @staticmethod
    def sect_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        sect.tag_insert(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                        line=line_to_read)

    @staticmethod
    def sectd_process(debug_dir: str, xml_tag_num: str, line_to_read: str):
        sectd.tag_insert(debug_dir=debug_dir, xml_tag_num=xml_tag_num,
                         line=line_to_read)

    def line_parse(self):
        tag_bag = []
        tag_dict = {}

        process_dict = {
            "par": Parser.par_process,
            "pard": Parser.pard_process,
            "sect": Parser.sect_process,
            "sectd": Parser.sectd_process,
            "header_beg": Parser.header_beg_process,
            "header_end": Parser.header_end_process,
            "footnote_beg": Parser.footnote_beg_process,
            "footnote_end": Parser.footnote_end_process,
            }

        for element in self.keyword_linenumber_list:
            keyword = element[0]
            line_number = element[1]
            if keyword == "cs_beg":
                tag_bag, tag_dict = Parser.cs_open_process(
                    line_to_read=line_number,
                    xml_tag_num=self.xml_tag_num,
                    debug_dir=self.debug_dir,
                    working_file=self.working_file)
            elif keyword == "cs_end":
                Parser.cs_close_process(debug_dir=self.debug_dir,
                                        tag_bag=tag_bag,
                                        tag_dict=tag_dict,
                                        line_to_read=line_number)
            else:
                process_dict[keyword](debug_dir=self.debug_dir,
                                      xml_tag_num=self.xml_tag_num,
                                      line_to_read=line_number)
