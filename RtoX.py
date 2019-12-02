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
import pytest
import rtox.color_table
import rtox.csv_prep
import rtox.doc_info_read
import rtox.file_table
import rtox.first_line
import rtox.font_table
import rtox.header_structure
import rtox.input_file_prep
import rtox.prelim
import rtox.read_configuration
import rtox.rtf_codes_file_prep
import rtox.style_sheet_table


class MainRtoX:
    def __init__(self,
                 bs_dir,
                 db_dir,
                 if_name,
                 of_name,
                 config_file
                 ):
        self.__base_script_dir = bs_dir
        self.__debug_dir = db_dir
        self.__input_file_name = if_name
        self.__output_file_name = of_name
        self.__config_file = config_file

    def prelim_routine(self):
        """
        Gather and record in dictionaries command line and config settings
        to run RtoX.
        :return: self.__base_script_dir: directory for main RtoX script
        :return: self.__debug_dir: directory for working files created during
        program run
        :return: self.__input_file_name: name of RTF file to convert
        :return: self.__output_file_name: name of XML file to create
        """
        prelim_vars = rtox.prelim.Prelim.prelim_settings(
            rtox.prelim.Prelim(
                config_file=self.__config_file,
                base_script_dir=self.__base_script_dir,
                debug_dir=self.__debug_dir))
        self.__base_script_dir = prelim_vars[0]
        self.__debug_dir = prelim_vars[1]
        config_file = prelim_vars[2]

        config_vars = rtox.prelim.Prelim.config_messages(
            config_file=config_file,
            debug_dir=self.__debug_dir)
        self.__input_file_name = config_vars[0]
        self.__output_file_name = config_vars[1]

        return self.__base_script_dir, self.__debug_dir, \
            self.__input_file_name, self.__output_file_name

    @staticmethod
    def prep_rtf_file(debug_dir, base_script_dir):
        """
        Create a copy of the input file for use during processing. Create an
        XML file to place tags during processing (will become the output file).
        :param debug_dir:
        :param base_script_dir:
        :return: working_file: variable name for copy of input file used during
        processing
        """
        working_file = rtox.input_file_prep.InputPrep.input_file_prep(
            rtox.input_file_prep.InputPrep(
                input_file_name=input_file_name,
                debug_dir=debug_dir,
                base_script_dir=base_script_dir))
        return working_file

    @staticmethod
    def header_structure():
        """
        Determine what tables are in the RTF header and store the table name
        and its line location in a dictionary.
        """
        rtox.header_structure.HeaderStructure.table_check(
            rtox.header_structure.HeaderStructure(
                working_file=working_file_pass,
                debug_dir=debug_dir_pass))

    @staticmethod
    def rtf_first_line():
        """
        Process the first line of the RTF file.
        """
        rtox.first_line.FirstLine.line_parse(
            rtox.first_line.FirstLine(
                debug_dir=debug_dir_pass,
                working_file=working_file_pass,
                base_script_dir=base_script_dir_pass))

    @staticmethod
    def xml_tag_pref():
        """
        Determine user's prefersence for XML tag style and use appropriate
        dictionary.
        :return: tag_dict: XML dictionary based on user preference
        """

        from debugdir.config_dict import config_dictionary as rtf_settings_dict

        xml_tag_num = rtf_settings_dict.get("tag-style")
        if xml_tag_num is None:
            xml_tag_num = 1
        else:
            pass

        if xml_tag_num == "1":
            tag_dict = os.path.join(debug_dir_pass, "xml_tags.py")
        elif xml_tag_num == "2":
            tag_dict = os.path.join(debug_dir_pass, "tei_tags.py")
        elif xml_tag_num == "3":
            tag_dict = os.path.join(debug_dir_pass, "tpres_tags.py")
        else:
            tag_dict = os.path.join(debug_dir_pass, "xml_tags.py")

        return tag_dict, xml_tag_num

    @staticmethod
    def font_table():
        """
        If there is a font table, process the font settings for each font
        number. Those settings become tag(s) in the XML document.
        :return: line_to_check: tracks the line in the working file to process
        :return: xml_tag_num: tracks the user's XML tag-style selection
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "fonttbl" in htd.keys():
            table_state = 0
        else:
            table_state = 1

        line_to_check = htd['fonttbl'] + 1

        while table_state == 0:

            table_state = rtox.font_table.FonttblParse.find_fonts(
                self=rtox.font_table.FonttblParse(
                    working_file=working_file_pass,
                    line_to_read=line_to_check,
                    debug_dir=debug_dir_pass,
                    table_state=table_state,
                    xml_tag_num=xml_tag_num_pass))

    @staticmethod
    def file_table(xml_tag_num):
        """
        If a file table exists in RTF file, add appropriate tags to XML file.
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "filetbl" in htd.keys():

            line_to_check = htd['filetbl'] + 1

            file_table_vars = rtox.file_table.FiletblParse.file_table(
                rtox.file_table.FiletblParse(
                    working_file=working_file_pass,
                    line_to_check=line_to_check,
                    debug_dir=debug_dir_pass),
                xml_tag_num=xml_tag_num)
            line_to_check = file_table_vars

            return line_to_check

        else:
            pass

    @staticmethod
    def color_table(xml_tag_num):
        """
        If a color table exists in RTF file, add appropriate tags to XML file.
        """

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "colortbl" in htd.keys():

            line_to_check = htd['colortbl'] + 1

            color_table_vars = rtox.color_table.ColortblParse.color_table(
                rtox.color_table.ColortblParse(
                    working_file=working_file_pass,
                    line_to_check=line_to_check,
                    debug_dir=debug_dir_pass),
                xml_tag_num=xml_tag_num)
            line_to_check = color_table_vars

            return line_to_check

        else:
            pass

    @staticmethod
    def style_sheet_table():

        from debugdir.header_tables_dict import header_tables_dictionary as htd
        if "stylesheet" in htd.keys():
            style_state = 0
        else:
            style_state = 1

        line_to_check = htd['stylesheet'] + 1

        while style_state == 0:

            style_state = rtox.style_sheet_table.StyleSheetParse.find_styles(
                self=rtox.style_sheet_table.StyleSheetParse(
                    debug_dir=debug_dir_pass,
                    line_to_check=line_to_check,
                    working_file=working_file_pass,
                    style_state=style_state,
                    xml_tag_num=xml_tag_num_pass))


