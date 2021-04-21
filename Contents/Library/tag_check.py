#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" The tag registry maintains the status of tags. Check the status and
perform the appropriate operation based on the status. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-22"
__name__ = "Contents.Library.tag_check"

# From standard libraries
import logging
import sys
from typing import Any

log = logging.getLogger(__name__)


def tc_processor(tag_info: dict, main_dict: dict) -> Any:
    """ Evaluate whether the tag is open. closed, or not in the registry.
    Options:
    open    and tag_action is open: do nothing
    open    and tag_action is close: close tag
    close   and tag_action is open: open tag
    close   and tag_action is close: do nothing
    absent  and tag_action is open: open tag
    absent  and tag_action is close: do nothing
    Finally, update the registry. """
    update_output = ""
    name = tag_info["name"]
    try:  # is tag open or closed
        if main_dict[name] == "open" and tag_info["tag_setting"] == \
                "close":
            update_output = tag_info["tag_close_str"]
        elif main_dict[name] == "close" and tag_info["tag_setting"] == \
                "open":
            update_output = tag_info["tag_open_str"]
        elif main_dict[name] == "close" and tag_info["tag_setting"] == \
                "close":
            update_output = ""
        elif main_dict[name] == "open" and tag_info["tag_setting"] == \
                "open":
            update_output = ""
    except KeyError:  # control word not in the tag registry
        # Add the tag to the tag registry and update its status.
        # TODO For at least some toggles (aspalpha, aspanum) there isn't
        #  a close tag. Need to identify these situations and mark the
        #  status in the tag registry appropriately.
        if tag_info["tag_setting"] == "open":
            update_output = tag_info["tag_open_str"]
        elif tag_info["tag_setting"] == "close":
            update_output = tag_info["tag_close_str"]
    if tag_info["tag_setting"] != "":
        main_dict[tag_info["name"]] = tag_info["tag_setting"]
    if main_dict is None:
        log.debug("Tag_check: main_dict is none.")
        sys.exit(1)
    return main_dict, update_output
