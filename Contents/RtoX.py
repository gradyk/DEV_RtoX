#!/usr/local/bin
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
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
import create_files
import debugdir_clean
import doc_parser
import header_parser_step_one
import header_parser_step_two
import header_parser_step_three
import output_file_header
import output_file_transition
import prepare_to_process

from process_body.doc_parser import MainDocManager

# TODO Add PYTHONDONTWRITEBYTECODE=1 to environment variables before making
#  app package. This will permanently suppress __pycache__


if __name__ == "__main__":
    # TODO Add garbage module as last run module to clean out debugdir and do
    #  any other necessary cleanup, instead of doing cleanup here.
    # TODO Sort control_word_dict as part of end of program cleanup.
    debugdir_clean.cleaner()

    # Get and store configuration information.
    base_script_dir, debug_dir, config_file = \
        prepare_to_process.extract_config_settings(
            base_script_dir="", debug_dir="", config_file="Config.ini")

    input_file_name, output_file_name = \
        prepare_to_process.extract_file_info(
            base_script_dir=base_script_dir, debug_dir=debug_dir,
            config_file=config_file)

    # Get the user's preference for XML tag set.
    tag_set = prepare_to_process.extract_users_xml_tag_set(
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

    # Prepare to parse the main portion of the document.
    cw_dirs = [base_script_dir, "/Library/dicts/", "control_word_dict.json"]
    control_word_dict = ''.join(cw_dirs)

    output_file_header.processor()
    output_file_transition.processor()

    doc_parser.MainDocManager.body_parse_manager(
        self=MainDocManager(
            working_input_file=working_input_file,
            debug_dir=debug_dir,
            control_word_dict=control_word_dict,
            tag_set=tag_set))

    # Close open tags where possible and produce list of remaining open tags.
    # tag_closer.tag_closer(debug_dir=debug_dir,
    #                       tag_set=tag_set)

    # TODO Include in final step: 1) garbage cleanup, 2) any needed/wanted
    #  post-processing, 3) sort control_word_symbol file, 3) rename
    #  output_file and put it in the output directory.
    # final_step.final_step(debug_dir=debug_dir,
    #                       tag_set=tag_set,
    #                       output_file_name=output_file_name,
    #                       base_script_dir=base_script_dir)
