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
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Split a string between two characters. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.split_between_characters"

# From standard libraries
import logging

# From application library
from read_log_config import logger_basic


def split_between(text_to_process: str, split_characters: str):
    """ Splits the text_to_process between two characters into
    separate items in a list (result_list). """
    try:
        len(split_characters) == 2
    except TypeError:
        if logger_basic.isEnabledFor(logging.DEBUG):
            logger_basic.debug(
                msg="'split_characters' must be two characters (you provided "
                    f"{split_characters} as the split_characters.")

    text_to_process = text_to_process.replace("}{", "}|{")
    code_strings_list = text_to_process.split("|")

    return code_strings_list
