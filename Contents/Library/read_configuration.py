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
Converts the configuration file (Config.ini) into a
Python dictionary and adds command line options to the dictionary.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-23"
__name__ = "read_configuration"

import configparser
import argparse
import os


class Configuration:

    def __init__(self,
                 debug_dir: str,
                 config_file: str
                 ):
        self.config_file = config_file
        self.debug_dir = debug_dir

    @staticmethod
    def get_system_arguments():
        """
        Read the arguments from the command line.
        """

        parser = argparse.ArgumentParser(description="Process command line "
                                                     "arguments for RtoX.py.")

        parser.add_argument("--input", required=True, help="RTF file to "
                                                           "convert.")
        parser.add_argument("--output", required=True, help="XML file to "
                                                            "produce.")

        config_args = vars(parser.parse_args())

        return config_args

    def get_configuration(self, config_file_dict_args):
        """
        1. Pull user configuration settings from Config.ini.
        2. Put key:value pairs in from command line and Config.ini into
        config_setting_dict dictionary.
        """

        config = configparser.ConfigParser()
        config.read(self.config_file)
        for section in config.sections():
            for key, val in config.items(section):
                config_file_dict_args.update({key: val})
        config_settings_dict = config_file_dict_args

        with open(os.path.join(self.debug_dir, "config_dict.py"), "w+") as f:
            f.write("config_dictionary = " + str(config_settings_dict))

        return config_settings_dict
