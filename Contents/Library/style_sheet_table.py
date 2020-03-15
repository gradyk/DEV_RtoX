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
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Parse the style sheet table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "style_sheet_table"

# From standard libraries
import json
import os
import re

# From local application
from Contents.Library.dicts.style_controlwords import style_controlwords_dict


class StyleSheetParse(object):
    """ An RTF file uses the following structure for a stylesheet (if present):
    <stylesheet>        '{' \\stylesheet <style>+ '}'
    <style>             '{' <styledef>?<keycode>? <formatting> <additivie>?
                            <based>? <next>? <autoupd>? <link>?
                            <stylename>?';''}'
    <styledef>          \\s |\\*\\cs | \\ds | \ts\tsrowd
    <keycode>           '{' \\keycode <keys> '}'
    <keys>              ( \\shift? & \\ctrl? & \alt?)
    <key>               \fn | #PCDATA
    <additive>          \additive
    <based>             \\sbasedon
    <next>              \\snext
    <autoupd>           \\sautoupd
    <hidden>            \\shidden
    <link>              \\slinkN
    <locked>            \\slocked
    <personal>          \\spersonal
    <compose>           \\scompose
    <reply>             \\sreply
    <formatting>        (<brdrder> | <parfmt> | <apoctl> | <tabdef> |
                        <shading> | <chrfmt>)+
    <styleid>           \\styrsidN
    <semihidden>        \\ssemihidden
    <stylename>         #PCDATA
    """
    def __init__(self,
                 code_strings_to_process: list,
                 debug_dir: str) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.debug_dir = debug_dir
        self.code_stack = []

    def process_code_strings(self):

        StyleSheetParse.prepare_style_file(
            self=StyleSheetParse(
                debug_dir=self.debug_dir,
                code_strings_to_process=self.code_strings_to_process))

        master_code_stack = []
        for code_string in self.code_strings_to_process:

            # Ignore code strings in the style sheet that start with the \*\cs
            # control word.
            test = re.match(r"({)\\\*\\(cs)", code_string)
            if test is None:

                StyleSheetParse.process_style_codes(
                    self=StyleSheetParse(
                        debug_dir=self.debug_dir,
                        code_strings_to_process=self.code_strings_to_process),
                    code_string=code_string,
                    code_stack=self.code_stack)

                master_code_stack.append(self.code_stack)

                self.code_stack = []

            else:
                pass

        store_style_contents(debug_dir=self.debug_dir,
                             master_code_stack=master_code_stack)

    def prepare_style_file(self):

        with open(os.path.join(self.debug_dir, "style_file.json"), "w+") as \
                style_file_pre:
            json.dump([], style_file_pre)

    def process_style_codes(self, code_string: str, code_stack: list):
        """ Parse each style code string into its constituent setting and
        store them in a dictionary under the style code number. """

        get_style_codes = GetStyleCodes(code_string=code_string,
                                        debug_dir=self.debug_dir,
                                        code_stack=code_stack)

        GetStyleCodes.check_stylecode(self=get_style_codes)
        GetStyleCodes.check_emphasis_controlwords(self=get_style_codes)
        GetStyleCodes.check_additive(self=get_style_codes)
        GetStyleCodes.check_style_name(self=get_style_codes)
        GetStyleCodes.check_style_next_paragraph(self=get_style_codes)
        GetStyleCodes.check_font_alignment(self=get_style_codes)
        self.code_stack = GetStyleCodes.stylelist(self=get_style_codes)


class GetStyleCodes(object):

    def __init__(self, code_string: str, debug_dir: str,
                 code_stack: list) -> None:
        self.code_string = code_string
        self.debug_dir = debug_dir
        self.code_stack = code_stack

    def check_stylecode(self) -> None:
        """  """
        code_styles = [
            r"{\s",  # Paragraph style code
            r"{\ds",  # Section style code
            r'{\ts',  # Table style code
            r"{\trowd",  # Table row (tables in RTF are contiguous paragraphs).
            r"{\tsrowd",  # Table style definitions
        ]

        for item in code_styles:
            test = re.match(re.escape(item) + r'[0-9]*', self.code_string)
            if test is not None:
                self.code_stack.append(
                    ("stylecode", test[0].replace("{\\", "")))
            else:
                pass

    def check_emphasis_controlwords(self) -> None:

        for key in style_controlwords_dict:
            pattern = rf"{style_controlwords_dict[key][4]}[0-9]*"
            test = re.search(re.escape(pattern), self.code_string)
            if test is None:
                self.code_stack.append((style_controlwords_dict[key][0], "0"))
            else:
                replace_text = style_controlwords_dict[key][5]
                key_setting = GetStyleCodes.get_controlword_setting(
                    replace_text, test[0])
                self.code_stack.append(
                    (key, GetStyleCodes.evaluate_setting(key_setting)))

    @staticmethod
    def get_controlword_setting(replace_text: str, test: str) -> str:
        setting = test.replace(test[0], replace_text)
        return setting

    @staticmethod
    def evaluate_setting(setting: str) -> str:
        if setting is None or setting >= "0":
            tag_switch = "1"
        else:
            tag_switch = "0"

        return tag_switch

    def check_additive(self) -> None:
        """  """
        try:
            if re.search(r'\\additive', self.code_string) is not None:
                self.code_stack.append(("additive", True))
            else:
                self.code_stack.append(("additive", False))
        except TypeError:
            self.code_stack.append(("additive", False))

    def check_style_name(self) -> None:
        """  """
        pattern = r'\s(\b\w+|\s)+'
        test = re.search(pattern, self.code_string)
        if test:
            self.code_stack.append(
                ("style_name", test[0].rstrip().lstrip()))
        else:
            self.code_stack.append(("style_name", "None"))

    def check_style_next_paragraph(self) -> None:
        """  """
        test = re.search(r"\\snext[0-9]*", self.code_string)
        if test:
            self.code_stack.append(("snext", test[0].replace("\\snext", "")))
        else:
            self.code_stack.append(("snext", "0"))

    def check_font_alignment(self) -> None:
        """  """
        font_align_list = [
            "faauto",
            "fahang",
            "facenter",
            "faroman",
            "favar",
            "fafixed"
        ]

        for item in font_align_list:
            test = re.search(r"\\"+item, self.code_string)
            if test:
                self.code_stack.append(
                    ("font_align", test[0].replace("\\", "")))
            else:
                pass

    def stylelist(self):
        return self.code_stack


def store_style_contents(debug_dir: str, master_code_stack: list) -> None:

    style_file = os.path.join(debug_dir, "style_file.json")
    with open(style_file, "w") as style_file_pre:
        json.dump(master_code_stack, style_file_pre)
