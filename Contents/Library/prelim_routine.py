#!/usr/bin/env python3
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

# From local application
import read_configuration
from read_log_config import logger_basic, logger_debug


class Prelim:

    def __init__(self, config_file: str, base_script_dir: str,
                 debug_dir: str) -> None:
        self.config_file = config_file
        self.base_script_dir = base_script_dir
        self.debug_dir = debug_dir

    def prelim_settings(self):

        self.base_script_dir = os.path.dirname(os.path.abspath(
            sys.argv[0]))

        # Set the path for the main script and confirm it exists.
        main_script = os.path.join(self.base_script_dir, "RtoX.py")

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
        self.config_file = os.path.join(self.base_script_dir, "Config.ini")

        # Set the debug_dir directory to store working files created by the
        # program.
        self.debug_dir = os.path.join(self.base_script_dir, "debugdir")

        # Determine if the base directory is in sys.path; if not, add it.
        if self.base_script_dir in sys.path:
            current_in_path = 1
            temp = []
        else:
            logger_debug.debug(msg="The base directory is not in sys.path.")
            sys.exit(1)

        # Copy all of sys.path to temp and list the base directory last.
        for path in sys.path:
            if path != sys.path:
                temp.append(path)
            else:
                pass

        sys.path = []
        for path in temp:
            sys.path.append(path)

        if current_in_path:
            sys.path.append(self.base_script_dir)
        else:
            pass

        return self.base_script_dir, self.debug_dir, self.config_file

    def create_config_dict(self):
        """ Depending on the user's preference (problem-report-level),
        report the settings before running the remainder of the program. """

        config_file_dict_args = read_configuration.get_system_arguments()

        config_settings_dict = read_configuration.get_configuration(
            config_file=self.config_file, debug_dir=self.debug_dir,
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
        # debugdir and base_script_dir.

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
            logging.exception("")

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
            logging.exception("______________")
