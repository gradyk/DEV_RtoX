#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" This module checks for open tags using a list (status_list). If any tags on
the list are open, they are closed by inserting closing tags into the
working_xml_file. The tag_registry is updated. These steps are performed by
open_tag_check. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-07"
__name__ = "Contents.Library.tag_closer"

# From standard libraries
import json
import os

# From local application
import build_output_file
import tag_check


def tc_processor(main_dict: dict) -> dict:
    xml_tags_file = os.path.join(main_dict["control_info"]["dicts_dir"],
                                 "xml_tags.json")
    with open(xml_tags_file, "r+") as xml_tags_pre:
        xml_tags_dicts = json.load(xml_tags_pre)
    xml_tags = xml_tags_dicts[str(main_dict["processing_dict"]["tag_set"])]
    status_list = [
        "par",
        "section",
        "body",
        "bodytext",
        "wrapper"
    ]

    for tag in status_list:
        tag_info = {
            "name":          tag,
            "tag_open_str":  xml_tags[tag][0],
            "tag_close_str": xml_tags[tag][1],
            "tag_setting":   "close",
            "tag_set":       main_dict["processing_dict"]["tag_set"]
        }
        main_dict, update_output = tag_check.tc_processor(
            tag_info=tag_info, main_dict=main_dict)
        build_output_file.bof_processor(
            update_output=update_output, main_dict=main_dict)
    return main_dict
