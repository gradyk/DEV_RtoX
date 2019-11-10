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
    <font table>, <file table>, <color table>, <style sheet>, <list table>,
    <rev table>, <rsid table>, <generator>.
    """

    def __init__(self,
                 input_file_name,
                 debug_dir
                 ):
        self.__input_file_name = input_file_name
        self.__debug_dir = debug_dir

    def table_check(self):
        """
        Check input file for each possible table in header. If located,
        record the line on which the table starts.
        :return:
        """
        header_tables_dict_args = {}
        line_count = 0
        header_tables = ["rtf", "fonttbl", "filetbl", "colortbl", "stylesheet",
                         "listtables", "revtbl", "rsidtable", "generator"]

        for header in header_tables:
            line_to_read = linecache.getline(line_count, self.__input_file_name)
            match = re.search(header, line_to_read)
            if match:
                header_tables_dict_args.update({header: line_to_read})
                header_table_dict = header_tables_dict_args
                f = open(os.path.join(self.__debug_dir,
                                      "header_tables_dict.py"),
                         "w+")
                f.write(str(header_table_dict))
                f.close()
                line_count = 0
            else:
                line_to_read += 1
