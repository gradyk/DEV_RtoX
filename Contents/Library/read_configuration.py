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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

""" Converts the configuration file (Config.ini) into a
Python dictionary and adds command line options to the dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-23"
__name__ = "Contents.Library.read_configuration"

# From standard libraries
import argparse
import configparser
import json
import os
import sys


def get_system_arguments():
    """ Read the arguments from the command line. """

    parser = argparse.ArgumentParser(description="Process command line "
                                                 "arguments for RtoX.py.")
    parser.add_argument("--input", required=True, help="RTF file to "
                                                       "convert.")
    parser.add_argument("--output", required=True, help="XML file to "
                                                        "produce.")
    config_args = vars(parser.parse_args())
    return config_args


def get_configuration(config_file: str, config_file_dict_args: dict,
                      debug_dir: str):
    """
    1. Pull user configuration settings from Config.ini.
    2. Put key:value pairs in from command line and Config.ini into
    config_setting_dict dictionary.
    """
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))
    dict_dir = os.path.join(base_script_dir, "debugdir")
    dict_path = os.path.join(dict_dir, "config_dict.json")
    with open(dict_path, "w+") as open_dict:
        json.dump({}, open_dict)

    config = configparser.ConfigParser()
    config.read(config_file)
    for section in config.sections():
        for key, value in config.items(section):
            config_file_dict_args.update({key: value})
    config_settings_dict = config_file_dict_args
    dict_to_update = os.path.join(debug_dir, "config_dict.json")
    with open(dict_to_update, "r+") as dict_pre:
        dict_new = json.load(dict_pre)
        dict_new.update(config_file_dict_args)
        dict_pre.seek(0)
        json.dump(dict_new, dict_pre, indent=4)

    return config_settings_dict
