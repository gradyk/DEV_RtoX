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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-23"
__name__ = "footnote_boundaries"

# Standard library imports
import linecache
import re


class FootnoteBounds:
    def __init__(self,
                 line_number: str,
                 working_file: str,
                 file_length: int
                 ) -> None:
        self.line_number = line_number
        self.working_file = working_file
        self.file_length = file_length

    def run_tests(self):
        """
        Called from footnote.py. Finds the start and end of footnotes. When
        self.line_number equals or exceeds the file_length, the module
        returns to footnote.py.
        """
        footnote_open = FootnoteBoundsTests.footnote_start(
            self=FootnoteBoundsTests(
                line_number=self.line_number,
                working_file=self.working_file,
                file_length=self.file_length))

        if int(footnote_open) < self.file_length:

            footnote_end = FootnoteBoundsTests.footnote_end(
                self=FootnoteBoundsTests(
                    line_number=self.line_number,
                    working_file=self.working_file,
                    file_length=self.file_length),
                footnote_open=footnote_open)

        else:
            footnote_end = footnote_open

        return footnote_open, footnote_end


class FootnoteBoundsTests:
    def __init__(self,
                 line_number: str,
                 working_file: str,
                 file_length: int
                 ) -> None:
        self.line_number = line_number
        self.working_file = working_file
        self.file_length = file_length

    def footnote_start(self) -> str:

        footnote_open = self.line_number
        open_test = 0

        while open_test == 0:

            line_to_search = linecache.getline(self.working_file,
                                               self.line_number)
            test_open_bracket = re.search(r"{\\footnote", line_to_search)
            if test_open_bracket is None:
                self.line_number += 1

                if self.line_number == self.file_length:
                    open_test = 1
                    footnote_open = self.file_length + 1
                else:
                    pass

            else:
                footnote_open = self.line_number
                open_test = 1

        return footnote_open

    def footnote_end(self,
                     footnote_open: str
                     ) -> str:
        self.line_number = footnote_open

        close_test = 0
        footnote_close = self.line_number
        while close_test == 0:
            line_to_search = linecache.getline(self.working_file,
                                               self.line_number)
            line_to_search_plus = linecache.getline(self.working_file,
                                                    int(self.line_number)+1)
            test_close_bracket = re.search("}", line_to_search[0]) and \
                re.search("}", line_to_search_plus[0])
            if test_close_bracket is not None:
                footnote_close = self.line_number
                close_test = 1
            else:
                self.line_number += 1

        return footnote_close
