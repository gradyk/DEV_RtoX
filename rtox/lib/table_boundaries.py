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
1. Library module used to determine beginning and end of a table definition in
an RTF document header.
2. Works with font table, color table, stylesheet, file table, list table,
___________.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "table_boundaries"

import linecache
import os
import regex as re
import sys

base_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
wif_directory = os.path.join(base_directory, "debugdir")
working_file = os.path.join(wif_directory, "working_input_file.txt")


class TableBounds:

    def __init__(self,
                 line_number: str,
                 table: str
                 ) -> None:
        self.debug_dir = wif_directory
        self.working_file = working_file
        self.line_number = line_number
        self.table = table

    def table_start_end(self) -> tuple:

        table_open = self.line_number
        table_close = self.line_number
        running_line = ""
        table_status = 0

        while table_status == 0:
            line_to_search = linecache.getline(self.working_file,
                                               self.line_number)
            test_close_bracket = re.search("}", line_to_search[0])
            if test_close_bracket is not None:
                running_line = running_line + line_to_search.rstrip()
                table_close = self.line_number
                table_status = 1
            else:
                running_line = running_line + line_to_search.rstrip()
                table_status = 0
                self.line_number += 1

        text_to_process_pre = running_line.replace("{\\"+self.table, "")
        text_to_process = text_to_process_pre.replace("\n", "").\
            replace("}}", "}")

        return table_open, table_close, text_to_process
