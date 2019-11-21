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
Parse the font table and create a dictionary of values.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "font_table"

import csv
import linecache
import os
import re
import sys
from log_config import logger


class FonttblParse:
    """
    Process Header font table settings.
    """

    def __init__(
                 self,
                 working_file,
                 line_to_read,
                 debug_dir,
                 table_state,
                 xml_tag_num
                 ):
        self.__working_file = working_file
        self.__line_to_read = line_to_read
        self.__debug_dir = debug_dir
        self.__table_state = table_state
        self.__xml_tag_num = xml_tag_num

    def find_fonts(self):
        """
        Capture the beginning and end of a font definition.
        :return: text_to_process: the complete font definition
        """

        line_status = 1
        line_count = self.__line_to_read
        cb_line_count = line_count
        line_to_parse_start = ""

        # Check if this line is the end of the table.
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
                    pass
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
            FonttblParse.set_fonts(
                self=FonttblParse(
                    working_file=self.__working_file,
                    line_to_read=self.__line_to_read,
                    debug_dir=self.__debug_dir,
                    table_state=self.__table_state,
                    xml_tag_num=self.__xml_tag_num),
                text_to_process=text_to_process)

            line_count = cb_line_count + 1
            self.__line_to_read = line_count

        else:
            self.__table_state = 1

        return self.__table_state

    def set_fonts(self, text_to_process):
        """
        For each font number (e.g., f0), capture the relevant settings.
        :return: hdr_line_count, fontnum, fontfamily, fcharset, fprq, panose, \
            name, altname, fontemb, fontfile, cpg, font_table
        """

        fontnum, fontfamily, fcharset, fprq, panose, name, altname, \
            fontemb, fontfile, cpg = "", "", "", "", "", "", "", "", "", ""
        families = ["fnil", "froman", "fswiss", "fmodern",
                    "fscript", "fdecor", "ftech", "fbidi"]
        c_sets = ["ansi", "mac", "pc", "pca"]

        match = re.search(r'f[0-9]+', text_to_process)
        if match:
            fontnum = match[0]
        else:
            logger.debug(msg="There appears to be an error in the font "
                             f'table at line {self.__line_to_read}. A '
                             f'font number is missing. RtoX will now quit.\n')
            sys.exit(1)

        for family in families:
            match = re.search(family, text_to_process)
            if match:
                fontfamily = match[0]

        match = re.search(r'\\fcharset([0-9])+', text_to_process)
        if match:
            fcharset = match[0].replace("\\fcharset", "")
        else:
            fcharset = 0

        match = re.search(r'\\fprq([0-9])+', text_to_process)
        if match:
            fprq = match[0].replace("\\fprq", "")
        else:
            fprq = 0

        match = re.search(re.compile(r'\\\*\\[0-9]+'), text_to_process)
        if match:
            panose = match[0].replace(match[0], "")
        else:
            panose = 0

        match = re.search(r'(\s\w+)+(;)*', text_to_process)
        if match:
            name_pre = match.group(0).replace(";", "")
            name = name_pre.lstrip()
        else:
            name = "None"

        match = re.search(re.compile(r'\\\*\\falt\s'), text_to_process)
        if match:
            altname = match[0].replace(match[0], "")
        else:
            altname = "None"

        match = re.search(r'{\\fontemb', text_to_process)
        if match:
            fontemb = "Yes"
        else:
            fontemb = "No"

        for c_set in c_sets:
            match = re.search(c_set+"cpg", text_to_process)
            if match:
                cpg = match.group(1).replace(match.group(1), "")
            else:
                cpg = 0

        # Select tags to add to XML file based on user's preference.
        if self.__xml_tag_num == "1":
            xml_tag_set = (
                f'\n'
                f'<rendition scheme="css" selector="{fontnum}">\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{fontfamily}";\n'
                f'\tcolor: rgb(0,0,0);\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "</header>"

        elif self.__xml_tag_num == "2":
            xml_tag_set = (
                f'\n'
                f'<rendition scheme="css" selector="{fontnum}">\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{fontfamily}";\n'
                f'\tfont-color: ;\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}\n'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "</tei:tagsDecl>"

        elif self.__xml_tag_num == "3":
            xml_tag_set = (
                f'\n'
                f'\t\t\t<ts:rendFormat scheme="css" '
                f'selector="{fontnum}">\n'
                '\t\t\t\tpBody.normal {\n'
                f'\t\t\t\t\tfont-style: normal;\n'
                f'\t\t\t\t\tfontfamily: "{fontfamily};"\n'
                f'\t\t\t\t\tcolor: rgb(0,0,0);\n'
                f'\t\t\t\t\tfont-size: 12pt;\n'
                f'\t\t\t\t\tfont-weight: normal;\n'
                f'\t\t\t\t\tfont-variant: normal;\n'
                '\t\t\t\t}\n'
                f"\t\t\t</ts:rendFormat>\n"
                f"\n"
            )
            xml_pattern = "</ts:tagsDecl>"

        else:
            xml_tag_set = (
                f'\n'
                f'<rendition scheme="css" selector="{fontnum}">\n'
                '\tp.normal {\n'
                f'\tfont-style: normal;\n'
                f'\tfont-family: "{fontfamily}";\n'
                f'\tcolor: rgb(0,0,0);\n'
                f'\tfont-size: 12pt;\n'
                f'\tfont-weight: normal;\n'
                f'\tfont-variant: normal;\n'
                '\t}'
                f'</rendition>\n'
                f'\n'
            )
            xml_pattern = "</header>"

        # Write tags to XML file.
        xfile = os.path.join(self.__debug_dir, "working_xml_file.xml")

        line_len = FonttblParse.file_len(
            xfile=xfile)

        xml_line_track = 0
        while xml_line_track < line_len:

            line_to_parse = linecache.getline(xfile, xml_line_track)
            match = re.search(xml_pattern, line_to_parse)
            if match:
                xml_line_track -= 2

                with open(xfile, "r") as xfile_temp:
                    lines = xfile_temp.readlines()

                if len(lines) > int(xml_line_track):
                    lines[xml_line_track] = xml_tag_set

                with open(xfile, "w") as xfile_update:
                    xfile_update.writelines(lines)

                xml_line_track = line_len + 1

            else:
                xml_line_track += 1

        # Record font information in csv file.
        FonttblParse.font_tags(
            self=FonttblParse(
                debug_dir=self.__debug_dir,
                line_to_read=self.__line_to_read,
                working_file=self.__working_file,
                table_state=self.__table_state,
                xml_tag_num=self.__xml_tag_num),
            fontnum=fontnum,
            name=name,
            fcharset=fcharset,
            fprq=fprq,
            panose=panose,
            fontfamily=fontfamily,
            altname=altname,
            fontemb=fontemb,
            cpg=cpg)

    def font_tags(self, fontnum, name, fcharset, fprq, panose,
                  fontfamily, altname, fontemb, cpg):
        """
        Write the font information to a csv file.
        """

        font_file = os.path.join(self.__debug_dir, "fonts.csv")
        with open(font_file, 'a') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, delimiter=",",
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)

            if fontnum is not None:
                line = [fontnum, name, fcharset, fprq, panose, fontfamily,
                        altname, fontemb, cpg]
                temp_file_writer.writerow(line)

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
