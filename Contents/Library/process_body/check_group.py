#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.check_group"

# From standard libraries
import logging
import re

# From local application
import build_group_contents_list
import group_boundaries
import group_contents


def cg_processor(main_dict: dict, collections_dict: dict) -> dict:
    item = None
    try:
        test = re.search(r"^{", main_dict["parse_text"])
        if test is not item:
            main_dict = group_boundaries.define_boundaries(main_dict=main_dict)

            main_dict = build_group_contents_list.pre_process(
                main_dict=main_dict)

            main_dict = group_contents.gc_processor(
                main_dict=main_dict, collections_dict=collections_dict)
        else:
            pass
        return main_dict
    except TypeError as error:
        logging.exception(error, f"Check_group: "
                          f"{main_dict['processing_dict']['line_to_parse']}:"
                          f"{main_dict['processing_dict']['parse_index']}--"
                          f"{main_dict['processing_dict']['parse_text']}")
    except Exception as error:
        logging.exception(error, "Check_group error.")
        pass
