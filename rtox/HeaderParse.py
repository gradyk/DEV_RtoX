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
This module is the control center for parsing the RTF document.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "HeaderParse"

import linecache
import os
import sys
import rtox.header_start
import rtox.font_table
import rtox.color_table
import rtox.style_sheet_table
import rtox.dictionaries.xml_tags
from log_config import logger


class HeaderParse:

    def __init__(
                 self,
                 input_file_name,
                 debug_file_dir,
                 base_script_dir
                ):
        self.__input_file = input_file_name
        self.__debug_file_dir = debug_file_dir
        self.__base_script_dir = base_script_dir

    def input_file_prep(self, debug_file_dir):
        """
        Copy the input_file to a working file called
        "working_input_file.data" in the debug directory. Check input file is
        1) ASCII encoded, 2) starts with {\rtf, and 3) uses ANSI code page
        1252 character set.
        """

        # Copy input file to working_input_file.data in debugdir and give
        # it the variable name working_rtf_file.
        with open(os.path.join(self.__base_script_dir, self.__input_file)) as \
                input_file_copy:
            read_file = input_file_copy.read()

        working_rtf_file = os.path.join(self.__debug_file_dir,
                                        "working_input_file.data")

        with open(working_rtf_file, "w+") as write_file_object:
            write_file_object.write(read_file)

        # Open the file in which the XML tags and text will be
        # added as the conversion progresses. Add first line to file. Assign
        # tagging dictionary to td based on user configuration.
        # TODO The xml tags should vary depending on user tag preference.
        with open(os.path.join(self.__debug_file_dir,
                               "working_xml_file.data"), "w+") as \
                working_xml_file:
            xml_header = open(os.path.join(self.__base_script_dir,
                                           "tpresheader.xml"), "r")
            xml_header_tags = xml_header.read()
            working_xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                                   '<ts:TPRES>\n'
                                   '\t<ts:tpresHeader>\n'
                                   f'{xml_header_tags}\n')

        # Check ASCII, {\rtf, and ANSI.
        code_vars = rtox.header_start.check_file_rtf(
            working_rtf_file=working_rtf_file,
            debug_file_dir=debug_file_dir)

        hdr_line_count = code_vars[1] + 1
        return self, hdr_line_count

    @staticmethod
    def font_table(hdr_line_count, working_rtf_file):
        """
        Call method to check for font table existence.
        :param hdr_line_count: line to reade
        :param working_rtf_file: copy of input file
        :return:
        """
        font_vars = rtox.font_table.FonttblParse.font_table_exist(
            working_rtf_file=working_rtf_file,
            hdr_line_count=hdr_line_count)
        font_table = font_vars[0]
        hdr_line_count = font_vars[1]

        return hdr_line_count, working_rtf_file, font_table

    @staticmethod
    def font_table_end(working_rtf_file, hdr_line_count, font_table):
        """
        Check to see if there is a line of font code or if the end of the
        font table has been reached.
        :param working_rtf_file: copy of input file
        :param hdr_line_count: line to read in the file
        :param font_table: 1 = font table exists, 0 = no font table
        :return: hdr_line_count and font_table
        """
        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)
        if line_to_read[0] is "}":
            font_table = 0
            return hdr_line_count, font_table

        elif line_to_read[0] is "{":
            return hdr_line_count, font_table

        else:
            logger.debug(msg=f"There seems to be an error in the RTF "
                             f"formatting at working_rtf_file line "
                             f"{hdr_line_count} : {line_to_read}. The program "
                             f"will now quit.")
            sys.exit(1)

    def build_font_dict(self, working_rtf_file, hdr_line_count, font_table,
                        debug_dir):
        """
        Build font codes for each font number in input file.
        :param working_rtf_file: copy of input file
        :param hdr_line_count: line to read
        :param font_table: 1 = font table exists, 0 = no font table
        :param debug_dir: directory for working files
        :return:
        """
        if logger.isEnabledFor(level=10):
            logger.info(msg=f"header line count = {hdr_line_count}\n"
                            f"font table = {font_table}\n")

        config_dict = os.path.join(debug_dir, "config_dict.py")
        with open(config_dict) as file:
            font_codes_list = file.readlines()

        font_codes = rtox.font_table.FonttblParse.set_fonts(
            working_rtf_file=working_rtf_file,
            hdr_line_count=hdr_line_count,
            font_table=font_table)
        hdr_line_count = font_codes[0]
        fontnum = font_codes[1]
        fontfamily = font_codes[2]
        fcharset = font_codes[3]
        fprq = font_codes[4]
        panose = font_codes[5]
        name = font_codes[6]
        altname = font_codes[7]
        fontemb = font_codes[8]
        fontfile = font_codes[9]
        cpg = font_codes[10]
        font_table = font_codes[11]

        font_codes_list.append("{"
                               f"'fontnum': '{fontnum}', 'fontfamily': "
                               f"'{fontfamily}', 'fcharset': '{fcharset}',"
                               f" 'fprq': '{fprq}', 'panose': '{panose}', "
                               f"'name': '{name}', 'altname': '{altname}', "
                               f"'fontemb': '{fontemb}', 'fontfile': "
                               f"'{fontfile}', 'cpg': '{cpg}'"
                               "}")

        with open(os.path.join(self.__debug_file_dir,
                               "config_dict.py"), "w+") as config_dict:
            font_codes_list = str(font_codes_list).replace("[", "").replace(
                "]", "").replace("\\", "").replace("\"", "")
            config_dict.write(font_codes_list)

        if logger.isEnabledFor(level=10):
            msg = (f"header line = {hdr_line_count}, "
                   f"fontnum = {fontnum}, "
                   f"fontfamily = {fontfamily}, "
                   f"fcharset = {fcharset}, "
                   f"fprq = {fprq}, "
                   f"panose = {panose}, "
                   f"name = {name}, "
                   f"altname = {altname}, "
                   f"fontemb = {fontemb}, "
                   f"fontfile = {fontfile}, "
                   f"cpg = {cpg}")
            logger.info(msg)

        hdr_line_count += 1

        return self, hdr_line_count, font_table

    @staticmethod
    def color_table(working_rtf_file, hdr_line_count):
        """
        Check for color table.
        :return:
        """
        color_vars = rtox.color_table.ColortblParse.color_table_exist(
            working_rtf_file=working_rtf_file,
            hdr_line_count=hdr_line_count)
        hdr_line_count = color_vars

        return hdr_line_count

    @staticmethod
    def style_sheet(working_rtf_file, hdr_line_count):
        """
        Check for stylesheet(s).
        :param working_rtf_file:
        :param hdr_line_count:
        :return:
        """
        rtf_line_to_read = ""
        match_symbol = ""
        style_sheet_vars = rtox.style_sheet_table.StyleSheetParse.\
            style_sheet_exist(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                self=rtox.style_sheet_table.StyleSheetParse(
                    rtf_line_to_read=rtf_line_to_read,
                    match_symbol=match_symbol))
        style_sheet = style_sheet_vars[0]
        hdr_line_count = style_sheet_vars[1]

        return style_sheet, hdr_line_count

    def build_style_sheet_dict(self, working_rtf_file, hdr_line_count,
                               style_sheet, debug_dir, rtf_line_to_read,
                               match_symbol):
        """
        Proceed to capture codes for each stylesheet in a file.
        :param working_rtf_file:
        :param hdr_line_count:
        :param style_sheet:
        :param debug_dir:
        :param rtf_line_to_read:
        :param match_symbol
        :return:
        """

        if logger.isEnabledFor(level=10):
            logger.info(msg=f"header line count = {hdr_line_count}\n"
                            f"stylesheet = {style_sheet}\n")

        config_dict = os.path.join(debug_dir, "config_dict.py")
        with open(config_dict) as file:
            style_codes_list = file.readlines()

        style_codes = \
            rtox.style_sheet_table.StyleSheetParse.set_styles(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                style_sheet=style_sheet,
                self=rtox.style_sheet_table.StyleSheetParse(
                    rtf_line_to_read=rtf_line_to_read,
                    match_symbol=match_symbol,))
        hdr_line_count = style_codes[0]
        para_style = style_codes[1]
        char_style = style_codes[2]
        sec_style = style_codes[3]
        table_style = style_codes[4]
        table_row_style = style_codes[5]
        additive = style_codes[6]
        para_next_style = style_codes[7]
        style_name = style_codes[8]
        italic = style_codes[9]
        bold = style_codes[10]
        underline = style_codes[11]
        small_caps = style_codes[12]
        strikethrough = style_codes[13]

        style_codes_list.append("{"
                                f"'para_style': '{para_style}, 'char_style': "
                                f"'{char_style}', 'sec_style': '{sec_style}', "
                                f"'table_style': '{table_style}', "
                                f"'table_row_style': '{table_row_style}, "
                                f"'additive': '{additive}, 'para_next_style': "
                                f"'{para_next_style}, 'style_name': '"
                                f"'{style_name}', 'italic': '{italic}', "
                                f"'bold': '{bold}', 'underline': '"
                                f"{underline}', 'small_caps': '{small_caps}', "
                                f"'strikethrough': '{strikethrough}'"
                                "}")

        with open(os.path.join(self.__debug_file_dir,
                               "config_dict.py"), "w+") as config_dict:
            font_codes_list = str(style_codes_list).replace("[", "").replace(
                "]", "").replace("\\", "").replace("\"", "")
            config_dict.write(font_codes_list)

        if logger.isEnabledFor(level=10):
            msg = (f"para_style: {para_style}, "
                   f"char_style: {char_style}, "
                   f"sec_style: {sec_style}, "
                   f"table_style: {table_style}, "
                   f"table_row_style: {table_row_style}, "
                   f"additive: {additive}, "
                   f"para_next_style: {para_next_style}, "
                   f"style_name: '{style_name}, "
                   f"italic: {italic}, "
                   f"bold: {bold}, "
                   f"underline: {underline}, "
                   f"small_caps: {small_caps}, "
                   f"strikethrough: {strikethrough}")
            logger.info(msg)

        hdr_line_count += 1

        return self, hdr_line_count, style_sheet
