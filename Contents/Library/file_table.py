#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
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

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
Parse the file table (if the table exists in the document it means the pre-RTF 
file included sub-documents).
1.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "file_table"

# From standard libraries
import linecache
import psycopg2
import re
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# From local application
import Contents.Library.xml_file_tags


class FiletblParse:
    """
    Process file table in document header.
    1. Find the beginning and end of the file table.
    2. Process the text from the working file, by separating the file table
    into its constituent pieces. [NOTE - Not in current version; may be in
    future versions.]
    3. Store the file table text in the rtox_db, filecodes schema.
    4. Turn the settings into XML tags using the tag style preference set by
    the user.
    """

    def __init__(self, line_to_read, debug_dir, working_file, xml_tag_num):
        self.line_to_read = line_to_read
        self.debug_dir = debug_dir
        self.working_file = working_file
        self.xml_tag_num = xml_tag_num

    def find_file_table_scope(self):
        """
        1. Find the beginning and end of a file table.
        """

        line_status = 1
        line_count = self.line_to_read
        cb_line_count = line_count
        line_to_parse_start = ""
        text_to_process = ""

        # Check if this line is the end of the table.
        while linecache.getline(self.working_file,
                                self.line_to_read).rstrip() != '}':

            # Find beginning and end of line to process and extract text to
            # process.
            while line_status == 1:
                line_to_parse_start = linecache.getline(self.working_file,
                                                        line_count)
                if re.search(r'{', line_to_parse_start[0]):
                    cb_line_count = line_count
                else:
                    line_count += 1

                if re.search(r'}', line_to_parse_start):
                    line_status = 0
                else:
                    line_status = 0
                    cb_line_count += 1

            running_line = ""
            while line_status == 0:
                line_to_parse_end = linecache.getline(self.working_file,
                                                      cb_line_count)
                if re.search(r'}', line_to_parse_end):
                    line_status = 1
                    running_line = line_to_parse_end.rstrip()
                else:
                    line_status = 0
                    cb_line_count += 1
                    running_line = running_line + line_to_parse_end.rstrip()

            line_to_process = line_to_parse_start.rstrip() + running_line

            text_to_process = line_to_process[line_to_process.
                                              find("{") +
                                              1:line_to_process.find("}")]

            self.line_to_read = line_count

        # 2. Process the file table.
        #    [As of this version, file tables are not processed in RtoX. The
        #     file table code is stored in the rtox_db, filecodes schema.
        #     As a general rule, information contained in file tables is not
        #     helpful in XML files used for content analysis. Future versions
        #     of RtoX may process file tables.]

        if text_to_process is None:
            text_to_process = ""
        else:
            pass

        return text_to_process

    @staticmethod
    def file_db(text_to_process):
        """
        3. Store the settings for the file table in the rtox_db, filecodes
        schema.
        """

        from config_dict import config_dictionary

        host = config_dictionary.get("host")
        database = config_dictionary.get("database")
        user = config_dictionary.get("user")
        password = config_dictionary.get("password")

        con = psycopg2.connect(host=host, database=database, user=user,
                               password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        try:
            postgres_insert_query = """INSERT INTO rtox_db.filecodes.filecodes
                    (FILETBL) VALUES (%s)"""
            record_to_insert = text_to_process
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering filecodes in database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()

    @staticmethod
    def tag_it(self):
        """
        4. Call the module/functions that turns the file codes into XML tags.
        """

        file_tags_vars = Contents.Library.xml_file_tags.XMLTagSets.file_tags(
            self=Contents.Library.xml_file_tags.XMLTagSets(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num))
        xml_tags = file_tags_vars[0]
        ns = file_tags_vars[1]
        prefix = file_tags_vars[2]
        xml_pattern_two = file_tags_vars[3]

        Contents.Library.xml_file_tags.XMLTagSets.tags_to_db(
            self=Contents.Library.xml_file_tags.XMLTagSets(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num),
            ns=ns, prefix=prefix, xml_pattern_two=xml_pattern_two,
            xml_tags=xml_tags)

    @staticmethod
    def file_len(xfile):
        """
        Determines number of lines in the XML file for help in placing tags.
        """
        i = -1
        with open(xfile) as file_size:
            for i, l in enumerate(file_size):
                pass
        return i + 1
