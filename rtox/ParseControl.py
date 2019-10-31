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
This module is the control center for parsing the RTF document.
"""

import os
import rtox.file_prep

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "ParseControl"


class ParseControl:

    def __init__(
                 self,
                 input_file_name,
                 debug_file_dir,
                 base_script_dir
                ):
        self.__input_file = input_file_name
        self.__debug_file_dir = debug_file_dir
        self.__base_script_dir = base_script_dir

    def input_file_prep(self, debug_file_dir):
        """
        Copy the input_file to a working file called
        "working_input_file.data" in the debug directory. Check input file is
        1) ASCII encoded, 2) starts with {\rtf, and 3) uses ANSI code page
        1252 character set.
        """

        # Copy input file to working_input_file.data in debugdir.
        with open(os.path.join(self.__base_script_dir, self.__input_file)) as \
                input_file_copy:
            read_file = input_file_copy.read()
        working_rtf_file = os.path.join(self.__debug_file_dir,
                                        "working_input_file.data")
        with open(working_rtf_file, "w+") as write_file_object:
            write_file_object.write(read_file)

        # Check ASCII, {\rtf, and ANSI.
        rtox.file_prep.FilePrep.check_file_rtf(
            working_rtf_file=working_rtf_file,
            debug_file_dir=debug_file_dir)

        # Split header from body.
        # rtox.file_prep.FilePrep.head_from_body(
        #
        #
        # )
