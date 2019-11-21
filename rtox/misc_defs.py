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
Check for stylesheet(s) and parse if present.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-20"
__name__ = "misc_defs"

import linecache
import re


# Find beginning and end of line to process and extract text to
# process.
while line_status == 1:
    line_to_parse_start = linecache.getline(self.__working_file,
                                            line_count)
    open_bracket = re.search(r'{', line_to_parse_start[0])
    if open_bracket:
        cb_line_count = line_count
    else:
        line_count += 1

    close_bracket = re.search(r'}', line_to_parse_start)
    if close_bracket:
        line_status = 0
        self.__style_state = 1
    else:
        line_status = 0
        self.__style_state = 0
        cb_line_count += 1

running_line = ""
while line_status == 0:
    line_to_parse_end = linecache.getline(self.__working_file,
                                          cb_line_count)
    close_bracket = re.search(r'}', line_to_parse_end)
    if close_bracket:
        line_status = 1
        running_line = line_to_parse_end.rstrip()
    else:
        line_status = 0
        cb_line_count += 1
        running_line = running_line + line_to_parse_end.rstrip()
        continue

line_to_process = line_to_parse_start.rstrip() + running_line

text_to_process = line_to_process[
                  line_to_process.find("{")
                  + 1:line_to_process.find("}")]
