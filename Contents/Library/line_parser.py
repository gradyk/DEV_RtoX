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


class LineParseController:
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
                 working_input_file: str,
                 debug_dir: str,
                 tag_dict: dict) -> None:
        self.keyword_linenumber_list = keyword_linenumber_list
        self.line_to_read = line_to_read
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.tag_dict = tag_dict

    def cs_open_process(self, line_to_read: str):

        cs_line_dict, text = cs.cs_line_parse(
            working_file=self.working_input_file,
            line_to_read=line_to_read)

        tag_bag = cs.cs_opening_tags(cs_line_dict=cs_line_dict,
                                     text=text,
                                     debug_dir=self.debug_dir,
                                     line=line_to_read,
                                     tag_dict=self.tag_dict)
        return tag_bag

    def cs_close_process(self, line_to_read: str, tag_bag: list):
        cs.cs_closing_tags(debug_dir=self.debug_dir,
                           tag_bag=tag_bag,
                           tag_dict=self.tag_dict,
                           line=line_to_read)

    def footnote_beg_process(self,  line_to_read: str):
        footnote.footnote_start(debug_dir=self.debug_dir,
                                tag_dict=self.tag_dict,
                                line=line_to_read)

    def footnote_end_process(self, line_to_read: str):
        footnote.footnote_end(debug_dir=self.debug_dir,
                              tag_dict=self.tag_dict,
                              line=line_to_read)

    def header_beg_process(self, line_to_read: str):
        header.header_start(debug_dir=self.debug_dir,
                            tag_dict=self.tag_dict,
                            line=line_to_read)

    def header_end_process(self, line_to_read: str):
        header.header_end(debug_dir=self.debug_dir,
                          tag_dict=self.tag_dict,
                          line=line_to_read)

    def par_process(self, line_to_read: str):
        par.tag_insert(debug_dir=self.debug_dir,
                       tag_dict=self.tag_dict,
                       line=line_to_read)

    def pard_process(self, line_to_read: str):
        pard.tag_insert(debug_dir=self.debug_dir,
                        tag_dict=self.tag_dict,
                        line=line_to_read)

    def sect_process(self, line_to_read: str):
        sect.tag_insert(debug_dir=self.debug_dir,
                        tag_dict=self.tag_dict,
                        line=line_to_read)

    def sectd_process(self, line_to_read: str):
        sectd.tag_insert(debug_dir=self.debug_dir,
                         tag_dict=self.tag_dict,
                         line=line_to_read)

    def line_parse(self):
        tag_bag = []
        tag_dict = {}

        process_dict = {
            "par":          LineParseController.par_process,
            "pard":         LineParseController.pard_process,
            "sect":         LineParseController.sect_process,
            "sectd":        LineParseController.sectd_process,
            "header_beg":   LineParseController.header_beg_process,
            "header_end":   LineParseController.header_end_process,
            "footnote_beg": LineParseController.footnote_beg_process,
            "footnote_end": LineParseController.footnote_end_process,
            }

        for element in self.keyword_linenumber_list:
            keyword = element[0]
            line_number = element[1]
            if keyword == "cs_beg":
                tag_bag = LineParseController.cs_open_process(
                    self=LineParseController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file,
                        keyword_linenumber_list=self.keyword_linenumber_list,
                        line_to_read=self.line_to_read,
                        tag_dict=tag_dict),
                    line_to_read=line_number)
            elif keyword == "cs_end":
                LineParseController.cs_close_process(
                    self=LineParseController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file,
                        keyword_linenumber_list=self.keyword_linenumber_list,
                        line_to_read=self.line_to_read,
                        tag_dict=tag_dict),
                    tag_bag=tag_bag,
                    line_to_read=line_number)
            else:
                process_dict[keyword](line_to_read=line_number)
