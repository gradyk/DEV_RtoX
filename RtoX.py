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
This is the main script for the RtoX program.
1. Call prepare_to_process and set basic variables: base script
directory, config file directory, debug directory, input file name,
and output file name.
2. Call modules to get and store configuration information.
3. Clean the rtox_db by wiping all rows from all tables.
4. Set which XML tag file to use based on the user's preference.
5. Copy the input file to a working file for use during processing,
and create a file for XML tags that will become the XML output file.
6. [Setup csv file(s) for storing codes -- WILL BE DELETED ONCE DATABASE FULLY
FUNCTIONAL.]
7. Call the module to process the header.
8. Call the module to process the info portion of the document body.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "__main__"

# import pytest
import rtox.docinfo_parser
import rtox.header_parser
import rtox.prepare_to_process
import rtox.style_sheet_table


if __name__ == "__main__":
    # pytest.main()

    # 1. Set basic variables.
    file_structure_vars = rtox.prepare_to_process.PrepareToProcess\
        .file_structure(self=rtox.prepare_to_process.PrepareToProcess())
    base_script_dir_pass = file_structure_vars[0]
    config_file_pass = file_structure_vars[1]
    debug_dir_pass = file_structure_vars[2]
    input_file_name_pass = file_structure_vars[3]
    output_file_name_pass = file_structure_vars[4]

    # 2. Get and store configuration information.
    prelim_routine_vars = rtox.prepare_to_process.PrepareToProcess\
        .prelim_routine(
            self=rtox.prepare_to_process.PrepareToProcess(
                base_script_dir=base_script_dir_pass,
                config_file=config_file_pass, debug_dir=debug_dir_pass,
                input_file_name=input_file_name_pass,
                output_file_name=output_file_name_pass))
    base_script_dir_pass = prelim_routine_vars[0]
    debug_dir_pass = prelim_routine_vars[1]
    input_file_name = prelim_routine_vars[2]
    output_file_name = prelim_routine_vars[3]

    # 3. Clean the database.
    rtox.prepare_to_process.PrepareToProcess.rtox_db_clean()

    # 4. Set the file for XML tags.
    xml_vars = rtox.prepare_to_process.PrepareToProcess.xml_tag_pref(
        self=rtox.prepare_to_process.PrepareToProcess(
            base_script_dir=base_script_dir_pass, config_file=config_file_pass,
            debug_dir=debug_dir_pass, input_file_name=input_file_name_pass,
            output_file_name=output_file_name_pass))
    tag_dict_pass = xml_vars[0]
    xml_tag_num_pass = xml_vars[1]

    # 5. Prepare a copy of the input file and the file for XML tags.
    working_file_pass = rtox.prepare_to_process.StartProcess.prep_rtf_file(
        self=rtox.prepare_to_process.StartProcess(
            base_script_dir=base_script_dir_pass,
            debug_dir=debug_dir_pass,
            input_file_name=input_file_name,
            output_file_name=output_file_name),
        xml_tag_num=xml_tag_num_pass)

    # 6. Call the module to process the header.
    rtox.header_parser.DocHeaderParser.process_header(
        self=rtox.header_parser.DocHeaderParser(
            base_script_dir=base_script_dir_pass, debug_dir=debug_dir_pass,
            working_file=working_file_pass, xml_tag_num=xml_tag_num_pass))

    # 7. Call the module to process the info portion of the document body.
    rtox.docinfo_parser.DocinfoParse.process_docinfo(
        self=rtox.docinfo_parser.DocinfoParse(
            debug_dir=debug_dir_pass,
            working_file=working_file_pass,
            xml_tag_num=xml_tag_num_pass))

    # 8. Call the module to process the main portion of the document body.
