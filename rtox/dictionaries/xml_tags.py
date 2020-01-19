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
Tag dictionaries for plain XML tags.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "xml_tags"

xml_tag_dict = {
        "para-beg":         "<p>",
        "para-attr":        "<p ",
        "para-end":         "</p>",
        "title-beg":        "<>",
        "title-attr":       "< ",
        "title-end":        "</>",
        "heading-beg":      "<>",
        "heading-attr":     "< ",
        "heading-end":      "</>",
        "footnote-beg":     "<>",
        "footnote-attr":    "< ",
        "footnote-end":     "</>",
        "italic-beg":       '<>',
        "italic-end":       "</>",
        "bold-beg":         '<>',
        "bold-end":         '</>',
        "underscore-beg":   '<>',
        "underscore-end":   "</>",
        "normal-beg":       '<>',
        "normal-end":       "</>",
        "list-beg":         "<>",
        "list-attr":        "< ",
        "list-end":         "</>",
        "rend-beg":         "<>",
        "rend-attr":        "< ",
        "rend-end":         "</>",
        "smallcaps-beg":    "<>",
        "smallcaps-end":    "</>",
}

tei_tag_dict = {
        "paragraph":        "<p>",
        "title":            "<title>",
        "heading":          "<head>",
        "footnote":         "<note>",
        'italic':           '<hi rend="italic">',
        'bold':             '<hi rend="bold">',
        'underscore':       '<hi rend="underscore">',
        "list":             "<list>",
        "rendition":        "<rendition>",
}

tpres_tag_dict = {
        "para-beg":         "<ts:pBody>",
        "para-attr":        "<ts:pBody ",
        "para-end":         "</ts:pBody>",
        "title-beg":        "<ts:generalTitle>",
        "title-attr":       "<ts:generalTitle ",
        "title-end":        "</ts:generalTitle>",
        "heading-beg":      "<ts:headDiv>",
        "heading-attr":     "<ts:headDiv ",
        "heading-end":      "</ts:headDiv>",
        "footnote-beg":     "<ts:footNote>",
        "footnote-attr":    "<ts:footNote ",
        "footnote-end":     "</ts:footNote>",
        "italic-beg":       '<ts:hiText rend="italic">',
        "italic-end":       "</ts:hiText>",
        "bold-beg":         '<ts:hiText rend="bold">',
        "bold-end":         '</ts:hiText>',
        "underscore-beg":   '<ts:hiText rend="underscore">',
        "underscore-end":   "</hiText>",
        "normal-beg":       '<ts:hiText rend="normal">',
        "normal-end":       "</ts:hiText>",
        "list-beg":         "<ts:listGenl>",
        "list-attr":        "<ts:listGenl ",
        "list-end":         "</ts:listGenl>",
        "rend-beg":         "<ts:rendFormat>",
        "rend-attr":        "<ts:rendFormat ",
        "rend-end":         "</ts:rendFormat>",
        "smallcaps-beg":    '<ts:hiText rend="smallcaps">',
        "smallcaps-end":    "</ts:hiText>",
        "start-tags":       "\t<ts:matterText>\n\t\t<ts:matterBody>\n\t\t\t<ts"
                            ":pBody>"
}
