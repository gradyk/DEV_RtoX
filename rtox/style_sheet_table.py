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
Parse stylesheet(s).
1.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "style_sheet"

import psycopg2
import re
import rtox.lib.split_between_characters
import rtox.lib.table_boundaries
import rtox.xml_style_tags
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class StyleSheetParse:
    def __init__(self,
                 working_file: str,
                 debug_dir: str,
                 xml_tag_num: str,
                 line_number: str,
                 table: str) -> None:
        self.working_file = working_file
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.line_number = line_number
        self.table = table

    def find_styles(self):
        """
        1. Find the beginning and end of the table.
        """
        tse_vars = rtox.lib.table_boundaries.TableBounds.table_start_end(
            self=rtox.lib.table_boundaries.TableBounds(
                line_number=self.line_number,
                table=self.table))

        """
        2. Split the style code list into separate strings, one per style code.
        """
        style_code_strings = rtox.lib.split_between_characters.SplitBetween.\
            split_between(self=rtox.lib.split_between_characters.SplitBetween(
                            text_to_process=tse_vars[2],
                            split_characters="}{"))

        """
        3. Separate each style code string into its parts and return the 
        values for each part so that they can be stored in the rtox_db database.
        """
        for style_code in style_code_strings:

            try:

                code_vars = SetStyles.code(self=SetStyles(
                    style_code=style_code))
                status = code_vars[0]
                code = code_vars[1]

                if status == 1:

                    italic = SetStyles.italic(
                        self=SetStyles(style_code=style_code))
                    bold = SetStyles.bold(self=SetStyles(style_code=style_code))
                    underline = SetStyles.underline(
                        self=SetStyles(style_code=style_code))
                    strikethrough = SetStyles.strikethrough(
                        self=SetStyles(style_code=style_code))
                    small_caps = SetStyles.small_caps(
                        self=SetStyles(style_code=style_code))
                    additive = SetStyles.additive(
                        self=SetStyles(style_code=style_code))
                    style_name = SetStyles.style_name(
                        self=SetStyles(style_code=style_code))
                    style_next_paragraph = SetStyles.style_next_paragraph(
                        self=SetStyles(style_code=style_code))

                    set_styles_vars = [code, italic, bold, underline,
                                       strikethrough, small_caps, additive,
                                       style_name, style_next_paragraph]

                    StoreStyles.style_db(
                        self=StoreStyles(set_styles_vars=set_styles_vars,
                                         debug_dir=self.debug_dir,
                                         code=code))

                else:
                    pass

            except TypeError:
                pass


class SetStyles:
    def __init__(self,
                 style_code: str
                 ):
        self.style_code = style_code

    def code(self) -> tuple:
        """

        """
        code = None
        code_styles = [
            r"{\s",
            r"{\*\cs",
            r"{\ds",
            r"{\trowd",
            r"{\tsrowd",
        ]

        status = 0
        for key in code_styles:
            test = re.search(re.escape(key) + r'[0-9]*', self.style_code)
            if test is not None:
                test = test[0]
                code = test.replace("{\\", "")
                code = code.replace("*\\", "")
                status = 1
            else:
                pass

        return status, code

    def italic(self) -> str:
        """

        """
        try:
            test = re.search(r"\\i[0-9]*", self.style_code)
            italic = test[0].replace("\\i", "")
            if italic == "":
                italic = "1"
            else:
                pass
            return italic
        except TypeError:
            italic = "0"
            return italic

    def bold(self) -> str:
        """

        """
        try:
            test = re.search(r"\\b[0-9]*", self.style_code)
            bold = test[0].replace("\\b", "")
            if bold == "":
                bold = "1"
            else:
                pass
            return bold
        except TypeError:
            bold = "0"
            return bold

    def underline(self) -> str:
        """

        """
        try:
            test = re.search(r"\\ul[0-9]*", self.style_code)
            underline = test[0].replace("\\ul", "")
            if underline == "":
                underline = "1"
            else:
                pass
            return underline
        except TypeError:
            underline = "0"
            return underline

    def strikethrough(self) -> str:
        """

        """
        try:
            test = re.search(r"\\strike[0-9]*", self.style_code)
            strikethrough = test[0].replace("\\strike", "")
            if strikethrough == "":
                strikethrough = "1"
            else:
                pass
            return strikethrough
        except TypeError:
            strikethrough = "0"
            return strikethrough

    def small_caps(self) -> str:
        """

        """
        try:
            test = re.search(r"\\scaps[0-9]*", self.style_code)
            small_caps = test[0].replace("\\scaps", "")
            if small_caps == "":
                small_caps = "1"
            else:
                pass
            return small_caps
        except TypeError:
            small_caps = "0"
            return small_caps

    def additive(self) -> bool:
        """

        """
        try:
            if re.search(r'\\additive', self.style_code) is not None:
                additive = True
                return additive
            else:
                additive = False
                return additive
        except TypeError:
            additive = False
            return additive

    def style_name(self) -> str:
        """

        """
        pattern = r'\s(\w+|\s|\W)+'
        styledef = re.search(pattern, self.style_code)
        if styledef:
            style_name_pre_1 = styledef[0].rstrip()
            style_name = style_name_pre_1[:-1]
            return style_name
        else:
            style_name = "None"
            return style_name

    def style_next_paragraph(self) -> str:
        """

        """
        try:
            test = re.search(r"\\snext[0-9]*", self.style_code)
            style_next_paragraph = test[0].replace("\\", "")
            return style_next_paragraph
        except TypeError:
            style_next_paragraph = "0"
            return style_next_paragraph


class StoreStyles:
    def __init__(self,
                 set_styles_vars: list,
                 debug_dir: str,
                 code: str
                 ) -> None:
        self.set_styles_vars = set_styles_vars
        self.debug_dir = debug_dir
        self.code = code

    def style_db(self) -> None:
        """
        13. Store the settings for each font code in the rtox_db, fontcode
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
            postgres_insert_query = """INSERT INTO rtox_db.stylecodes.style_type
                (CODE, ITALIC, BOLD, UNDERLINE, STRIKETHROUGH, SMALL_CAPS, 
                ADDITIVE, STYLE_NAME, STYLE_NEXT_PARAGRAPH) VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

            record_to_insert = (self.set_styles_vars[0],
                                self.set_styles_vars[1],
                                self.set_styles_vars[2],
                                self.set_styles_vars[3],
                                self.set_styles_vars[4],
                                self.set_styles_vars[5],
                                self.set_styles_vars[6],
                                self.set_styles_vars[7],
                                self.set_styles_vars[8])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering style codes in database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()

    def tag_it(self) -> None:
        """
        Write the style information to a csv file.
        """

        rtox.xml_style_tags.XMLTagSets.xml_style_tags(
            self=rtox.xml_style_tags.XMLTagSets(
                debug_dir=self.debug_dir,
                code=self.code,
                set_styles_vars=self.set_styles_vars))
