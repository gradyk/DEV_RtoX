#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-22"
__name__ = "Contents.RtoX"

# From standard libraries
import logging
import os
import sys
from pathlib import Path

# From local application
import character_cleanup
import create_files
import debugdir_clean
import doc_parser
import final_step
import header_parser_step_one
import header_parser_step_two
import main_dict_creator
import output_file_header
import output_file_transition
import prepare_to_process
import read_log_config
import rtf_file_lead_parse
import tag_closer

log = logging.getLogger(__name__)

# TODO Add PYTHONDONTWRITEBYTECODE=1 to environment variables before making
#  app package. This will permanently suppress __pycache__


if __name__ == "Contents.RtoX":
    # TODO Add garbage module as last run module to clean out debugdir
    #  and do any other necessary cleanup, instead of doing cleanup here.
    try:
        read_log_config.logging_setup()
        debugdir_clean.cleaner()
        base_dir = Path.cwd()
        debug_dir = os.path.join(base_dir, "debugdir")
        dicts_dir = os.path.join(base_dir, "Library/dicts")
        main_script = os.path.join(base_dir, "RtoX.py")
        config_ini = os.path.join(base_dir, "Config.ini")

        # Create the main dictionary used throughout processing.
        main_dict = main_dict_creator.mdc_processor(
            base_dir=base_dir, debug_dir=debug_dir, dicts_dir=dicts_dir,
            main_script=main_script, config_ini=config_ini)

        # Get and store configuration information.
        prepare_to_process.get_config_settings(main_dict=main_dict)

        # Add settings to rtox_basic.log and update main_dict.
        main_dict, config_settings_dict = \
            prepare_to_process.extract_file_info(main_dict=main_dict)

        # Get the user's preference for XML tag set.
        main_dict = prepare_to_process.xml_tag_set_pref(
            config_settings_dict=config_settings_dict, main_dict=main_dict)

        # Prepare working files.
        create_files.create_dict_files(main_dict=main_dict)

        # Clean up control words in working file version of submitted file.
        main_dict = rtf_file_lead_parse.check_for_opening_brace(
            main_dict=main_dict)
        rtf_file_codes_update = \
            rtf_file_lead_parse.code_process(main_dict=main_dict)

        # Clean up characters in working file version of submitted file.
        main_dict = character_cleanup.cc_processor(main_dict=main_dict)

        # Start the output file and put the header (based on the user's
        # preference) in the file.
        main_dict = output_file_header.ofh_processor(
            main_dict=main_dict, config_settings_dict=config_settings_dict)

        # Place the initial tags in the output file and create the starting
        # tag registry (used to track open/closed XML tags).
        main_dict = output_file_transition.oft_processor(
            main_dict=main_dict, config_settings_dict=config_settings_dict)

        # Process the table portion of the header.
        header_parser_step_one.process_the_tables(main_dict=main_dict)

        header_parser_step_two.ProcessTheTables.\
            analyze_table_code_strings_controller(
                self=header_parser_step_two.ProcessTheTables(
                    main_dict=main_dict))

        # TODO Add capability to handle numbered paragraphs: spec p.48.
        # TODO Add capability to handle tables: spec p.59.

        main_dict = doc_parser.body_parse_manager(main_dict=main_dict)
        main_dict = tag_closer.tc_processor(main_dict=main_dict)

        # TODO Add to final_step: 1) garbage cleanup, 2) any needed/wanted
        #  post-processing.
        final_step.fs_processor(main_dict=main_dict)
        exit()
    except Exception as error:
        log.debug(error, "Exited at RtoX.py")
