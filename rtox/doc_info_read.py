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
Each rtf file, after the header section, may have an "info" section that
captures metadata about the document. This module controls the processing of
the "info" section.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-29"
__name__ = "doc_info_read"

import csv
import linecache
import os
import re


class DocInfoRead:

    def __init__(
                 self,
                 working_file,
                 debug_dir
                ):
        self.__working_file = working_file
        self.__debug_dir = debug_dir

    cat_dict = {
        "title":      0,
        "subject":    1,
        "author":     2,
        "manager":    3,
        "company":    4,
        "operator":   5,
        "category":   6,
        "keywords":   7,
        "comment":    8,
        "doccomm":    9,
        "hlinkbase":  10,
        "yr":         11,
        "mo":         12,
        "dy":         13,
        "min":        14,
        "sec":        15,
        "version":    16,
        "edmins":     17,
        "nofpages":   18,
        "nofwords":   19,
        "nofchars":   20,
        "nofcharsws": 21,
        "vern":       22,
    }

    def info_start(self):
        """
        Find the beginning of the info section (line_to_scan_start).
        """

        line_number = DocInfoRead.file_len(
            self=DocInfoRead(
                debug_dir=self.__debug_dir,
                working_file=self.__working_file))

        line_counter = 0
        start_line = ""
        line_to_scan = ""

        while line_counter < line_number:
            line_to_scan = linecache.getline(self.__working_file,
                                             line_counter)
            info_regex = r'{\\info'
            match_info = re.search(info_regex, line_to_scan)
            if match_info:
                start_line = line_to_scan.rstrip()

                close_bracket = re.search(r'}}', line_to_scan)
                if close_bracket:
                    line_counter = line_number + 1
                    return line_counter, line_number, start_line, line_to_scan
                else:
                    line_counter += 1
                    return line_counter, line_number, start_line, line_to_scan
            else:
                line_counter += 1

        return line_counter, line_number, start_line, line_to_scan

    def info_end_test(self, line_counter, running_line):
        """
        Make first attempt to find the end of the info section (
        line_to_scan_end). Look for "}}" at end of line.
        """

        line_status = 0
        cb_line_count = line_counter

        while line_status == 0:

            line_to_scan_test = linecache.getline(self.__working_file,
                                                  cb_line_count).rstrip()
            running_line = running_line + line_to_scan_test.rstrip()
            line_to_scan_test_plus = linecache.getline(self.__working_file,
                                                       cb_line_count + 1)
            line_end = len(line_to_scan_test) - 1

            if line_to_scan_test[line_end] is "}" and \
                    line_to_scan_test_plus[0] is "}":
                line_status = 1
                running_line = running_line + line_to_scan_test_plus.rstrip()
            else:
                line_status = 0
                cb_line_count += 1

        return running_line

    @staticmethod
    def process_text(line_to_scan, running_line):
        """
        The running_line is the contents of the info section, plus the
        beginning ({\\info) and the end (}). This function processes the
        running_line by removing the beginning and end, leaving a series of {
        _____}.
        """

        line_to_process = line_to_scan + running_line

        # Note this may leave a \n before the first { at the start of the
        # text to process.
        line_to_process = line_to_process.replace('{\\info', "")

        text_to_process = line_to_process.replace('\n', "").replace('}}', "}")

        return text_to_process

    @staticmethod
    def split_between(text_to_process, chars):
        if len(chars) is not 2:
            raise IndexError("Argument chars must contain two characters.")

        result_list = [chars[1] + line + chars[0] for line in
                       text_to_process.split(chars)]

        result_list[0] = result_list[0][1:]
        result_list[-1] = result_list[-1][:-1]

        return result_list

    def info_csv(self, category, category_text, line_count):

        info_file = os.path.join(self.__debug_dir, "info.csv")
        with open(info_file, 'a') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, csv.QUOTE_ALL, delimiter=",")

            line = [category,  line_count, category_text]
            temp_file_writer.writerow(line)

    def file_len(self):
        with open(self.__working_file) as \
                file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1

# {\info{\title Template}{\author John Doe}{\operator JOHN
# DOE}{\creatim\yr1999\mo4\dy27\min1}{\revtim\yr1999\mo4\dy27\min1}{\printim\yr1999\mo
# 3\dy17\hr23\min5}{\version2}{\edmins2}{\nofpages183}{\nofwords53170}{\nofchars303071
# }{\*\company Microsoft}{\nofcharsws372192}{\vern8247}}
