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
Process color table (version 0.1.0a0 notes the existence of the table in the
XML file and the codes dictionary).
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "color_table"

import linecache
import os
import re


class ColortblParse:
    """
    Process Header color table.
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

    def color_table(self, xml_tag_num):
        """
        Record a tag about the color table, but do not save all color table
        settings (not relevant for most XML applications).
        """

        if xml_tag_num == "1":
            xml_tag_set = (
                '\n'
                '\t\t\t<ts:rendFormat scheme="css" selector="colortbl">\n'
                '\t\t\t\tp.normal = {\n'
                '\t\t\t\tcolor: rgb(0,0,0);\n'
                '\t\t\t\t}\n'
                '\t\t\t</ts:rendFormat>\n'
                '\n'
            )
            # TODO What if XML file does not have this tag? Question
            #  applies to all RTF tables.
            xml_pattern = '</header>'

        elif xml_tag_num == "2":
            xml_tag_set = (
                '\n'
                '\t\t\t<tei:rendition scheme="css" selector="colortbl">\n'
                '\t\t\t\tp.normal = {\n'
                '\t\t\t\tcolor: rgb(0,0,0);\n'
                '\t\t\t\t}\n'
                '\t\t\t</tei:rendition>\n'
                '\n'
            )
            # TODO What if TEI file does not have this tag? Question
            #  applies to all RTF tables.
            xml_pattern = '</tei:tagsDecl>'

        elif xml_tag_num == "3":
            xml_tag_set = (
                '\n'
                '\t\t\t<rendition scheme="css" selector="colortbl">\n'
                '\t\t\t\tp.normal = {\n'
                '\t\t\t\t\tcolor: rgb(0,0,0);\n'
                '\t\t\t\t}\n'
                '\t\t\t</rendition>\n'
                '\n'
            )
            # TODO What if TPRES file does not have this tag? Question
            #  applies to all RTF tables.
            xml_pattern = '</ts:tagsDecl>'

        else:
            xml_tag_set = (
                '\n'
                '\t<ts:rendFormat scheme="css" selector="colortbl">\n'
                '\t\tp.normal = {\n'
                '\t\t\tcolor: rgb(0,0,0);\n'
                '\t\t}\n'
                '\t</ts:rendFormat>\n'
                '\n'
            )
            # TODO What if XML file does not have this tag? Question
            #  applies to all RTF tables.
            xml_pattern = '</header>'

        xfile = os.path.join(self.__debug_dir, "working_xml_file.xml")

        line_len = ColortblParse.file_len(
            xfile=xfile)

        line_count = 0
        while line_count < line_len:

            line_to_parse = linecache.getline(xfile, line_count)
            match = re.search(xml_pattern, line_to_parse)
            if match:
                line_count -= 1

                with open(xfile, "r") as xfile_temp:
                    lines = xfile_temp.readlines()

                if len(lines) > int(line_count):
                    lines[line_count] = xml_tag_set

                with open(xfile, "w") as xfile_update:
                    xfile_update.writelines(lines)

                line_count = line_len + 1

            else:
                line_count += 1

        # TODO this needs to get written to a dictionary here - call
        #  update_rtf_file_codes??
        color_code_list = {"colortbl": 'Skipped'}

        return color_code_list

    @staticmethod
    def file_len(xfile):
        """
        Determines number of lines in XML file for help in placing tags.
        :param xfile:
        :return: line length
        """

        with open(xfile) as \
                file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
