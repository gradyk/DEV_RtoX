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
Set up tables in rtox_db.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-08"
__name__ = "table_structure"

import psycopg2
import psycopg2.errorcodes
import sys


class TableStructure:

    def __init__(self, con, cur):
        self.con = con
        self.cur = cur

    def style_table(self):
        sys.stdout.write("Starting table creation... \n")
        sys.stdout.write("Creating style code tables...\n")
        try:
            self.cur.execute("""CREATE TABLE STYLECODES.STYLE_TYPE(
                CODE varchar(10),
                BOLD varchar(2),
                ITALIC varchar(2),
                UNDERLINE varchar(2),
                STRIKETHROUGH varchar(2),
                SMALL_CAPS varchar(2),
                ADDITIVE varchar(10),
                STYLE_NEXT_PARAGRAPH varchar(10),
                STYLE_NAME varchar
                )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

    def font_table(self):
        sys.stdout.write("Creating font codes table...\n")
        try:
            self.cur.execute("""CREATE TABLE FONTCODES.FONTINFO(
                FONTNUM varchar(4),
                FNAME varchar,
                FCHARSET varchar(6),
                FPRQ varchar(3),
                PANOSE varchar,
                FONTFAMILY varchar,
                ALTNAME varchar,
                FONTEMB boolean,
                CPG varchar(6)
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

    def docinfo_table(self):
        sys.stdout.write("Creating document information codes tables...\n")
        try:
            self.cur.execute("""CREATE TABLE DOCINFOCODES.GENERAL(
                TITLE char(255),
                SUBJECT char(255),
                AUTHOR char(100),
                MANAGER char(100),
                COMPANY char(100),
                OPERATOR char(100),
                CATEGORY char(100),
                COMMENT text,
                DOCCOMM text,
                HLINKBASE text,
                VERSION char(4),
                EDMINS char(10),
                NOFPAGES char(4),
                NOFWORDS char(10),
                NOFCHARS char(14),
                NOFCHARSWS char(14),
                VERN char(255),
                KEYWORDS char(255)
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

        try:
            self.cur.execute("""CREATE TABLE DOCINFOCODES.CREATE(
                YEAR int,
                MONTH int,
                DAY int,
                HOUR int,
                MINUTES int,
                SECONDS int
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

        try:
            self.cur.execute("""CREATE TABLE DOCINFOCODES.REVISE(
                YEAR int,
                MONTH int,
                DAY int,
                HOUR int,
                MINUTES int,
                SECONDS int
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

        try:
            self.cur.execute("""CREATE TABLE DOCINFOCODES.PRINT(
                YEAR int,
                MONTH int,
                DAY int,
                HOUR int,
                MINUTES int,
                SECONDS int
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

        try:
            self.cur.execute("""CREATE TABLE DOCINFOCODES.BACKUP(
                YEAR int,
                MONTH int,
                DAY int,
                HOUR int,
                MINUTES int,
                SECONDS int
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

    def doc_table(self):
        sys.stdout.write("Creating document codes table...\n")
        try:
            self.cur.execute("""CREATE TABLE DOCCODES.DOCCODES(
                PAR int,
                PARD int,
                SECT int,
                SECTD int,
                FS int,
                FOOTNOTE int,
                FONT_CODE char(4),
                BOLD int,
                ITALIC int,
                UNDERLINE int,
                STRIKETHROUGH int,
                SMALL_CAPS int,
                TEXT text
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

    def file_table(self):
        sys.stdout.write("Creating file codes table...\n")
        try:
            self.cur.execute("""CREATE TABLE FILECODES.FILECODES(
                FILETBL text
            )""")

        except psycopg2.DatabaseError as err:
            TableStructure.error_code(err=err)

    def tables_finished(self):
        sys.stdout.write("Table creation complete.\n")
        self.con.commit()
        self.con.close()
        self.cur.close()

    @staticmethod
    def error_code(err):

        if str(err.pgcode) == "42P07":
            # Table already exists.
            sys.stdout.write(f"{err}.\n")
        else:
            # There is a different problem.
            pg_err = str(err.pgcode)
            print(f"Error number {pg_err}; {err}.\n")
            sys.exit(1)
