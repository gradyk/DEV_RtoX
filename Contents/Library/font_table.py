#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#   RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

""" Parse the font table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "Contents.Library.font_table"

# From standard libraries
import re

# From local application
import dict_updater
from read_log_config import logger_basic


class FonttblParse(object):
    """ An RTF file uses the following structure for a fonttbl (if present):
    <fonttbl>       '{' \fonttbl (<fontinfo> | ('{' <fontinfo> '}'))+ '}'
    <fontinfo>      <fontnum> <fontfamily> <fcharset>? <fprq>? <panose>?
                    <nontaggedname>? <fontemb>? <codepage>? <fontname>
                    <fontaltname>?';'
    <fontnum>       \f
    <fontfamily>    \fnil | \froman | \fswiss | \fmodern | fscript | \fdecor
                    | \ftech | \fbidi
    <fcharset>      \fcharset
    <fprq>          \fprq
    <panose>        <data>
    <nontaggedname> \\*\\fname
    <fontname>      #PCDATA
    <fontaltname>   '{\\*' \falt #PCDATA '}'
    <fontemb>       '{\\*' \fontemb <fonttype> <fontfname>? <data>? '}'
    <fonttype>      \ftnil | \fttruetype
    <fontfname>     '{\\*' \fontfile <codepage>? #PCDATA '}'
    <codepage>      \\cpg
    """

    def __init__(self, debug_dir: str, code_strings_to_process: list) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.debug_dir = debug_dir
        self.code_dict = {}

    def process_code_strings(self):

        for code_string in self.code_strings_to_process:
            # Ignore code strings in the font table that start with the \*\cs
            # control word.
            try:
                test = re.match(r"({)\\\*\\(cs)", code_string)

                FonttblParse.process_font_codes(
                    self=FonttblParse(
                        debug_dir=self.debug_dir,
                        code_strings_to_process=self.code_strings_to_process),
                    code_string=code_string,
                    code_dict=self.code_dict)
            except ValueError:
                pass

            dict_updater.json_dict_updater(dict_name="font_table_file.json",
                                           dict_update=self.code_dict,
                                           debug_dir=self.debug_dir)
            self.code_dict = {}

    def process_font_codes(self, code_string: str, code_dict: dict) -> None:
        """ Parse each font code string into its constituent settings and
        store them in a dictionary under the font code number. """

        get_font_codes = GetFontCodes(code_string=code_string,
                                      debug_dir=self.debug_dir,
                                      code_dict=code_dict)

        GetFontCodes.check_fontnum(self=get_font_codes)
        GetFontCodes.check_fontfamily(self=get_font_codes)
        GetFontCodes.check_fcharset(self=get_font_codes)
        GetFontCodes.check_fprq(self=get_font_codes)
        GetFontCodes.check_panose(self=get_font_codes)
        GetFontCodes.check_fontname(self=get_font_codes)
        GetFontCodes.check_fname(self=get_font_codes)
        GetFontCodes.check_altname(self=get_font_codes)
        GetFontCodes.check_fontemb(self=get_font_codes)
        GetFontCodes.check_cpg(self=get_font_codes)


class GetFontCodes:
    def __init__(self, debug_dir: str, code_string: str,
                 code_dict: dict) -> None:
        self.code_string = code_string
        self.debug_dir = debug_dir
        self.code_dict = code_dict
        self.current_key = ""
        self.beg_index = 0
        self.end_index = 0

    def check_fontnum(self) -> None:
        """ Each font code is defined by a unique font number (e.g., fontnum
        = f0). """
        try:
            test = re.search(r'\\f[0-9]+', self.code_string)
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])
            self.current_key = test[0].replace("\\", "")
            self.code_dict.update({self.current_key: {}})
        except TypeError:
            # TODO Check that the program continues even if it encounters
            #  this problem.
            logger_basic.debug(msg="There is an error in the font table "
                                   f'A font number is missing. RtoX will '
                                   f'ignore this font table.\n')

    def check_fontfamily(self) -> None:
        """ Each font code may define its font family. """
        font_families = [
            ("fbidi", "Miriam"),
            ("fdecor", "Old English"),
            ("fmodern", "Courier"),
            ("fnil", "default"),
            ("froman", "Times New Roman"),
            ("fscript", "Cursive"),
            ("fswiss", "Arial"),
            ("ftech", "Symbol"),
            ]

        for key in font_families:
            if re.search(r"\\"+key[0], self.code_string) is not None:
                self.code_dict[self.current_key][key[0]] = key[1]
            else:
                pass

    def check_fcharset(self) -> None:
        """ Each font code may define the character set it uses. """
        try:
            test = re.search(r'\\fcharset([0-9])+', self.code_string)
            value = test[0].replace("\\fcharset", "")
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])
            self.code_dict[self.current_key]["fcharset"] = value
        except TypeError:
            self.end_index = self.beg_index
            self.code_dict[self.current_key]["fcharset"] = 0

    def check_fprq(self) -> None:
        """ Each font code may define the font pitch (default, fixed or
        variable). """
        try:
            test = re.search(r'\\fprq([0-9])+', self.code_string)
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])
            value = test[0].replace("\\fprq", "")
            self.code_dict[self.current_key]["fprq"] = value
        except TypeError:
            self.end_index = self.beg_index
            self.code_dict[self.current_key]["fprq"] = 0

    def check_panose(self) -> None:
        """ If present, panose contains a 10-byte Panose 1 number. Each byte
        represents a single font property as defined by the Panose 1 standard
        specification. """
        try:
            test = re.search(r'{(\\)(\*)(\\)(panose)\s[0-9a-zA-Z]+}',
                             self.code_string)
            result = test[0].replace("{\\*\\panose", "").replace("}", "")
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])
            result = result.lstrip()
            self.code_dict[self.current_key]["panose"] = result
        except TypeError:
            self.beg_index = self.end_index + 1
            self.end_index = self.end_index + 1
            self.code_dict[self.current_key]["panose"] = 0

    def check_fontname(self) -> None:
        test = re.search(r'(\A\w+.)(\w+.)+(.\w+.)+(?<![{;])|\w+',
                         self.code_string[self.end_index:])
        if test is not None:
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])
            result = test[0]
            self.code_dict[self.current_key]["fontname"] = result
        else:
            GetFontCodes.check_fontname_two(self=GetFontCodes(
                code_string=self.code_string,
                debug_dir=self.debug_dir,
                code_dict=self.code_dict))

    def check_fontname_two(self):
        pass

    def check_fname(self) -> None:
        """ Each code may have a non-tagged name. """
        try:
            test = re.search(r'{(\\)(\*)(\\)(fname)\s(...)', self.code_string)
            value = test[0].replace("{\\*\\fname ", "").replace('}', "")
            self.code_dict[self.current_key]["fname"] = value
        except TypeError:
            self.code_dict[self.current_key]["fname"] = "None"

    def check_altname(self) -> None:
        """ Each font code may use an alternative name. """
        try:
            test = re.search(re.compile(r'\\\*\\falt\s'), self.code_string)
            self.beg_index = self.code_string.index(test[0])
            self.end_index = self.beg_index + len(test[0])

            alt_name_test = re.search(r'(\A\w+.)(\w+.)+(.\w+.)+(?<![}{;])|\w+',
                                      self.code_string[self.end_index:])
            value = alt_name_test[0]
            self.code_dict[self.current_key]["altname"] = value
        except TypeError:
            self.code_dict[self.current_key]["altname"] = "None"

    def check_fontemb(self) -> None:
        """ Each code may contain an embedded font. At present, RtoX does not
        support capturing information about the embedded font. """
        try:
            if re.search(r'{\\fontemb', self.code_string) is not None:
                self.code_dict[self.current_key]["fontemb"] = True
            else:
                self.code_dict[self.current_key]["fontemb"] = False
        except TypeError:
            self.code_dict[self.current_key]["fontemb"] = False

    def check_cpg(self) -> None:
        """ Each font code may use a specified code page (e.g. Microsoft 1252).
        """
        try:
            test = re.search(r'{\\cpg([0-9])+', self.code_string)
            value = test[0].replace("\\cpg", "")
            self.code_dict[self.current_key]["cpg"] = value
        except TypeError:
            self.code_dict[self.current_key]["cpg"] = "0"
