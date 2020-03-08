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
Iterates through each line of the RTF file (starting at the \\info line or,
if there is no info table, at line 0). Records in a list
(keyword_linenumber_list) every line that starts with one of a specified list of
keywords (keyword, line number). Returns the list. This list is fed to the
line_parser module.
"""

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
import xml_transition_tags
import Contents.Library.file_length
from read_log_config import logger_mismatch


def choose_starting_line_number(debug_dir: str) -> str:
    """ Determine whether to start at the info line or line 0. """
    with open(os.path.join(debug_dir, "header_tables_dict.json")) as \
            header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)
    try:
        header_tables_dict.keys("info")
        line_to_get = header_tables_dict["info"]
        return line_to_get
    except TypeError:
        line_to_get = "0"
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


def search_for_cs_keyword(line_to_search: str):
    """ Search the line to search for the cs keyword. If present, find the
    beginning and end of the keyword. """
    try:
        cs_keyword_begin = re.match(r"{\\cs", line_to_search, re.M)
    except TypeError:
        cs_keyword_begin = None
    return cs_keyword_begin


def identify_cs_keyword_bounds(line_to_search: str, working_input_file: str):
    """ If the cs keyword is in the line to search, find the keyword
    beginning and end. """
    cs_end_line = cs.cs_bounds(working_file=working_input_file,
                               line_to_search=line_to_search)
    return cs_end_line


def search_for_par_keyword(line_to_search: str):
    """ Search the line to search for the par keyword, which marks the end of a
    paragraph. """
    par_keyword = re.match(r"\\par[\s]?(\\n)?", line_to_search, re.M)
    return par_keyword


def search_for_pard_keyword(line_to_search: str):
    """ Search the line to search for the pard keyword. It indicates how the
    following paragraph should be formatted. """
    pard_keyword = re.match(r"\\pard\\", line_to_search, re.M)
    return pard_keyword


def search_for_sect_keyword(line_to_search: str):
    """ Search the line to search for the sect keyword, which marks the end
    of a section. """
    sect_keyword = re.match(r"\\sect[\s]?(\\n)?", line_to_search, re.M)
    return sect_keyword


def search_for_sectd_keyword(line_to_search: str):
    """ Search the line to search for the pard keyword. It indicates how the
    following paragraph should be formatted. """
    sectd_keyword = re.match(r"\\sectd\\", line_to_search, re.M)
    return sectd_keyword


def search_for_header_keyword(line_to_search: str):
    """ Search the line to search for the header keyword. """
    try:
        header_keyword_begin = re.match(r"{\\header", line_to_search, re.M)
    except TypeError:
        header_keyword_begin = None
    return header_keyword_begin


def identify_header_keyword_bounds(line_to_search: str,
                                   working_input_file: str):
    """ If the header keyword is in the line to search, find the keyword
    beginning and end. """
    header_end_line = header.header_bounds(
        working_input_file=working_input_file,
        line_to_search=line_to_search)
    return header_end_line


def search_for_footnote_keyword(line_to_search: str):
    """ Search the line to search for the footnote keyword. """
    try:
        footnote_keyword_begin = re.match(r"{\\footnote", line_to_search, re.M)
    except TypeError:
        footnote_keyword_begin = None
    return footnote_keyword_begin


def identify_footnote_keyword_bounds(line_to_search: str,
                                     working_input_file: str):
    """ If the footnote keyword is in the line to search, find the beginning
    and end of the keyword. """
    footnote_end_line = footnote.footnote_bounds(
        working_input_file=working_input_file,
        line_to_search=line_to_search)
    return footnote_end_line


class GetKeywordsAndLinenumbers:
    """ Loop through each line in the working_input_file recording the keyword
        and line number for each line that starts with a keyword (note: this
        searches for a very limited number of RTF keywords). For three
        keywords (cs, header, footnote), the beginning and end of the keyword
        must be captured. """
    def __init__(self, working_input_file: str, line_to_get: str,
                 file_length: str, debug_dir: str):
        self.working_input_file = working_input_file
        self.line_to_get = line_to_get
        self.file_length = file_length
        self.line_to_search = identify_line_to_search(
            working_input_file=self.working_input_file,
            line_to_get=self.line_to_get)
        self.keyword_linenumber_list = []
        self.keyword_linenumber_list = os.path.join(
            debug_dir, "keyword_linenumber_list.json")

    def line_keyword_checker_processor(self):
        super().__init__()
        while self.line_to_get <= self.file_length:

            cs_keyword_begin, cs_keyword_end, cs_end_line = \
                GetKeywordsAndLinenumbers.cs_keyword_checker(self)
            par_keyword = GetKeywordsAndLinenumbers.par_keyword_checker(self)
            pard_keyword = GetKeywordsAndLinenumbers.pard_keyword_checker(self)
            sect_keyword = GetKeywordsAndLinenumbers.sect_keyword_checker(self)
            sectd_keyword = GetKeywordsAndLinenumbers.\
                sectd_keyword_checker(self)
            header_keyword_begin, header_keyword_end, header_end_line = \
                GetKeywordsAndLinenumbers.header_keyword_checker(self)
            footnote_keyword_begin, footnote_keyword_end, footnote_end_line = \
                GetKeywordsAndLinenumbers.footnote_keyword_checker(self)

            keyword_tag_translation_list = [
                (cs_keyword_begin, "cs_beg", self.line_to_get),
                (cs_keyword_end, "cs_end", cs_end_line),
                (par_keyword, "par", self.line_to_get),
                (pard_keyword, "pard", self.line_to_get),
                (sect_keyword, "sect", self.line_to_get),
                (sectd_keyword, "sectd", self.line_to_get),
                (header_keyword_begin, "header_beg", self.line_to_get),
                (header_keyword_end, "header_end", header_end_line),
                (footnote_keyword_begin, "footnote_beg", self.line_to_get),
                (footnote_keyword_end, "footnote_end", footnote_end_line)
                ]

            GetKeywordsAndLinenumbers.build_keyword_linenumber_list(
                self=self,
                keyword_tag_translation_list=keyword_tag_translation_list)

            self.line_to_get += 1

            self.line_to_search = identify_line_to_search(
                working_input_file=self.working_input_file,
                line_to_get=self.line_to_get)

    def build_keyword_linenumber_list(self, keyword_tag_translation_list: list):
        """ Create the keyword list (keyword_linenumber_list) based on the
        keyword and the line on which it starts or ends. """
        for keyword, tag_type, line_number in keyword_tag_translation_list:
            if keyword is not None:
                with open(self.keyword_linenumber_list, "r") as \
                        keyword_linenumber_list_pre:
                    keyword_linenumber_list = \
                        json.load(keyword_linenumber_list_pre)
                    keyword_linenumber_list.update((tag_type, int(line_number)))
            else:
                pass

    def cs_keyword_checker(self):
        cs_keyword_end = None
        cs_end_line = "0"
        cs_keyword_begin = search_for_cs_keyword(
            line_to_search=self.line_to_search)
        if cs_keyword_begin is not None:
            cs_keyword_end = True
            cs_end_line = identify_cs_keyword_bounds(
                line_to_search=self.line_to_search,
                working_input_file=self.working_input_file)
        return cs_keyword_begin, cs_keyword_end, cs_end_line

    def par_keyword_checker(self):
        par_keyword = search_for_par_keyword(line_to_search=self.line_to_search)
        return par_keyword

    def pard_keyword_checker(self):
        pard_keyword = search_for_pard_keyword(
            line_to_search=self.line_to_search)
        return pard_keyword

    def sect_keyword_checker(self):
        sect_keyword = search_for_sect_keyword(
            line_to_search=self.line_to_search)
        return sect_keyword

    def sectd_keyword_checker(self):
        sectd_keyword = search_for_sectd_keyword(
            line_to_search=self.line_to_search)
        return sectd_keyword

    def header_keyword_checker(self):
        header_keyword_end = None
        header_end_line = "0"
        header_keyword_begin = search_for_header_keyword(
            line_to_search=self.line_to_search)
        if header_keyword_begin is not None:
            header_keyword_end = True
            header_end_line = identify_header_keyword_bounds(
                line_to_search=self.line_to_search,
                working_input_file=self.working_input_file)
        return header_keyword_begin, header_keyword_end, header_end_line

    def footnote_keyword_checker(self):
        footnote_keyword_end = None
        footnote_end_line = "0"
        footnote_keyword_begin = search_for_footnote_keyword(
            line_to_search=self.line_to_search)
        if footnote_keyword_begin is not None:
            footnote_keyword_end = True
            footnote_end_line = identify_footnote_keyword_bounds(
                line_to_search=self.line_to_search,
                working_input_file=self.working_input_file)
        return footnote_keyword_begin, footnote_keyword_end, footnote_end_line


def identify_line_to_search(working_input_file: str, line_to_get: str):
    """ Get the working_input_file line to search for keywords. """
    line_to_search = linecache.getline(working_input_file, line_to_get)
    return line_to_search


def sort_keyword_linenumber_list(keyword_linenumber_list: list):
    """ Sort the keyword_linenumber_list in ascending order according to
    line number. """
    # TODO This may not work if list entries are in ().
    keyword_linenumber_list_length = len(keyword_linenumber_list)
    for i in range(0, keyword_linenumber_list_length):
        for j in range(0, keyword_linenumber_list_length - i - 1):
            if keyword_linenumber_list[j][1] > \
                    keyword_linenumber_list[j + 1][1]:
                tempo = keyword_linenumber_list[j]
                keyword_linenumber_list[j] = keyword_linenumber_list[j + 1]
                keyword_linenumber_list[j + 1] = tempo

    try:
        if logger_mismatch.isEnabledFor(logging.ERROR):
            msg = str(keyword_linenumber_list)
            logger_mismatch.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_mismatch.")


def insert_transition_tags(debug_dir: str, tag_dict: dict):
    """ Insert transition tags in the working_xml_file based on the user's
    tag style preference. """
    xml_transition_tags.xml_transition_tags(debug_dir=debug_dir,
                                            tag_dict=tag_dict)


def parse_each_keyword_line(keyword_linenumber_list: list,
                            debug_dir: str, working_input_file: str,
                            tag_dict: dict, line_to_read: str):
    """ Use the line parse function to interpret each controlwords in the
    keyword_linenumber_list and insert the appropriate XML tag(s) in the
    working_xml_file. """
    line_parser.LineParseController.line_parse(
        self=line_parser.LineParseController(
            keyword_linenumber_list=keyword_linenumber_list,
            debug_dir=debug_dir,
            tag_dict=tag_dict,
            line_to_read=line_to_read,
            working_input_file=working_input_file))
