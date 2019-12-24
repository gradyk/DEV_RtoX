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

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "text_boundaries"

import linecache
import re


class TextBounds:

    def __init__(self,
                 line_number: str,
                 working_file: str
                 ) -> None:
        self.line_number = line_number
        self.working_file = working_file

    def run_tests(self):
        text_open = TextBoundsTests.text_start(
            self=TextBoundsTests(
                line_number=self.line_number,
                working_file=self.working_file))

        text_bounds_vars = TextBoundsTests.text_end(
            self=TextBoundsTests(
                line_number=self.line_number,
                working_file=self.working_file),
            text_open=text_open)
        text_end = text_bounds_vars[0]
        text_line = text_bounds_vars[1]

        return text_open, text_end, text_line


class TextBoundsTests:
    def __init__(self,
                 line_number: str,
                 working_file: str
                 ) -> None:
        self.line_number = line_number
        self.working_file = working_file

    def text_start(self) -> str:

        text_open = self.line_number
        open_test = 0

        while open_test == 0:

            line_to_search = linecache.getline(self.working_file,
                                               self.line_number)
            test_open_bracket = re.search(r"{\\cs", line_to_search)
            if test_open_bracket is None:
                self.line_number += 1
            else:
                text_open = self.line_number
                open_test = 1
                pass

        return text_open

    def text_end(self,
                 text_open: str
                 ) -> tuple:
        self.line_number = text_open

        close_test = 0
        running_line = ""
        text_close = self.line_number
        while close_test == 0:
            line_to_search = linecache.getline(self.working_file,
                                               self.line_number)
            test_close_bracket = re.search("}\n", line_to_search)
            if test_close_bracket is not None:
                running_line = running_line + line_to_search
                text_close = self.line_number
                close_test = 1
            else:
                running_line = running_line + line_to_search
                self.line_number += 1

        text_line_pre = running_line.replace("{\\", "")
        text_line = text_line_pre.replace("\n", "").replace("}", "")

        return text_close, text_line
