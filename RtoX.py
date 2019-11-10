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

import rtox.read_configuration
import rtox.HeaderParse


__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "__main__"

import rtox.first_line
import rtox.header_structure
import rtox.prelim


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

    @staticmethod
    def header_structure():
        rtox.header_structure.HeaderStructure.table_check(
            self=input_file_name)

    @staticmethod
    def rtf_first_line():
        rtox.first_line.FirstLine.line_parse(
            rtox.first_line.FirstLine(
                debug_dir=debug_dir,
                input_file_name=input_file_name))

    def font_table(self):

        font_table_vars = rtox.HeaderParse.HeaderParse.font_table(
            hdr_line_count=hdr_line_count,
            working_rtf_file=input_file_name
        )
        hdr_line_count = font_table_vars[0]
        working_rtf_file = font_table_vars[1]
        font_table = font_table_vars[2]

        while font_table == 1:

            build_font_vars = rtox.HeaderParse.HeaderParse.build_font_dict(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                font_table=font_table,
                debug_dir=debug_dir,
                self=rtox.HeaderParse.HeaderParse(
                    input_file_name=input_file_name,
                    debug_file_dir=debug_dir,
                    base_script_dir=base_script_dir))
            hdr_line_count = build_font_vars[1]
            font_table = build_font_vars[2]

            font_table_end_check = rtox.HeaderParse.HeaderParse.font_table_end(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                font_table=font_table)
            hdr_line_count = font_table_end_check[0]
            font_table = font_table_end_check[1]

    def header_routine(self, base_script_dir, debug_dir, input_file_name):
        """
        Check to make sure RTF input file actually is an rtf file.
        """

        rtox.HeaderParse.HeaderParse(
            input_file_name=input_file_name,
            debug_file_dir=debug_dir,
            base_script_dir=base_script_dir)

        header_vars = rtox.HeaderParse.HeaderParse.input_file_prep(
            self=rtox.HeaderParse.HeaderParse(
                input_file_name=input_file_name,
                debug_file_dir=debug_dir,
                base_script_dir=base_script_dir),
            debug_file_dir=debug_dir)

        hdr_line_count = header_vars[1]

        font_table_vars = rtox.HeaderParse.HeaderParse.font_table(
            hdr_line_count=hdr_line_count,
            working_rtf_file=input_file_name
        )
        hdr_line_count = font_table_vars[0]
        working_rtf_file = font_table_vars[1]
        font_table = font_table_vars[2]

        while font_table == 1:

            build_font_vars = rtox.HeaderParse.HeaderParse.build_font_dict(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                font_table=font_table,
                debug_dir=debug_dir,
                self=rtox.HeaderParse.HeaderParse(
                    input_file_name=input_file_name,
                    debug_file_dir=debug_dir,
                    base_script_dir=base_script_dir))
            hdr_line_count = build_font_vars[1]
            font_table = build_font_vars[2]

            font_table_end_check = rtox.HeaderParse.HeaderParse.font_table_end(
                working_rtf_file=working_rtf_file,
                hdr_line_count=hdr_line_count,
                font_table=font_table)
            hdr_line_count = font_table_end_check[0]
            font_table = font_table_end_check[1]

        hdr_line_count += 1
        color_vars = rtox.HeaderParse.HeaderParse.color_table(
            working_rtf_file=working_rtf_file,
            hdr_line_count=hdr_line_count)
        hdr_line_count = color_vars

        style_sheet_vars = rtox.HeaderParse.HeaderParse.style_sheet(
            working_rtf_file=working_rtf_file,
            hdr_line_count=hdr_line_count)
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

    MainRtoX.header_structure()

    MainRtoX.rtf_first_line()

    MainRtoX.font_table()

    header_routine(
        base_script_dir=base_script_dir,
        debug_dir=debug_dir,
        input_file_name=input_file_name,
        self=())
