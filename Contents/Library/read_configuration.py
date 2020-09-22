#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

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
from pathlib import Path


def get_system_arguments() -> dict:
    """ Read the arguments from the command line. """
    parser = argparse.ArgumentParser(description="Process command line "
                                                 "arguments.")
    parser.add_argument("--input", required=True, help="Input RTF file.")
    parser.add_argument("--output", required=True, help="Output XML file.")
    config_args = vars(parser.parse_args())
    return config_args


def get_configuration(config_file: str, config_file_dict_args: dict) -> dict:
    """ 1. Pull user configuration settings from Config.ini. 2. Put key:value
    pairs in from command line and Config.ini into config_setting_dict
    dictionary. """
    base_dir = Path.cwd()
    debug_dir = os.path.join(base_dir, "debugdir")
    config_dict_path = os.path.join(debug_dir, "config_dict.json")
    with open(config_dict_path, "w+") as open_dict:
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
