#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

"""
Parse the font table and pass the values to the rtox_db, fontcodes schema.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "Contents.Library.font_table"

# From standard libraries
import psycopg2
import re
import sys

# From local application
import split_between_characters
import table_boundaries
import xml_font_tags
from Contents.log_config import logger
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class FonttblParse:
    """
    Process font table settings from the RTF header.
    1. Find the beginning and end of a font code definition.
    2. Process the text from the working file, by separating the font code
    into its constituent pieces (e.g., font number, font family).
    3. Store the settings for the font code in the rtox_db, fontcodes schema.
    4. Turn the settings into XML tags using the tag style preference set by
    the user.
    """

    def __init__(self,
                 working_file: str,
                 line_to_read: str,
                 debug_dir: str,
                 xml_tag_num: str,
                 table: str) -> None:
        self.working_file = working_file
        self.line_to_read = line_to_read
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.table = table

    def find_fonts(self) -> None:
        """
        Find the start and end of the font table and then parse the font
        table into font code strings and each string into its constituent parts.
        """
        # Find the text to process in the table.
        text_to_process = table_boundaries.TableBounds.table_start_end(
            self=table_boundaries.TableBounds(
                line_number=self.line_to_read,
                table=self.table))

        # Split the font code list into separate strings, one per font code.
        font_code_strings = split_between_characters.SplitBetween.\
            split_between(self=split_between_characters.SplitBetween(
                            text_to_process=text_to_process,
                            split_characters="}{"))

        # TODO Continue using database for storage?
        # Separate each font code string into its parts and return the
        # values for each part.
        for font_code in font_code_strings:
            # TODO Could this be simplified using a list (fontnum,
            #  fontfamily, etc) and a string plus f string?
            fontnum = SetFonts.fontnum(self=SetFonts(font_code=font_code))
            fontfamily = SetFonts.fontfamily(self=SetFonts(font_code=font_code))
            fcharset = SetFonts.fcharset(self=SetFonts(font_code=font_code))
            fprq = SetFonts.fprq(self=SetFonts(font_code=font_code))
            panose = SetFonts.panose(self=SetFonts(font_code=font_code))
            fname = SetFonts.fname(self=SetFonts(font_code=font_code))
            altname = SetFonts.altname(self=SetFonts(font_code=font_code))
            fontemb = SetFonts.fontemb(self=SetFonts(font_code=font_code))
            cpg = SetFonts.cpg(self=SetFonts(font_code=font_code))

            set_font_vars = [fontnum, fontfamily, fcharset, fprq, panose,
                             fname, altname, fontemb, cpg]

            StoreFonts.font_db(self=StoreFonts(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num,
                set_font_vars=set_font_vars))

            StoreFonts.tag_it(self=StoreFonts(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num,
                set_font_vars=set_font_vars),
                fontnum=fontnum, fontfamily=fontfamily)


class SetFonts:
    def __init__(self,
                 font_code: str
                 ) -> None:
        self.font_code = font_code

    def fontnum(self) -> str:
        """
        Each font code is defined by a unique font number (e.g.,
        fontnum = f0).
        """

        try:
            test = re.search(r'\\f[0-9]+', self.font_code)
            fontnum = test[0].replace("\\", "")
            return fontnum
        except TypeError:
            # TODO The remedy here is not to quit but simply to provide the
            #  information. This is not critical to the program's function.
            logger.debug(msg="There is an error in the font table "
                             f'A font number is missing. RtoX will now quit.\n')
            sys.exit(1)

    def fontfamily(self) -> str:
        """
        Each font code may define its font family.
        """

        # TODO Update font names to valid names for XML/HTML.
        font_families = dict([
                        ("fnil", "default"),
                        ("froman", "Times New Roman"),
                        ("fswiss", "Arial"),
                        ("fmodern", "Courier"),
                        ("fscript", "Cursive"),
                        ("fdecor", "Old English"),
                        ("ftech", "Symbol"),
                        ("fbidi", "Miriam")
        ])

        for key in font_families:
            if re.search(r"\\"+key, self.font_code) is not None:
                fontfamily = font_families.get(key, "None")
                return fontfamily
            else:
                pass

    def fcharset(self) -> str:
        """
        Each font code may define the character set it uses.
        """
        try:
            test = re.search(r'\\fcharset([0-9])+', self.font_code)
            fcharset = test[0].replace("\\fcharset", "")
            return fcharset
        except TypeError:
            fcharset = "0"
            return fcharset

    def fprq(self) -> str:
        """
        Each font code may define the font pitch (default, fixed or
        variable).
        """
        try:
            test = re.search(r'\\fprq([0-9])+', self.font_code)
            fprq = test[0].replace("\\fprq", "")
            return fprq
        except TypeError:
            fprq = "0"
            return fprq

    def panose(self) -> str:
        """
        If present, it contains a 10-byte Panose 1 number. Each byte
        represents a single font property as defined by the Panose 1 standard
        specification.
        """
        try:
            test = re.search(re.compile(r'\\\*\\[0-9]+'), self.font_code)
            panose = test[0].replace(test[0], "")
            return panose
        except TypeError:
            panose = "0"
            return panose

    def fname(self) -> str:
        """
        Each code may have a non-tagged name.
        """
        try:
            test = re.search(r'(\s\w+)+(;)*', self.font_code)
            fname_pre = test.group(0).replace(";", "")
            fname = fname_pre.lstrip()
            return fname
        except TypeError:
            fname = "None"
            return fname

    def altname(self) -> str:
        """
        Each font code may use an alternative name.
        """
        try:
            test = re.search(re.compile(r'\\\*\\falt\s'), self.font_code)
            altname = test[0].replace(test[0], "")
            return altname
        except TypeError:
            altname = "None"
            return altname

    def fontemb(self) -> bool:
        """
        Each code may contain an embedded font. At present, RtoX does not
        support capturing information about the embedded font.
        """
        try:
            if re.search(r'{\\fontemb', self.font_code) is not None:
                fontemb = True
                return fontemb
            else:
                fontemb = False
                return fontemb
        except TypeError:
            fontemb = False
            return fontemb

    def cpg(self) -> str:
        """
        Each font code may use a specified code page (e.g. Microsoft 1252).
        """
        try:
            test = re.search(r'{\\cpg([0-9])+', self.font_code)
            cpg = test[0].replace("\\cpg", "")
            return cpg
        except TypeError:
            cpg = "0"
            return cpg


class StoreFonts:
    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str,
                 set_font_vars: list
                 ) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num
        self.set_font_vars = set_font_vars

    def font_db(self) -> None:
        """
        Store the settings for each font code in the rtox_db, fontcode
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
            postgres_insert_query = """INSERT INTO rtox_db.fontcodes.fontinfo
                (FONTNUM, FONTFAMILY, FCHARSET, FPRQ, PANOSE, FNAME,
                 ALTNAME, FONTEMB, CPG) VALUES (%s, %s, %s, %s, %s, 
                 %s, %s, %s, %s)"""
            record_to_insert = (self.set_font_vars[0], self.set_font_vars[1],
                                self.set_font_vars[2], self.set_font_vars[3],
                                self.set_font_vars[4], self.set_font_vars[5],
                                self.set_font_vars[6], self.set_font_vars[7],
                                self.set_font_vars[8])
            cur.execute(postgres_insert_query, record_to_insert)
            con.commit()

        except psycopg2.DatabaseError as err:
            pg_err = str(err.pgcode)
            sys.stdout.write("Problem entering font codes in database.\n"
                             f"Error number {pg_err}; {err}\n")

        if con is not None:
            cur.close()
            con.close()

    # TODO The whole tag creation and writing process does not result in
    #  anything used in the final product. Decide what to do with these and
    #  associated functions.
    def tag_it(self, fontnum: str, fontfamily: str) -> None:
        """
        Turn the font code into XML tags.
        """

        xml_font_tags_vars = xml_font_tags.XMLTagSets.xml_font_tags(
            self=xml_font_tags.XMLTagSets(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num),
            fontnum=fontnum,
            fontfamily=fontfamily)

        xml_font_tags.XMLTagSets.make_new_tags(
            self=xml_font_tags.XMLTagSets(
                debug_dir=self.debug_dir,
                xml_tag_num=self.xml_tag_num),
            xml_font_tags_vars=xml_font_tags_vars)
