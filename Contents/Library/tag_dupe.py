#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
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
When converting an RTF file to an XML file, some unwanted back-to-back tag
combinations are created.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-29"
__name__ = "Contents.Library.tag_dupe"

# From standard libraries
import linecache
import os
import re

# From local application


@staticmethod
def tag_deduper(debug_dir: str, test_file: str):

    tag_list = [
        '<hiText rend="italic">',
        '<hiText rend="bold">',
        '<hiText rend="underline">',
        '<hiText rend="strikethrough">',
        '<hiText rend="smallcaps">',
        ]


    for tag in tag_list:
        ctr = 0
        line = linecache.getline(test_file, ctr)
        open_test = re.search(tag, line)
        if open_test:
            close_test = re.search("</hiText>", line)
            if close_test is None:
                ctr_plus = ctr + 1
            else:
        else:
            pass

            2. find the closing tag (eg, </hiText>)

            3. check to see if there is another tag OF THE SAME TYPE backed up against
                the closing tag (eg, </hiText><hiText rend="bold">)

            4. if so, find the closing tag for the second open tag (eg, </hiText>)

            5. now delete the middle two tags (eg, </hiText><hiText rend="bold">)

            6. repeat loop until answer to 3 is no

            7. repeat process using next tag (eg, <hiText rend="italic">)

[ALTERNATIVE]
def tag_deduper(debug_dir: str, tag_dict: dict):
    working_xml_file = os.path.join(debug_dir, "working_xml_file.xml")

    back_to_back_tag_list = [
        "italic-beg",
        "bold-beg",
        "underline-beg",
        "strikethrough-beg",
        "small-caps-beg"
    ]

    with open(working_xml_file, "r") as working_xml_file_pre:
        working_file = working_xml_file_pre.read()



        for tag in back_to_back_tag_list:

            [SEARCH FOR BACK TO BACK TAGS]
            [REPLACE BACK TO BACK TAGS WITH ONE TAG SET]
        [LOOP END]


