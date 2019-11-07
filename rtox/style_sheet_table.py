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
Check for stylesheet(s) and parse if present.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "style_sheet"

import linecache
import re
import sys
from log_config import logger


class StyleSheetParse:
    """
    Process Header stylesheets
    """

    def __init__(
                 self,
                 rtf_line_to_read,
                 match_symbol
                ):
        self.__line_to_read = rtf_line_to_read
        self.__match = match_symbol

    def style_sheet_exist(self, working_rtf_file, hdr_line_count):
        """
        Check to see if input file contains stylesheets.
        :param working_rtf_file:
        :param hdr_line_count:
        :return: hdr_line_count:
        """

        self.__line_to_read = linecache.getline(working_rtf_file,
                                                hdr_line_count)
        self.__match = re.search(r'\\stylesheet', self.__line_to_read)
        if self.__match:
            style_sheet = 1
            hdr_line_count += 1
            return style_sheet, hdr_line_count

        else:
            style_sheet = 0
            return style_sheet, hdr_line_count

    def set_styles(self, style_sheet, working_rtf_file, hdr_line_count):
        """
        For each stylesheet, capture the relevant settings.
        :return:
        """

        para_style, char_style, sec_style, table_style, table_row_style,\
            para_next_style, style_name = "", "", "", "", "", "", ""
        additive = False
        italic, bold, underline, small_caps, strikethrough = 0, 0, 0, 0, 0

        text_to_process = ""
        while style_sheet == 1:
            self.__line_to_read = linecache.getline(working_rtf_file,
                                                    hdr_line_count)
            hdr_line_count += 1
            open_bracket = re.search(r'{', self.__line_to_read[0])
            if open_bracket == "{":
                open_bracket_count = 0
                state = 1
            else:
                logger.debug(msg=f"There seems to be an error in the RTF "
                                 f"formatting at working_rtf_file line "
                                 f"{hdr_line_count} : "
                                 f"{self.__line_to_read}. The program will "
                                 f"now quit.")
                sys.exit(1)

            while state == 1:
                new_line_to_read = hdr_line_count + open_bracket_count
                self.__line_to_read = linecache.getline(
                    working_rtf_file, new_line_to_read)
                close_bracket = re.search(r'}', self.__line_to_read)
                if close_bracket == "}":
                    text_to_process = self.__line_to_read[
                                      self.__line_to_read.find("{")
                                      + 1:self.__line_to_read.find("}")]
                    hdr_line_count = hdr_line_count + open_bracket_count + 1
                    state = 0
                else:
                    open_bracket_count += 1

            styledef = re.search(r'\\s[0-9]*', text_to_process)
            if styledef:
                para_style = styledef[0].replace("\\s", "")
            else:
                para_style = 0

            styledef = re.search(r'\\\*\\cs[0-9]+', text_to_process)
            if styledef:
                char_style = styledef[0].replace("\\\\*\\cs", "")
            else:
                char_style = 0

            styledef = re.search(r'\\ds[0-9]+', text_to_process)
            if styledef:
                sec_style = styledef[0].replace("\\ds", "")
            else:
                sec_style = 0

            styledef = re.search(r'\\ts[0-9]+', text_to_process)
            if styledef:
                table_style = styledef[0].replace("\\ts", "")
            else:
                table_style = 0

            styledef = re.search(r'\\tsrowd', text_to_process)
            if styledef:
                table_row_style = styledef[0].replace("\\tsrowd", "")
            else:
                table_row_style = 0

            styledef = re.search(r'\\additive', text_to_process)
            if styledef:
                additive = styledef[0].replace("", "")
            else:
                additive = False

            styledef = re.search(r'\\snext[0-9]*', text_to_process)
            if styledef:
                para_next_style = styledef[0].replace("\\snext", "")
            else:
                para_next_style = 0

            pattern = r'(\s\w+)+(;)*'
            styledef = re.search(pattern, text_to_process)
            if styledef:
                style_name = styledef[0].replace(pattern, "")
            else:
                style_name = "None"

            styledef = re.search(r'\\i[0-9]*', text_to_process)
            if styledef:
                italic = styledef[0].replace("\\i", "")
            else:
                italic = 0

            styledef = re.search(r'\\b[0-9]*', text_to_process)
            if styledef:
                bold = styledef[0].replace("\\b", "")
            else:
                bold = 0

            styledef = re.search(r'\\ul[0-9]*', text_to_process)
            if styledef:
                underline = styledef[0].replace("\\ul", "")
            else:
                underline = 0

            styledef = re.search(r'\\scaps', text_to_process)
            if styledef:
                small_caps = styledef[0].replace("\\scaps", "")
            else:
                small_caps = 0

            styledef = re.search(r'\\strike', text_to_process)
            if styledef:
                strikethrough = styledef[0].replace("\\strike", "")
            else:
                strikethrough = 0

        return hdr_line_count, para_style, char_style, sec_style, table_style, \
               table_row_style, additive, para_next_style, style_name, \
               italic, bold, underline, small_caps, strikethrough
