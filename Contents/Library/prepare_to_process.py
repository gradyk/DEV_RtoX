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
This module performs preparatory housekeeping steps before the RTF file can
be processed.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.prepare_to_process"

# From standard libraries
import json
import os
import sys

# From local application
import prelim_routine


def extract_config_settings(config_file: str, base_script_dir: str,
                            debug_dir: str) -> tuple:
    """ Extract command line and Config.ini settings to run RtoX. Store
    the settings in the config_dict.py (config_dictionary). """
    base_script_dir, debug_dir, config_file = \
        prelim_routine.Prelim.prelim_settings(
            prelim_routine.Prelim(config_file=config_file,
                                  base_script_dir=base_script_dir,
                                  debug_dir=debug_dir))
    return base_script_dir, debug_dir, config_file


def extract_file_info(config_file: str, base_script_dir: str,
                      debug_dir: str) -> tuple:
    input_file_name, output_file_name = \
        prelim_routine.Prelim.create_config_dict(
            self=prelim_routine.Prelim(config_file=config_file,
                                       base_script_dir=base_script_dir,
                                       debug_dir=debug_dir))
    return input_file_name, output_file_name


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
