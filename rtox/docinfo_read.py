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
__name__ = "docinfo_read"

import psycopg2
import re
import rtox.lib.table_boundaries
import rtox.lib.split_between_characters
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class InfoParse:

    def __init__(self,
                 working_file: str,
                 debug_dir: str,
                 line_to_read: str,
                 xml_tag_num: int,
                 table: str):
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.line_to_read = line_to_read
        self.xml_tag_num = xml_tag_num
        self.table = table

    def find_docinfo(self):
        """
        1. Find the beginning and end of the info section.
        """
        tse_vars = rtox.lib.table_boundaries.TableBounds.table_start_end(
            self=rtox.lib.table_boundaries.TableBounds(
                line_number=self.line_to_read,
                table=self.table))

        # 2. Split the info code list into separate strings, one per info code.
        info_code_strings = rtox.lib.split_between_characters.SplitBetween. \
            split_between(self=rtox.lib.split_between_characters.SplitBetween(
                            text_to_process=tse_vars[2],
                            split_characters="}{"))

        # 3. Separate each info code string into its parts and return the
        # values for each part so that they can be stored in the rtox_db
        # database.
        for info_code in info_code_strings:

            info_part = "title"
            title = SetInfo.info_part_test(self=SetInfo(info_code=info_code),
                                           info_part=info_part)
            info_part = "subject"
            subject = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "author"
            author = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "manager"
            manager = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "company"
            company = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "operator"
            operator = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "category"
            category = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "comment"
            comment = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "doccomm"
            doccomm = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "hlinkbase"
            hlinkbase = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "version"
            version = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "edmins"
            edmins = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "nofpages"
            nofpages = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "nofwords"
            nofwords = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "nofchars"
            nofchars = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "nofcharsws"
            nofcharsws = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "vern"
            vern = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            info_part = "keywords"
            keywords = SetInfo.info_part_test(self=SetInfo(
                info_code=info_code), info_part=info_part)

            c_time_data_vars = SetInfo.creatim(self=SetInfo(
                info_code=info_code))
            r_time_data_vars = SetInfo.revtim(self=SetInfo(info_code=info_code))
            p_time_data_vars = SetInfo.printim(self=SetInfo(
                info_code=info_code))
            b_time_data_vars = SetInfo.buptim(self=SetInfo(info_code=info_code))

            set_info_vars = [title, subject, author, manager, company,
                             operator, category, comment, doccomm, hlinkbase,
                             version, edmins, nofpages, nofwords, nofchars,
                             nofcharsws, vern, keywords, c_time_data_vars,
                             r_time_data_vars, p_time_data_vars,
                             b_time_data_vars
                             ]

            StoreDocInfo.docinfo_db(
                self=StoreDocInfo(set_info_vars=set_info_vars))

            # StoreDocInfo.tag_it(
            #    self=StoreDocInfo(set_info_vars=set_info_vars))


class SetInfo:
    """

    """
    def __init__(self,
                 info_code: str
                 ) -> None:
        self.info_code = info_code

    def info_part_test(self, info_part) -> str:
        """

        """
        try:
            test = re.search(info_part, self.info_code)
            if test is None:
                result = "None"
                return result
            else:
                result = test[0].replace("{\\" + info_part, "").replace("}", "")
                result = result.lstrip()
                return result
        except TypeError:
            result = "None"
            return result

    def creatim(self) -> list:
        """
        _.
        """
        try:
            test = re.search("creatim", self.info_code)
            if test is None:
                c_time_data_vars = [0, 0, 0, 0, 0, 0]
                return c_time_data_vars
            else:
                cat_time = test[0].replace("{\\creatim", "").replace("}", "")
                cat_time_list = cat_time.split("\\")
                for time_item in cat_time_list:
                    c_time_data_vars = TimeData.time_data(
                                        time_item=time_item)
                    return c_time_data_vars
        except TypeError:
            c_time_data_vars = [0, 0, 0, 0, 0, 0]
            return c_time_data_vars

    def revtim(self) -> list:
        """
        _.
        """
        try:
            test = re.search("revtim", self.info_code)
            if test is None:
                r_time_data_vars = [0, 0, 0, 0, 0, 0]
                return r_time_data_vars
            cat_time = test[0].replace("{\\revtim", "").replace("}", "")
            cat_time_list = cat_time.split("\\")
            for time_item in cat_time_list:
                r_time_data_vars = TimeData.time_data(
                                    time_item=time_item)
                return r_time_data_vars
        except TypeError:
            r_time_data_vars = [0, 0, 0, 0, 0, 0]
            return r_time_data_vars

    def printim(self) -> list:
        """

        """
        try:
            test = re.search("printim", self.info_code)
            if test is None:
                p_time_data_vars = [0, 0, 0, 0, 0, 0]
                return p_time_data_vars
            cat_time = test[0].replace("{\\printim", "").replace("}", "")
            cat_time_list = cat_time.split("\\")
            for time_item in cat_time_list:
                p_time_data_vars = TimeData.time_data(
                                    time_item=time_item)
                return p_time_data_vars
        except TypeError:
            p_time_data_vars = [0, 0, 0, 0, 0, 0]
            return p_time_data_vars

    def buptim(self) -> list:
        """

        """
        try:
            test = re.search("buptim", self.info_code)
            if test is None:
                b_time_data_vars = [0, 0, 0, 0, 0, 0]
                return b_time_data_vars
            cat_time = test[0].replace("{\\buptim", "").replace("}", "")
            cat_time_list = cat_time.split("\\")
            for time_item in cat_time_list:
                b_time_data_vars = TimeData.time_data(
                                    time_item=time_item)
                return b_time_data_vars
        except TypeError:
            b_time_data_vars = [0, 0, 0, 0, 0, 0]
            return b_time_data_vars


