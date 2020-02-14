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
import importlib
import json
import os
import sys

# From local application
import tag_registry_update
import working_xml_file_update


class TagCheck:

    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def tag_style(self):
        """
        Import an XML tag dictionary based on user XML tag style preference.
        """

        # TODO allow for possibility that the user did not express a
        #  preference. Also put this function in a separate .py.
        # Possible xml tag dictionaries.
        options = {
            "1": "xml_tag_dict",
            "2": "tei_tag_dict",
            "3": "tpres_tag_dict",
        }

        if options[self.xml_tag_num]:
            value = options[self.xml_tag_num]
            xtags = importlib.import_module("Contents.Library.dicts.xml_tags")
            tag_dict_pre = {value: getattr(xtags, value)}
            tag_dict = tag_dict_pre[value]
        else:
            from Contents.Library.dicts.xml_tags import xml_tag_dict as tag_dict

        return tag_dict

    def tag_check(self, tag_dict: dict, status_list: list):
        """
        The tag_dict includes tags for various settings based on the style
        chosen by the user (e.g., TEI, TPRES). The status_list identifies the
        specific tags to check.
        """

        tag_registry = os.path.join(self.debug_dir, "tag_registry.json")

        with open(tag_registry) as tag_registry_data_pre:
            tag_registry_data = json.load(tag_registry_data_pre)

            for tag_type in status_list:
                # 0 = closed, 1 = open
                if tag_registry_data[tag_type] == "0":
                    pass
                else:
                    # Update the working_xml_file.
                    tag_update = tag_dict[tag_type+"-end"]
                    working_xml_file_update.tag_append(
                        debug_dir=self.debug_dir,
                        tag_update=tag_update)
                    sys.stdout.write(tag_dict[tag_type+"-end"])

                    # Update the tag registry.
                    tag_update_dict = {tag_type: "0"}
                    tag_registry_update.tag_registry_update(
                        debug_dir=self.debug_dir,
                        tag_update_dict=tag_update_dict)
