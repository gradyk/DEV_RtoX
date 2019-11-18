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
import os
import re


class StyleSheetParse:
    """
    Process Header stylesheets
    """

    def __init__(
                 self,
                 working_file,
                 line_to_check,
                 debug_dir
                 ):
        self.__working_file = working_file
        self.__line_to_read = line_to_check
        self.__debug_dir = debug_dir

    def find_styles(self, style_sheet):
        """
        For each stylesheet, capture the relevant settings.
        :return:
        """

        state = 0
        line_status = 1
        line_count = self.__line_to_read
        cb_line_count = line_count
        line_to_parse_start = ""

        while style_sheet == 1:

            while line_status == 1:
                line_to_parse_start = linecache.getline(self.__working_file,
                                                        line_count)
                open_bracket = re.search(r'{', line_to_parse_start[0])
                if open_bracket:
                    cb_line_count = line_count
                else:
                    line_count += 1

                close_bracket = re.search(r'}', line_to_parse_start)
                if close_bracket:
                    line_status = 0
                    state = 1
                else:
                    line_status = 0
                    state = 0
                    cb_line_count += 1

            running_line = ""
            while state == 0:
                line_to_parse_end = linecache.getline(self.__working_file,
                                                      cb_line_count)
                close_bracket = re.search(r'}', line_to_parse_end)
                if close_bracket:
                    state = 1
                    running_line = line_to_parse_end.rstrip()
                else:
                    state = 0
                    cb_line_count += 1
                    running_line = running_line + line_to_parse_end.rstrip()
                    continue

            line_to_process = line_to_parse_start.rstrip() + running_line

            text_to_process = line_to_process[
                              line_to_process.find("{")
                              + 1:line_to_process.find("}")]
            print(text_to_process)

            StyleSheetParse.set_styles(
                self=StyleSheetParse(
                    debug_dir=self.__debug_dir,
                    working_file=self.__working_file,
                    line_to_check=self.__line_to_read),
                text_to_process=text_to_process)

    def set_styles(self, text_to_process):

            styledef = re.search(r'\\s[0-9]*', text_to_process)
            if styledef:
                para_style = styledef[0].replace("\\", "")
            else:
                para_style = 0

            styledef = re.search(r'\\\*\\cs[0-9]+', text_to_process)
            if styledef:
                char_style = styledef[0].replace("\\\\*\\", "")
            else:
                char_style = 0

            styledef = re.search(r'\\ds[0-9]+', text_to_process)
            if styledef:
                sec_style = styledef[0].replace("\\", "")
            else:
                sec_style = 0

            styledef = re.search(r'\\ts[0-9]+', text_to_process)
            if styledef:
                table_style = styledef[0].replace("\\", "")
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
                italic = styledef[0].replace("\\", "")
            else:
                italic = 0

            styledef = re.search(r'\\b[0-9]*', text_to_process)
            if styledef:
                bold = styledef[0].replace("\\", "")
            else:
                bold = 0

            styledef = re.search(r'\\ul[0-9]*', text_to_process)
            if styledef:
                underline = styledef[0].replace("\\", "")
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

            style_file = os.path.join(self.__debug_dir, "styles.csv")
            line = "code","bold_on","bold_off","italic_on","italic_off"

            with open(style_file, 'w') as temp_file:
                temp_file.write(line)

            StyleSheetParse.styles_tags(
                self=StyleSheetParse(
                    working_file=self.__working_file,
                    line_to_check=self.__line_to_read,
                    debug_dir=self.__debug_dir),
                # xml_tag_num=,
                para_style=para_style,
                # char_style=char_style,
                # sec_style=sec_style,
                # table_style=table_style,
                # table_row_style=table_row_style,
                # additive=additive,
                # para_next_style=para_next_style,
                # style_name=style_name,
                italic=italic,
                bold=bold,
                # underline=underline,
                # small_caps=small_caps,
                # strikethrough=strikethrough
            )

    def styles_tags(self, para_style, italic, bold):

        style_file = os.path.join(self.__debug_dir, "styles.csv")
        with open(style_file, 'w') as temp_file:
            if para_style is not None:
                line = f'{para_style}',f'{bold}',f'{bold}',f'{italic}',\
                       f'{italic}'
                temp_file.write(line)
            else:
                pass
