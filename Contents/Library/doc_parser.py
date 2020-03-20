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

""" Iterates through each line of the RTF file (starting at the \\info line or,
if there is no info table, at line 0). Records in a list
(keyword_translation_stack) every line that starts with one of a specified
list of keywords (keyword, line number). Returns the list. This list is fed
to the line_parser module. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.doc_parser"

# From standard libraries
import json
import linecache
import logging
import os
import re

# From local application
import cs
import footnote
import header
import line_parser
import tag_style
import Contents.Library.file_length
from read_log_config import logger_mismatch


def choose_starting_line_number(debug_dir: str) -> int:
    """ Determine whether to start at the info line or line 0. """
    with open(os.path.join(debug_dir, "header_tables_dict.json")) as \
            header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)
    try:
        header_tables_dict.keys("info")
        line_to_get = header_tables_dict["info"]
        return line_to_get
    except TypeError:
        line_to_get = 1
    return line_to_get


def select_tag_dict(xml_tag_num: str):
    """ Determine tag dictionary based on user's preference. """
    tag_dict = tag_style.tag_dict_selection(xml_tag_num=xml_tag_num)
    return tag_dict


def find_length_working_input_file(working_input_file: str):
    """ Determine the number of lines in the working_input_file. """
    file_length = Contents.Library.file_length.working_input_file_length(
        working_input_file=working_input_file)
    return file_length


class GetKeywordsAndLinenumbers:
    """ Loop through each line in the working_input_file recording the keyword
        and line number for each line that starts with a keyword (note: this
        searches for a very limited number of RTF keywords). For three
        keywords (cs, header, footnote), the beginning and end of the keyword
        must be captured. """
    def __init__(self, working_input_file: str, line_to_get: int,
                 file_length: int):
        self.working_input_file = working_input_file
        self.line_to_get = line_to_get
        self.file_length = file_length
        self.line_to_search = self.line_to_get
        self.keyword_translation_stack = []

    def line_keyword_checker_processor(self):
        super().__init__()
        while self.line_to_get <= self.file_length:

            GetKeywordsAndLinenumbers.cs_keyword_checker(self)
            GetKeywordsAndLinenumbers.par_keyword_checker(self)
            GetKeywordsAndLinenumbers.pard_keyword_checker(self)
            GetKeywordsAndLinenumbers.sect_keyword_checker(self)
            GetKeywordsAndLinenumbers.sectd_keyword_checker(self)
            GetKeywordsAndLinenumbers.header_keyword_checker(self)
            GetKeywordsAndLinenumbers.footnote_keyword_checker(self)
            self.keyword_translation_stack = GetKeywordsAndLinenumbers.\
                retrieve_keyword_translation_stack(self)

            self.line_to_get += 1

            self.line_to_search = self.line_to_get

        return self.keyword_translation_stack, self.line_to_search

    def cs_keyword_checker(self) -> None:
        try:
            search_text = linecache.getline(self.working_input_file,
                                            self.line_to_search)
            cs_keyword_begin = re.match(r"{\\cs", search_text, re.M)
        except TypeError:
            cs_keyword_begin = None

        if cs_keyword_begin is not None:
            cs_end_line = cs.determine_cs_bounds(
                working_input_file=self.working_input_file,
                line_to_search=self.line_to_search)
            self.keyword_translation_stack.append(
                (True, "cs_beg", self.line_to_get))
            self.keyword_translation_stack.append(
                (True, "cs_end", cs_end_line))
        else:
            pass

    def par_keyword_checker(self) -> None:
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        par_keyword = re.match(r"\\par[\s]?(\\n)?", search_text, re.M)
        if par_keyword is not None:
            self.keyword_translation_stack.append(
                (True, "par", self.line_to_get))
        else:
            pass

    def pard_keyword_checker(self) -> None:
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        pard_keyword = re.match(r"\\pard\\", search_text, re.M)
        if pard_keyword is not None:
            self.keyword_translation_stack.append(
                (True, "pard", self.line_to_get))
        else:
            pass

    def sect_keyword_checker(self) -> None:
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        sect_keyword = re.match(r"\\sect[\s]?(\\n)?", search_text, re.M)
        if sect_keyword is not None:
            self.keyword_translation_stack.append(
                (True, "sect", self.line_to_get))
        else:
            pass

    def sectd_keyword_checker(self) -> None:
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        sectd_keyword = re.match(r"\\sectd\\", search_text, re.M)
        if sectd_keyword is not None:
            self.keyword_translation_stack.append(
                (True, "sectd", self.line_to_get))
        else:
            pass

    def header_keyword_checker(self) -> None:
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        try:
            header_keyword_begin = re.match(r"{\\header", search_text,
                                            re.M)
        except TypeError:
            header_keyword_begin = None
        if header_keyword_begin is not None:
            header_end_line = header.determine_header_bounds(
                working_input_file=self.working_input_file,
                line_to_search=self.line_to_search)
            self.keyword_translation_stack.append(
                (True, "header_beg", self.line_to_get))
            self.keyword_translation_stack.append(
                (True, "header_end", header_end_line))

    def footnote_keyword_checker(self):
        search_text = linecache.getline(self.working_input_file,
                                        self.line_to_search)
        try:
            footnote_keyword_begin = re.match(r"{\\footnote", search_text,
                                              re.M)
        except TypeError:
            footnote_keyword_begin = None
        if footnote_keyword_begin is not None:
            footnote_end_line = footnote.determine_footnote_bounds(
                working_input_file=self.working_input_file,
                line_to_search=self.line_to_search)
            self.keyword_translation_stack.append(
                (True, "footnote_beg", self.line_to_get))
            self.keyword_translation_stack.append(
                (True, "footnote_end", footnote_end_line))

    def retrieve_keyword_translation_stack(self):
        return self. keyword_translation_stack


def sort_keyword_translation_stack(keyword_translation_stack: list):
    """ Sort the keyword_linenumber_list in ascending order according to
    line number. """
    # TODO Does this work if list entries are in ().
    keyword_translation_stack_length = len(keyword_translation_stack)
    for i in range(0, keyword_translation_stack_length):
        for j in range(0, keyword_translation_stack_length - i - 1):
            if keyword_translation_stack[j][2] > \
                    keyword_translation_stack[j + 1][2]:
                tempo = keyword_translation_stack[j]
                keyword_translation_stack[j] = keyword_translation_stack[j + 1]
                keyword_translation_stack[j + 1] = tempo
    try:
        print(str(keyword_translation_stack))
        logging.getLogger("Logger Mismatch")
        if logger_mismatch.isEnabledFor(logging.ERROR):
            logger_mismatch.error(str(keyword_translation_stack))
    except AttributeError:
        logging.exception("Check setLevel for logger_mismatch.")

    return keyword_translation_stack


def parse_each_keyword_line(keyword_translation_stack: list,
                            debug_dir: str, working_input_file: str,
                            tag_dict: dict):
    """ Use the line parse function to interpret each control word in the
    keyword_translation_stack and insert the appropriate XML tag(s) in the
    working_xml_file. """
    line_parser.LineParseController.line_parse(
        self=line_parser.LineParseController(
            keyword_translation_stack=keyword_translation_stack,
            debug_dir=debug_dir,
            tag_dict=tag_dict,
            working_input_file=working_input_file))
