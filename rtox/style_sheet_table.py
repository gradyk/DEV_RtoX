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

import csv
import linecache
import os
import re


class StyleSheetParse:
    """
    Process header stylesheets.
    """

    def __init__(
                 self,
                 working_file,
                 line_to_check,
                 debug_dir,
                 style_state,
                 xml_tag_num
                 ):
        self.__working_file = working_file
        self.__line_to_read = line_to_check
        self.__debug_dir = debug_dir
        self.__style_state = style_state
        self.__xml_tag_num = xml_tag_num

    def find_styles(self):

        """
        Capture the the beginning and end of a style definition.
        :return: text_to_process: the complete style definition
        """

        line_status = 1
        line_count = self.__line_to_read
        cb_line_count = line_count
        line_to_parse_start = ""

        # Check to see if this line is the end of the table.
        while linecache.getline(self.__working_file,
                                self.__line_to_read).rstrip() != '}':

            # Find beginning and end of line to process and extract text to
            # process.
            while line_status == 1:
                line_to_parse_start = linecache.getline(self.__working_file,
                                                        line_count)
                open_bracket = re.search(r'{', line_to_parse_start[0])
                if open_bracket:
                    cb_line_count = line_count
                    pass
                else:
                    line_count += 1

                close_bracket = re.search(r'}', line_to_parse_start)
                if close_bracket:
                    line_status = 0
                else:
                    line_status = 0
                    cb_line_count += 1

            running_line = ""
            while line_status == 0:
                line_to_parse_end = linecache.getline(self.__working_file,
                                                      cb_line_count)
                close_bracket = re.search(r'}', line_to_parse_end)
                if close_bracket:
                    line_status = 1
                    running_line = line_to_parse_end.rstrip()
                else:
                    line_status = 0
                    cb_line_count += 1
                    running_line = running_line + line_to_parse_end.rstrip()
                    continue

            line_to_process = line_to_parse_start.rstrip() + running_line

            text_to_process = line_to_process[
                              line_to_process.find("{")
                              + 1:line_to_process.find("}")]

            self.__line_to_read = line_count

            # Process the text.
            StyleSheetParse.set_styles(
                self=StyleSheetParse(
                    debug_dir=self.__debug_dir,
                    working_file=self.__working_file,
                    line_to_check=self.__line_to_read,
                    style_state=self.__style_state,
                    xml_tag_num=self.__xml_tag_num),
                text_to_process=text_to_process)

            line_count = cb_line_count + 1
            self.__line_to_read = line_count

        else:
            self.__style_state = 1

        return self.__style_state

    def set_styles(self, text_to_process):
        """
        Parses a style sheet entry, which is the text_to_process.
        """

        styledef = re.search(r'\\s[0-9]+', text_to_process)
        if styledef:
            code = styledef[0].replace('\\', "")
        else:
            styledef = re.search(r'\\\*\\cs[0-9]+', text_to_process)
            if styledef:
                code = styledef[0].replace('\\*\\', "")
            else:
                styledef = re.search(r'\\ds[0-9]+', text_to_process)
                if styledef:
                    code = styledef[0].replace('\\', "")
                else:
                    styledef = re.search(r'\\ts[0-9]+', text_to_process)
                    if styledef:
                        code = styledef[0].replace('\\', "")
                    else:
                        styledef = re.search(r'\\tsrowd', text_to_process)
                        if styledef:
                            code = styledef[0].replace('\\', "")
                        else:
                            code = "None"
        if code == "None":
            return
        else:
            pass

        styledef = re.search(r'\\additive', text_to_process)
        if styledef:
            additive = True
        else:
            additive = False

        styledef = re.search(r'\\snext[0-9]*', text_to_process)
        if styledef:
            para_next_style = styledef[0].replace("\\snext", "")
        else:
            para_next_style = 0

        pattern = re.compile(r'\s(\w+|\s|\W)+')
        styledef = re.search(pattern, text_to_process)
        if styledef:
            style_name_pre_1 = styledef[0].rstrip()
            style_name = style_name_pre_1[:-1]
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

        styledef = re.search(r'\\strike[0-9]*', text_to_process)
        if styledef:
            strikethrough = styledef[0].replace("\\", "")
        else:
            strikethrough = 0

        styledef = re.search(r'\\scaps[0-9]*', text_to_process)
        if styledef:
            small_caps = styledef[0].replace("\\", "")
        else:
            small_caps = 0

    # rtox.xml_tags.XMLTagSets.xml_style_tags()
        # Select tags to add to XML file based on user's preference.

        # Write tags to XML file.

        # Record style information in csv file.
        StyleSheetParse.styles_tags(
            self=StyleSheetParse(
                working_file=self.__working_file,
                line_to_check=self.__line_to_read,
                debug_dir=self.__debug_dir,
                style_state=self.__style_state,
                xml_tag_num=self.__xml_tag_num),
            code=code,
            additive=additive,
            para_next_style=para_next_style,
            bold=bold,
            italic=italic,
            underline=underline,
            small_caps=small_caps,
            strikethrough=strikethrough,
            style_name=style_name)

    def styles_tags(self, code, additive, para_next_style, bold,
                    italic, underline, small_caps, strikethrough, style_name):
        """
        Write the style information to a csv file.
        """

        style_file = os.path.join(self.__debug_dir, "styles.csv")
        with open(style_file, 'a') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, delimiter=",",
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if code is not None:
                line = [code, additive, para_next_style, bold,
                        italic, underline, small_caps, strikethrough,
                        style_name]
                temp_file_writer.writerow(line)
