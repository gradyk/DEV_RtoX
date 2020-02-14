#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2019. Kenneth A. Grady
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
Prepare the rtf codes xml ile.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-27"
__name__ = "Contents.Library.rtf_codes_file_prep"

import os
from lxml import etree as et


# TODO While this class/function creates the rtf_tags file (which other
#  functions may contribute to) the rtf_tags file is not used by anything.
class RTFCodesPrep:

    def __init__(self, debug_dir: str, xml_tag_num: int) -> None:
        self.debug_dir = debug_dir
        self.xml_tag_num = xml_tag_num

    def rtf_codes_to_xml_prep(self):
        """
        Open the file in which the XML tags and text will be
        added as the conversion progresses. Add first line and header tags to
        the file.
        """

        xml_list = [[1, "http://www.w3.org/1999/xml", None],
                    [2, "http://www.tei-c.org/ns/1.0", "tei"],
                    [3, "http://kennethgrady.com/ns/1.0.0", "ts"],
                    [None, "http://www.w3.org/1999/xml", None]]

        ns = xml_list[int(self.xml_tag_num)-1][1]
        prefix = xml_list[int(self.xml_tag_num)][2]

        with open(os.path.join(self.debug_dir, "rtf_tags.xml"), "w+") as rcx:

            namespace = "{%s}" % ns
            nsmapped = {prefix: ns}
            root = et.Element(namespace + "rtfCodes", nsmap=nsmapped)
            root_string = et.tostring(root, method="html").decode("utf-8")
            rcx.write(root_string)
