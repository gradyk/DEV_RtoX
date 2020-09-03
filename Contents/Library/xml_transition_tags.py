#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
As the working_xml_file transitions from the header to the body of the
document, certain tags need to be opened (the exact tags depend on the user's
tag style preference). They are (in order): <text><body><section><paragraph>.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-18"
__name__ = "Contents.Library.xml_transition_tags"

# From standard libraries
import logging

# From application library
import tag_registry_update
import output_file_update
from read_log_config import logger_debug


def xml_transition_tags(debug_dir: str, tag_dict: dict, line="0"):
    """ Insert the XML tags to start the document portion of the XML file (
    after the header). """
    content_update = tag_dict["start-tags"]
    output_file_update.content_append(debug_dir=debug_dir,
                                      content_update=content_update)
    # Update the tag registry.
    content_update_dict = {"bodytext":  "1",
                           "section":   "1",
                           "paragraph": "1",
                           "body":      "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, content_update_dict=content_update_dict)

    # Used for debugging.
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(tag_dict["start-tags"] + f"{line}")
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")
