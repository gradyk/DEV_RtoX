#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" This module checks for open tags using a list (status_list). If any tags on
the list are open, they are closed by inserting closing tags into the
working_xml_file. The tag_registry is updated. These steps are performed by
open_tag_check. """

# TODO Problems: 1) tag close needs to be nested correctly (which this
#  doesn't do), 2) tag list should be dynamic, reflecting tags added to the
#  output file. Perhaps use a deque to track open tags?

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-07"
__name__ = "Contents.Library.tag_closer"

# From standard libraries
from typing import Tuple

# From local application
import tag_check


def processor(main_dict: dict) -> Tuple[dict, dict]:
    tag_info = {}
    status_list = ["par", "section", "body", "bodytext", "wrapper"]
    for tag in status_list:
        tag_info = {
            "name":          tag,
            "tag_open_str":  main_dict["tags"][tag][0],
            "tag_close_str": main_dict["tags"][tag][1],
            "tag_status":    main_dict[tag],
        }
        tag_info, main_dict = tag_check.processor(
            tag_info=tag_info, main_dict=main_dict)
    return tag_info, main_dict
