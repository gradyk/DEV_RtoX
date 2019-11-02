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
Parse the font table and create a dictionary of values.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "font_table"

import linecache
import os
import re

class FonttblParse:
    """
    Process Header font table settings.
    """

    def __init__(
                 self,
                ):
        self.__init__()

    @staticmethod
    def file_write(debug_file_dir, rtf_file_codes):
        with open(os.path.join(debug_file_dir, "rtf_file_codes.data"),
                  "w+") as rtf_dict:
            rtf_dict.write(str(rtf_file_codes))
            rtf_dict.close()
        return rtf_file_codes

    # Check for font table. If yes, increment line count and move to function
    # to set fonts. If no, move to function to check for file table.
    @staticmethod
    def font_table_scope(working_rtf_file, hdr_line_count):
        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)
        if line_to_read == re.compile(r'{\\fonttbl'):
            font_table = 1
            hdr_line_count += 1
            return font_table, hdr_line_count
        else:
            font_table = 0
            return font_table, hdr_line_count

    def set_fonts(self, working_rtf_file, hdr_line_count):
        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)
        line_to_read = line_to_read.replace("{", "").replace("}", "")
        




        {\f0\froman\fcharset0 Time New Roman;}
        {\f1\fnil\fcharset0 Courier New;}
        }