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
Pard signifies that the paragraph just beginning uses the same formatting as
the preceding paragraph.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "pard"


# From standard library
import linecache
import re


def pard(working_file: str,
         line_to_read: str,
         styles_status_list: list,
         ) -> None:

    search_area = linecache.getline(working_file, line_to_read)
    di = {}
    b = {}
    match = re.search(r"\\s[0-9]+", search_area)
    if match is None:
        pass
    else:
        set_style = match[0].replace("\\", "")
        code_set = [i for i in styles_status_list if set_style in i]
        for a, b in code_set:
            di.setdefault(a, b)
        di_b = dict(b)

        di_b_vars= PardParse.code(self=PardParse(di_b=di_b))
        code = di_b_vars[0]
        italic = di_b_vars[1]
        bold = di_b_vars[2]
        underline = di_b_vars[3]
        strikethrough = di_b_vars[4]
        small_caps = di_b_vars[5]
        additive = di_b_vars[6]
        style_name = di_b_vars[7]
        style_next_paragraph = di_b_vars[8]
        
        
class PardParse:
    def __init__(self,
                 di_b: dict) -> None:
        self.di_b = di_b
        
    def code(self):
        """

        """
        try:
            code_value = self.di_b["code"]
            return code_value
        except TypeError:
            code_value = "0"
            return code_value

    def italic(self):
        """

        """
        try:
            italic_value = self.di_b["italic"]
            return italic_value
        except TypeError:
            italic_value = "0"
            return italic_value

    def bold(self):
        """

        """
        try:
            bold_value = self.di_b["bold"]
            return bold_value
        except TypeError:
            bold_value = "0"
            return bold_value
        
    def underline(self):
        """

        """
        try:
            underline_value = self.di_b["underline"]
            return underline_value
        except TypeError:
            underline_value = "0"
            return underline_value
        
    def strikethrough(self):
        """

        """
        try:
            strikethrough_value = self.di_b["strikethrough"]
            return strikethrough_value
        except TypeError:
            strikethrough_value = "0"
            return strikethrough_value
        
    def small_caps(self):
        """

        """
        try:
            small_caps_value = self.di_b["small_caps"]
            return small_caps_value
        except TypeError:
            small_caps_value = "0"
            return small_caps_value

    def additive(self):
        """

        """
        try:
            additive_value = self.di_b["additive"]
            return additive_value
        except TypeError:
            additive_value = False
            return additive_value

    def style_name(self):
        """

        """
        try:
            style_name_value = self.di_b["style_name"]
            return style_name_value
        except TypeError:
            style_name_value = False
            return style_name_value

    def style_next_paragraph(self):
        """

        """
        try:
            style_next_paragraph_value = self.di_b["style_next_paragraph"]
            return style_next_paragraph_value
        except TypeError:
            style_next_paragraph_value = False
            return style_next_paragraph_value

    linecache.clearcache()
