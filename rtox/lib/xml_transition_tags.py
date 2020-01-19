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

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-18"
__name__ = "xml_transition_tags"

# From standard libraries
import importlib
import os


class XMLTransition:

    def __init__(self,
                 debug_dir: str,
                 xml_tag_num: str) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def xml_transition_tags(self):
        """

        """
        options = {
            "1": "xml_tag_dict",
            "2": "tei_tag_dict",
            "3": "tpres_tag_dict",
        }

        # Import xml tag dictionary based on user xml tag style preference.
        if options[self.xml_tag_num]:
            value = options[self.xml_tag_num]
            xtags = importlib.import_module("rtox.dictionaries.xml_tags")
            tag_dict_pre = {value: getattr(xtags, value)}
            tag_dict = tag_dict_pre[value]
        else:
            from rtox.dictionaries.xml_tags import xml_tag_dict as tag_dict

        with open(os.path.join(self.debug_dir, "working_xml_file.xml"),
                  "w") as working_xml_file:
            xml_transition_tags = tag_dict["start-tags"]
            working_xml_file.write(xml_transition_tags)
