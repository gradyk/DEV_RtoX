#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Each keyword "line" (which may consist of several lines in the RTF input
file) must be parsed to extract settings and text. """

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
    """ The line parser calls a function (or, in the case of the cs, footnote,
        and header keywords a beginning and closing function) to parse the
        settings and text for the keyword. """
    def __init__(self,
                 keyword_translation_stack: list,
                 working_input_file: str,
                 debug_dir: str,
                 tag_dict: dict) -> None:
        self.keyword_translation_stack = keyword_translation_stack
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        self.tag_dict = tag_dict

    def line_parse(self) -> None:
        tag_bag = []

        process_dict = {
            "par":          LineParseController.par_process,
            "pard":         LineParseController.pard_process,
            "sect":         LineParseController.sect_process,
            "sectd":        LineParseController.sectd_process,
            "header_beg":   LineParseController.header_beg_process,
            "header_end":   LineParseController.header_end_process,
            "footnote_beg": LineParseController.footnote_beg_process,
            "footnote_end": LineParseController.footnote_end_process
            }

        for element in self.keyword_translation_stack:
            keyword = element[1]
            line_number = element[2]
            if keyword == "cs_beg":
                tag_bag = LineParseController.cs_open_process(
                    self=LineParseController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file,
                        keyword_translation_stack=self.keyword_translation_stack,
                        tag_dict=self.tag_dict),
                    line_to_read=line_number)
            elif keyword == "cs_end":
                LineParseController.cs_close_process(
                    self=LineParseController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file,
                        keyword_translation_stack=self.keyword_translation_stack,
                        tag_dict=self.tag_dict),
                    tag_bag=tag_bag,
                    line_to_read=line_number)
            else:
                process_dict[keyword](
                    self=LineParseController(
                        debug_dir=self.debug_dir,
                        working_input_file=self.working_input_file,
                        tag_dict=self.tag_dict,
                        keyword_translation_stack=
                        self.keyword_translation_stack),
                    line_to_read=line_number)

    def cs_open_process(self, line_to_read: str) -> list:

        cs_line_dict, text = cs.cs_line_parse(
            line_to_read=line_to_read,
            working_input_file=self.working_input_file)

        cs.open_emphasis_tag_cleanup_start(tag_dict=self.tag_dict,
                                           debug_dir=self.debug_dir)

        tag_bag = cs.insert_opening_cs_tag(cs_line_dict=cs_line_dict, text=text,
                                           tag_dict=self.tag_dict,
                                           debug_dir=self.debug_dir,
                                           line_to_read=line_to_read)

        return tag_bag

    def cs_close_process(self, line_to_read: str, tag_bag: list) -> None:
        cs.insert_closing_cs_tags(debug_dir=self.debug_dir,
                                  tag_bag=tag_bag,
                                  tag_dict=self.tag_dict,
                                  line=line_to_read)

    def footnote_beg_process(self,  line_to_read: str) -> None:

        footnote.open_emphasis_tag_cleanup_start(debug_dir=self.debug_dir,
                                                 tag_dict=self.tag_dict)

        footnote.insert_opening_footnote_tag(debug_dir=self.debug_dir,
                                             tag_dict=self.tag_dict,
                                             line_to_read=line_to_read)

        footnote.update_tag_registry_start(debug_dir=self.debug_dir)

    def footnote_end_process(self, line_to_read: str) -> None:
        footnote.footnote_process_controller_end(
            debug_dir=self.debug_dir,
            tag_dict=self.tag_dict,
            line=line_to_read)

    def header_beg_process(self, line_to_read: str) -> None:

        header.open_emphasis_tag_cleanup_start(debug_dir=self.debug_dir,
                                               tag_dict=self.tag_dict)

        header.insert_opening_header_tag(debug_dir=self.debug_dir,
                                         tag_dict=self.tag_dict,
                                         line_to_read=line_to_read)

        header.update_tag_registry_start(debug_dir=self.debug_dir)

    def header_end_process(self, line_to_read: str) -> None:
        header.header_process_controller_end(
            debug_dir=self.debug_dir,
            tag_dict=self.tag_dict,
            line=line_to_read)

    def par_process(self, line_to_read: str) -> None:
        par.par_tag_process(debug_dir=self.debug_dir,
                            tag_dict=self.tag_dict,
                            line=line_to_read)

    def pard_process(self, line_to_read: str) -> None:
        pard.pard_tag_process(debug_dir=self.debug_dir,
                              tag_dict=self.tag_dict,
                              line=line_to_read)

    def sect_process(self, line_to_read: str) -> None:
        sect.sect_tag_process(debug_dir=self.debug_dir,
                              tag_dict=self.tag_dict,
                              line=line_to_read)

    def sectd_process(self, line_to_read: str) -> None:
        sectd.sectd_tag_process(debug_dir=self.debug_dir,
                                tag_dict=self.tag_dict,
                                line=line_to_read)
