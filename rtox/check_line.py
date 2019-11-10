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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-08"
__name__ = "check_line"

import linecache
import re


class CheckLine:
    def __init__(
                 self,
                 hdr_line_count,
                 working_rtf_file
                ):
        self.__line_to_read = hdr_line_count
        self.__working_file = working_rtf_file

    def line_evaluate(self):
        """
        Evaluate line start and decide next steps.
        :return:
        """

        stack_track = 0
        char_index = 0
        counter = 0
        open_bracket_count = 0
        text_to_process = ""
        cw_chars = ["{", "\\", "*"]
        line_to_read = linecache.getline(self.__line_to_read,
                                         self.__working_file)
        while counter == 0:
            for char in cw_chars:
                match = re.search(char, line_to_read[char_index])
                if match:
                    char_index += 1
                    stack_track = 1
                else:
                    pass
            counter = 1

        close_bracket = re.search(r'}', self.__line_to_read)
        if close_bracket == "}":
            text_to_process = self.__line_to_read[
                              self.__line_to_read.find("{")
                              + 1:self.__line_to_read.find("}")]
           self.__line_to_read = self.__line_to_read + \
                                 open_bracket_count + 1
            state = 0
        else:
            open_bracket_count += 1
