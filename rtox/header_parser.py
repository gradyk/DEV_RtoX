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
This module controls parsing the document header. Evaluation results are
stored in the rtox_db, schema associated with the table.
1. Determine header structure.
2. Read and evaluate first line of rtf file.
3. Read and evaluate header font table codes.
4. Read and evaluate header file table codes. [TBD]
5. Read and evaluate header color table codes. [TBD]
6. Read and evaluate header style sheet table codes.
7. Read and evaluate header list table codes. [TBD]
8. Read and evaluate header revision table codes. [TBD]
9. Read and evaluate header rsid table codes. [TBD]
10. Read and evaluate header generator codes. [TBD]
 """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "header_parser"

import rtox.color_table
import rtox.file_table
import rtox.first_line
import rtox.font_table
import rtox.header_structure
import rtox.style_sheet_table


class DocHeaderParser:

    def __init__(self, base_script_dir, debug_dir, working_file, xml_tag_num):
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.base_script_dir = base_script_dir
        self.xml_tag_num = xml_tag_num

    def process_header(self):
        # Determine header structure of rtf input document.
        HeaderParse.header_structure(
            self=HeaderParse(debug_dir=self.debug_dir,
                             working_file=self.working_file,
                             base_script_dir=self.base_script_dir,
                             xml_tag_num=self.xml_tag_num))

        # Process first line of rtf input document.
        HeaderParse.rtf_first_line(
            self=HeaderParse(debug_dir=self.debug_dir,
                             working_file=self.working_file,
                             base_script_dir=self.base_script_dir,
                             xml_tag_num=self.xml_tag_num))

        # Process font table rtf codes.
        HeaderParse.font_table(
            self=HeaderParse(debug_dir=self.debug_dir,
                             working_file=self.working_file,
                             base_script_dir=self.base_script_dir,
                             xml_tag_num=self.xml_tag_num))

        # Process file table rtf codes.
        HeaderParse.file_table(
            self=HeaderParse(debug_dir=self.debug_dir,
                             working_file=self.working_file,
                             base_script_dir=self.base_script_dir,
                             xml_tag_num=self.xml_tag_num))

        # Process color table rtf codes.
        HeaderParse.color_table(
            self=HeaderParse(debug_dir=self.debug_dir,
                             working_file=self.working_file,
                             base_script_dir=self.base_script_dir,
                             xml_tag_num=self.xml_tag_num))

        # Process style sheet table rtf codes.
        HeaderParse.style_sheet_table()

        # HeaderParse.list_table(
        #   xml_tag_num=xml_tag_num_pass)

        # HeaderParse.rev_table(
        #   xml_tag_num=xml_tag_num_pass)

        # HeaderParse.rsid_table(
        #   xml_tag_num=xml_tag_num_pass)

        # HeaderParse.generator(
        #   xml_tag_num=xml_tag_num_pass)


class HeaderParse:

    def __init__(self, debug_dir, working_file, base_script_dir, xml_tag_num):
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.base_script_dir = base_script_dir
        self.xml_tag_num = xml_tag_num

    def header_structure(self):
        """
        Determine what tables are in the RTF header and store the table name
        and its line location in a dictionary.
        """
        rtox.header_structure.HeaderStructure.table_check(
            rtox.header_structure.HeaderStructure(
                working_file=self.working_file,
                debug_dir=self.debug_dir))

    def rtf_first_line(self):
        """
        Process the first line of the RTF file.
        """
        rtox.first_line.FirstLine.line_parse(
            rtox.first_line.FirstLine(
                debug_dir=self.debug_dir,
                working_file=self.working_file,
                base_script_dir=self.base_script_dir))

    def font_table(self):
        """
        If there is a font table, process the font settings for each font
        number and store them in the rtox_db database, fontcodes schema.
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "fonttbl" in htd.keys():
            table_state = 0
        else:
            table_state = 1

        line_to_check = htd['fonttbl'] + 1

        while table_state == 0:

            table_state = rtox.font_table.FonttblParse.find_fonts(
                self=rtox.font_table.FonttblParse(
                    working_file=self.working_file,
                    line_to_read=line_to_check,
                    debug_dir=self.debug_dir,
                    table_state=table_state,
                    xml_tag_num=self.xml_tag_num))

    def file_table(self):
        """
        If a file table exists in RTF file, add appropriate tags to XML file.
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "filetbl" in htd.keys():

            line_to_read = htd['filetbl'] + 1

            file_table_vars = rtox.file_table.FiletblParse.file_table(
                rtox.file_table.FiletblParse(
                    line_to_read=line_to_read,
                    debug_dir=self.debug_dir),
                xml_tag_num=self.xml_tag_num)
            line_to_check = file_table_vars

            return line_to_check

        else:
            pass

    def color_table(self):
        """
        If a color table exists in RTF file, add appropriate tags to XML file.
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "colortbl" in htd.keys():

            line_to_check = htd['colortbl'] + 1

            color_table_vars = rtox.color_table.ColortblParse.color_table(
                rtox.color_table.ColortblParse(
                    working_file=self.working_file,
                    line_to_check=line_to_check,
                    debug_dir=self.debug_dir),
                xml_tag_num=self.xml_tag_num)
            line_to_check = color_table_vars

            return line_to_check

        else:
            pass

    @staticmethod
    def style_sheet_table():
        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "stylesheet" in htd.keys():
            line_to_check = htd['stylesheet'] + 1

            rtox.style_sheet_table. \
                StyleSheetParse(line_num_pass=line_to_check)
