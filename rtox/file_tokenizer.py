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
Tokenize rtf file into one line per field. Each line will contain
information useful for the rest of the script.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "file_tokenize"

import os
import re


class RTFTokenize:
    def __init__(self,
                 in_file,
                 bug_handler,
                 copy=None,
                 write_to=None,
                 current_dir=None,
                 ):
        self.__file = in_file
        self.__bug_handler = bug_handler
        self.__copy = copy
        self.__special_tokens = ['_', '~', "'", '{', '}']
        self.__write_to = write_to
        self.__current_dir = current_dir

    @staticmethod
    def __from_ms_to_utf8(match_obj):
        # RTF control words (since RTF 1.5) generally accept signed 16-bit
        # numbers as arguments. Unicode values greater than 32767 must be
        # expressed as negative numbers. \uN uses signed, 16-bit decimal
        # values. To find out what the characters are you must add 65536 to
        # negative values and then convert to hexidecimal.

        uni_char = int(match_obj.group(1))
        if uni_char < 0:
            uni_char += 65536
        return "&#x" + str(f"{uni_char:X}") + ';'

    @staticmethod
    def __neg_unicode_func(match_obj):
        #
        neg_uni_char = int(match_obj.group(1)) * -1
        uni_char = neg_uni_char + 65536
        return "&#x" + str(f"{uni_char:X}") + ';'

    def __sub_line_reg(self, line):
        line = line.replace("\\\\", "\\backslash ")
        line = line.replace("\\~", "\\~ ")
        line = line.replace("\\;", "\\; ")
        line = line.replace("&", "&amp;")
        line = line.replace("<", "&lt;")
        line = line.replace(">", "&gt;")
        line = line.replace("\\~", "\\~ ")
        line = line.replace("\\_", "\\_ ")
        line = line.replace("\\:", "\\: ")
        line = line.replace("\\-", "\\- ")
        # turn into a generic token to eliminate special
        # cases and make processing easier
        line = line.replace("\\{", "\\ob ")
        # turn into a generic token to eliminate special
        # cases and make processing easier
        line = line.replace("\\}", "\\cb ")
        # put a backslash in front of to eliminate special cases and
        # make processing easier
        line = line.replace("{", "\\{")
        # put a backslash in front of to eliminate special cases and
        # make processing easier
        line = line.replace("}", "\\}")
        line = re.sub(self.__utf_exp, self.__from_ms_to_utf8, line)
        # line = re.sub( self.__neg_utf_exp, self.__neg_unicode_func, line)
        line = re.sub(self.__ms_hex_exp, "\\mshex0\\g<1> ", line)
        # line = line.replace("\\backslash", "\\\\")
        # this is for older RTF
        line = re.sub(self.__par_exp, "\\par ", line)
        return line

    def __compile_expressions(self):
        self.__ms_hex_exp = re.compile(r"\\\'(..)")
        self.__utf_exp = re.compile(r"\\u(-?\d{3,6})")

        self.__splitexp = re.compile(r"(\\[\\{}]|{|}|\\[^\s\\{}&]+(?:\s)?)")
        self.__par_exp = re.compile(r"\\$")
        self.__mixed_exp = re.compile(r"(\\[a-zA-Z]+\d+)(\D+)")

    def __create_tokens(self):
        self.__compile_expressions()
        token_temp_file = os.path.join(self.__write_to, "file_tokenized.data")
        read_obj = open(self.__file, "r")
        write_obj = open(token_temp_file, "w+")
        line_to_read = "dummy"
        while line_to_read:
            line_to_read = read_obj.readline()
            line = line_to_read
            line = line.replace("\n", "")
            line = self.__sub_line_reg(line)
            tokens = re.split(self.__splitexp, line)
            for token in tokens:
                if token != "":
                    write_obj.write(token + "\n")
        read_obj.close()
        write_obj.close()

    def tokenize(self):
        # Main class for handling other methods. Reads in one line
        # at a time, uses method self.__sub_line to make basic
        # substitutions, uses self.__splitexp to process tokens.

        self.__create_tokens()
