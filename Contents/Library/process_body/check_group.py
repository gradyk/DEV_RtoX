#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.check_group"

# From standard libraries
import logging
import re
import sys

# From local application
import adjust_process_text
import build_group_contents_list
import group_boundaries
import group_contents


def cg_processor(main_dict: dict, collections_dict: dict) -> dict:
    item = None
    try:
        test = re.search(r"^{", main_dict["parse_text"])
        if test is not item:
            main_dict["table_start_line"] = main_dict["line_to_parse"]
            main_dict["table_start_index"] = main_dict["parse_index"]
            main_dict = group_boundaries.define_boundaries(main_dict=main_dict)
            main_dict = \
                build_group_contents_list.pre_process(main_dict=main_dict)
            main_dict = group_contents.gc_processor(
                main_dict=main_dict, collections_dict=collections_dict)
            main_dict["parse_text"] = \
                main_dict["parse_text"].replace(main_dict["group_contents"],
                                                "", 1)
            main_dict["group_contents"] = ""
            main_dict["contents_list"] = []
            main_dict["table_start_line"] = 0
            main_dict["table_start_index"] = 0
            main_dict["parse_index"] = 0
            main_dict = adjust_process_text.apt_processor(main_dict=main_dict)
        else:
            pass
    except (TypeError, IndexError, Exception) as error:
        logging.exception(error, f"Check_group: "
                          f"{main_dict['line_to_parse']}:"
                          f"{main_dict['parse_index']}--"
                          f"{main_dict['parse_text']}")
        sys.exit()
    return main_dict
