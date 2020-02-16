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
if there is no info table, at line 0). Record in a list
(keyword_linenumber_list) every line starting with one of a specified list of
keywords (keyword, line number). Return the list. This list is fed to the
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
# import sys

# From local application
import cs
import footnote
import header
import line_parser
from read_log_config import logger_mismatch
import xml_transition_tags
import Contents.Library.file_length


def doc_body(working_file: str, debug_dir: str, xml_tag_num: str) -> None:
    # Determine whether to start at the info line or line 0.
    with open(os.path.join(debug_dir, "header_tables_dict.json")) as \
            header_tables_dict_pre:
        header_tables_dict = json.load(header_tables_dict_pre)

    if "info" in header_tables_dict.keys():
        line_to_read = header_tables_dict["info"]
    else:
        line_to_read = 0

    # Determine the number of lines in the working_input_file.
    file_length = Contents.Library.file_length.working_file_length(
        working_file=working_file)

    keyword_linenumber_list = []
    cs_end_line = ""
    header_end_line = ""
    footnote_end_line = ""

    # Loop through each line in the working_input_file recording the keyword
    # and line number for each line that starts with a keyword (note: this
    # searches for a very limited number of RTF keywords). For three
    # keywords (cs, header, footnote), the beginning and end of the keyword must
    # be captured.
    while line_to_read <= file_length:

        area_search = linecache.getline(working_file, line_to_read)

        cs_keyword_begin = re.match(r"{\\cs", area_search, re.M)
        if cs_keyword_begin:
            cs_end_line = cs.cs_bounds(working_file=working_file,
                                       line_to_read=line_to_read)
            cs_keyword_end = True
        else:
            cs_keyword_end = None
            pass

        par_keyword = re.match(r"\\par\n", area_search, re.M)
        pard_keyword = re.match(r"\\pard", area_search, re.M)
        sect_keyword = re.match(r"\\sect\n", area_search, re.M)
        sectd_keyword = re.match(r"\\sectd", area_search, re.M)
        header_keyword_begin = re.match(r"{\\header", area_search, re.M)

        if header_keyword_begin:
            header_end_line = header.header_bounds(working_file=working_file,
                                                   search_line=line_to_read)
            header_keyword_end = True
        else:
            header_keyword_end = None
            pass

        footnote_keyword_begin = re.match(r"{\\footnote", area_search, re.M)

        if footnote_keyword_begin:
            footnote_end_line = footnote.footnote_bounds(
                working_file=working_file,
                search_line=line_to_read)
            footnote_keyword_end = True
        else:
            footnote_keyword_end = None
            pass

        # Create the keyword list (keyword_linenumber_list) based on the
        # keyword and the line on which it starts or ends.
        keyword_process_list = [
            (cs_keyword_begin, "cs_beg", line_to_read),
            (cs_keyword_end, "cs_end", cs_end_line),
            (par_keyword, "par", line_to_read),
            (pard_keyword, "pard", line_to_read),
            (sect_keyword, "sect", line_to_read),
            (sectd_keyword, "sectd", line_to_read),
            (header_keyword_begin, "header_beg", line_to_read),
            (header_keyword_end, "header_end", header_end_line),
            (footnote_keyword_begin, "footnote_beg", line_to_read),
            (footnote_keyword_end, "footnote_end", footnote_end_line)
            ]

        for keyword, tag_type, line_number in keyword_process_list:
            if keyword is not None:
                keyword_linenumber_list.append((tag_type, int(line_number)))
            else:
                pass

        line_to_read += 1

    linecache.clearcache()

    # Sort the keyword_linenumber_list in ascending order according to
    # line number.
    keyword_linenumber_list_length = len(keyword_linenumber_list)
    for i in range(0, keyword_linenumber_list_length):
        for j in range(0, keyword_linenumber_list_length - i - 1):
            if keyword_linenumber_list[j][1] > \
                    keyword_linenumber_list[j + 1][1]:
                tempo = keyword_linenumber_list[j]
                keyword_linenumber_list[j] = keyword_linenumber_list[j + 1]
                keyword_linenumber_list[j + 1] = tempo

    # TODO put a logger here that will write the keyword_linenumber_list to a
    #  file when the debug log level is set.
    try:
        if logger_mismatch.isEnabledFor(logging.ERROR):
            msg = str(keyword_linenumber_list)
            logger_mismatch.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_mismatch.")

    # TODO Should this be in a separate file? A separate def?
    # Insert transition tags in the working_xml_file based on the user's
    # tag style preference.
    xml_transition_tags.xml_transition_tags(debug_dir=debug_dir,
                                            xml_tag_num=xml_tag_num)

    # TODO Should RtoX call this?
    line_parser.Parser.line_parse(
        self=line_parser.Parser(keyword_linenumber_list=keyword_linenumber_list,
                                debug_dir=debug_dir,
                                xml_tag_num=xml_tag_num,
                                line_to_read=line_to_read,
                                working_file=working_file))
