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
Iterates through each line of the RTF file (starting at the \\info line or
line 0). Records in a list (kw_list) every line starting with one of a
specified list of keywords (keyword, line number). Returns the list.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "doc_parser"

# From Standard library
import linecache
import re

# From local application
import cs
import footnote
import header
import xml_transition_tags
import line_parser
import Contents.Library.file_length


def doc_body(working_file: str, debug_dir: str, xml_tag_num: str) -> None:
    """

    """
    # Determine whether to start at the info line or line 0.
    from header_tables_dict import header_tables_dictionary as htd

    if "info" in htd.keys():
        line_to_read = htd["info"]
    else:
        line_to_read = 0

    # Check the number of lines in the working file.
    file_length = Contents.Library.file_length.working_file_length(
        working_file=working_file)

    kw_list = []
    cs_end_line = ""
    header_end_line = ""
    footnote_end_line = ""

    while line_to_read <= file_length:

        area_search = linecache.getline(working_file, line_to_read)
        cs_kw_beg = re.match(r"{\\cs", area_search, re.M)
        if cs_kw_beg:
            cs_end_line = cs.cs_bounds(working_file=working_file,
                                       line_to_read=line_to_read)
            cs_kw_end = True
        else:
            cs_kw_end = None
            pass

        par_kw = re.match(r"\\par\n", area_search, re.M)
        pard_kw = re.match(r"\\pard", area_search, re.M)
        sect_kw = re.match(r"\\sect\n", area_search, re.M)
        sectd_kw = re.match(r"\\sectd", area_search, re.M)
        header_kw_beg = re.match(r"{\\header", area_search, re.M)

        if header_kw_beg:
            header_end_line = header.header_bounds(working_file=working_file,
                                                   search_line=line_to_read)
            header_kw_end = True
        else:
            header_kw_end = None
            pass

        footnote_kw_beg = re.match(r"{\\footnote", area_search, re.M)

        if footnote_kw_beg:
            footnote_end_line = footnote.footnote_bounds(
                working_file=working_file,
                search_line=line_to_read)
            footnote_kw_end = True
        else:
            footnote_kw_end = None
            pass

        keywords = [(cs_kw_beg, "cs_beg", line_to_read),
                    (cs_kw_end, "cs_end", cs_end_line),
                    (par_kw, "par", line_to_read),
                    (pard_kw, "pard", line_to_read),
                    (sect_kw, "sect", line_to_read),
                    (sectd_kw, "sectd", line_to_read),
                    (header_kw_beg, "header_beg", line_to_read),
                    (header_kw_end, "header_end", header_end_line),
                    (footnote_kw_beg, "footnote_beg", line_to_read),
                    (footnote_kw_end, "footnote_end", footnote_end_line)
                    ]

        for kw, tagtype, line in keywords:
            if kw is not None:
                kw_list.append((tagtype, int(line)))
            else:
                pass

        line_to_read += 1

    linecache.clearcache()

    # Sorts kw_list in ascending order according to value.
    listlen = len(kw_list)
    for i in range(0, listlen):
        for j in range(0, listlen - i - 1):
            if kw_list[j][1] > kw_list[j + 1][1]:
                tempo = kw_list[j]
                kw_list[j] = kw_list[j + 1]
                kw_list[j + 1] = tempo

    # Insert transition tags in the working_xml_file based on the user's
    # tag style preference.
    xml_transition_tags.xml_transition_tags(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num,
            line="0")

    line_parser.Parser.line_parse(
        self=line_parser.Parser(kw_list=kw_list,
                                debug_dir=debug_dir,
                                xml_tag_num=xml_tag_num,
                                line_to_read=line_to_read,
                                working_file=working_file))
