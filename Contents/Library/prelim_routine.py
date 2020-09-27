#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
First processing step for RTF file.
1. Establish the directory for the main script (RtoX.py) and confirm the
script is in that directory.
2. Establish the directory for the Config.ini file and confirm the file is in
that directory.
3. Establish the debugdir directory, where working files are stored during
processing.
4. Make sure the base script directory is in the system path.
TODO Is this a problem in a Windows installation?
5. Copy all of path to temp.
TODO Is this needed or a holdover from rtf2xml?
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-09"
__name__ = "Contents.Library.extract_config_settings"

# From standard libraries
import logging
import os
import sys
from pathlib import Path

# From local application
import read_configuration
from read_log_config import logger_basic, logger_debug


class Prelim(object):
    def __init__(self) -> None:
        self.config_info = "Config.ini"
        self.base_dir = Path.cwd()
        self.debug_dir = os.path.join(self.base_dir, "debugdir")

    def prelim_settings(self) -> str:
        # Test the path for the main script.
        main_script = os.path.join(self.base_dir, "RtoX.py")

        if main_script and not os.path.isfile(main_script):
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

        # Set the path for the Config.ini file.
        config_file = os.path.join(self.base_dir, "Config.ini")

        return config_file

    @staticmethod
    def create_config_dict(config_file: str):
        """ Depending on the user's preference (problem-report-level),
        report the settings before running the remainder of the program. """

        config_file_dict_args = read_configuration.get_system_arguments()

        config_settings_dict = read_configuration.get_configuration(
            config_file=config_file,
            config_file_dict_args=config_file_dict_args)

        # Get the input file from the command line.
        input_file = ""

        if config_settings_dict.get("input") is not None:
            input_file = config_settings_dict.get("input")
            try:
                logger_basic.isEnabledFor(level=10)
                logger_basic.info(msg=f"The file you want to convert is "
                                      f"{input_file}.")
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
            output_file = config_settings_dict.get("output")
            try:
                logger_basic.isEnabledFor(level=10)
                logger_basic.info(msg=f"The file you want to produce is "
                                      f"{output_file}.")
            except TypeError:
                logging.exception("There is a logging problem: user output "
                                  "file.")
        else:
            try:
                logger_basic.isEnabledFor(level=10)
                logger_basic.info(msg="The converted file will have the same "
                                      "base name as your original file, but "
                                      "with a .xml extension.")
            except TypeError:
                logging.exception("There is a logging problem: default output "
                                  "file.")

            output_file = os.path.splitext(input_file)[0]+'.xml'

        # Settings for the following variables are supplied by the program:
        # debugdir and base_dir.

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
            tag_set: f'You chose "{tag_set}" for your XML tags.',
            output_header: f'You chose {output_header}for your header setting.',
            convert_symbol: f"You chose to have all symbols converted "
                            f"to UTF-8 characters.",
            convert_caps: f'You chose {convert_caps} for your caps setting.',
            report_level: f"You selected a problem report level of "
                          f"{report_level}.",
            xml_indenting: f"You chose to have XML indenting turned on.",
            create_lists: "You chose to have create lists turned on."
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

        return input_file, output_file

    @staticmethod
    def print_input_error_message():
        """
        Log an error message if the configuration (as recorded in the
        config_file_dict) is not valid.
        """
        try:
            logger_basic.isEnabledFor(level=10)

            logger_basic.critical(msg="You did not provide information the "
                                      "RtoX program needs. The program will "
                                      "now quit.")
            sys.exit(1)
        except TypeError:
            # TODO Complete logging exception.
            logging.exception("_______________")

    @staticmethod
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
