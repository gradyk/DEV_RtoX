#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
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
Parse the font table and create a dictionary of values.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "font_table"

import linecache
import os
import re


class FonttblParse:
    """
    Process Header font table settings.
    """

    def __init__(
                 self,
                ):
        self.__init__()

    @staticmethod
    def file_write(debug_file_dir, rtf_file_codes):
        """
        Write the RTF file codes to a list file.
        :param debug_file_dir: directory for list file
        :param rtf_file_codes: key/value code pairs
        :return: rtf file codes as a list
        """
        with open(os.path.join(debug_file_dir, "rtf_file_codes.data"),
                  "w+") as rtf_dict:
            rtf_dict.write(str(rtf_file_codes))
            rtf_dict.close()
        return rtf_file_codes

    # Check for font table. If yes, increment line count and move to function
    # to set fonts. If no, move to function to check for file table.
    @staticmethod
    def font_table_exist(working_rtf_file, hdr_line_count):
        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)

        match = re.search(r'{\\fonttbl', line_to_read)
        if match:
            font_table = 1
            hdr_line_count += 1
            return font_table, hdr_line_count
        else:
            font_table = 0
            return font_table, hdr_line_count

    @staticmethod
    def set_fonts(working_rtf_file, hdr_line_count, font_table):
        """
        For each font number (e.g., f0), capture the settings.
        :param working_rtf_file: copy of the input file
        :param hdr_line_count: current line in the working_rtf_file
        :param font_table: 0 = no font table, 1 = font table exists
        :return: hdr_line_count, fontnum, fontfamily, fcharset, fprq, panose, \
            name, altname, fontemb, fontfile, cpg, font_table
        """
        fontnum, fontfamily, fcharset, fprq, panose, name, altname, fontemb, \
            fontfile, cpg = "", "", "", "", "", "", "", "", "", ""
        families = ["fnil", "froman", "fswiss", "fmodern",
                    "fscript", "fdecor", "ftech", "fbidi"]
        c_sets = ["ansi", "mac", "pc", "pca"]

        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)

        match = re.search(r'f[0-9]+', line_to_read)
        if match:
            fontnum = match[0]
            for family in families:
                match = re.search(family, line_to_read)
                if match:
                    fontfamily = match[0]

        match = re.search(r'\\fcharset([0-9])+', line_to_read)
        if match:
            fcharset = match[0].replace("\\fcharset", "")

        match = re.search(r'\\fprq([0-9])+', line_to_read)
        if match:
            fprq = match[0].replace("\\fprq", "")

        match = re.search(re.compile(r'\\\*\\[0-9]+'), line_to_read)
        if match:
            panose = match[0].replace(match[0], "")

        match = re.search(r'(\s\w+)+(;)*', line_to_read)
        if match:
            name_pre = match.group(0).replace(";", "")
            name = name_pre.lstrip()

        match = re.search(re.compile(r'\\\*\\falt\s'), line_to_read)
        if match:
            altname = match[0].replace(match[0], "")

        match = re.search(r'{\\fontemb', line_to_read)
        if match:
            fontemb = "Yes"
        else:
            fontemb = "No"

        for c_set in c_sets:
            match = re.search(c_set+"cpg", line_to_read)
            if match:
                cpg = match.group(1).replace(match.group(1), "")

        return hdr_line_count, fontnum, fontfamily, fcharset, fprq, panose, \
            name, altname, fontemb, fontfile, cpg, font_table
