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
import json
import os

# From local application
import prelim_routine


def extract_config_settings() -> str:
    """ Extract command line and Config.ini settings to run RtoX. Store
    the settings in the config_dict.py (config_dictionary). """
    config_file = prelim_routine.Prelim.prelim_settings(
        prelim_routine.Prelim())
    return config_file


def extract_file_info(config_file: str) -> tuple:
    input_file, output_file_name = \
        prelim_routine.Prelim.create_config_dict(config_file=config_file)
    return input_file, output_file_name


def extract_users_xml_tag_set(debug_dir: str) -> int:
    """ Extract the user's preference for XML tag set. """
    config_settings_dict = os.path.join(debug_dir, "config_dict.json")
    with open(config_settings_dict, "r+") as rtf_settings_dict_pre:
        rtf_settings_dict = json.load(rtf_settings_dict_pre)
        try:
            tag_set = int(rtf_settings_dict["tag-set"])
        except TypeError:
            tag_set = 1
    return tag_set
