#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "__main__"

# From local application
import debugdir_clean
import doc_parser
import docinfo_parser
import final_step
import header_parser_step_one
import header_parser_step_two
import header_parser_step_three
import prepare_to_process
import tag_closer


# TODO Add PYTHONDONTWRITEBYTECODE=1 to environment variables before making
#  app package. This will permanently suppress __pycache__

if __name__ == "__main__":
    # Working files are left in debugdir at the end of a run for debugging
    # purposes, but cleaned out at the beginning of a run.
    debugdir_clean.cleaner()

    # Set basic variables.
    base_script_dir_pass = ""
    config_file_pass = "Config.ini"
    debug_dir_pass = ""
    input_file_name_pass = ""
    output_file_name_pass = ""

    styles_status_list = []

    # Get and store configuration information.
    # TODO Renaming needed: preparetoprocess, prepare_to_process,
    #  PrepareToProcess
    preparetoprocess = prepare_to_process.PrepareToProcess(
        base_script_dir=base_script_dir_pass,
        config_file=config_file_pass,
        debug_dir=debug_dir_pass,
        input_file_name=input_file_name_pass,
        output_file_name=output_file_name_pass)

    # TODO Break this into four function calls?
    base_script_dir_pass, debug_dir_pass, input_file_name, output_file_name = \
        prepare_to_process.PrepareToProcess.extract_config_settings(
            self=preparetoprocess)

    # Get the user's preference for XML tag style.
    xml_tag_num_pass = prepare_to_process.PrepareToProcess.\
        extract_users_preferred_xml_tag_style()

    # Prepare a working copy of the input file.
    working_input_file_pass = prepare_to_process.PrepareToProcess\
        .prepare_working_input_file(
            self=preparetoprocess)

    # Prepare a working copy of the file for XML tags.
    prepare_to_process.PrepareToProcess.prepare_working_xml_file(
        self=preparetoprocess, xml_tag_num=xml_tag_num_pass)

    # Prepare a working copy of the tag registry.
    prepare_to_process.PrepareToProcess.create_working_tag_registry(
        self=preparetoprocess)

    # Create dictionary to store header table information.
    prepare_to_process.PrepareToProcess.create_header_table_dict(
        self=preparetoprocess)

    # Process the pre-table portion of the header.
    header_parser_step_one.PretableController(
        debug_dir=debug_dir_pass,
        working_input_file=working_input_file_pass)

    # Process the table portion of the header.
    header_parser_step_two.process_the_tables(
        working_input_file=working_input_file_pass,
        debug_dir=debug_dir_pass)

    header_parser_step_three.ProcessTheTables(
        working_input_file=working_input_file_pass,
        debug_dir=debug_dir_pass)

    # Process the info portion of the document body.
    docinfo_parser.DocinfoParse.process_docinfo(
        self=docinfo_parser.DocinfoParse(
            debug_dir=debug_dir_pass,
            working_input_file=working_input_file_pass))

    # Process the main portion of the document body.
    # TODO Add capability to handle numbered paragraphs: spec p.48.
    # TODO Add capability to handle tables: spec p.59.
    line_to_get = doc_parser.choose_starting_line_number(
        debug_dir=debug_dir_pass)
    tag_dict = doc_parser.select_tag_dict(xml_tag_num=xml_tag_num_pass)
    file_length = doc_parser.find_length_working_input_file(
        working_input_file=working_input_file_pass)

    keyword_process_list, line_to_search = \
        doc_parser.GetKeywordsAndLinenumbers.line_keyword_checker_processor(
            self=doc_parser.GetKeywordsAndLinenumbers(
                working_input_file=working_input_file_pass,
                file_length=file_length, line_to_get=line_to_get,
                debug_dir=debug_dir_pass))

    doc_parser.sort_keyword_linenumber_list(
        keyword_linenumber_list=keyword_linenumber_list)
    doc_parser.insert_transition_tags(
        debug_dir=debug_dir_pass, tag_dict=tag_dict)
    doc_parser.parse_each_keyword_line(
        keyword_linenumber_list=keyword_linenumber_list,
        debug_dir=debug_dir_pass, tag_dict=tag_dict,
        working_input_file=working_input_file_pass, line_to_read=____)

    # Close open tags where possible and produce list of remaining open tags.
    tag_closer.tag_closer(debug_dir=debug_dir_pass,
                          xml_tag_num=xml_tag_num_pass)

    # Do file clean up, post-processing, and put the renamed file in the
    # output directory.
    final_step.final_step(debug_dir=debug_dir_pass,
                          xml_tag_num=xml_tag_num_pass,
                          output_file_name=output_file_name,
                          base_script_dir=base_script_dir_pass)
