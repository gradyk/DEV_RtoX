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
__name__ = "prelim_routine"

import os
import sys
import rtox.read_configuration
from log_config import logger


class Prelim:

    def __init__(self,
                 config_file: str,
                 base_script_dir: str,
                 debug_dir: str
                 ):
        self.config_file = config_file
        self.base_script_dir = base_script_dir
        self.debug_dir = debug_dir

    def prelim_settings(self):

        self.base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # Set the path for the main script and confirm it exists.
        main_script = os.path.join(self.base_script_dir, "RtoX.py")

        if main_script and not os.path.isfile(main_script):
            logger.critical(msg="What script are you using? The program uses "
                                "RtoX.py as the main script.")
            sys.exit(1)

        # Set the directory for the config file and confirm it exists.
        self.config_file = os.path.join(self.base_script_dir, "Config.ini")

        if self.config_file and not os.path.isfile(self.config_file):
            logger.critical(msg="RtoX cannot find the configuration "
                                "file (Config.ini). Please make sure it is "
                                'in the folder "DEV_RtoX".')
            sys.exit(1)

        # Set the debug_dir directory to store working files created by the
        # program.
        self.debug_dir = os.path.join(self.base_script_dir, "debugdir")

        # Determine if the base directory is in sys.path; if not, add it.
        if self.base_script_dir in sys.path:
            current_in_path = 1
            temp = []
        else:
            logger.debug(msg="The base directory is not in sys.path.")
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
        """
        Depending on the user's preference (problem-report-level),
        report the settings before running the remainder of the program.
        TODO Change this to just logging the configuration in the rtox.log file.
        """

        config_file_dict_args = rtox.read_configuration.Configuration\
            .get_system_arguments()

        config_settings_dict = \
            rtox.read_configuration.Configuration.get_configuration(
                rtox.read_configuration.Configuration(
                    config_file=self.config_file, debug_dir=self.debug_dir),
                config_file_dict_args=config_file_dict_args)

        # file_to_convert and file_to_produce are from the command line.
        if config_settings_dict.get("input") is not None:
            input_file = config_settings_dict.get("input")
            if logger.isEnabledFor(level=10):
                logger.info(msg=f"The file you want to convert is "
                                f"{input_file}.")
        else:
            logger.critical(msg="You did not provide a file to convert. The "
                                "program must have a file to convert and will "
                                "now quit.")
            sys.exit(1)

        if config_settings_dict.get("output") is not None:
            output_file = config_settings_dict.get("output")
            if logger.isEnabledFor(level=10):
                logger.info(msg=f"The file you want to produce is "
                                f"{output_file}.")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="The converted file will have the same base "
                                "name as your original file, but with a .xml "
                                "extension.")
            output_file = os.path.splitext(input_file)[0]+'.xml'

        # These settings come from the Config.ini file.
        tag_style = config_settings_dict.get("tag-style")

        convert_symbol = config_settings_dict.get("convert-symbol")
        convert_caps = config_settings_dict.get("convert-caps")
        report_level = config_settings_dict.get("problem-report-level")
        xml_indenting = config_settings_dict.get("xml-indenting")
        create_lists = config_settings_dict.get("create-lists")

        # Settings for the following variables are supplied by the program:
        # debugdir and base_script_dir.

        if tag_style:
            if logger.isEnabledFor(level=10):
                logger.info(msg=f'You chose "{tag_style}" for your XML tags.')
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="You did not choose a tag style. The program "
                            "defaults to XML tags.")
        if convert_symbol:
            if logger.isEnabledFor(level=10):
                logger.info(msg=f"You chose to have all symbols converted "
                            f"to UTF-8 characters.")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="Symbols will not be converted to UTF-8 "
                                'characters and may appear as a "?" or other '
                                "character in the text.")
        if convert_caps:
            if logger.isEnabledFor(level=10):
                logger.info(msg="")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="")
        if report_level:
            if logger.isEnabledFor(level=10):
                logger.info(msg=f"You selected a problem report level of "
                            f"{report_level}.")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="The default problem report level is 3.")
        if xml_indenting:
            if logger.isEnabledFor(level=10):
                logger.info(msg=f"You chose to have XML indenting turned on.")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg="The default option is no XML indenting.")
        if create_lists:
            if logger.isEnabledFor(level=10):
                logger.info(msg="You chose to have create lists turned on.")
        else:
            if logger.isEnabledFor(level=10):
                logger.info(msg='The default option for creating lists is '
                                '"off".')

        return input_file, output_file

    @staticmethod
    def print_input_error_message():
        """
        Log an error message if the configuration (as recorded in the
        config_file_dict) is not valid.
        """

        logger.critical(msg="You did not provide information the RtoX program "
                            "needs. The program will now quit.")
        sys.exit(1)

    @staticmethod
    def print_output_error_message():
        """
        Log a message if no file_to_produce is specified.
        """
        # TODO Check that program can handle no name provided properly.
        logger.info(msg="You did not provide a file name for the converted "
                        "file. The program will use the name of the file to "
                        "convert and change the extension to .xml")
