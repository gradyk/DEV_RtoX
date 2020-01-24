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
__date__ = "2020-01-09"
__name__ = "final_step"

# From standard libraries
import lxml.etree as etree
import os
from shutil import copy

# From local application
import rtox.lib.open_tag_check


def final_step(debug_dir: str,
               xml_tag_num: str,
               output_file_name: str,
               base_script_dir: str) -> None:

    tag_dict = rtox.lib.open_tag_check.TagCheck.tag_style(
        self=rtox.lib.open_tag_check.TagCheck(debug_dir=debug_dir,
                                              xml_tag_num=xml_tag_num))

    # Insert closing tags based on user's style preferences.

    tag_pairs = [
        tag_dict["paragraph-beg"]+tag_dict["paragraph-end"],
        tag_dict["italic-beg"]+tag_dict["italic-end"],
        tag_dict["bold-beg"]+tag_dict["bold-end"],
        tag_dict["heading-beg"]+tag_dict["heading-end"],
        tag_dict["footnote-beg"]+tag_dict["footnote-end"]

    ]

    with open(os.path.join(debug_dir, "new_xml_file.xml"), "r") as \
            test_file_pre:
        test_file = test_file_pre.read()
        test_file = test_file + \
            tag_dict["paragraph-end"] + "\n\t\t" + \
            tag_dict["section-end"] + "\n\t" + \
            tag_dict["body-end"] + "\n\t" + \
            tag_dict["bodytext-end"] + "\n" + \
            tag_dict["wrapper-end"]

        # Run through the file twice looking for empty tag pairs (deleting
        # empty pairs on the first run through may create new empty pairs).
        i = 1
        while i < 3:
            for item in tag_pairs:
                test_file = test_file.replace(item, "")
            i += 1

    # Save the cleaned up file.
    with open(os.path.join(debug_dir, "new_xml_file.xml"), "w") as \
            final_step_file:
        final_step_file.write(test_file)

    # Post-process the file.
    # rtox.post_process._______________

    # Attempt to "prettify" if (indent and line breaks).
    with open(os.path.join(debug_dir, "new_xml_file.xml"), "r") as fp:
        etree.parse(fp)

    # Put the final xml file in the output directory and rename if per
    # the user's preference.
    output_dir = base_script_dir + "/output"
    copy(os.path.join(debug_dir, "new_xml_file.xml"), output_dir)
    os.rename(output_dir + "/new_xml_file.xml",
              output_dir + f'/{output_file_name}')
