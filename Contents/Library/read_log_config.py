#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


"""  """

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

console_handler = logging.StreamHandler()
file_handler = logging.handlers.RotatingFileHandler(
   filename="rtox_basic.log", mode="w+")
logger_basic.setLevel(logging.INFO)

console_format = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(filename)s | %(lineno)d | '
    '%(message)s')
file_format = logging.Formatter(
    '%(asctime)s | %(name)s | %(levelname)s | %(filename)s | %(lineno)d | '
    '%(message)s')

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

logger_basic.addHandler(file_handler)


# ----Second logger----
logger_mismatch = logging.getLogger("Logger_Mismatch")
logger_mismatch.setLevel(logging.ERROR)
logger_mismatch.propagate = False

mismatch_file_handler = logging.handlers.RotatingFileHandler(
    filename="rtox_mismatch.log", mode="w+")

mismatch_format = logging.Formatter("%(message)s")

mismatch_file_handler.setFormatter(mismatch_format)

logger_mismatch.addHandler(mismatch_file_handler)


# ----Third logger----
logger_debug = logging.getLogger("Logger_Debug")
logger_debug.setLevel(logging.DEBUG)
logger_debug.propagate = False

debug_file_handler = logging.handlers.RotatingFileHandler(
    filename="rtox_debug.log", mode="w+")
debug_file_handler.terminator = ""

debug_format = logging.Formatter('%(message)s')

debug_file_handler.setFormatter(debug_format)

logger_debug.addHandler(debug_file_handler)

# setLevels
# CRITICAL 50
# ERROR 40
# WARNING 30
# INFO 20
# DEBUG 10
# NOTSET 0
