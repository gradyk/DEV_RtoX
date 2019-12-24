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
__name__ = "text"

# Standard library imports
import psycopg2
import re
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Local application imports
import rtox.lib.text_boundaries


class CSLine:
    def __init__(self,
                 working_file: str,
                 debug_dir: str,
                 xml_tag_num: str,
                 ) -> None:
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def cs_line_process(self):
        """
        Read the the doc starting at the info line (if it exists) or at the
        first line (0), if not. Find each text line (which begins "{\\cs").
        Parse the text line and store the results in the rtox_db, doccodes
        schema.
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

            # Read each line and find the text line boundaries ({\cs ... }).
            doc_read_vars = CSLine.doc_read(
                self=CSLine(
                    working_file=self.working_file,
                    debug_dir=self.debug_dir,
                    xml_tag_num=self.xml_tag_num),
                line_to_read=line_to_read)
            lineno = doc_read_vars[0]
            text_close = doc_read_vars[1]
            text_line = doc_read_vars[2]

            # Parse a text line.
            cs_fs = SetText.cs_fs(self=SetText(text_line=text_line))
            cs_italic = SetText.cs_italic(self=SetText(text_line=text_line))
            cs_bold = SetText.cs_bold(self=SetText(text_line=text_line))
            cs_underline = SetText.cs_underline(self=SetText(
                text_line=text_line))
            cs_strikethrough = SetText.cs_strikethrough(self=SetText(
                text_line=text_line))
            cs_small_caps = SetText.cs_small_caps(self=SetText(
                text_line=text_line))
            cs_text = SetText.cs_text(self=SetText(text_line=text_line))

            cs_line_list = [lineno, cs_fs,
                            cs_italic, cs_bold, cs_underline,
                            cs_strikethrough, cs_small_caps, cs_text]

            # Store the results in the rtox_db, doccodes schema.
            StoreText.text_db(self=StoreText(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num,
                cs_line_list=cs_line_list))

            # Create XML tags.
            # StoreText.tag_it()

            # Advance to the next line and repeat.
            line_to_read = text_close + 1

    def doc_read(self,
                 line_to_read: str
                 ) -> tuple:
        """
        Find the beginning and end of each text line.
        """
        text_results = rtox.lib.text_boundaries.TextBounds.run_tests(
            self=rtox.lib.text_boundaries.TextBounds(
                line_number=line_to_read,
                working_file=self.working_file))
        text_open = text_results[0]
        text_close = text_results[1]
        text_line = text_results[2]

        return text_open, text_close, text_line


class SetText:
    """
    Parse each text line.
    """

    def __init__(self,
                 text_line: str
                 ) -> None:
        self.text_line = text_line

    def cs_fs(self):
        """

        """
        try:
            test = re.search(r"\\fs[0-9]*", self.text_line)
            fs = test[0].replace("\\fs", "")
            return fs
        except TypeError:
            fs = "0"
            return fs

    def cs_italic(self):
        """

        """
        try:
            test = re.search(r"\\i[0-9]*", self.text_line)
            italic = test[0].replace("\\i", "")
            if italic == "":
                italic = "1"
            else:
                pass
            return italic
        except TypeError:
            italic = "0"
            return italic

    def cs_bold(self):
        """

        """
        try:
            test = re.search(r"\\b[0-9]*", self.text_line)
            bold = test[0].replace("\\b", "")
            if bold == "":
                bold = "1"
            else:
                pass
            return bold
        except TypeError:
            bold = "0"
            return bold

    def cs_underline(self):
        """

        """
        try:
            test = re.search(r"\\ul[0-9]*", self.text_line)
            underline = test[0].replace("\\ul", "")
            if underline == "":
                underline = "1"
            else:
                pass
            return underline
        except TypeError:
            underline = "0"
            return underline

    def cs_strikethrough(self):
        """

        """
        try:
            test = re.search(r"\\strike[0-9]*", self.text_line)
            strikethrough = test[0].replace("\\strike", "")
            if strikethrough == "":
                strikethrough = "1"
            else:
                pass
            return strikethrough
        except TypeError:
            strikethrough = "0"
            return strikethrough

    def cs_small_caps(self):
        """

        """
        try:
            test = re.search(r"\\scaps[0-9]*", self.text_line)
            small_caps = test[0].replace("\\scaps", "")
            if small_caps == "":
                small_caps = "1"
            else:
                pass
            return small_caps
        except TypeError:
            small_caps = "0"
            return small_caps

    def cs_text(self):
        pattern = r'\s(\w+|\s|\W)+'
        info_text = re.search(pattern, self.text_line)
        if info_text:
            result = info_text[0].rstrip()
            return result
        else:
            result = "None"
            return result


class StoreText:
    """
    Store the results of each parsed text line in the rtox_db, doccodes schema.
    """

    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str,
                 cs_line_list: list
                 ) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.cs_line_list = cs_line_list

    def text_db(self):

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
            postgres_insert_query = """INSERT INTO rtox_db.doccodes.cslinecodes
                            (LINENO, FS, ITALIC, BOLD, UNDERLINE, 
                            STRIKETHROUGH, SMALL_CAPS, TEXT) VALUES (
                            %s, %s, %s, %s, %s, %s, %s, %s)"""
            record_to_insert = (self.cs_line_list[0], self.cs_line_list[1],
                                self.cs_line_list[2], self.cs_line_list[3],
                                self.cs_line_list[4], self.cs_line_list[5],
                                self.cs_line_list[6], self.cs_line_list[7])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering csline codes in database.\n"
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

    def working_file_length(self):
        with open(self.working_file) as file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
