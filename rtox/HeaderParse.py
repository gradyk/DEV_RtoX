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
import rtox.header_start
import rtox.font_table
import rtox.dictionaries.xml_tags
import sys
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
        with open(os.path.join(self.__debug_file_dir,
                               "working_xml_file.data"), "w+") as \
                working_xml_file:
            working_xml_file.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                                   '<ts:TPRES>\n'
                                   '\t<ts:tpresHeader>\n')

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
        if line_to_read[0] is "{":
            hdr_line_count += 1
            return hdr_line_count, font_table

        elif line_to_read[0] is "}":
            hdr_line_count += 1
            font_table = 0
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
        :return:
        """
        if logger.isEnabledFor(level=10):
            logger.info(msg="header line count  = " + str(hdr_line_count) + "\n"
                        "font table = " + str(font_table) + "\n")

        config_dict = os.path.join(debug_dir, "config_dict.py")
        with open(config_dict) as file:
            font_codes_list = file.readlines()
        # if debugdir.config_dict.config_dict.get("tag-style") == "1":
        #     from rtox.dictionaries.xml_tags import xml_tags_dict as td
        #
        # elif debugdir.config_dict.config_dict.get("tag-style") == "2":
        #     from rtox.dictionaries.xml_tags import tei_tags_dict as td
        #
        # elif debugdir.config_dict.config_dict.get("tag-style") == "3":
        #     from rtox.dictionaries.xml_tags import tpres_tags_dict as td
        # else:
        #     from rtox.dictionaries.xml_tags import xml_tags_dict as td

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

        font_codes_list.append(f"fontnum: {fontnum}, fontfamily: "
                               f"{fontfamily}, fcharset: {fcharset}, fprq: "
                               f"{fprq}, panose: {panose}, name: "
                               f"{name}, altname: {altname}, fontemb: "
                               f"{fontemb}, fontfile: {fontfile}, "
                               f"cpg: {cpg}")

        with open(os.path.join(self.__debug_file_dir,
                               "config_dict.py"), "w+") as config_dict:
            config_dict.write(str(font_codes_list))

        if logger.isEnabledFor(level=10):
            msg = (f'header line = {hdr_line_count}'
                   f'fontnum = {fontnum}'
                   f"fontfamily = {fontfamily}"
                   f"fcharset = {fcharset}",
                   f"fprq = {fprq}",
                   f"panose = {panose}",
                   f"name = {name}",
                   f"altname = {altname}",
                   f"fontemb = {fontemb}",
                   f"fontfile = {fontfile}",
                   f"cpg = {cpg}")
            logger.info(msg)

        return self, hdr_line_count, font_table
