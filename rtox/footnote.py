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
__date__ = "2019-12-22"
__name__ = "footnote"

# Standard library imports
import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Local application imports
import rtox.lib.footnote_boundaries


class Footnotes:

    def __init__(self,
                 working_file: str,
                 debug_dir: str,
                 xml_tag_num: str,
                 ) -> None:
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def footnote_line_process(self):
        """
        Read the the doc starting at the info line (if it exists) or at the
        first line (0), if not. Find each section which begins "{
        \\footnote") and find the end of the footnote section.
        """

        # Determine whether to start at the info line or line 0.
        from debugdir.header_tables_dict import header_tables_dictionary as htd

        if "info" in htd.keys():
            line_to_read = htd["info"]
        else:
            line_to_read = "0"

        # Check the number of lines in the working file.
        file_length = FileStats.working_file_length(
            self=FileStats(working_file=self.working_file))

        # Loop over all lines in the file from the starting point to the end.
        while line_to_read + 1 < file_length:

            # Read each line and find the footnote boundaries ({\footnote ...
            # }).
            doc_read_vars = Footnotes.doc_read(
                self=Footnotes(
                    working_file=self.working_file,
                    debug_dir=self.debug_dir,
                    xml_tag_num=self.xml_tag_num),
                line_to_read=line_to_read,
                file_length=file_length)
            lineno = doc_read_vars[0]
            text_close = doc_read_vars[1]

            if lineno <= file_length:

                footnote_list = [lineno, text_close]

                # Store the results in the rtox_db database, doccodes schema.
                StoreFootnotes.footnotes_db(self=StoreFootnotes(
                    debug_dir=self.debug_dir,
                    xml_tag_num=self.xml_tag_num,
                    footnote_list=footnote_list))

                # Create XML tags.
                # StoreFootnote.tag_it()

                # Advance to the next line and repeat.
                line_to_read = text_close + 1

            else:
                line_to_read = file_length
                pass

    def doc_read(self,
                 line_to_read: str,
                 file_length: int
                 ) -> tuple:
        """
        Find the beginning and end of each text line. Use the
        footnote_boundaries module in the lib folder.
        """
        footnote_results = rtox.lib.footnote_boundaries.FootnoteBounds\
            .run_tests(
                self=rtox.lib.footnote_boundaries.FootnoteBounds(
                    line_number=line_to_read,
                    working_file=self.working_file,
                    file_length=file_length))
        footnote_open = footnote_results[0]
        footnote_close = footnote_results[1]

        return footnote_open, footnote_close


class StoreFootnotes:
    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str,
                 footnote_list: list
                 ) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.footnote_list = footnote_list

    def footnotes_db(self):

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
            postgres_insert_query = """INSERT INTO rtox_db.doccodes.footnotes
                                (LINENO, LINEEND) VALUES (%s, %s)"""
            record_to_insert = (self.footnote_list[0], self.footnote_list[1])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering footnote codes in database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()

    # def tag_it(self):


class FileStats:
    """
    Determine the number of lines in the working file.
    """

    def __init__(self,
                 working_file: str
                 ) -> None:
        self.working_file = working_file

    def working_file_length(self) -> int:
        with open(self.working_file) as file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
