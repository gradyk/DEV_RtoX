#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" When RtoX encounters a control word it has not seen before, it adds the
control word to its dictionary and gives it a null function. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.csv_modifier"

# From standard libraries
import logging
import os
import re


def csvm_processor(main_dict: dict, collections_dict: dict, cw_text: str):
    cw_update = {cw_text: "null"}
    cw_csv_update = f"\n{cw_text},Unknown,Unknown,null"
    util_dir = os.path.join(main_dict["base_dir"], "Utilities")
    csv_file = os.path.join(util_dir, "control_words_collections.csv")
    collections_dict.update(cw_update)
    with open(csv_file, "r+") as csv_file_pre:
        raw_csv = csv_file_pre.read()
    item = None
    test = re.search(rf"{cw_text}", raw_csv)
    try:
        if test is not item:
            pass
        else:
            with open(csv_file, "a+") as csv_file_pre:
                csv_file_pre.write(cw_csv_update)
    except (ValueError, KeyError, TypeError):
        logging.exception(msg="RtoX has encountered a problem adding an "
                              "unknown control word to its dictionary. The "
                              f"control word is: {cw_text}.")
