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
Check for a color table and capture color definitions.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "color_table"

import linecache
import re


class ColortblParse:
    """
    Process Header color table.
    """

    def __init__(
                 self,
                ):
        self.__init__()

    @staticmethod
    def color_table_exist(working_rtf_file, hdr_line_count):
        """
        Check for color table. If yes, increment line count and search for end
        of color table. If no, return and begin search for not table in header.
        :param working_rtf_file:
        :param hdr_line_count:
        :return: hdr_line_count:
        """
        line_to_read = linecache.getline(working_rtf_file, hdr_line_count)

        match = re.search(r'{\\colortbl', line_to_read)
        if match:
            color_table = 1
            hdr_line_count += 1

            while color_table == 1:
                line_to_read = linecache.getline(working_rtf_file,
                                                 hdr_line_count)
                sub_match = re.search(r'}', line_to_read)
                if sub_match:
                    hdr_line_count += 1
                    return hdr_line_count
                else:
                    hdr_line_count += 1
        else:
            return hdr_line_count
