#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" As the second step in RtoX, delete files the debugdir directory left from
the prior run. (The files are not deleted at the end of a run so they can be
accessed for debugging purposes.) """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-09"
__name__ = "Contents.Library.debugdir_clean"

# From standard libraries
import logging
import os
import sys

log = logging.getLogger(__name__)


def cleaner():
    folder = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),
                          "debugdir")
    for filename in os.listdir(folder):
        try:
            if filename != "__pycache__":
                os.remove(os.path.join(folder, filename))
        except OSError as error:
            msg = "Problem cleaning out debug_dir directory."
            log.debug(error, msg)
            sys.exit()
