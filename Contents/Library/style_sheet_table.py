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
Parse stylesheet(s).
1.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "style_sheet_table"

# From standard libraries
import re

# From local application
import split_between_characters
import table_boundaries


# TODO This entire module should be reviewed and re-written to shorten it.
class StyleSheetParse:
    def __init__(self,
                 working_file: str,
                 debug_dir: str,
                 xml_tag_num: str,
                 line_number: str,
                 table: str,
                 styles_status_list: list) -> None:
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.line_number = line_number
        self.table = table
        self.styles_status_list = styles_status_list

    def find_styles(self):
        """
        1. Find the beginning and end of the table.
        """
        text_to_process = table_boundaries.TableBounds.table_start_end(
            self=table_boundaries.TableBounds(
                line_number=self.line_number,
                table=self.table))

        """
        2. Split the style code list into separate strings, one per style code.
        """
        style_code_strings = split_between_characters.SplitBetween.\
            split_between(self=split_between_characters.SplitBetween(
                            text_to_process=text_to_process,
                            split_characters="}{"))

        """
        3. Separate each style code string into its parts and return the 
        values for each part and save the results in a dictionary.
        """
        for style_code in style_code_strings:

            options = [
                r"{\s",
                r"{\*\cs",
                r"{\ds",
                r"{\trowd",
                r"{\tsrowd",
                ]

            for option in options:
                if re.match(re.escape(option), style_code) is None:
                    pass
                else:
                    try:

                        status, code = code_set(style_code=style_code)

                        if status == 1:

                            italic = italic_set(style_code=style_code)
                            bold = bold_set(style_code=style_code)
                            underline = underline_set(style_code=style_code)
                            strikethrough = strikethrough_set(
                                style_code=style_code)
                            small_caps = small_caps_set(style_code=style_code)
                            additive = additive_set(style_code=style_code)
                            style_name = style_name_set(style_code=style_code)
                            style_next_paragraph = style_next_paragraph_set(
                                style_code=style_code)

                            set_styles_vars = [code, italic, bold, underline,
                                               strikethrough, small_caps,
                                               additive, style_name,
                                               style_next_paragraph]

                            self.styles_status_list = StoreStyle.store_style(
                                self=StoreStyle(
                                    set_styles_vars=set_styles_vars,
                                    styles_status_list=self.styles_status_list))

                        else:
                            pass

                    except TypeError:
                        # TODO Need something here - logger?
                        pass

        return self.styles_status_list


def code_set(style_code: str) -> tuple:
    """

    """
    code = None
    code_styles = [
        r"{\s",
        r"{\*\cs",
        r"{\ds",
        r"{\trowd",
        r"{\tsrowd",
    ]

    status = 0
    for item in code_styles:
        test = re.match(re.escape(item) + r'[0-9]*', style_code)
        if test is not None:
            test = test[0]
            code = test.replace("{\\", "")
            code = code.replace("*\\", "")
            status = 1
        else:
            pass

    return status, code


def italic_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\i[0-9]*", style_code)
        italic = test[0].replace("\\i", "")
        if italic == "":
            italic = 1
        else:
            pass
        return italic
    except TypeError:
        italic = 0
        return italic


def bold_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\b[0-9]*", style_code)
        bold = test[0].replace("\\b", "")
        if bold == "":
            bold = 1
        else:
            pass
        return bold
    except TypeError:
        bold = 0
        return bold


def underline_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\ul[0-9]*", style_code)
        underline = test[0].replace("\\ul", "")
        if underline == "":
            underline = 1
        else:
            pass
        return underline
    except TypeError:
        underline = 0
        return underline


def strikethrough_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\strike[0-9]*", style_code)
        strikethrough = test[0].replace("\\strike", "")
        if strikethrough == "":
            strikethrough = 1
        else:
            pass
        return strikethrough
    except TypeError:
        strikethrough = 0
        return strikethrough


def small_caps_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\scaps[0-9]*", style_code)
        small_caps = test[0].replace("\\scaps", "")
        if small_caps == "":
            small_caps = 1
        else:
            pass
        return small_caps
    except TypeError:
        small_caps = 0
        return small_caps


def additive_set(style_code: str) -> bool:
    """

    """
    try:
        if re.search(r'\\additive', style_code) is not None:
            additive = True
            return additive
        else:
            additive = False
            return additive
    except TypeError:
        additive = False
        return additive


def style_name_set(style_code: str) -> str:
    """

    """
    pattern = r'\s(\w+|\s|\W)+'
    styledef = re.search(pattern, style_code)
    if styledef:
        style_name_pre_1 = styledef[0].rstrip()
        style_name = style_name_pre_1[:-1]
        return style_name
    else:
        style_name = "None"
        return style_name


def style_next_paragraph_set(style_code: str) -> int:
    """

    """
    try:
        test = re.search(r"\\snext[0-9]*", style_code)
        style_next_paragraph = test[0].replace("\\", "")
        style_next_paragraph = int(style_next_paragraph)
        return style_next_paragraph
    except TypeError:
        style_next_paragraph = 0
        return style_next_paragraph


class StoreStyle:
    def __init__(self,
                 set_styles_vars: list,
                 styles_status_list: list) -> None:
        self.set_styles_vars = set_styles_vars
        self.styles_status_list = styles_status_list

    def store_style(self):

        settings = (("code", self.set_styles_vars[0]),
                    ("italic", self.set_styles_vars[1]),
                    ("bold", self.set_styles_vars[2]),
                    ("underline", self.set_styles_vars[3]),
                    ("strikethrough", self.set_styles_vars[4]),
                    ("small_caps", self.set_styles_vars[5]),
                    ("additive", self.set_styles_vars[6]),
                    ("style_name", self.set_styles_vars[7]),
                    ("style_next_paragraph", self.set_styles_vars[8])
                    )

        self.styles_status_list.append((self.set_styles_vars[0], settings))

        return self.styles_status_list
