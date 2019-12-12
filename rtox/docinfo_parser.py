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
This script controls parsing of the info section of the document.
1. Find beginning of document info section.
2. Find end of document info section.
3. Split the info section into categories (each category bounded by "{" "}").
4. Capture settings in each category and write them to the rtox_db,
docinfocodes schema, docinfocodes tables.
 """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "docinfo_parser"

import rtox.doc_info_read


class DocinfoParse:

    def __init__(self, debug_dir, working_file):
        self.debug_dir = debug_dir
        self.working_file = working_file

    def docinfo_begin(self):

        # Process info section of document.

        # Find beginning of info section.
        info_start_vars = rtox.doc_info_read.DocInfoRead.info_start(
            self=rtox.doc_info_read.DocInfoRead(
                debug_dir=self.debug_dir,
                working_file=self.working_file))
        line_counter_pass = info_start_vars[0]
        line_number_pass = info_start_vars[1]
        line_to_scan_pass = info_start_vars[2]

        if line_counter_pass < line_number_pass:

            running_line = ""
            # Test for end of info section.
            first_test_vars = rtox.doc_info_read.DocInfoRead.info_end_test(
                self=rtox.doc_info_read.DocInfoRead(
                    debug_dir=self.debug_dir,
                    working_file=self.working_file),
                line_counter=line_counter_pass,
                running_line=running_line)
            running_line_pass = first_test_vars

        else:
            running_line_pass = line_to_scan_pass
            pass

        text_to_process_pass = rtox.doc_info_read.DocInfoRead.process_text(
            line_to_scan=line_to_scan_pass,
            running_line=running_line_pass)

        chars = "}{"
        info_list = rtox.doc_info_read.DocInfoRead.split_between(
            text_to_process=text_to_process_pass,
            chars=chars)

        docinfo_vars = rtox.doc_info_read.DocInfoRead.docinfo_for_db(
            result_list=info_list)
        title = docinfo_vars[0]
        subject = docinfo_vars[1]
        author = docinfo_vars[2]
        manager = docinfo_vars[3]
        company = docinfo_vars[4]
        operator = docinfo_vars[5]
        category = docinfo_vars[6]
        comment = docinfo_vars[7]
        doccomm = docinfo_vars[8]
        hlinkbase = docinfo_vars[9]
        version = docinfo_vars[10]
        edmins = docinfo_vars[11]
        nofpages = docinfo_vars[12]
        nofwords = docinfo_vars[13]
        nofchars = docinfo_vars[14]
        nofcharsws = docinfo_vars[15]
        vern = docinfo_vars[16]
        keywords = docinfo_vars[17]
        c_year = docinfo_vars[18]
        c_month = docinfo_vars[19]
        c_day = docinfo_vars[20]
        c_hour = docinfo_vars[21]
        c_minutes = docinfo_vars[22]
        c_seconds = docinfo_vars[23]
        r_year = docinfo_vars[24]
        r_month = docinfo_vars[25]
        r_day = docinfo_vars[26]
        r_hour = docinfo_vars[27]
        r_minutes = docinfo_vars[28]
        r_seconds = docinfo_vars[29]
        p_year = docinfo_vars[30]
        p_month = docinfo_vars[31]
        p_day = docinfo_vars[32]
        p_hour = docinfo_vars[33]
        p_minutes = docinfo_vars[34]
        p_seconds = docinfo_vars[35]
        b_year = docinfo_vars[36]
        b_month = docinfo_vars[37]
        b_day = docinfo_vars[38]
        b_hour = docinfo_vars[39]
        b_minutes = docinfo_vars[40]
        b_seconds = docinfo_vars[41]

        rtox.doc_info_read.DocInfoRead.docinfo_db(
            title=title, subject=subject, author=author, manager=manager,
            company=company, operator=operator, category=category,
            comment=comment, doccomm=doccomm, hlinkbase=hlinkbase,
            version=version, edmins=edmins, nofpages=nofpages,
            nofwords=nofwords, nofchars=nofchars, nofcharsws=nofcharsws,
            vern=vern, keywords=keywords, c_year=c_year, c_month=c_month,
            c_day=c_day, c_hour=c_hour, c_minutes=c_minutes,
            c_seconds=c_seconds,
            r_year=r_year, r_month=r_month, r_day=r_day, r_hour=r_hour,
            r_minutes=r_minutes, r_seconds=r_seconds, p_year=p_year,
            p_month=p_month, p_day=p_day, p_hour=p_hour, p_minutes=p_minutes,
            p_seconds=p_seconds, b_year=b_year, b_month=b_month, b_day=b_day,
            b_hour=b_hour, b_minutes=b_minutes, b_seconds=b_seconds)
