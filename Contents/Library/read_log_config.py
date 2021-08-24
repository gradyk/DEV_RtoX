#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


""" Set up logging function. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.read_log_config"

# From standard libraries
import logging
import logging.handlers
import ntpath
import os


def logging_setup():
    # setLevels: CRITICAL 50, ERROR 40, WARNING 30, INFO 20, DEBUG 10,
    # NOTSET 0
    path = os.path.realpath("RtoX.py")
    head, tail = ntpath.split(path)
    log_file = os.path.join(head, "rtox.log")
    open(log_file, "w").close()
    handler = logging.handlers.WatchedFileHandler(
        os.environ.get("LOGFILE", log_file))
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    log = logging.getLogger()
    log.setLevel(os.environ.get("LOGLEVEL", "DEBUG"))
    log.addHandler(handler)
