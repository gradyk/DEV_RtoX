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
An RTF file typically uses Microsoft code page 1252 character encoding (
though it may use other encodings). Various MS1252 characters need to be
replaced with unicode characters (the equivalence table is in
Contents.Library.dicts.code_1252_array.py). The first part of this module
makes the switch. The second part (cleanup_dict) replaces miscellaneous
characters and formatting signals with acceptable unicode characters.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-27"
__name__ = "Contents.Library.convert_1252_to_unicode"


# From standard libraries
import os
import re

# From local application
from Contents.Library.dicts.code_page_1252_array import cp1252_to_unicode_dict \
    as code_page_dict


def convert_ms1252(debug_dir):
    """
    Convert characters from MS1252 to unicode.
    """
    working_input_file_pre = os.path.join(debug_dir,
                                          "working_input_file_pre.txt")
    with open(working_input_file_pre, "r") as working_file:
        working_file_use = working_file.read()
        test = re.findall(r"\\'[A_Z0-9][A-Z0-9]", working_file_use)

        for item in test:
            item_clean = item.replace("\\'", "")
            if item_clean in code_page_dict.keys():
                working_file_use = \
                    working_file_use.replace(item, code_page_dict[item_clean])
            else:
                pass

        # Convert miscellaneous characters to unicode.
        cleanup_dict = {
            "&":        "&amp;",
            "HT\\tab":  "\t",
            "\\tab":    "\t",
        }

        for key in cleanup_dict:
            working_file_use = working_file_use.replace(key, cleanup_dict[key])

        # Save the corrected text in a new file in the debug_dir. This file
        # is regenerated each time RtoX is run.
        with open(os.path.join(debug_dir, "working_input_file.txt"), "w+")\
                as working_file_final:
            working_file_final.write(working_file_use)

    os.remove(working_input_file_pre)
