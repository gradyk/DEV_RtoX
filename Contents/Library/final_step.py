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
import os
import sys
from shutil import copy

# From local application
import open_tag_check
# import post_process
import xmlformatter


def final_step(debug_dir: str,
               xml_tag_num: str,
               output_file_name: str,
               base_script_dir: str) -> None:

    new_xml_file = os.path.join(debug_dir, "new_xml_file.xml")

    tag_dict = open_tag_check.TagCheck.tag_style(
        self=open_tag_check.TagCheck(debug_dir=debug_dir,
                                     xml_tag_num=xml_tag_num))

    # Converting to RTF creates instances of empty tags.
    # Run through the file twice looking for empty tags (deleting
    # empty tags on the first run through may create new empty tags).
    tag_pairs = [
        tag_dict["paragraph-beg"]+tag_dict["paragraph-end"],
        tag_dict["italic-beg"]+tag_dict["italic-end"],
        tag_dict["bold-beg"]+tag_dict["bold-end"],
        tag_dict["header-beg"]+tag_dict["header-end"],
        tag_dict["footnote-beg"]+tag_dict["footnote-end"],
        tag_dict["section-beg"]+tag_dict["section-end"],
        "  "
    ]

    with open(new_xml_file, "r") as draft_file_pre:
        draft_file = draft_file_pre.read()
        i = 1
        while i < 3:
            for item in tag_pairs:
                draft_file = draft_file.replace(item, "")
            i += 1
        with open(new_xml_file, "w") as final_file_pre:
            final_file_pre.write(draft_file)

    # Insert XML closing tags based on user's style preferences.
    with open(new_xml_file, "r") as final_file_pre:
        final_file = final_file_pre.read()
        close_tags = tag_dict["body-end"] + tag_dict["bodytext-end"] + \
            tag_dict["wrapper-end"]
    with open(new_xml_file, "w") as final_file_pre:
        final_file_pre.write(final_file + close_tags)

    sys.stdout.write(tag_dict["body-end"] + tag_dict["bodytext-end"] +
                     tag_dict["wrapper-end"])

    # TODO Clean up back-to-back tag use (e.g., <hiText rend="bold>This
    #  </hiText><hiText rend="bold">is </hitext> ...).
    #  tag_dupe.deduper(test_file)

    # Insert the appropriate header based on the user's preference.
    # TODO There should be a default header file for each tag style.
    try:
        insert = open(os.path.join(base_script_dir+"/input", tag_dict[
            "xmlheader"]), "r")
        insert_tags = insert.read()

        with open(new_xml_file, "r") as final_xml_file_pre:
            final_xml_file = tag_dict["wrapper-beg"] + insert_tags + \
                             final_xml_file_pre.read()
        with open(new_xml_file, "w") as final_step_xml_file:
            final_step_xml_file.write(final_xml_file)

    except TypeError:
        # TODO A logger message should go here.
        pass

    # Post-process the file.
    # post_process.line_cleanup(debug_dir=debug_dir)

    xml_formatted_text = xmlformatter.xmlformatter_start(
        infile=new_xml_file, outfile=new_xml_file)

    with open(new_xml_file, "w") as new:
        new.write(xml_formatted_text)

    # Put the final xml file in the output directory and rename if per
    # the user's preference.
    output_dir = base_script_dir + "/output"
    copy(new_xml_file, output_dir)
    os.rename(output_dir + "/new_xml_file.xml",
              output_dir + f'/{output_file_name}')
