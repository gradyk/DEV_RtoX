#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
The tag registry maintains the status of open and closed tags. Check for an
open tag of the type specified and, if open, close and update
the tag registry.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-22"
__name__ = "Contents.Library.open_tag_check"

# Standard library imports
import json
import logging
import os
import sys

# From local application
import tag_registry_update
import build_output_file
from read_log_config import logger_debug


def tag_check(debug_dir: str, tag_dict: dict, status_list: list):
    """ Check for and, if necessary, close open tags. The status_list provides
    the tags to check. """
    tag_registry = os.path.join(debug_dir, "tag_registry.json")
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    tag_dict_file = os.path.join(base_dir, "xml_tags.json")
    with open(tag_registry) as tag_registry_data_pre:
        tag_registry_data = json.load(tag_registry_data_pre)
    with open(tag_dict_file, "r+") as tag_dict_file_pre:
        tag_dict_options = json.load(tag_dict_file_pre)

        tag_set = tag_dict_options[________[______]]

        for tag_type in status_list:
            tag_closed = "close"
            if tag_registry_data[tag_type] == tag_closed:
                pass
            else:
                # Update the build_output_file.
                content_update = tag_dict[tag_type]
                build_output_file.processor(update_output=content_update)
                try:
                    if logger_debug.isEnabledFor(logging.DEBUG):
                        msg = "______________"
                        logger_debug.error(msg)
                except AttributeError:
                    logging.exception("Check setLevel for logger_debug.")

                # Update the tag registry.
                content_update_dict = {tag_type: "close"}
                tag_registry_update.processor(debug_dir=debug_dir,
                                              tag_update_dict=content_update_dict)
