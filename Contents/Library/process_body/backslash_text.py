#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.backslash_text"

# From standard libraries
import logging
import re

# From local application
import adjust_process_text
import build_output_file


def bt_processor(main_dict: dict) -> dict:
    # Test for backslash character as part of text.
    text = ""
    item = None
    try:
        test = re.search(r"^(\\\\)", main_dict["parse_text"])
        if test is not item:
            text = "\\"
            build_output_file.bof_processor(update_output=text,
                                            main_dict=main_dict)
        else:
            pass
    except TypeError:
        logging.exception(f"{main_dict['line_to_parse']}:"
                          f"{main_dict['parse_index']}--"
                          f"{main_dict['parse_text']}")

    main_dict["parse_text"] = \
        main_dict["parse_text"].replace(text, "")
    main_dict["parse_index"] = 0
    main_dict = adjust_process_text.apt_processor(main_dict=main_dict)
    return main_dict
