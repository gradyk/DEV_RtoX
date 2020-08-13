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
import re

# From local application
import dict_updater
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
    def __init__(self, code_strings_to_process: list, debug_dir: str) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.debug_dir = debug_dir
        self.code_dict = {}

    def trim_stylesheet(self):
        for code_string in self.code_strings_to_process:
            if re.search(r'{\\stylesheet', code_string) is not None:
                place = self.code_strings_to_process.index(code_string)
                new_code_string = code_string.replace("{\\stylesheet{", "{\\s0")
                self.code_strings_to_process[place] = new_code_string
            else:
                pass

    def remove_code_strings(self):
        remove_list = []
        for code_string in self.code_strings_to_process:
            # Ignore code strings in the style sheet that start with the \*\cs
            # or \*\ts control word.
            pattern = re.compile(r"{\\\*\\")
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
                StyleSheetParse.process_style_codes(
                    self=StyleSheetParse(
                        debug_dir=self.debug_dir,
                        code_strings_to_process=
                        self.code_strings_to_process),
                    code_string=code_string,
                    code_dict=self.code_dict)
            except ValueError:
                pass

            dict_updater.json_dict_updater(
                dict_name="style_sheet_table_file.json",
                dict_update=self.code_dict,
                debug_dir=self.debug_dir)

            self.code_dict = {}

    def process_style_codes(self, code_string: str, code_dict: dict):
        """ Parse each style code string into its constituent setting and
        store them in a dictionary under the style code number. """
        get_style_codes = GetStyleCodes(code_string=code_string,
                                        debug_dir=self.debug_dir,
                                        code_dict=code_dict)

        GetStyleCodes.check_stylecode(self=get_style_codes)
        GetStyleCodes.check_emphasis_controlwords(self=get_style_codes)
        GetStyleCodes.check_additive(self=get_style_codes)
        GetStyleCodes.check_style_name(self=get_style_codes)
        GetStyleCodes.check_style_next_paragraph(self=get_style_codes)
        GetStyleCodes.check_font_alignment(self=get_style_codes)


class GetStyleCodes(object):

    def __init__(self, code_string: str, debug_dir: str,
                 code_dict: dict) -> None:
        self.code_string = code_string
        self.debug_dir = debug_dir
        self.code_dict = code_dict
        self.current_key = ""

    def check_stylecode(self) -> None:
        """ With the exception of the default style, each style has an
        identifying number. """
        # TODO Check and fix code_styles. May need to process \*\cs and \*\ts
        code_styles = [
            r"{\s",  # Paragraph style code
            r"{\ds",  # Section style code
            r'{\ts',  # Table style code [ PROBABLY \*\ts ]
            r"{\trowd",  # Table row (tables in RTF are contiguous paragraphs).
            r"{\tsrowd",  # Table style definitions [ PROBABLY \*\tsrowd ]
        ]

        for style in code_styles:
            try:
                test = re.match(re.escape(style) + r'[0-9]*', self.code_string)
                self.current_key = test[0].replace("{\\", "")
                self.code_dict.update({self.current_key: {}})
            except (ValueError, TypeError):
                pass

    def check_emphasis_controlwords(self) -> None:
        """  """
        for key in style_controlwords_dict:
            pattern = rf"{style_controlwords_dict[key][4]}[0-9]*"
            try:
                test = re.search(re.escape(pattern), self.code_string)
                value = test[0].replace(f"{style_controlwords_dict[key][4]}",
                                        "")
                something = style_controlwords_dict[key][0]
                self.code_dict[self.current_key][something] = value
            except (ValueError, TypeError):
                pass

    def check_additive(self) -> None:
        """  """
        try:
            if re.search(r'\\additive', self.code_string) is not None:
                self.code_dict[self.current_key]["additive"] = True
            else:
                self.code_dict[self.current_key]["additive"] = False
        except TypeError:
            self.code_dict[self.current_key]["additive"] = False

    def check_style_name(self) -> None:
        """  """
        pattern = r'\s(\b\w+|\s)+'
        test = re.search(pattern, self.code_string)
        if test:
            self.code_dict[self.current_key]["style_name"] = \
                    test[0].lstrip()
        else:
            self.code_dict[self.current_key]["style_name"] = "None"

    def check_style_next_paragraph(self) -> None:
        """  """
        test = re.search(r"\\snext[0-9]*", self.code_string)
        if test:
            self.code_dict[self.current_key]["snext"] = test[0].replace(
                "\\snext", "")
        else:
            self.code_dict[self.current_key]["snext"] = "0"

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
                self.code_dict[self.current_key][
                    "font_align"] = test[0].replace("\\", "")
            else:
                pass
