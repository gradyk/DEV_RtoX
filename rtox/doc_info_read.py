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
        running_line by removing the beginning and end, leaving a list of items
        enclosed in brackets (the text_to_process).
        """

        line_to_process = line_to_scan + running_line

        # Note this may leave a \n before the first { at the start of the
        # text to process.
        line_to_process = line_to_process.replace('{\\info', "")

        text_to_process = line_to_process.replace('\n', "").replace('}}', "}")

        return text_to_process

    @staticmethod
    def split_between(text_to_process, chars):
        """
        Splits the text to process into separate items in a list (result_list).
        """
        if len(chars) is not 2:
            raise IndexError("Argument chars must contain two characters.")

        result_list = [chars[1] + line + chars[0] for line in
                       text_to_process.split(chars)]

        result_list[0] = result_list[0][1:]
        result_list[-1] = result_list[-1][:-1]

        return result_list

    def info_to_csv(self, result_list):
        """
        Take the contents of the info section (result_list), separate into
        components, transfer the component information to a csv file.
        """

        # Basic categories.
        title, subject, author, manager, company, \
            operator, category, comment, doccomm, \
            hlinkbase, version, edmins, nofpages, \
            nofwords, nofchars, nofcharsws, vern = "", "", "", "", "",  "", \
                                                   "", "", "", "", "", "", "",\
                                                   "", "", "", "",

        # Special time categories.
        creatim = ""
        c_year, c_month, c_day, c_hour, \
            c_minutes, c_seconds = 0, 0, 0, 0, 0, 0

        revtim = ""
        r_year, r_month, r_day, r_hour, \
            r_minutes, r_seconds = 0, 0, 0, 0, 0, 0

        printim = ""
        p_year, p_month, p_day, p_hour, \
            p_minutes, p_seconds = 0, 0, 0, 0, 0, 0

        buptim = ""
        b_year, b_month, b_day, b_hour, \
            b_minutes, b_seconds = 0, 0, 0, 0, 0, 0

        # Other categories.
        keywords = ""

        # Begin by working through the basic categories one at a time.
        for item in result_list:

            if re.search("title", item):
                title = item.replace("{\\title", "").replace("}", "")
                title = title.lstrip()
            else:
                title = "None"

            if re.search("subject", item):
                subject = item.replace("{\\subject", "").replace("}", "")
                subject = subject.lstrip()
                if len(subject) is 0:
                    subject = "None"
                else:
                    pass
            else:
                subject = "None"

            if re.search("author", item):
                author = item.replace("{\\author", "").replace("}", "")
                author = author.lstrip()
                if len(author) is 0:
                    author = "None"
                else:
                    pass
            else:
                author = "None"

            if re.search("manager", item):
                manager = item.replace("{\\manager", "").replace("}", "")
                manager = manager.lstrip()
                if len(manager) is 0:
                    manager = "None"
                else:
                    pass
            else:
                manager = "None"

            if re.search("company", item):
                company = item.replace("{\\*\\company", "").replace("}", "")
                company = company.lstrip()
                if len(company) is 0:
                    company = "None"
                else:
                    pass
            else:
                company = "None"

            if re.search("operator", item):
                operator = item.replace("{\\operator", "").replace("}", "")
                operator = operator.lstrip()
                if len(operator) is 0:
                    operator = "None"
                else:
                    pass
            else:
                operator = "None"

            if re.search("category", item):
                category = item.replace("{\\category", "").replace("}", "")
                category = category.lstrip()
                if len(category) is 0:
                    category = "None"
                else:
                    pass
            else:
                category = "None"

            if re.search("comment", item):
                comment = item.replace("{\\comment", "").replace("}", "")
                comment = comment.lstrip()
                if len(comment) is 0:
                    comment = "None"
                else:
                    pass
            else:
                comment = "None"

            # TODO May need further work, see Microsoft spec p. 30.
            if re.search("doccomm", item):
                doccomm = item.replace("{\\doccomm", "").replace("}", "")
                doccomm = doccomm.lstrip()
                if len(doccomm) is 0:
                    doccomm = "None"
                else:
                    pass
            else:
                doccomm = "None"

            # TODO May need further work, see Microsoft spec p. 30.
            if re.search("hlinkbase", item):
                hlinkbase = item.replace("{\\hlinkbase", "").replace("}", "")
                hlinkbase = hlinkbase.lstrip()
                if len(hlinkbase) is 0:
                    hlinkbase = "None"
                else:
                    pass
            else:
                hlinkbase = "None"

            if re.search("version", item):
                version = item.replace("{\\version", "").replace("}", "")
                version = version.lstrip()
                if len(version) is 0:
                    version = "None"
                else:
                    pass
            else:
                version = "None"

            if re.search("edmins", item):
                edmins = item.replace("{\\edmins", "").replace("}", "")
                edmins = edmins.lstrip()
                if len(edmins) is 0:
                    edmins = "None"
                else:
                    pass
            else:
                edmins = "None"

            if re.search("nofpages", item):
                nofpages = item.replace("{\\nogpages", "").replace("}", "")
                nofpages = nofpages.lstrip()
                if len(nofpages) is 0:
                    nofpages = "None"
                else:
                    pass
            else:
                nofpages = "None"

            if re.search("nofwords", item):
                nofwords = item.replace("{\\nofwords", "").replace("}", "")
                nofwords = nofwords.lstrip()
                if len(nofwords) is 0:
                    nofwords = "None"
                else:
                    pass
            else:
                nofwords = "None"

            if re.search("nofchars", item):
                nofchars = item.replace("{\\nofchars", "").replace("}", "")
                nofchars = nofchars.lstrip()
                if len(nofchars) is 0:
                    nofchars = "None"
                else:
                    pass
            else:
                nofchars = "None"

            if re.search("nofcharsws", item):
                nofcharsws = item.replace("{\\nofcharsws", "").replace("}", "")
                nofcharsws = nofcharsws.lstrip()
                if len(nofcharsws) is 0:
                    nofcharsws = "None"
                else:
                    pass
            else:
                nofcharsws = "None"

            if re.search("vern", item):
                vern = item.replace("{\\vern", "").replace("}", "")
                vern = vern.lstrip()
                if len(vern) is 0:
                    vern = "None"
                else:
                    pass
            else:
                vern = "None"

            # Then address the other category.
            if re.search("keywords", item):
                keywords = item.replace("{\\keywords", "").replace("}", "")
                keywords = keywords.lstrip()
                if len(keywords) is 0:
                    keywords = "None"
                else:
                    pass
            else:
                keywords = "None"

            # Then address the special time categories.
            if re.search("creatim", item):
                creatim = "Yes"
                cat_time = item.replace("{\\creatim", "").replace("}", "")
                cat_time_list = cat_time.split("\\")
                for time_item in cat_time_list:
                    time_data_vars = DocInfoRead.time_data(
                                        time_item=time_item)
                    c_year = time_data_vars[0]
                    c_month = time_data_vars[1]
                    c_day = time_data_vars[2]
                    c_hour = time_data_vars[3]
                    c_minutes = time_data_vars[4]
                    c_seconds = time_data_vars[5]
            else:
                creatim = "No"
                c_year, c_month, c_day, c_hour, \
                    c_minutes, c_seconds = 0, 0, 0, 0, 0, 0

            if re.search("revtim", item):
                revtim = "Yes"
                cat_time = item.replace("{\\revtim", "").replace("}", "")
                cat_time_list = cat_time.split("\\")
                for time_item in cat_time_list:
                    time_data_vars = DocInfoRead.time_data(
                                        time_item=time_item)
                    r_year = time_data_vars[0]
                    r_month = time_data_vars[1]
                    r_day = time_data_vars[2]
                    r_hour = time_data_vars[3]
                    r_minutes = time_data_vars[4]
                    r_seconds = time_data_vars[5]
            else:
                revtim = "No"
                r_year, r_month, r_day, r_hour, \
                    r_minutes, r_seconds = 0, 0, 0, 0, 0, 0

            if re.search("printim", item):
                printim = "Yes"
                cat_time = item.replace("{\\printim", "").replace("}", "")
                cat_time_list = cat_time.split("\\")
                for time_item in cat_time_list:
                    time_data_vars = DocInfoRead.time_data(
                                        time_item=time_item)
                    p_year = time_data_vars[0]
                    p_month = time_data_vars[1]
                    p_day = time_data_vars[2]
                    p_hour = time_data_vars[3]
                    p_minutes = time_data_vars[4]
                    p_seconds = time_data_vars[5]
            else:
                printim = "No"
                p_year, p_month, p_day, p_hour, \
                    p_minutes, p_seconds = 0, 0, 0, 0, 0, 0

            if re.search("buptim", item):
                buptim = "Yes"
                cat_time = item.replace("{\\buptim", "").replace("}", "")
                cat_time_list = cat_time.split("\\")
                for time_item in cat_time_list:
                    time_data_vars = DocInfoRead.time_data(
                                        time_item=time_item)
                    b_year = time_data_vars[0]
                    b_month = time_data_vars[1]
                    b_day = time_data_vars[2]
                    b_hour = time_data_vars[3]
                    b_minutes = time_data_vars[4]
                    b_seconds = time_data_vars[5]
            else:
                buptim = "No"
                b_year, b_month, b_day, b_hour, \
                    b_minutes, b_seconds = 0, 0, 0, 0, 0, 0

            info_file = os.path.join(self.__debug_dir, "info.csv")
            with open(info_file, 'a') as temp_file:
                temp_file_writer = \
                    csv.writer(temp_file, csv.QUOTE_ALL, delimiter=",")

                line = [title, subject, author, manager, company, operator,
                        category, comment, doccomm, hlinkbase, version, edmins,
                        nofpages, nofwords, nofchars, nofcharsws, vern, creatim,
                        c_year, c_month, c_day, c_hour, c_minutes, c_seconds,
                        revtim, r_year, r_month, r_day, r_hour, r_minutes,
                        r_seconds, printim, p_year, p_month, p_day, p_hour,
                        p_minutes, p_seconds, buptim, b_year, b_month, b_day,
                        b_hour, b_minutes, b_seconds, keywords]

                temp_file_writer.writerow(line)

    def file_len(self):
        with open(self.__working_file) as \
                file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1

    @staticmethod
    def time_data(time_item):
        if re.search(r"\\yr", time_item):
            year = time_item.replace('\\yr', "")
        else:
            year = 0
        if re.search(r"\\mo", time_item):
            month = time_item.replace('\\mo', "")
        else:
            month = 0
        if re.search(r"\\dy", time_item):
            day = time_item.replace('\\dy', "")
        else:
            day = 0
        if re.search(r"\\hr", time_item):
            hour = time_item.replace('\\hr', "")
        else:
            hour = 0
        if re.search(r"\\min", time_item):
            minutes = time_item.replace('\\min', "")
        else:
            minutes = 0
        if re.search(r"\\sec", time_item):
            seconds = time_item.replace('\\sec', "")
        else:
            seconds = 0

        return year, month, day, hour, minutes, seconds
