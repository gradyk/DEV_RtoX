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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-12"
__name__ = "Contents.Library.emphasis"

# From standard library
import re


# TODO This module should be reworked (e.g., use a list and loop instead of a
#  function for each emphasis type).
def italic(area_search: str) -> str:
    """

    """
    try:
        test = re.search(r"\\i[0-9]*", area_search)
        italic_value = test[0].replace("\\i", "")
        return italic_value
    except TypeError:
        italic_value = "0"
        return italic_value


def bold(area_search: str) -> str:
    """

    """
    try:
        test = re.search(r"\\b[0-9]*", area_search)
        bold_value = test[0].replace("\\b", "")
        if bold_value == "":
            bold_value = "1"
        else:
            pass
        return bold_value
    except TypeError:
        bold_value = "0"
        return bold_value


def underline(area_search: str) -> str:
    """

    """
    try:
        test = re.search(r"\\ul[0-9]*", area_search)
        underline_value = test[0].replace("\\ul", "")
        return underline_value
    except TypeError:
        underline_value = "0"
        return underline_value


def strikethrough(area_search: str) -> str:
    """

    """
    try:
        test = re.search(r"\\strike[0-9]*", area_search)
        strikethrough_value = test[0].replace("\\strike", "")
        return strikethrough_value
    except TypeError:
        strikethrough_value = "0"
        return strikethrough_value


def small_caps(area_search: str) -> str:
    """

    """
    try:
        test = re.search(r"\\scaps[0-9]*", area_search)
        small_caps_value = test[0].replace("\\scaps", "")
        return small_caps_value
    except TypeError:
        small_caps_value = "0"
        return small_caps_value


def text(area_search: str) -> str:
    pattern = r'\s(\w+|\s|\W)+'
    info_text = re.search(pattern, area_search)
    if info_text:
        result = info_text[0].rstrip()
        return result
    else:
        result = ""
        return result
