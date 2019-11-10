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
Tag dictionary for TPRES tags.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "tpres_tags"

tpres_tags_dict = {
        "para-beg":         "<pBody>",
        "para-attr":        "<pBody ",
        "para-end":         "</pBody>",
        "title-beg":        "<generalTitle>",
        "title-attr":       "<generalTitle ",
        "title-end":        "</generalTitle>",
        "heading-beg":      "<headDiv>",
        "heading-attr":     "<headDiv ",
        "heading-end":      "</headDiv>",
        "footnote-beg":     "<footNote>",
        "footnote-attr":    "<footNote ",
        "footnote-end":     "</footNote>",
        "italic-beg":       '<hiText rend="italic">',
        "italic-end":       "</hiText>",
        "bold-beg":         '<hiText rend="bold">',
        "bold-end":         '</hiText>',
        "underscore-beg":   '<hiText rend="underscore">',
        "underscore-end":   "</hiText>",
        "list-beg":         "<listGenl>",
        "list-attr":        "<listGenl ",
        "list-end":         "</listGenl>",
        "rend-beg":         "<rendFormat>",
        "rend-attr":        "rendFormat ",
        "rend-end":         "</rendFormat>"
}

