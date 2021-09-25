#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Par marks the start of a new paragraph. It does not include any other
coding. When RtoX encounters par it: 1) checks for and closes relevant open
tags, 2) inserts a close paragraph tag, 3) inserts an open paragraph tag, and
4) updates the tag registry. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.control_words_symbols.par"

# Standard library imports
import logging
from typing import Tuple

# From local application
import build_output_file

log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    """ If the tag registry shows a closed paragraph, insert an open 
        paragraph tag. If it shows an open paragraph, close it and open a new
        paragraph. """
    if main_dict["tag_queue"]:
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["tag_queue"] = []
        main_dict["par"] = "closed"
    if main_dict["par"] == "closed":
        main_dict["update_output"] = main_dict["update_output"] + \
            main_dict["tags"]["par"][0]
        main_dict["tag_queue"].append(main_dict["tags"]["par"][1])
    elif main_dict["par"] == "open":
        main_dict["update_output"] = main_dict["update_output"] + \
            main_dict["tags"]["par"][1] + main_dict["tags"]["par"][0]
        main_dict["tag_queue"].append(main_dict["tags"]["par"][1])
    build_output_file.processor(main_dict=main_dict)
    main_dict["par"] = "open"
    return tag_info, main_dict
