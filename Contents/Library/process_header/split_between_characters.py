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


def processor(main_dict: dict):
    """ Splits the text_to_process between two characters into
    separate items in a list (result_list). """
    main_dict["group_contents"] = \
        main_dict["group_contents"].replace("}{", "}|{")
    code_strings_list = main_dict["group_contents"].split("|")
    return code_strings_list
