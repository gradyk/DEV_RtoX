#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
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

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
For an XML file to validate, it must have a closing tag properly matched to
every opening tag. The tag registry tracks whether a tag is open and
must be closed before adding a new open tag of the same type. The registry
does not depend on the style of XML tags the user chose.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-19"
__name__ = "tag_registry"

# Standard library imports
import importlib
import json
import os


def tag_check(debug_dir: str,
              tag_to_check: str,
              xml_tag_num: str):
    """

    """
    # Possible xml tag dictionaries.
    options = {
        "1": "xml_tag_dict",
        "2": "tei_tag_dict",
        "3": "tpres_tag_dict",
    }

    # Import xml tag dictionary based on user xml tag style preference.
    # Default is a plain XML tag dictionary.
    if options[xml_tag_num]:
        value = options[xml_tag_num]
        xtags = importlib.import_module("rtox.dictionaries.xml_tags")
        tag_dict_pre = {value: getattr(xtags, value)}
        tag_dict = tag_dict_pre[value]
    else:
        from Contents.Library import xml_tag_dict as tag_dict

    # Check the tag passed to the function (tag_to_check) to see if it is
    # open.
    try:
        with open(os.path.join(debug_dir, "tag_registry.json"), "r") \
                as trd_pre:
            trd_general = json.load(trd_pre)
        registry_value = trd_general[tag_to_check]

        # If the tag is not open, move on.
        if registry_value == 0:
            pass
        # If the tag is open, close it.
        elif registry_value >= 0:
            tag = tag_to_check + "-end"
            tag_to_insert = tag_dict[tag]
            with open(os.path.join(debug_dir, "working_xml_file.xml"),
                      "a") as file:
                file.write(tag_to_insert)
            # Update the tag registry.
            with open(os.path.join(debug_dir, "tag_registry.json"),
                      "r") as trd_general_final:
                trd_general = json.load(trd_general_final)
                trd_general_update = {tag_to_check, 0}
                trd_general.update(trd_general_update)
            with open(os.path.join(debug_dir, "tag_registry.json"),
                      "w") as trd_general_final:
                json.dump(trd_general, trd_general_final)
        else:
            # TODO This means there is a tag error, what should happen?
            pass

    except TypeError:
        # This means the tag_to_check is not in the tag_registry_dict.
        # TODO This should be a logger result.
        print("The tag registry dictionary does not contain the "
              f"{tag_to_check} tag.")
