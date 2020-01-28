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
Prepare the input file for processing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "input_file_prep"

# From standard libraries
import os

# From local application
import convert_1252_to_unicode


class InputPrep:

    def __init__(self,
                 input_file_name: str,
                 debug_dir: str,
                 base_script_dir: str
                 ):
        self.input_file = input_file_name
        self.debug_dir = debug_dir
        self.base_script_dir = base_script_dir

    def input_file_prep(self):
        """
        Copy the input_file to a working file called
        "working_input_file.data" in the debug directory. Create a working
        xml file where tags will be placed and insert a header section.
        """

        # Copy input file to working_input_file.data in debugdir.
        with open(os.path.join(self.base_script_dir, self.input_file)) as \
                input_file_copy:
            read_file = input_file_copy.read()

        with open(os.path.join(self.debug_dir, "working_input_file_pre.txt"),
                  "w+") as working_rtf_file_pre:
            working_rtf_file_pre.write(read_file)

        convert_1252_to_unicode.convert_ms1252(
            debug_dir=self.debug_dir)

        working_rtf_file = os.path.join(self.debug_dir,
                                        "working_input_file.txt")

        # Create the file in which the XML tags and text will be
        # added as the conversion progresses.
        working_xml_file = open(os.path.join(self.debug_dir,
                                "working_xml_file.xml"), "w+")

        working_xml_file.close()

        return working_rtf_file
