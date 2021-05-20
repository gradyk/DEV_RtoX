#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
    Determine if the first character in the text being parsed is an opening
bracket. If if is, use modules to define the group boundaries and
process the group contents. If not, advance to the next character in the
string (and if it is the last character, add to the text being parsed).
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

# From local application
import adjust_process_text
import build_group_contents_list
import group_boundaries
import group_contents

log = logging.getLogger(__name__)


def cg_processor(main_dict: dict, collections_dict: dict) -> dict:
    """
        If the first character test shows the beginning of an RTF group,
    capture the location of the group beginning, find the group end,
    parse the group into components, and process the components. Finally,
    re-set relevant variables.
    """
    try:
        if main_dict["parse_text"][0] == "{":
            main_dict["group_start_line"] = main_dict["line_to_parse"]
            main_dict["group_start_index"] = main_dict["parse_index"] - 1
            main_dict = group_boundaries.define_boundaries(main_dict=main_dict)
            main_dict = \
                build_group_contents_list.pre_process(main_dict=main_dict)
            main_dict = group_contents.gc_processor(
                main_dict=main_dict, collections_dict=collections_dict)
            main_dict["parse_text"] = \
                main_dict["parse_text"].replace(
                    main_dict["group_contents"], "", 1)
            main_dict["group_contents"] = ""
            main_dict["contents_list"] = []
            main_dict["group_start_line"] = 0
            main_dict["group_start_index"] = 1
            main_dict["parse_index"] = 1
            main_dict = adjust_process_text.apt_processor(main_dict=main_dict)
    except (TypeError, IndexError, Exception) as error:
        log.debug(error, msg=(f"Check_group error: "
                              f"{main_dict['line_to_parse']}:"
                              f"{main_dict['parse_index']}--"
                              f"{main_dict['parse_text']}"))
        sys.exit("Check_group error.")
    return main_dict
