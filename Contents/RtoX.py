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

# From standard libraries
import os

# From local application
import create_files
import debugdir_clean
from process_body import doc_parser
import header_parser_step_one
import header_parser_step_two
import header_parser_step_three
import prepare_to_process
# import xml_transition_tags


# TODO Add PYTHONDONTWRITEBYTECODE=1 to environment variables before making
#  app package. This will permanently suppress __pycache__
from process_body.doc_parser import MainDocManager

if __name__ == "__main__":
    # TODO Add garbage module as last run module to clean out debugdir and do
    #  any other necessary cleanup, instead of doing cleanup here.
    debugdir_clean.cleaner()

    # Get and store configuration information.
    base_script_dir, debug_dir, config_file = \
        prepare_to_process.extract_config_settings(
            base_script_dir="", debug_dir="", config_file="Config.ini")

    input_file_name, output_file_name = \
        prepare_to_process.extract_file_info(
            base_script_dir=base_script_dir, debug_dir=debug_dir,
            config_file=config_file)

    # Get the user's preference for XML tag style.
    xml_tag_num = prepare_to_process.extract_users_xml_tag_style(
        debug_dir=debug_dir)

    # Prepare working files.
    working_input_file = create_files.initiate_working_files(
        debug_dir=debug_dir,
        input_file_name=input_file_name,
        base_script_dir=base_script_dir)

    # Process the pre-table portion of the header.
    header_parser_step_one.PretableController(
        working_input_file=working_input_file, debug_dir=debug_dir)

    # Process the table portion of the header.
    header_parser_step_two.process_the_tables(
        working_input_file=working_input_file, debug_dir=debug_dir)

    header_parser_step_three.ProcessTheTables.\
        analyze_table_code_strings_controller(
            self=header_parser_step_three.ProcessTheTables(
                working_input_file=working_input_file, debug_dir=debug_dir))

    # TODO Add capability to handle numbered paragraphs: spec p.48.
    # TODO Add capability to handle tables: spec p.59.

    cw_dirs = [base_script_dir, "/Library/dicts/", "control_word_dict.json"]
    control_word_dict = ''.join(cw_dirs)

    doc_parser.MainDocManager.body_parse_manager(
        self=MainDocManager(
            working_input_file=working_input_file,
            debug_dir=debug_dir,
            control_word_dict=control_word_dict))

    # tag_dict = doc_parser.select_tag_dict(xml_tag_num=xml_tag_num)
    #
    # keyword_translation_stack, line_to_search = \
    #     doc_parser.GetKeywordsAndLinenumbers.line_keyword_checker_processor(
    #         self=doc_parser.GetKeywordsAndLinenumbers(
    #             working_input_file=working_input_file,
    #             line_to_get=line_to_get))
    #
    # keyword_translation_stack = doc_parser.sort_keyword_translation_stack(
    #     keyword_translation_stack=keyword_translation_stack)
    #
    # xml_transition_tags.xml_transition_tags(debug_dir=debug_dir,
    #                                         tag_dict=tag_dict)
    #
    # doc_parser.parse_each_keyword_line(
    #     keyword_translation_stack=keyword_translation_stack,
    #     debug_dir=debug_dir, tag_dict=tag_dict,
    #     working_input_file=working_input_file)

    # Close open tags where possible and produce list of remaining open tags.
    # tag_closer.tag_closer(debug_dir=debug_dir,
    #                       xml_tag_num=xml_tag_num)

    # Do file clean up, post-processing, and put the renamed file in the
    # output directory.
    # final_step.final_step(debug_dir=debug_dir,
    #                       xml_tag_num=xml_tag_num,
    #                       output_file_name=output_file_name,
    #                       base_script_dir=base_script_dir)
    # TODO Include in final step: 1) garbage cleanup, 2) copy
    #  control_word_missing_dict.json contents to XXX and sort
    #  that file.
