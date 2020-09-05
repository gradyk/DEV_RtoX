#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_text"

# From standard libraries
import logging
import re

# From local application
import adjust_process_text
import text_to_build


def processor(processing_dict: dict) -> dict:
    # Test for text.
    text = ""
    item = None
    try:
        test = re.search(r"^([a-zA-Z\-\s0-9]*)", processing_dict["parse_text"])
        if test is not item:
            text_to_build.processor(text=test[0])
        else:
            pass
    except TypeError:
        logging.exception(f"Check_text: "
                          f"{processing_dict['line_to_parse']}:"
                          f"{processing_dict['parse_index']}--"
                          f"{processing_dict['parse_text']}")

    parse_text_update = processing_dict[
        "parse_text"].replace(text, "", 1)
    processing_dict["parse_text"] = parse_text_update
    processing_dict["parse_index"] = 0
    processing_dict = \
        adjust_process_text.text_metric_reset(
            processing_dict=processing_dict)

    return processing_dict
