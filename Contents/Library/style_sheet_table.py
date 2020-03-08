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


class StyleSheetParse(object):
    """ An RTF file uses the following structure for a stylesheet (if present):
    <stylesheet>        '{' \\stylesheet <style>+ '}'
    <style>             '{' <styledef>?<keycode>? <formatting> <additivie>?
                            <based>? <next>? <autoupd>? <link>?
                            <stylename>?';''}'
    <styledef>          \\s |\\*\\cs | \\ds | \ts\tsrowd
    <keycode>           '{' \\keycode <keys> '}'
    <keys>              ( \\shift? & \\ctrl? & \alt?) <key>
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

        code_string = StyleSheetParse.process_code_strings(
            self=StyleSheetParse(
                code_strings_to_process=code_strings_to_process,
                debug_dir=self.debug_dir))

        StyleSheetParse.process_style_codes(
            self=StyleSheetParse(
                code_strings_to_process=code_strings_to_process,
                debug_dir=self.debug_dir),
            code_string=code_string)

    def process_code_strings(self):

        for code_string in self.code_strings_to_process:

            StyleSheetParse.process_style_codes(
                self=StyleSheetParse(
                    code_strings_to_process=self.code_strings_to_process,
                    debug_dir=self.debug_dir),
                code_string=code_string)
            
            return code_string

    def process_style_codes(self, code_string: str):
        """ Parse each style code string into its constituent setting and
        store them in a dictionary under the style code number. """

        get_style_codes = GetStyleCodes(code_string=code_string,
                                        debug_dir=self.debug_dir)

        try:

            stylecode = GetStyleCodes.stylecode_set(
                self=get_style_codes)
            italic = GetStyleCodes.italic_set(self=get_style_codes)
            bold = GetStyleCodes.bold_set(self=get_style_codes)
            underline = GetStyleCodes.underline_set(
                self=get_style_codes)
            strikethrough = GetStyleCodes.strikethrough_set(
                self=get_style_codes)
            small_caps = GetStyleCodes.small_caps_set(
                self=get_style_codes)
            additive = GetStyleCodes.additive_set(
                self=get_style_codes)
            style_name = GetStyleCodes.style_name_set(
                self=get_style_codes)
            style_next_paragraph = GetStyleCodes.\
                style_next_paragraph_set(self=get_style_codes)

            return stylecode, italic, bold, underline, \
                strikethrough, small_caps, additive, style_name, \
                style_next_paragraph

        except TypeError:
            # TODO Need something here - logger?
            pass


class GetStyleCodes(object):

    def __init__(self, code_string: str, debug_dir: str) -> None:
        self.code_string = code_string
        self.debug_dir = debug_dir

    def stylecode_set(self) -> str:
        """  """
        stylecode = ""
        code_styles = [
            r"{\s",
            r"{\*\cs",
            r"{\ds",
            r"{\trowd",
            r"{\tsrowd",
        ]

        for item in code_styles:
            test = re.match(re.escape(item) + r'[0-9]*', self.code_string)
            if test is not None:
                test = test[0]
                stylecode = test.replace("{\\", "")
                stylecode = stylecode.replace("*\\", "")
            else:
                pass

        return stylecode

    def italic_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\i[0-9]*", self.code_string)
            italic = test[0].replace("\\i", "")
            if italic == "":
                italic = "1"
            else:
                pass
            return italic
        except TypeError:
            italic = "0"
            return italic

    def bold_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\b[0-9]*", self.code_string)
            bold = test[0].replace("\\b", "")
            if bold == "":
                bold = "1"
            else:
                pass
            return bold
        except TypeError:
            bold = "0"
            return bold

    def underline_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\ul[0-9]*", self.code_string)
            underline = test[0].replace("\\ul", "")
            if underline == "":
                underline = "1"
            else:
                pass
            return underline
        except TypeError:
            underline = "0"
            return underline

    def strikethrough_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\strike[0-9]*", self.code_string)
            strikethrough = test[0].replace("\\strike", "")
            if strikethrough == "":
                strikethrough = "1"
            else:
                pass
            return strikethrough
        except TypeError:
            strikethrough = "0"
            return strikethrough

    def small_caps_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\scaps[0-9]*", self.code_string)
            small_caps = test[0].replace("\\scaps", "")
            if small_caps == "":
                small_caps = "1"
            else:
                pass
            return small_caps
        except TypeError:
            small_caps = "0"
            return small_caps

    def additive_set(self) -> bool:
        """  """
        try:
            if re.search(r'\\additive', self.code_string) is not None:
                additive = True
                return additive
            else:
                additive = False
                return additive
        except TypeError:
            additive = False
            return additive

    def style_name_set(self) -> str:
        """  """
        pattern = r'\s(\w+|\s|\W)+'
        styledef = re.search(pattern, self.code_string)
        if styledef:
            style_name_pre_1 = styledef[0].rstrip()
            style_name = style_name_pre_1[:-1]
            return style_name
        else:
            style_name = "None"
            return style_name

    def style_next_paragraph_set(self) -> str:
        """  """
        try:
            test = re.search(r"\\snext[0-9]*", self.code_string)
            style_next_paragraph = test[0].replace("\\", "")
            return style_next_paragraph
        except TypeError:
            style_next_paragraph = "0"
            return style_next_paragraph

    def store_style(self, stylecode: str, italic: str, bold: str, underline:
                    str, strikethrough: str, small_caps: str, additive: bool,
                    style_name: str, style_next_paragraph: str):

        with open(os.path.join(self.debug_dir, "style_file.json"), "w+") as \
                style_file_pre:

            style_file_updater = {stylecode:
                                  {"italic": italic,
                                   "bold": bold,
                                   "underline": underline,
                                   "strikethrough": strikethrough,
                                   "small_caps": small_caps,
                                   "additive": additive,
                                   "style_name": style_name,
                                   "style_next_paragraph": style_next_paragraph}
                                  }

            json.dump(style_file_updater, style_file_pre)
