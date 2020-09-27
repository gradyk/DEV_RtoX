#  Copyright (c) 2020. Kenneth A. Grady
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

# Standard library imports
import json
import os
import sys

# From local application
import tag_registry_update


def processor(tag_info: dict):
    """ Evaluate whether the tag is open. closed, or not in the registry.
    Options:
    open    and tag_action is open: do nothing
    open    and tag_action is close: close tag
    close   and tag_action is open: open tag
    close   and tag_action is close: do nothing
    absent  and tag_action is open: open tag
    absent  and tag_action is close: do nothing
    Finally, update the registry. """
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_dir, "debugdir")
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    update_output = ""
    with open(tag_registry_file, "r+") as tag_registry_file_pre:
        tag_registry = json.load(tag_registry_file_pre)
        name = tag_info["name"]
        try:  # is tag open or closed
            if tag_registry[name] == "open" and tag_info["tag_setting"] == \
                    "close":
                update_output = tag_info["tag_close_str"]
            elif tag_registry[name] == "close" and tag_info["tag_setting"] == \
                    "open":
                update_output = tag_info["tag_open_str"]
            elif tag_registry[name] == "close" and tag_info["tag_setting"] == \
                    "close":
                update_output = ""
            elif tag_registry[name] == "open" and tag_info["tag_setting"] == \
                    "open":
                update_output = ""
            tag_update = {tag_info["name"]: tag_info["tag_setting"]}
        except KeyError:  # control word not in the tag registry
            # Add the tag to the tag registry and update its status.
            # TODO For at least some toggles (aspalpha, aspanum) there isn't
            #  a close tag. Need to identify these situations and mark the
            #  status in the tag registry appropriately.
            if tag_info["tag_setting"] == "open":
                update_output = tag_info["tag_open_str"]
            elif tag_info["tag_setting"] == "close":
                update_output = tag_info["tag_close_str"]
            tag_update = {tag_info["name"]: tag_info["tag_setting"]}
        if tag_info["tag_setting"] == "":
            pass
        else:
            tag_registry_update.processor(tag_update=tag_update)
        return tag_info, update_output
