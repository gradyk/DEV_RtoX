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
This script controls parsing of the info section of the document.
1. Find beginning of document info section.
2. Find end of document info section.
3. Split the info section into categories (each category bounded by "{" "}").
4. Capture settings in each category and write them to the rtox_db,
docinfocodes schema, docinfocodes tables.
 """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "docinfo_parser"

import rtox.docinfo_read


class DocinfoParse:

    def __init__(self,
                 debug_dir: str,
                 working_file: str,
                 xml_tag_num: int):
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.xml_tag_num = xml_tag_num

    def process_docinfo(self):
        """
        Process info section of document.
        """
        table = "info"
        from debugdir.header_tables_dict import header_tables_dictionary as htd

        if table in htd.keys():

            line_to_check = htd[table]

            rtox.docinfo_read.InfoParse.find_docinfo(
                self=rtox.docinfo_read.InfoParse(
                    working_file=self.working_file,
                    debug_dir=self.debug_dir,
                    line_to_read=line_to_check,
                    xml_tag_num=self.xml_tag_num,
                    table=table))

        else:
            pass
