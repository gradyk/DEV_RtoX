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


def get_system_arguments() -> dict:
    """ Read the arguments from the command line. """
    parser = argparse.ArgumentParser(description="Process command line "
                                                 "arguments.")
    parser.add_argument("--input", required=True, help="Input RTF file.")
    parser.add_argument("--output", required=True, help="Output XML file.")
    config_settings_dict = vars(parser.parse_args())
    return config_settings_dict


def get_configuration(main_dict: dict, config_settings_dict: dict) -> dict:
    """ 1. Pull user configuration settings from Config.ini. 2. Put key:value
    pairs in from command line and Config.ini into config_setting_dict
    dictionary. """
    config = configparser.ConfigParser()
    config.read(main_dict["control_info"]["config_ini"])
    for section in config.sections():
        for key, value in config.items(section):
            config_settings_dict.update({key: value})
    return config_settings_dict
