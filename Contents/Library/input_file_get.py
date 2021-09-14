#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging
import posixpath
import sys

import read_configuration

log = logging.getLogger(__name__)


def retrieve(main_dict: dict) -> dict:
    config_settings_dict = read_configuration.get_system_arguments()
    config_settings_dict = read_configuration.get_configuration(
        main_dict=main_dict, config_settings_dict=config_settings_dict)
    # Store the input file from the command line as
    # main_dict["working_input_file"].
    try:
        main_dict["input_file"] = config_settings_dict.get("input")
    except Exception as error:
        msg = "You did not provide a file to convert."
        log.info(error, msg)
        sys.exit(1)
    try:
        input_file = posixpath.join(main_dict["base_dir"], "input",
                                    main_dict["input_file"])
        pre_file = [line.rstrip('\n') for line in open(input_file)]
        pre_file = [line.rstrip("\\") for line in pre_file]
        main_dict["working_input_file"] = pre_file
        main_dict["working_input_file_bak"] = \
            main_dict["working_input_file"]
        log.info(msg=f"Converting file: {main_dict['input_file']}.")
    except Exception as error:
        msg = "The input file cannot be used."
        log.debug(error, msg)
    return main_dict
