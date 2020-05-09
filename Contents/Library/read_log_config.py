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

"""

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.read_log_config"

# From standard libraries
import logging.handlers


# ----First logger----
logger_basic = logging.getLogger("basic_level_logging")
logger_basic.setLevel(logging.CRITICAL)
logger_basic.propagate = False

# Create handlers
console_handler = logging.StreamHandler()
file_handler = logging.handlers.RotatingFileHandler(
   filename="rtox_basic.log", mode="w+")
logger_basic.setLevel(logging.INFO)

# Create formatters
console_format = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(filename)s | %(lineno)d | '
    '%(message)s')
file_format = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(filename)s | %(lineno)d | '
    '%(message)s')

# Add formatters to handlers
console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# Add handlers to the logger
logger_basic.addHandler(file_handler)


# ----Second logger----
logger_mismatch = logging.getLogger("Logger_Mismatch")
logger_mismatch.setLevel(logging.ERROR)
logger_mismatch.propagate = False

# Create handlers
mismatch_file_handler = logging.handlers.RotatingFileHandler(
    filename="rtox_mismatch.log", mode="w+")

# Create formatters
mismatch_format = logging.Formatter("%(message)s")

# Add formatters to handlers
mismatch_file_handler.setFormatter(mismatch_format)

# Add handlers to the logger
logger_mismatch.addHandler(mismatch_file_handler)


# ----Third logger----
logger_debug = logging.getLogger("Logger_Debug")
logger_debug.setLevel(logging.DEBUG)
logger_debug.propagate = False

# Create handlers
debug_file_handler = logging.handlers.RotatingFileHandler(
    filename="rtox_debug.log", mode="w+")
debug_file_handler.terminator = ""

# Create formatters
debug_format = logging.Formatter('%(message)s')

# Add formatters to handlers
debug_file_handler.setFormatter(debug_format)

# Add handlers to the logger
logger_debug.addHandler(debug_file_handler)
