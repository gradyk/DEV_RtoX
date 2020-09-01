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


def processor(processing_dict: dict) -> dict:
    item = None
    try:
        test = re.search(r"^{", processing_dict["parse_text"])
        if test is not item:
            processing_dict = group_boundaries.\
                define_boundaries(processing_dict=processing_dict)

            processing_dict = build_group_contents_list.pre_process(
                processing_dict=processing_dict)

            processing_dict = group_contents.processor(
                processing_dict=processing_dict)
        else:
            pass
        return processing_dict
    except TypeError as error:
        logging.exception(error, f"Check_group: "
                          f"{processing_dict['line_to_parse']}:"
                          f"{processing_dict['parse_index']}--"
                          f"{processing_dict['parse_text']}")
    except Exception as error:
        logging.exception(error, "Check_group error.")
        pass
