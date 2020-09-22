#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

# From standard libraries
import json
import os
import sys

# From local application
import tag_registry_update


def tagger(tag_info: dict) -> dict:
    # For a toggle control word, \<control_word> turns on the feature and
    # \<control_word>N turns off the feature.
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    tag_dict_file = os.path.join(dicts_dir, "xml_tags.json")
    with open(tag_dict_file, "r+") as tag_dict_file_pre:
        tag_dict_options = json.load(tag_dict_file_pre)
    tag_set = str(tag_info["tag_set"])
    tag_dict = tag_dict_options[tag_set]
    item = ""
    open_str_empty = tag_dict["toggle"][0]
    name = tag_info["name"]
    open_str = open_str_empty.replace("zzz", name)
    if tag_info["cw_value"] == item:
        value = "open"
    else:
        value = "close"
    tag_action = {
        "value":        value,
        "open":         open_str,
        "close":        tag_dict["toggle"][1],
        "tag":          "",
        "tag_setting":  "",
        "tag_name":     tag_info["name"]
    }
    tag_checker(tag_action=tag_action)
    tag_info.clear()
    return tag_action


def tag_checker(tag_action: dict):
    """ Evaluate whether the tag is open. closed, or not in the registry (
    absent).
    Options:
    open    and tag_action is open: do nothing
    open    and tag_action is close: close tag
    close   and tag_action is open: open tag
    close   and tag_action is close: do nothing
    absent  and tag_action is open: open tag
    absent  and tag_action is close: do nothing
    Finally, updated the registry. """
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_dir, "debugdir")
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file, "r+") as tag_registry_file_pre:
        tag_registry = json.load(tag_registry_file_pre)
        name = tag_action["name"]
        try:  # open or close
            if tag_registry[name] == "open" and tag_action[""] == "open":
                pass
            elif tag_registry[name] == "open" and tag_action[""] == "close":
                tag_action["tag_setting"] = "close"
            elif tag_registry[name] == "close" and tag_action[""] == "open":
                tag_action["tag_setting"] = "open"
            elif tag_registry[name] == "close" and tag_action[""] == "close":
                pass
            tag_update = {tag_action["tag_name"]: tag_action["tag_setting"]}
        except KeyError:  # absent
            if tag_action[""] == "open":
                tag_action["tag_setting"] = "open"
                tag_update = {tag_action["tag_name"]: "open"}
            elif tag_action[""] == "close":
                tag_action["tag_setting"] = "close"
                tag_update = {tag_action["tag_name"]: "close"}
        tag_registry_update.processor(debug_dir=debug_dir,
                                      tag_update=tag_update)