if __name__ == "__main__":
    pytest.main()

    # Prepare rtf file and read codes to be used in processing document text.
    vars_init = MainRtoX.prelim_routine(
        self=MainRtoX(
            bs_dir="",
            db_dir="",
            if_name="",
            of_name="",
            config_file=""))
    base_script_dir_pass = vars_init[0]
    debug_dir_pass = vars_init[1]
    input_file_name = vars_init[2]
    output_file_name = vars_init[3]

    # Prepare rtf input file for processing.
    working_file_pass = MainRtoX.prep_rtf_file(
        base_script_dir=base_script_dir_pass,
        debug_dir=debug_dir_pass)

    # ############### Begin Header Processing

    # Determine header structure of rtf input document.
    MainRtoX.header_structure()

    # Process first line of rtf input document.
    MainRtoX.rtf_first_line()

    # Determine user's preference for xml tag style.
    tag_pref_vars = MainRtoX.xml_tag_pref()
    tag_dict_pass = tag_pref_vars[0]
    xml_tag_num_pass = tag_pref_vars[1]

    # Set up a basic xml file to store font, color, etc. rtf codes in xml
    # format.
    rtox.rtf_codes_file_prep.RTFCodesPrep.rtf_codes_to_xml_prep(
        self=rtox.rtf_codes_file_prep.RTFCodesPrep(
            debug_dir=debug_dir_pass,
            xml_tag_num=xml_tag_num_pass))

    # Set up csv files for processed rtf codes.
    rtox.csv_prep.CSVPrep.csv_file_prep(
        self=rtox.csv_prep.CSVPrep(
            debug_dir=debug_dir_pass))

    # Process font table rtf codes.
    MainRtoX.font_table()

    # Process file table rtf codes.
    MainRtoX.file_table(
        xml_tag_num=xml_tag_num_pass)

    # Process color table rtf codes.
    MainRtoX.color_table(
        xml_tag_num=xml_tag_num_pass)

    # Process style sheet table rtf codes.
    MainRtoX.style_sheet_table()

    # MainRtoX.list_table(
    #   xml_tag_num=xml_tag_num_pass)

    # MainRtoX.rev_table(
    #   xml_tag_num=xml_tag_num_pass)

    # MainRtoX.rsid_table(
    #   xml_tag_num=xml_tag_num_pass)

    # MainRtoX.generator(
    #   xml_tag_num=xml_tag_num_pass)

    # ############### End Header Processing

    # Process info section of document.
    # Find beginning of info section.
    info_start_vars = rtox.doc_info_read.DocInfoRead.info_start(
        self=rtox.doc_info_read.DocInfoRead(
            debug_dir=debug_dir_pass,
            working_file=working_file_pass))
    line_counter_pass = info_start_vars[0]
    line_number_pass = info_start_vars[1]
    start_line_pass = info_start_vars[2]
    line_to_scan_pass = info_start_vars[3]

    if line_counter_pass < line_number_pass:

        running_line = ""
        # Test for end of info section.
        first_test_vars = rtox.doc_info_read.DocInfoRead.info_end_test(
            self=rtox.doc_info_read.DocInfoRead(
                debug_dir=debug_dir_pass,
                working_file=working_file_pass),
            line_counter=line_counter_pass,
            running_line=running_line)
        running_line_pass = first_test_vars

    else:
        running_line_pass = line_to_scan_pass
        pass

    text_to_process_pass = rtox.doc_info_read.DocInfoRead.process_text(
        line_to_scan=line_to_scan_pass,
        running_line=running_line_pass)

    chars = "}{"
    info_list = rtox.doc_info_read.DocInfoRead.split_between(
        text_to_process=text_to_process_pass,
        chars=chars)

    rtox.doc_info_read.DocInfoRead.info_to_csv(
        self=rtox.doc_info_read.DocInfoRead(
            working_file=working_file_pass,
            debug_dir=debug_dir_pass),
        result_list=info_list)
