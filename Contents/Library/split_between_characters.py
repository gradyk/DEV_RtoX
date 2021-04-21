#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Split a string between two characters. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.split_between_characters"

# From standard libraries
import logging

log = logging.getLogger(__name__)


def split_between(text_to_process: str, split_characters: str):
    """ Splits the text_to_process between two characters into
    separate items in a list (result_list). """
    try:
        len(split_characters) == 2
    except TypeError:
        log.debug(
            msg="'split_characters' must be two characters (you provided "
                f"{split_characters} as the split_characters.")

    text_to_process = text_to_process.replace("}{", "}|{")
    code_strings_list = text_to_process.split("|")

    return code_strings_list