class StoreDocInfo:
    """

    """
    def __init__(self,
                 set_info_vars: list
                 ):
        self.set_info_vars = set_info_vars

    def docinfo_db(self):
        """

        """
        from debugdir.config_dict import config_dictionary

        host = config_dictionary.get("host")
        database = config_dictionary.get("database")
        user = config_dictionary.get("user")
        password = config_dictionary.get("password")

        con = psycopg2.connect(host=host, database=database, user=user,
                               password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        try:
            postgres_insert_query = """INSERT INTO 
            rtox_db.docinfocodes.general(title, subject, author, manager, 
            company, operator, category, comment, doccomm, hlinkbase, 
            version, edmins, nofpages, nofwords, nofchars, nofcharsws,
            vern, keywords) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            record_to_insert = (self.set_info_vars[0], self.set_info_vars[1],
                                self.set_info_vars[2], self.set_info_vars[3],
                                self.set_info_vars[4], self.set_info_vars[5],
                                self.set_info_vars[6], self.set_info_vars[7],
                                self.set_info_vars[8], self.set_info_vars[9],
                                self.set_info_vars[10], self.set_info_vars[11],
                                self.set_info_vars[12], self.set_info_vars[13],
                                self.set_info_vars[14], self.set_info_vars[15],
                                self.set_info_vars[16], self.set_info_vars[17])

            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            # TODO Replace sys.stdouts (several) with logger.
            sys.stdout.write("Problem entering docinfo (general) codes in "
                             "database.\n"
                             f"Error number {pg_err}; {err}\n")

        try:
            postgres_insert_query = """INSERT INTO 
            rtox_db.docinfocodes.create(year, month, day, hour, minutes, 
            seconds) VALUES (%s, %s, %s, %s, %s, %s)"""
            array = self.set_info_vars[18]
            record_to_insert = (array[0], array[1], array[2], array[3],
                                array[4], array[5])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering docinfo (creatim) codes in "
                             "database.\n"
                             f"Error number {pg_err}; {err}\n")

        try:
            postgres_insert_query = """INSERT INTO 
            rtox_db.docinfocodes.revise(year, month, day, hour, minutes, 
            seconds) VALUES (%s, %s, %s, %s, %s, %s)"""
            array = self.set_info_vars[19]
            record_to_insert = (array[0], array[1], array[2], array[3],
                                array[4], array[5])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering docinfo (revtim) codes in "
                             "database.\n"
                             f"Error number {pg_err}; {err}\n")

        try:
            postgres_insert_query = """INSERT INTO 
            rtox_db.docinfocodes.print(year, month, day, hour, minutes, 
            seconds) VALUES (%s, %s, %s, %s, %s, %s)"""
            array = self.set_info_vars[20]
            record_to_insert = (array[0], array[1], array[2], array[3],
                                array[4], array[5])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering docinfo (printim) codes in "
                             "database.\n"
                             f"Error number {pg_err}; {err}\n")

        try:
            postgres_insert_query = """INSERT INTO 
            rtox_db.docinfocodes.backup(year, month, day, hour, minutes, 
            seconds) VALUES (%s, %s, %s, %s, %s, %s)"""
            array = self.set_info_vars[21]
            record_to_insert = (array[0], array[1], array[2], array[3],
                                array[4], array[5])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()
        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering docinfo (buptim) codes in "
                             "database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()


class TimeData:
    """

    """
    def __init__(self,
                 time_item: str
                 ) -> None:
        self.time_item = time_item

    @staticmethod
    def time_data(time_item) -> list:
        """

        """
        time_data_test = ["yr", "mo", "dy", "hr", "min", "sec"]
        time_data_vars = []

        for item in time_data_test:

            try:
                test = re.search(r"\\"+item, time_item)
                if test is None:
                    item = 0
                else:
                    item = test[0].replace('\\'+item, "")
            except TypeError:
                item = 0

            time_data_vars.append(int(item))

        return time_data_vars
