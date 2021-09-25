#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

import logging
from typing import Tuple

import build_output_file

log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    # How to handle toggle controlwords?
    try:
        if tag_info["status"] == "open":
            # close tag then open tag
            main_dict["update_output"] = tag_info["tag_close_str"] + tag_info["tag_open_str"]
            main_dict[tag_info["cw_text"]] = "open"
        elif tag_info["status"] == "closed":
            # open tag
            main_dict[tag_info["cw_text"]] = "closed"
            main_dict["update_output"] = tag_info["tag_open_str"]
        else:
            # insert tag
            main_dict["update_output"] = tag_info["___________"]

        # Reset tag_info (except tag_set)
            tag_info = {
                "func":          "",
                "cw_text":       "",
                "cw_value":      "",
                "tag_status":    "",
                "tag_open_str":  "",
                "tag_close_str": ""
            }
        main_dict = build_output_file.processor(main_dict=main_dict)
    except (KeyError, Exception) as error:
        msg = f"RtoX had a problem processing the tag: {tag_info['cw_text']}"
        log.debug(error, msg)
    return tag_info, main_dict
