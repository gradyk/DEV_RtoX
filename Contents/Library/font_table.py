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
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Parse the font table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "Contents.Library.font_table"

# From standard libraries
import json
import os
import re

# From local application
from read_log_config import logger_basic


class FonttblParse(object):
    """ An RTF file uses the following structure for a fonttbl (if present):

    """
    def __init__(self, debug_dir: str, code_strings_to_process: list) -> None:
        self.debug_dir = debug_dir
        self.code_strings_to_process = code_strings_to_process

        for code_string in self.code_strings_to_process:

            fontnum, fontfamily, fcharset, fprq, panose, fname, \
                altname, fontemb, cpg = self.process_font_codes(
                    code_string=code_string)

            self.save_font_codes(fontnum=fontnum, fontfamily=fontfamily,
                                 fcharset=fcharset, fprq=fprq,
                                 panose=panose, fname=fname,
                                 altname=altname, fontemb=fontemb,
                                 cpg=cpg)

    def process_font_codes(self, code_string: str):
        """ Parse each font code string into its constituent setting and
        store them in a dictionary under the font code number. """

        get_font_codes = GetFontCodes(debug_dir=self.debug_dir,
                                      code_string=code_string)

        fontnum = GetFontCodes.fontnum(self=get_font_codes)
        fontfamily = GetFontCodes.fontfamily(self=get_font_codes)
        fcharset = GetFontCodes.fcharset(self=get_font_codes)
        fprq = GetFontCodes.fprq(self=get_font_codes)
        panose = GetFontCodes.panose(self=get_font_codes)
        fname = GetFontCodes.fname(self=get_font_codes)
        altname = GetFontCodes.altname(self=get_font_codes)
        fontemb = GetFontCodes.fontemb(self=get_font_codes)
        cpg = GetFontCodes.cpg(self=get_font_codes)

        return fontnum, fontfamily, fcharset, fprq, panose, \
            fname, altname, fontemb, cpg

    def save_font_codes(self, fontnum, fontfamily, fcharset, fprq, panose,
                        fname, altname, fontemb, cpg):

        with open(os.path.join(self.debug_dir, "font_file.json"), "w+") as \
                font_file_pre:

            font_file_updater = {fontnum:
                                 {"fontfamily": fontfamily,
                                  "fcharset": fcharset,
                                  "fprq": fprq,
                                  "panose": panose,
                                  "fname": fname,
                                  "altname": altname,
                                  "fontemb": fontemb,
                                  "cpg": cpg}
                                 }

            json.dump(font_file_updater, font_file_pre)


class GetFontCodes:
    def __init__(self, code_string: str, debug_dir: str) -> None:
        self.code_string = code_string
        self.debug_dir = debug_dir

    def fontnum(self) -> str:
        """ Each font code is defined by a unique font number (e.g., fontnum
        = f0). """
        try:
            test = re.search(r'\\f[0-9]+', self.code_string)
            fontnum = test[0].replace("\\", "")
            return fontnum
        except TypeError:
            # TODO Check that the program continues even if it encounters
            #  this problem.
            logger_basic.debug(msg="There is an error in the font table "
                                   f'A font number is missing. RtoX will '
                                   f'ignore this font table.\n')

    def fontfamily(self) -> str:
        """ Each font code may define its font family. """
        font_families = {"fnil": "default",
                         "froman": "Times New Roman",
                         "fswiss": "Arial",
                         "fmodern": "Courier",
                         "fscript": "Cursive",
                         "fdecor": "Old English",
                         "ftech": "Symbol",
                         "fbidi": "Miriam",
                         }

        for key in font_families:
            if re.search(r"\\"+key, self.code_string) is not None:
                fontfamily = font_families.get(key, "None")
                return fontfamily
            else:
                pass

    def fcharset(self) -> str:
        """ Each font code may define the character set it uses. """
        try:
            test = re.search(r'\\fcharset([0-9])+', self.code_string)
            fcharset = test[0].replace("\\fcharset", "")
            return fcharset
        except TypeError:
            fcharset = "0"
            return fcharset

    def fprq(self) -> str:
        """ Each font code may define the font pitch (default, fixed or
        variable). """
        try:
            test = re.search(r'\\fprq([0-9])+', self.code_string)
            fprq = test[0].replace("\\fprq", "")
            return fprq
        except TypeError:
            fprq = "0"
            return fprq

    def panose(self) -> str:
        """ If present, panose contains a 10-byte Panose 1 number. Each byte
        represents a single font property as defined by the Panose 1 standard
        specification. """
        try:
            test = re.search(r'{(\\)(\*)(\\)(panose)\s[0-9]+}',
                             self.code_string)
            panose = test[0].replace("{\\*\\panose ", "")
            panose = panose.replace("}", "")
            return panose
        except TypeError:
            panose = "0"
            return panose

    def fname(self) -> str:
        """ Each code may have a non-tagged name. """
        try:
            test = re.search(r'{(\\)(\*)(\\)(fname)\s(...)', self.code_string)
            fname = test[0].replace("{\\*\\fname ", "")
            fname = fname.replace('}', "")
            return fname
        except TypeError:
            fname = "None"
            return fname

    def altname(self) -> str:
        """ Each font code may use an alternative name. """
        try:
            test = re.search(re.compile(r'\\\*\\falt\s'), self.code_string)
            altname = test[0].replace(test[0], "")
            return altname
        except TypeError:
            altname = "None"
            return altname

    def fontemb(self) -> bool:
        """ Each code may contain an embedded font. At present, RtoX does not
        support capturing information about the embedded font. """
        try:
            if re.search(r'{\\fontemb', self.code_string) is not None:
                fontemb = True
                return fontemb
            else:
                fontemb = False
                return fontemb
        except TypeError:
            fontemb = False
            return fontemb

    def cpg(self) -> str:
        """ Each font code may use a specified code page (e.g. Microsoft 1252).
        """
        try:
            test = re.search(r'{\\cpg([0-9])+', self.code_string)
            cpg = test[0].replace("\\cpg", "")
            return cpg
        except TypeError:
            cpg = "0"
            return cpg
