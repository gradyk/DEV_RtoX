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
Parse the font table and pass the values to the rtox_db, fontcodes schema.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "font_table"

import linecache
import psycopg2
import re
import rtox.xml_font_tags
import sys
from log_config import logger
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class FonttblParse:
    """
    Process Header font table settings.
    1. Find the beginning and end of a font code definition.
    2. Process the text from the working file, by separating the font code
    into its constituent pieces (e.g., font number, font family).
    3. Store the settings for the font code in the rtox_db, fontcodes schema.
    4. Turn the settings into XML tags using the tag style preference set by
    the user.
    """

    def __init__(self, working_file, line_to_read, debug_dir, table_state,
                 xml_tag_num):
        self.working_file = working_file
        self.line_to_read = line_to_read
        self.debut_dir = debug_dir
        self.table_state = table_state
        self.xml_tag_num = xml_tag_num

    def find_fonts(self):
        """
        1. Find the beginning and end of a font code definition.
        """

        line_status = 1
        line_count = self.line_to_read
        cb_line_count = line_count
        line_to_parse_start = ""

        # Check if this line is the end of the table.
        while linecache.getline(self.working_file,
                                self.line_to_read).rstrip() != '}':

            # Find beginning and end of line to process and extract text to
            # process.
            while line_status == 1:
                line_to_parse_start = linecache.getline(self.working_file,
                                                        line_count)
                open_bracket = re.search(r'{', line_to_parse_start[0])
                if open_bracket:
                    cb_line_count = line_count
                    pass
                else:
                    line_count += 1

                close_bracket = re.search(r'}', line_to_parse_start)
                if close_bracket:
                    line_status = 0
                    pass
                else:
                    line_status = 0
                    cb_line_count += 1

            running_line = ""
            while line_status == 0:
                line_to_parse_end = linecache.getline(self.working_file,
                                                      cb_line_count)
                close_bracket = re.search(r'}', line_to_parse_end)
                if close_bracket:
                    line_status = 1
                    running_line = line_to_parse_end.rstrip()
                else:
                    line_status = 0
                    cb_line_count += 1
                    running_line = running_line + line_to_parse_end.rstrip()
                    continue

            line_to_process = line_to_parse_start.rstrip() + running_line

            text_to_process = line_to_process[
                              line_to_process.find("{")
                              + 1:line_to_process.find("}")]

            self.line_to_read = line_count

            # 2. Process the a font code.
            set_fonts_vars = FonttblParse.set_fonts(
                self=FonttblParse(
                    working_file=self.working_file,
                    line_to_read=self.line_to_read,
                    debug_dir=self.debut_dir,
                    table_state=self.table_state,
                    xml_tag_num=self.xml_tag_num),
                text_to_process=text_to_process)
            fontnum = set_fonts_vars[0]
            fontfamily = set_fonts_vars[1]
            fcharset = set_fonts_vars[2]
            fprq = set_fonts_vars[3]
            panose = set_fonts_vars[4]
            name = set_fonts_vars[5]
            altname = set_fonts_vars[6]
            fontemb = set_fonts_vars[7]
            fontfile = set_fonts_vars[8]
            cpg = set_fonts_vars[9]

            FonttblParse.font_db(fontnum=fontnum, fontfamily=fontfamily,
                                 fcharset=fcharset, fprq=fprq,
                                 panose=panose, name=name, altname=altname,
                                 fontemb=fontemb, fontfile=fontfile,
                                 cpg=cpg)

            line_count = cb_line_count + 1
            self.line_to_read = line_count

        else:
            self.table_state = 1

        return self.table_state

    def set_fonts(self, text_to_process):
        """
        2. For each font code defined by a unique font number (e.g.,
        fontnum = f0), capture the code settings.
        """

        fontnum, fontfamily, fcharset, fprq, panose, name, altname, \
            fontemb, fontfile, cpg = "", "", "", "", "", "", "", "", "", ""
        families = ["fnil", "froman", "fswiss", "fmodern",
                    "fscript", "fdecor", "ftech", "fbidi"]
        c_sets = ["ansi", "mac", "pc", "pca"]

        match = re.search(r'f[0-9]+', text_to_process)
        if match:
            fontnum = match[0]
        else:
            logger.debug(msg="There appears to be an error in the font "
                             f'table at line {self.line_to_read}. A '
                             f'font number is missing. RtoX will now quit.\n')
            sys.exit(1)

        for family in families:
            match = re.search(family, text_to_process)
            if match:
                if match[0] == "fnil":
                    fontfamily = "Default"
                elif match[0] == "froman":
                    fontfamily = "Times New Roman"
                elif match[0] == "fswiss":
                    fontfamily = "Arial"
                elif match[0] == "fmodern":
                    fontfamily = "Courier"
                elif match[0] == "fscript":
                    fontfamily = "Cursive"
                elif match[0] == "fdecor":
                    fontfamily = "Old English"
                elif match[0] == "ftech":
                    fontfamily = "Symbol"
                elif match[0] == "fidi":
                    fontfamily = "Miriam"

        match = re.search(r'\\fcharset([0-9])+', text_to_process)
        if match:
            fcharset = match[0].replace("\\fcharset", "")
        else:
            fcharset = 0

        match = re.search(r'\\fprq([0-9])+', text_to_process)
        if match:
            fprq = match[0].replace("\\fprq", "")
        else:
            fprq = 0

        match = re.search(re.compile(r'\\\*\\[0-9]+'), text_to_process)
        if match:
            panose = match[0].replace(match[0], "")
        else:
            panose = 0

        match = re.search(r'(\s\w+)+(;)*', text_to_process)
        if match:
            name_pre = match.group(0).replace(";", "")
            name = name_pre.lstrip()
            fontfamily = name
        else:
            name = "None"

        match = re.search(re.compile(r'\\\*\\falt\s'), text_to_process)
        if match:
            altname = match[0].replace(match[0], "")
        else:
            altname = "None"

        match = re.search(r'{\\fontemb', text_to_process)
        if match:
            fontemb = True
        else:
            fontemb = False

        for c_set in c_sets:
            match = re.search(c_set+"cpg", text_to_process)
            if match:
                cpg = match.group(1).replace(match.group(1), "")
            else:
                cpg = 0

        return fontnum, fontfamily, fcharset, fprq, panose, name, altname, \
            fontemb, fontfile, cpg

    @staticmethod
    def font_db(fontnum, name, fcharset, fprq, panose, fontfamily,
                altname, fontemb, fontfile, cpg):
        """
        3. Store the settings for each font code in the rtox_db, fontcode
        schema.
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
            postgres_insert_query = """INSERT INTO rtox_db.fontcodes.fontinfo
                (FONTNUM, NAME, FCHARSET, FPRQ, PANOSE, FONTFAMILY,
                 ALTNAME, FONTEMB, FONTFILE, CPG) VALUES (%s, %s, %s, %s, %s, 
                 %s, %s, %s, %s, %s)"""
            record_to_insert = (fontnum, name, fcharset, fprq, panose,
                                fontfamily, altname, fontemb, fontfile, cpg)
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering fontcodes in database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()

    def tag_it(self, fontnum, fontfamily):
        """
        4. Call the module that turns the font code into XML tags.
        """

        rtox.xml_font_tags.XMLTagSets.xml_font_tags(
            self=rtox.xml_font_tags.XMLTagSets(
                debug_dir=self.debut_dir,
                fontnum=fontnum,
                fontfamily=fontfamily,
                xml_tag_num=self.xml_tag_num))
