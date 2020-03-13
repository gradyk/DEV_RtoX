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

""" """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.docinfo_parser"

# From standard libraries
import json
import os

# From local applications
import docinfo_read


class DocinfoParse(object):

    def __init__(self,
                 debug_dir: str,
                 working_file: str,
                 xml_tag_num: int):
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.xml_tag_num = xml_tag_num

    def process_docinfo(self):
        """ Parse the info section of document and save the information in a
        dictionary. """
        table = "info"
        with open(os.path.join(self.debug_dir, "header_tables_dict.json")) as \
                header_tables_dict_pre:
            header_tables_dict = json.load(header_tables_dict_pre)

        if table in header_tables_dict.keys():

            line_to_check = header_tables_dict[table]

            docinfo_read.InfoParse.find_docinfo(
                self=docinfo_read.InfoParse(
                    working_file=self.working_file,
                    debug_dir=self.debug_dir,
                    line_to_read=line_to_check,
                    xml_tag_num=self.xml_tag_num,
                    table=table))

        else:
            pass
