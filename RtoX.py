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

""" This is the main script for the RtoX program. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "__main__"

import os
import rtox.color_table
import rtox.first_line
import rtox.font_table
import rtox.HeaderParse
import rtox.header_structure
import rtox.input_file_prep
import rtox.prelim
import rtox.read_configuration
import rtox.style_sheet_table


class MainRtoX:
    def __init__(self,
                 bs_dir,
                 db_dir,
                 if_name,
                 of_name
                 ):
        self.__base_script_dir = bs_dir
        self.__debug_dir = db_dir
        self.__input_file_name = if_name
        self.__output_file_name = of_name

    def prelim_routine(self):
        prelim_vars = rtox.prelim.Prelim.prelim_settings()
        self.__base_script_dir = prelim_vars[0]
        self.__debug_dir = prelim_vars[1]

        config_vars = rtox.prelim.Prelim.config_messages()
        self.__input_file_name = config_vars[0]
        self.__output_file_name = config_vars[1]

        return self.__base_script_dir, self.__debug_dir, \
            self.__input_file_name, self.__output_file_name

    def prep_rtf_file(self):
        rtox.input_file_prep.InputPrep.input_file_prep(
            rtox.input_file_prep.InputPrep(
                input_file_name=self.__input_file_name,
                debug_file_dir=self.__debug_dir,
                base_script_dir=self.__base_script_dir))

    def header_structure(self):
        rtox.header_structure.HeaderStructure.table_check(
            rtox.header_structure.HeaderStructure(
                input_file_name=self.__input_file_name,
                debug_dir=self.__debug_dir))

    def rtf_first_line(self):
        rtox.first_line.FirstLine.line_parse(
            rtox.first_line.FirstLine(
                debug_dir=self.__debug_dir,
                input_file_name=self.__input_file_name))

    @staticmethod
    def font_table():

        with open(os.path.join(debug_dir, "config_dict.py")) as cd:
            settings_dict = dict(cd)
            xml_tag = settings_dict["tag-style"]
            if xml_tag == 1:
                tag_dict = os.path.join(debug_dir, "xml_tags.py")
            elif xml_tag == 2:
                tag_dict = os.path.join(debug_dir, "tei_tags.py")
            elif xml_tag == 3:
                tag_dict = os.path.join(debug_dir, "tpres_tags.py")

        while font_table == 1:

            with open(os.path.join(debug_dir, "header_tables_dict.py")) as htd:

                table_dict = dict(htd)
                if table_dict["fonttbl"]:
                    line_to_read = table_dict['fonttbl'] + 1
                    build_font_vars = rtox.font_table.FonttblParse.set_fonts(
                        self=rtox.font_table.FonttblParse(
                            input_file_name=input_file_name,
                            line_to_read=line_to_read,
                            tag_dict=tag_dict,
                            debug_dir=debug_dir))
                    font_code_list = build_font_vars[0]

                    rtox.font_table.FonttblParse.update_rtf_file_codes(
                        font_code_list=font_code_list,
                        self=rtox.font_table.FonttblParse(
                            input_file_name=input_file_name,
                            line_to_read=line_to_read,
                            tag_dict=tag_dict,
                            debug_dir=debug_dir))
                else:
                    font_table_end_check = rtox.font_table.FonttblParse.\
                        font_table_end(
                            self=rtox.font_table.FonttblParse(
                                input_file_name=input_file_name,
                                line_to_read=line_to_read,
                                tag_dict=tag_dict,
                                debug_dir=debug_dir))
                    line_to_read = font_table_end_check[0]

        return xml_tag, line_to_read

    @staticmethod
    def color_table(xml_tag, line_to_read):
        """
        Check to make sure RTF input file actually is an rtf file.
        """

        line_to_read += 1
        color_vars = rtox.color_table.ColortblParse.color_table(
            rtox.color_table.ColortblParse(
                input_file_name=input_file_name,
                line_to_read=line_to_read,
                xml_tag=xml_tag))
        line_to_read = color_vars[0]

        return line_to_read

    def style_sheet_table(self):
        style_sheet_vars = rtox.style_sheet_table.StyleSheetParse.set_styles(
           )
        style_sheet = style_sheet_vars[0]
        hdr_line_count = style_sheet_vars[1]

        match_symbol = ""
        while style_sheet == 1:
            rtox.HeaderParse.HeaderParse.build_style_sheet_dict(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                style_sheet=style_sheet,
                debug_dir=debug_dir,
                rtf_line_to_read=hdr_line_count,
                match_symbol=match_symbol,
                self=rtox.HeaderParse.HeaderParse(
                    input_file_name=input_file_name,
                    debug_file_dir=debug_dir,
                    base_script_dir=base_script_dir))


if __name__ == "__main__":
    vars_init = MainRtoX.prelim_routine(
        self=MainRtoX(
            bs_dir="",
            db_dir="",
            if_name="",
            of_name=""))
    base_script_dir = vars_init[0]
    debug_dir = vars_init[1]
    input_file_name = vars_init[2]
    output_file_name = vars_init[3]

    MainRtoX.prep_rtf_file(
        rtox.input_file_prep.InputPrep.input_file_prep(
            rtox.input_file_prep.InputPrep(
                input_file_name=input_file_name,
                debug_file_dir=debug_dir,
                base_script_dir=base_script_dir)))

    MainRtoX.header_structure(
        rtox.header_structure.HeaderStructure.table_check(
            rtox.header_structure.HeaderStructure(
                input_file_name=input_file_name,
                debug_dir=debug_dir)))

    MainRtoX.rtf_first_line(
        rtox.first_line.FirstLine.line_parse(
            rtox.first_line.FirstLine(
                debug_dir=debug_dir,
                input_file_name=input_file_name)))

    font_table_vars = MainRtoX.font_table()
    xml_tag = font_table_vars[0]
    line_to_read = font_table_vars[1]

    MainRtoX.color_table(
        line_to_read=line_to_read,
        xml_tag=xml_tag)

    MainRtoX.style_sheet_table()



