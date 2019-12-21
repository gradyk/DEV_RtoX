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
This module is the control center for parsing the RTF document.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "header_structure"

import linecache
import os
import re


class HeaderStructure:
    """
    Check header for existence and location of sections: <first line>,
    <font table>, <file table>, <color table>, <stylesheet>, <list table>,
    <rev table>, <rsid table>, <generator>.
    """

    def __init__(self,
                 working_file: str,
                 debug_dir: str
                 ):
        self.working_file = working_file
        self.debug_dir = debug_dir

    def table_check(self):
        """
        Check input file for each possible table in header. If located,
        record the line on which the table starts.
        """

        line_len = HeaderStructure.file_len(
            self=HeaderStructure(
                debug_dir=self.debug_dir,
                working_file=self.working_file))

        header_tables_dict_args = {}
        header_tables = ["rtf", "fonttbl", "filetbl", "colortbl", "stylesheet",
                         "listtables", "revtbl", "rsidtable", "generator",
                         "info"]

        for header in header_tables:
            line_count = 0
            while line_count < line_len:
                line_to_read = linecache.getline(self.working_file,
                                                 line_count)
                match = re.search(header, line_to_read)
                if match:
                    header_tables_dict_args.update({header: line_count})
                    line_count += 1
                else:
                    line_count += 1

        header_table_dict = header_tables_dict_args
        with open(os.path.join(self.debug_dir,
                               "header_tables_dict.py"), "w+") as file:
            file.write("header_tables_dictionary = " + str(header_table_dict))

    def file_len(self):
        with open(self.working_file) as \
                file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
