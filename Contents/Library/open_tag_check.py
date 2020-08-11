#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

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

# From local application
import tag_registry_update
import output_file_update
from read_log_config import logger_debug


def tag_check(debug_dir: str, tag_dict: dict, status_list: list):
    """
    Check for and, if necessary, close open tags. The status_list provides
    the tags to check.
    """

    tag_registry = os.path.join(debug_dir, "tag_registry.json")

    with open(tag_registry) as tag_registry_data_pre:
        tag_registry_data = json.load(tag_registry_data_pre)

        for tag_type in status_list:
            tag_closed = "0"

            if tag_registry_data[tag_type] == tag_closed:
                pass
            else:
                # Update the working_xml_file.
                content_update = tag_dict[tag_type+"-end"]
                output_file_update.content_append(
                    debug_dir=debug_dir,
                    content_update=content_update)
                try:
                    if logger_debug.isEnabledFor(logging.DEBUG):
                        msg = str(tag_dict[tag_type+"-end"])
                        logger_debug.error(msg)
                except AttributeError:
                    logging.exception("Check setLevel for logger_debug.")

                # Update the tag registry.
                content_update_dict = {tag_type: "0"}
                tag_registry_update.tag_registry_update(
                    debug_dir=debug_dir,
                    content_update_dict=content_update_dict)
