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
__date__ = "2020-01-08"
__name__ = "line_parser"

# From local application.
import rtox.lib.cs
import rtox.lib.par
import rtox.lib.pard
import rtox.lib.sect
import rtox.lib.sectd
import rtox.lib.footnote_end
import rtox.lib.footnote_start
import rtox.lib.heading_end
import rtox.lib.heading_start


class LineParser:

    def __init__(self,
                 kw_list: list,
                 working_file: str,
                 xml_tag_num: str,
                 debug_dir: str,
                 styles_status_list: list
                 ) -> None:
        self.kw_list = kw_list
        self.working_file = working_file
        self.xml_tag_num = xml_tag_num
        self.debug_dir = debug_dir
        self.styles_status_list = styles_status_list

    def body_line_prep(self):
        body_line = DocLine(working_file=self.working_file,
                            xml_tag_num=self.xml_tag_num,
                            debug_dir=self.debug_dir,
                            styles_status_list=self.styles_status_list)

        return body_line

    def wo_body_line_prep(self):
        wo_body_line = WODocLine(debug_dir=self.debug_dir,
                                 xml_tag_num=self.xml_tag_num)

        return wo_body_line

    def line_parse(self, body_line, wo_body_line):
        options_dict_body_line = {
            "cs": body_line.cs_process,
        }

        options_dict_wo_body_line = {
            "par": wo_body_line.par_process,
            "pard": wo_body_line.pard_process,
            "sect": wo_body_line.sect_process,
            "sectd": wo_body_line.sectd_process,
            "heading_beg": wo_body_line.heading_start_process,
            "heading_end": wo_body_line.heading_end_process,
            "footnote_beg": wo_body_line.footnote_start_process,
            "footnote_end": wo_body_line.footnote_end_process
        }

        for a, b in self.kw_list:
            try:
                to_do = options_dict_body_line[a]
                to_do(b)
            except KeyError:
                to_do = options_dict_wo_body_line[a]
                to_do()


class DocLine:
    def __init__(self,
                 working_file: str,
                 styles_status_list: list,
                 xml_tag_num: str,
                 debug_dir: str) -> None:
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.xml_tag_num = xml_tag_num
        self.styles_status_list = styles_status_list

    def cs_process(self, line_to_read):
        text_line = rtox.lib.cs.cs_line_boundaries(
            working_file=self.working_file,
            line_to_read=line_to_read)

        line_parse_vars = rtox.lib.cs.cs_line_parse(text_line=text_line)
        cs_line_dict = line_parse_vars[0]
        text = line_parse_vars[1]
        rtox.lib.cs.cs_tag_write(cs_line_dict=cs_line_dict,
                                 text=text,
                                 xml_tag_num=self.xml_tag_num,
                                 debug_dir=self.debug_dir)


class WODocLine:
    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def par_process(self):
        rtox.lib.par.tag_insert(
            debug_dir=self.debug_dir,
            xml_tag_num=self.xml_tag_num)

    def pard_process(self):
        rtox.lib.pard.tag_insert(xml_tag_num=self.xml_tag_num,
                                 debug_dir=self.debug_dir)

    def sect_process(self):
        rtox.lib.sect.tag_insert(debug_dir=self.debug_dir,
                                 xml_tag_num=self.xml_tag_num)

    def sectd_process(self):
        rtox.lib.sectd.sectd(debug_dir=self.debug_dir,
                             xml_tag_num=self.xml_tag_num)

    def heading_start_process(self):
        rtox.lib.heading_start.HeadingBlock.heading_start(
            self=rtox.lib.heading_start.HeadingBlock(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))

    def heading_end_process(self):
        rtox.lib.heading_end.HeadingBlock.heading_end(
            self=rtox.lib.heading_end.HeadingBlock(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))

    def footnote_start_process(self):
        rtox.lib.footnote_start.FootnoteBlock.footnote_start(
            self=rtox.lib.footnote_start.FootnoteBlock(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))

    def footnote_end_process(self):
        rtox.lib.footnote_end.FootnoteBlock.footnote_end(
            self=rtox.lib.footnote_end.FootnoteBlock(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))
