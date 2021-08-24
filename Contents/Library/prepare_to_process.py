#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Perform housekeeping steps before processing the RTF file. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.prepare_to_process"

# From standard libraries
import logging
import os
import sys
from typing import Tuple

# From local application
import input_file_get
import other_settings_get
import output_file_get

log = logging.getLogger(__name__)


def get_config_settings(main_dict: dict) -> None:
    """ Extract command line and Config.ini settings to run RtoX. Store
    the settings in the config_dict.py (config_dictionary). """
    try:
        if os.path.isfile(main_dict["main_script"]) is not None:
            log.debug("Main script found.")
    except (AttributeError, Exception) as error:
        msg = "Problem with the main script: RtoX.py"
        log.debug(error, msg)
        sys.exit()


def extract_file_info(main_dict: dict) -> Tuple[dict, dict]:
    main_dict = input_file_get.retrieve(main_dict=main_dict)
    main_dict = output_file_get.retrieve(main_dict=main_dict)
    config_settings_dict = other_settings_get.retrieve(main_dict=main_dict)
    return main_dict, config_settings_dict


def xml_tag_set_pref(config_settings_dict: dict, main_dict: dict) -> dict:
    """ Get user's preference for XML tag set. """
    try:
        tag_set = int(config_settings_dict["tag-set"])
    except TypeError:
        tag_set = 1
    main_dict["tag_set"] = tag_set
    return main_dict
