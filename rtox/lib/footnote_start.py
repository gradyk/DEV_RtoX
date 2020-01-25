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
Starting from the beginning of a footnote (as identified in kw_list),
process the footnote and write the necessary tags to the working xml file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-22"
__name__ = "footnote_start"

# Standard library imports
import os

# From local appliation
import rtox.lib.open_tag_check


# TODO Combine with footnote_start
class FootnoteBlock:

    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str,
                 ) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def footnote_start(self):
        """
        Read the the doc starting at the footnote line indicated in kw_list.
        Find the end of the footnote and insert that line with a label in
        kw_list. Insert a footnote start tag. (Wait to insert the footnote
        end tag until that entry is reached in kw_list).
        """

        tag_dict = rtox.lib.open_tag_check.TagCheck.tag_style(
            self=rtox.lib.open_tag_check.TagCheck(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))

        with open(os.path.join(self.debug_dir, "working_xml_file.xml"),
                  "a") as wxf_pre:
            wxf_pre.write(tag_dict["footnote-beg"])
