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
import sys
from collections import deque

# From local application
import dict_updater
from read_log_config import logger_basic


class FonttblParse(object):
    """ An RTF file uses the following structure for a fonttbl (if present):
    <fonttbl>       '{' \fonttbl (<fontinfo> | ('{' <fontinfo> '}'))+ '}'
    <fontinfo>      <fontnum> <fontfamily> <fcharset>? <fprq>? <panose>?
                    <nontaggedname>? <fontemb>? <codepage>? <fontname>
                    <fontaltname>?';'
    <themefont>     \flomajor | \fhimajor | \fdbmajor | \flominor | \fdbminor |
                    \fbiminor
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

    def trim_fonttbl(self):
        for code_string in self.code_strings_to_process:
            if re.search(r'^{\\fonttbl', code_string) is not None:
                place = self.code_strings_to_process.index(code_string)
                new_code_string = code_string.replace("{\\fonttbl", "")
                self.code_strings_to_process[place] = new_code_string
            else:
                pass

    def remove_code_strings(self):
        remove_list = []
        for code_string in self.code_strings_to_process:
            # Ignore code strings in the font table that start with \*\.
            pattern = re.compile(r"^{\\\*\\")
            place = self.code_strings_to_process.index(code_string)
            if re.search(pattern, code_string) is not None:
                remove_list.append(place)
            else:
                pass

        for ele in sorted(remove_list, reverse=True):
            del self.code_strings_to_process[ele]

    def process_code_strings(self):

        for code_string in self.code_strings_to_process:
            try:
                FonttblParse.parse_fonts(
                    self=FonttblParse(
                        debug_dir=self.debug_dir,
                        code_strings_to_process=self.code_strings_to_process),
                    code_string=code_string,
                    code_dict=self.code_dict)
            except ValueError:
                pass

            dict_updater.json_dict_updater(
                dict_name="font_table_file.json",
                dict_update=self.code_dict,
                debug_dir=self.debug_dir)

            self.code_dict = {}

    def parse_fonts(self, code_string: str, code_dict: dict) -> None:
        """ Parse each font code string into its constituent settings and
        store them in a dictionary under the font code number. """

        get_font_codes = FontParser(debug_dir=self.debug_dir,
                                    code_dict=code_dict)

        code_string = FontParser.delete_themes(code_string=code_string)
        code_string = FontParser.check_fontnum(self=get_font_codes,
                                               code_string=code_string)
        code_string = FontParser.check_fontfamily(self=get_font_codes,
                                                  code_string=code_string)
        code_string = FontParser.check_fcharset(self=get_font_codes,
                                                code_string=code_string)
        code_string = FontParser.check_fprq(self=get_font_codes,
                                            code_string=code_string)
        code_string = FontParser.check_panose(self=get_font_codes,
                                              code_string=code_string)
        code_string = FontParser.check_fname(self=get_font_codes,
                                             code_string=code_string)
        code_string = FontParser.check_altname(self=get_font_codes,
                                               code_string=code_string)
        code_string = FontParser.check_fontemb(self=get_font_codes,
                                               code_string=code_string)
        code_string = FontParser.check_fontname_tagged(
            self=get_font_codes, code_string=code_string)
        FontParser.check_cpg(self=get_font_codes,
                             code_string=code_string)


class FontParser(object):
    def __init__(self, debug_dir: str, code_dict: dict) -> None:
        self.debug_dir = debug_dir
        self.code_dict = code_dict
        self.current_key = ""

    @staticmethod
    def delete_themes(code_string: str) -> str:
        """ Starting with Microsoft Word 2007, Word introduced themes. Some
        font definitions may include theme names. However, the definitions
        also include related font information (e.g., font name). RtoX,
        therefore, ignores theme names. """
        theme_list = ["flomajor", "fhimajor", "fdbmajor", "fbimajor",
                      "flominor", "fhiminor", "fdbminor", "fbiminor"]
        for ele in theme_list:
            try:
                test = re.search(fr'\\{ele}', code_string)
                code_string = code_string.replace(test[0], "")
            except TypeError:
                pass
        return code_string

    def check_fontnum(self, code_string: str) -> str:
        """ Each font code is defined by a unique font number (e.g., fontnum
        = f0). """
        item = None
        try:
            test = re.search(r'\\f[0-9]+', code_string)
            if test is not item:
                self.current_key = test[0].replace("\\", "")
                self.code_dict.update({self.current_key: {}})
                code_string = code_string.replace(test[0], "")
                return code_string
            else:
                return code_string
        except TypeError:
            # TODO Check that the program continues even if it encounters
            #  this problem.
            logger_basic.debug(msg="There is an error in the font table "
                                   f'A font number is missing. RtoX will '
                                   f'ignore this font table.\n')

    def check_fontfamily(self, code_string: str) -> str:
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
            if re.search(r"\\"+key[0], code_string) is not None:
                self.code_dict[self.current_key][key[0]] = key[1]
                code_string = code_string.replace(f"\\{key[0]}", "")
            else:
                pass
        return code_string

    def check_fcharset(self, code_string: str) -> str:
        """ Each font code may define the character set it uses. """
        item = None
        try:
            test = re.search(r'\\fcharset([0-9])+', code_string)
            if test is not item:
                value = test[0].replace("\\fcharset", "")
                self.code_dict[self.current_key]["fcharset"] = value
                code_string = code_string.replace(test[0], "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["fcharset"] = 0

    def check_fprq(self, code_string: str) -> str:
        """ Each font code may define the font pitch (default, fixed or
        variable). """
        item = None
        try:
            test = re.search(r'\\fprq([0-9])+', code_string)
            if test is not item:
                value = test[0].replace("\\fprq", "")
                self.code_dict[self.current_key]["fprq"] = value
                code_string = code_string.replace(test[0], "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["fprq"] = 0

    def check_panose(self, code_string: str) -> str:
        """ If present, panose contains a 10-byte Panose 1 number. Each byte
        represents a single font property as defined by the Panose 1 standard
        specification. """
        item = None
        try:
            test = re.search(r'{\\\*\\panose\s[0-9a-zA-Z]+}',
                             code_string)
            if test is not item:
                group_contents = group_boundaries(
                    working_parse_text=code_string,
                    test=test)
                result = group_contents.replace("{\\*\\panose ", "").replace(
                    "}", "")
                self.code_dict[self.current_key]["panose"] = result
                code_string = code_string.replace(group_contents, "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["panose"] = 0

    def check_fname(self, code_string: str) -> str:
        """ Each code may have a non-tagged name, if the document was
        created using WordPad. RtoX ignores this control word."""
        item = None
        try:
            test = re.search(r'{\\\*\\fname ', code_string)
            if test is not item:
                group_contents = group_boundaries(
                    working_parse_text=code_string,
                    test=test)
                code_string = code_string.replace(group_contents, "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["fname"] = "None"

    def check_altname(self, code_string: str) -> str:
        """ Each font code may use an alternative name. """
        item = None
        try:
            test = re.search(r'{\\\*\\falt ', code_string)
            if test is not item:
                group_contents = group_boundaries(
                    working_parse_text=code_string,
                    test=test)
                result = group_contents.replace("{\\*\\falt ", "")
                self.code_dict[self.current_key]["altname"] = result
                code_string = code_string.replace(group_contents, "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["altname"] = "None"

    def check_fontemb(self, code_string: str) -> str:
        """ Each code may contain an embedded font. At present, RtoX does not
        support capturing information about the embedded font. """
        item = None
        try:
            test = re.search(r'{\\\*\\fontemb', code_string)
            if test is not item:
                group_contents = group_boundaries(
                    working_parse_text=code_string,
                    test=test)
                self.code_dict[self.current_key]["fontemb"] = group_contents
                code_string = code_string.replace(group_contents, "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["fontemb"] = False

    def check_fontname_tagged(self, code_string: str) -> str:
        """ A tagged fontname means that the "bytes in runs tagged with the
        associated\\fN are character codes in the codepage corresponding to
        the charset N. If \\cpgN appears, it supersedes the codepage given by
        \\fcharsetN. """
        item = None
        try:
            test = re.search(r"[\w|\s()\-]+", code_string)
            if test is not item:
                result = test[0].lstrip()
                self.code_dict[self.current_key]["fontname"] = result
                code_string = code_string.replace(test[0], "")
                return code_string
            else:
                FontParser.check_fontname_nontagged(code_string=code_string)
        except TypeError:
            self.code_dict[self.current_key]["fontname"] = None

    @staticmethod
    def check_fontname_nontagged(code_string: str):
        return code_string

    def check_cpg(self, code_string: str) -> str:
        """ Each font code may use a specified code page (e.g. Microsoft 1252).
        """
        item = None
        try:
            test = re.search(r'{\\cpg([0-9])+', code_string)
            if test is not item:
                value = test[0].replace("\\cpg", "")
                self.code_dict[self.current_key]["cpg"] = value
                code_string = code_string.replace(test[0], "")
                return code_string
            else:
                return code_string
        except TypeError:
            self.code_dict[self.current_key]["cpg"] = "0"


def group_boundaries(working_parse_text: str, test) -> str:
    deck = deque()
    group_contents = ""
    working_index = test.start()
    while working_index < len(working_parse_text) + 1:

        if working_parse_text[working_index] == "{":
            deck.append(working_parse_text[working_index])
            group_contents = group_contents + \
                working_parse_text[working_index]
            working_index += 1
        elif working_parse_text[working_index] == "}":
            group_contents = group_contents + \
                working_parse_text[working_index]
            deck.popleft()

            if not deck:  # If deck is empty ...
                deck.clear()
                return group_contents
            else:
                working_index += 1

        else:
            group_contents = group_contents + \
                             working_parse_text[working_index]
            working_index += 1
