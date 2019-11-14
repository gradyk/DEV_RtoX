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
                 tag_dict,
                 debug_dir
                ):
        self.__working_file = working_file
        self.__line_to_read = line_to_read
        self.__tag_dict = tag_dict
        self.__debug_dir = debug_dir

    def set_fonts(self):
        """
        For each font number (e.g., f0), capture the relevant settings.
        :return: hdr_line_count, fontnum, fontfamily, fcharset, fprq, panose, \
            name, altname, fontemb, fontfile, cpg, font_table
        """

        font_code_list = {}
        fontnum, fontfamily, fcharset, fprq, panose, name, altname, fontemb, \
            fontfile, cpg = "", "", "", "", "", "", "", "", "", ""
        families = ["fnil", "froman", "fswiss", "fmodern",
                    "fscript", "fdecor", "ftech", "fbidi"]
        c_sets = ["ansi", "mac", "pc", "pca"]

        line_to_parse = linecache.getline(self.__working_file,
                                          self.__line_to_read)

        match = re.search(r'f[0-9]+', line_to_parse)
        if match:
            fontnum = match[0]

            for family in families:
                match = re.search(family, line_to_parse)
                if match:
                    fontfamily = match[0]

            match = re.search(r'\\fcharset([0-9])+', line_to_parse)
            if match:
                fcharset = match[0].replace("\\fcharset", "")

            match = re.search(r'\\fprq([0-9])+', line_to_parse)
            if match:
                fprq = match[0].replace("\\fprq", "")

            match = re.search(re.compile(r'\\\*\\[0-9]+'), line_to_parse)
            if match:
                panose = match[0].replace(match[0], "")

            match = re.search(r'(\s\w+)+(;)*', line_to_parse)
            if match:
                name_pre = match.group(0).replace(";", "")
                name = name_pre.lstrip()

            match = re.search(re.compile(r'\\\*\\falt\s'), line_to_parse)
            if match:
                altname = match[0].replace(match[0], "")

            match = re.search(r'{\\fontemb', line_to_parse)
            if match:
                fontemb = "Yes"
            else:
                fontemb = "No"

            for c_set in c_sets:
                match = re.search(c_set+"cpg", line_to_parse)
                if match:
                    cpg = match.group(1).replace(match.group(1), "")
            # TODO This needs to change based on tag-style selection.
            # TODO Consider what needs to be in a tag inserted in the body of
            #  the file when the font style changes.
            xml_tag_set = (
                f'\t<ts:tagsDecl>\n'
                f'\t\t<ts:rendFormat scheme="rtf" selector="{fontnum}">\n'
                f'\t\t\tfont-style="{name}"\n'
                f'\t\t\tcharset="{fcharset}"\n'
                f'\t\t\tfprq="{fprq}"\n'
                f'\t\t\tpanose="{panose}"\n'
                f'\t\t\tfontfamily="{fontfamily}"\n'
                f'\t\t\taltname="{altname}"\n'
                f'\t\t\tfontemb="{fontemb}"\n'
                f'\t\t\tcpg="{cpg}"\n'
                f"\t\t</ts:rendFormat>\n"
                f'\t</ts:tagsDecl>\n'
                f'\n'
                f'</ts:tpresHeader>\n'
            )

            xfile = os.path.join(self.__debug_dir, "working_xml_file.xml")

            line_len = FonttblParse.file_len(
                xfile=xfile)

            line_count = 0
            while line_count < line_len:

                line_to_parse = linecache.getline(xfile, line_count)
                match = re.search("</ts:tpresHeader>", line_to_parse)
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
            font_code_list = {"fontnum": fontnum, "name": name, "fcharset":
                              fcharset, "fprq": fprq, "panose": panose,
                              "fontfamily": fontfamily, "altname": altname,
                              "fontemb": fontemb, "cpg": cpg}

        else:
            pass

        return font_code_list, self.__line_to_read

    @staticmethod
    def update_rtf_file_codes(font_code_list):
        """
        Write the RTF file codes to a file.
        :param font_code_list:
        """

        from debugdir.rtf_file_codes import rtf_codes_dictionary as rtf_dict
        rtf_dict.update(font_code_list)

    def font_table_end(self):
        self.__line_to_read += 1
        line_to_parse = linecache.getline(self.__working_file,
                                          self.__line_to_read)

        match_beg = re.search(r"{\\f[0-9]+", line_to_parse)
        if match_beg:
            FonttblParse.set_fonts(
                self=FonttblParse(
                    working_file=self.__working_file,
                    line_to_read=self.__line_to_read,
                    tag_dict=self.__tag_dict,
                    debug_dir=self.__debug_dir))

            return self.__line_to_read
        else:
            match_end = re.search(r'}', line_to_parse)
            if match_end:
                return
            else:
                logger.critical(msg="There appears to be an error in the "
                                    "RTF file structure. RtoX can't find "
                                    "the end of the fonttbl. RtoX will "
                                    "now quite.")
                sys.exit(1)

    @staticmethod
    def file_len(xfile):
        with open(xfile) as \
                file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
