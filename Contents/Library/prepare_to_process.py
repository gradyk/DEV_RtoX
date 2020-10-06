#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Perform preparatory housekeeping steps before processing the RTF file. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.prepare_to_process"

# From standard libraries
import logging
import os
import posixpath
import sys
from typing import Any

# From local application
import read_configuration
from read_log_config import logger_basic


def get_config_settings(main_dict: dict) -> None:
    """ Extract command line and Config.ini settings to run RtoX. Store
    the settings in the config_dict.py (config_dictionary). """
    if main_dict["main_script"] and not os.path.isfile(
            main_dict["main_script"]):
        try:
            logger_basic.critical(msg="What script are you using? The "
                                      "program uses RtoX.py as the "
                                      "main script. The program will now "
                                      "quit.")
            sys.exit(1)
        except AttributeError:
            logging.exception(msg="There is something wrong with the "
                                  "program installation. The program "
                                  "will now quit.")
            sys.exit(1)


def extract_file_info(main_dict: dict) -> Any:
    item = None
    config_settings_dict = read_configuration.get_system_arguments()
    config_settings_dict = read_configuration.get_configuration(
        main_dict=main_dict, config_settings_dict=config_settings_dict)

    # Get the input file from the command line and store as
    # working_input_file in the main_dict.
    if config_settings_dict.get("input") is not item:
        main_dict["input_file"] = \
            config_settings_dict.get("input")
        try:
            input_file = posixpath.join(main_dict["base_dir"],
                                        "input",
                                        main_dict["input_file"])
            main_dict["working_input_file"] = \
                [line.rstrip('\n') for line in open(input_file)]
            main_dict["working_input_file_bak"] = \
                main_dict["working_input_file"]
            logger_basic.isEnabledFor(level=10)
            logger_basic.info(msg=f"The file you want to convert is "
                                  f"{main_dict['input_file']}.")
        except TypeError:
            logging.exception("There is a logging problem: user input "
                              "file.")

    else:
        try:
            logger_basic.critical(msg="You did not provide a file to "
                                      "convert. The program must have a "
                                      "file to convert and will now quit.")
            sys.exit(1)
        except TypeError:
            logging.exception("There is a logging problem: input file "
                              "absent.")

    # Get the name of the output file from the command line.
    if config_settings_dict.get("output") is not None:
        main_dict["output_file_name"] = \
            config_settings_dict.get("output")
        try:
            logger_basic.isEnabledFor(level=10)
            logger_basic.info(
                msg=f"The RtoX will produce this XML file: "
                f"{main_dict['output_file_name']}.")
        except TypeError:
            logging.exception("There is a logging problem: user output "
                              "file.")
    else:
        try:
            final_output_file = \
                os.path.splitext(main_dict["input_file"])[0] + '.xml'
            main_dict["output_file_name"] = \
                posixpath.join(main_dict["base_dir"], "output",
                               final_output_file)
            logger_basic.isEnabledFor(level=10)
            logger_basic.info(
                msg="RtoX will produce this XML file: "
                f"{main_dict['output_file_name']}.")
        except TypeError:
            logging.exception("There is a logging problem: default output "
                              "file.")

    # The program supplies settings for the following variables:
    # base_dir, debug_dir, and dicts_dir.
    # These settings come from the Config.ini file.
    tag_set = config_settings_dict.get("tag-set")
    output_header = config_settings_dict.get("output-file-header")
    convert_symbol = config_settings_dict.get("convert-symbol")
    convert_caps = config_settings_dict.get("convert-caps")
    report_level = config_settings_dict.get("problem-report-level")
    xml_indenting = config_settings_dict.get("xml-indenting")
    create_lists = config_settings_dict.get("create-lists")

    # TODO These need to reflect user input rather than be hard-coded.
    user_input_choices_dict = {
        tag_set:        f'You chose "{tag_set}" for your XML tags.',
        output_header:  f'You chose {output_header}for your header setting.',
        convert_symbol: f"You chose to have all symbols converted "
                        f"to UTF-8 characters.",
        convert_caps:   f'You chose {convert_caps} for your caps setting.',
        report_level:   f"You selected a problem report level of "
                        f"{report_level}.",
        xml_indenting:  f"You chose to have XML indenting turned on.",
        create_lists:   "You chose to have create lists turned on."
    }

    # TODO This code section doesn't make sense.
    for menu_item in user_input_choices_dict:
        if menu_item:
            try:
                logger_basic.isEnabledFor(level=10)
                logger_basic.info(msg=user_input_choices_dict[menu_item])
            except TypeError:
                logging.exception(f"There is a logging problem: "
                                  f"{menu_item}.")
        else:
            try:
                logger_basic.isEnabledFor(level=10)
                logger_basic.info(msg=f"The program will be set at "
                                      f"default for: {menu_item}.")
            except TypeError:
                logging.exception("")
    return main_dict, config_settings_dict


def xml_tag_set_pref(config_settings_dict: dict, main_dict: dict) -> dict:
    """ Get user's preference for XML tag set. """
    try:
        tag_set = int(config_settings_dict["tag-set"])
    except TypeError:
        tag_set = 1
    main_dict["tag_set"] = tag_set
    return main_dict


# TODO This is not called by anything.
def print_input_error_message():
    """ Log an error message if the configuration (as recorded in the
    config_file_dict) is not valid. """
    try:
        logger_basic.isEnabledFor(level=10)

        logger_basic.critical(msg="You did not provide information the "
                                  "RtoX program needs. The program will "
                                  "now quit.")
        sys.exit(1)
    except TypeError:
        # TODO Complete logging exception.
        logging.exception("_______________")


# TODO This is not called by anything.
def print_output_error_message():
    """ Log a message if no file_to_produce is specified. """
    # TODO Check that program can handle no name provided properly.
    try:
        logger_basic.isEnabledFor(level=10)

        logger_basic.info(msg="You did not provide a file name for the "
                              "converted file. The program will use the "
                              "name of the file to convert and change "
                              "the extension to .xml")
    except TypeError:
        # TODO Complete logging exception.
        logging.exception("______________")
