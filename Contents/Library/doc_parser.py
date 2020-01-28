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
import keyword_end
import xml_transition_tags
import line_parser
import Contents.Library.file_length


def doc_body(working_file: str,
             debug_dir: str,
             xml_tag_num: str,
             styles_status_list: list
             ) -> list:

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

    while line_to_read <= file_length:

        area_search = linecache.getline(working_file, line_to_read)
        cs = re.match(r"{\\cs", area_search, re.M)
        par = re.match(r"\\par\n", area_search, re.M)
        pard = re.match(r"\\pard", area_search, re.M)
        sect = re.match(r"\\sect\n", area_search, re.M)
        sectd = re.match(r"\\sectd", area_search, re.M)
        heading_start = re.match(r"{\\header", area_search, re.M)

        if heading_start:
            heading_end = keyword_end.keyword_end(
                working_file=working_file,
                line_number=line_to_read)
        else:
            heading_end = None

        footnote_start = re.match(r"{\\footnote", area_search, re.M)

        if footnote_start:
            footnote_end = keyword_end.keyword_end(
                working_file=working_file,
                line_number=line_to_read)
        else:
            footnote_end = None

        # TODO Consider whether key and value should be switched.
        keywords = [(cs, "cs"),
                    (par, "par"),
                    (pard, "pard"),
                    (sect, "sect"),
                    (sectd, "sectd"),
                    (heading_start, "heading_beg"),
                    (heading_end, "heading_end"),
                    (footnote_start, "footnote_beg"),
                    (footnote_end, "footnote_end")
                    ]

        for kw, value in keywords:
            if kw:
                new = (value, line_to_read)
                kw_list.append(new)
            else:
                pass

        line_to_read += 1

    linecache.clearcache()

    # Insert transition tags in the working_xml_file based on the user's
    # tag style preference.
    xml_transition_tags.xml_transition_tags(
            debug_dir=debug_dir,
            xml_tag_num=xml_tag_num)

    body_line = line_parser.LineParser.body_line_prep(
        self=line_parser.LineParser(
            kw_list=kw_list,
            styles_status_list=styles_status_list,
            debug_dir=debug_dir,
            working_file=working_file,
            xml_tag_num=xml_tag_num))

    wo_body_line = line_parser.LineParser.wo_body_line_prep(
        self=line_parser.LineParser(
            kw_list=kw_list,
            styles_status_list=styles_status_list,
            debug_dir=debug_dir,
            working_file=working_file,
            xml_tag_num=xml_tag_num))

    line_parser.LineParser.line_parse(
        self=line_parser.LineParser(
            kw_list=kw_list,
            styles_status_list=styles_status_list,
            debug_dir=debug_dir,
            working_file=working_file,
            xml_tag_num=xml_tag_num),
        body_line=body_line,
        wo_body_line=wo_body_line)

    return kw_list
