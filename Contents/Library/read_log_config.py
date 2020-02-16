#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.read_log_config"

# From standard libraries
import logging.handlers
import os
import sys

directory = os.path.dirname(sys.argv[0])
os.chdir(os.path.join(directory + "/logs"))

# ----First logger----
logger_basic = logging.getLogger("basic_level_logging")

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
logger_basic.addHandler(console_handler)
logger_basic.addHandler(file_handler)


# ----Second logger----
logger_mismatch = logging.getLogger("Logger_Mismatch")
# logger_mismatch.setLevel(logging.ERROR)
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
