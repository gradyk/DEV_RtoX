#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Determine if the first character in the text being parsed is an opening
bracket. If it is, use modules to define the group boundaries and
process the group contents. If not, advance to the next character in the
string. If it is the last character, add to the text being parsed).
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.check_group"

# From standard libraries
import logging
import sys
from typing import Tuple

# From local application
import adjust_process_text
import build_group_contents_list
import dict_updater
import group_boundaries
import group_contents

log = logging.getLogger(__name__)


def cg_processor(main_dict: dict, collections_dict: dict) -> Tuple[dict, dict]:
    """ If the first character test shows the beginning of an RTF group,
    capture the location of the group beginning, find the group end,
    parse the group into components, and process the components. Finally,
    reset relevant variables.
    """
    try:
        if main_dict["parse_text"][0] == "{":
            main_dict, temp_dict = _group_processor(main_dict=main_dict)
            main_dict = \
                build_group_contents_list.pre_process(main_dict=main_dict)
            main_dict = group_contents.gc_processor(
                main_dict=main_dict, collections_dict=collections_dict)
            main_dict["parse_text"] = \
                main_dict["parse_text"].replace(
                    main_dict["group_contents"], "", 1)
            main_dict["group_contents"], main_dict["contents_list"],\
                main_dict["group_start_line"], main_dict["group_start_index"],\
                main_dict["parse_index"] = "", [], 0, 1, 1
            main_dict = adjust_process_text.apt_processor(main_dict=main_dict)
        else:
            temp_dict = {}
    except (TypeError, IndexError, Exception) as error:
        msg = f"Check_group File error: Working Input File Line" \
              f" {main_dict['line_to_parse']}:Index " \
              f"{main_dict['parse_index']} -- Parse Text: " \
              f"{main_dict['parse_text']}"
        log.debug(error, msg)
        sys.exit()
    return main_dict, temp_dict


def _group_processor(main_dict: dict) -> Tuple[dict, dict]:
    main_dict["group_id"] += 1
    working_input_file = main_dict["working_input_file"]
    listpos = main_dict["group_start_line"]
    temp_dict = {}
    while listpos in range(len(working_input_file)):
        temp_dict = group_boundaries.initialize(main_dict=main_dict)
        group_boundaries_info = {main_dict["group_id"]: [
            main_dict["group_start_line"],
            main_dict["group_start_index"],
            main_dict["group_end_line"],
            main_dict["group_end_index"]]
        }
        dict_updater.json_dict_updater(
            dict_name="group_log.json",
            dict_update=group_boundaries_info,
            main_dict=main_dict)
        listpos = len(working_input_file) + 1
    return main_dict, temp_dict
