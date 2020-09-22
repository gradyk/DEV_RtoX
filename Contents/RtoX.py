#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "__RtoX__"

# From standard libraries
import os
from pathlib import Path

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
import script_timer
from process_body.doc_parser import MainDocManager

# TODO Add PYTHONDONTWRITEBYTECODE=1 to environment variables before making
#  app package. This will permanently suppress __pycache__


if __name__ == "__RtoX__":

    script_timer.open_processor()
    # TODO Add garbage module as last run module to clean out debugdir and do
    #  any other necessary cleanup, instead of doing cleanup here.
    # TODO Sort control_word_dict as part of end of program cleanup.
    debugdir_clean.cleaner()
    base_dir = Path.cwd()
    debug_dir = os.path.join(base_dir, "debugdir")

    # Get and store configuration information.
    config_file = \
        prepare_to_process.extract_config_settings()

    input_file, output_file_name = \
        prepare_to_process.extract_file_info(config_file=config_file)

    # Get the user's preference for XML tag set.
    tag_set = \
        prepare_to_process.extract_users_xml_tag_set(debug_dir=debug_dir)

    # Prepare working files.
    working_input_file = \
        create_files.CreateFile.initiate_working_files(input_file=input_file)

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
    cw_dirs = [base_dir, "/Library/dicts/", "control_word_dict.json"]
    control_word_dict = ''.join(cw_dirs)

    output_file_header.processor()
    output_file_transition.processor()

    doc_parser.MainDocManager.body_parse_manager(
        self=MainDocManager(
            working_input_file=working_input_file,
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
    #                       base_dir=base_dir)
