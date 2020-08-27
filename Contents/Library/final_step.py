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
After the appropriate tags have been inserted into the working_xml_file,
several clean up operations need to be performed. They include:
1) Removing empty tag pairs (e.g., <p></p>).
2) Putting closing tags at the end of the working_xml_file that match the
opening tags added ot the file.
3) Adding the first line of the file and any header that precedes the main body.
4) Post-processing the file. This may include steps such as adding tags (
e.g., putting quoted material in tags).
5) Indenting and formatting the working_xml_file.
6) Copying the working_xml_file to the output directory and changing the file
name to the name specified in the user's preferences.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-09"
__name__ = "Contents.Library.final_step"

# From standard libraries
import logging
import os
from shutil import copy

# From local application
import tag_style
# import post_process
import xmlformatter
import output_file_update
from read_log_config import logger_debug


def final_step(debug_dir: str,
               tag_style_selector: str,
               output_file_name: str,
               base_script_dir: str) -> None:

    working_xml_file = os.path.join(debug_dir, "working_xml_file.xml")

    tag_dict = tag_style.tag_dict_selection(tag_style_selector=tag_style_selector)

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

    with open(working_xml_file, "r") as working_xml_file_pre:
        updated_xml_file = working_xml_file_pre.read()
        i = 1
        while i < 3:
            for item in tag_pairs:
                updated_xml_file = updated_xml_file.replace(item, "")
            i += 1

    with open(working_xml_file, "w") as working_xml_file_pre:
        working_xml_file_pre.write(updated_xml_file)

    # Insert XML closing tags based on user's style preferences.
    content_update = tag_dict["body-end"] + tag_dict["bodytext-end"] + \
        tag_dict["wrapper-end"]
    output_file_update.content_append(debug_dir=debug_dir,
                                  content_update=content_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(tag_dict["body-end"] + tag_dict["bodytext-end"] +
                      tag_dict["wrapper-end"])
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")

    # TODO Clean up back-to-back tag use (e.g., <hiText rend="bold>This
    #  </hiText><hiText rend="bold">is </hitext> ...).
    #  tag_dupe.deduper(test_file)

    # Insert the appropriate header based on the user's preference.
    # TODO There should be a default header file for each tag style.
    try:
        insert = open(os.path.join(base_script_dir+"/input", tag_dict[
            "xmlheader"]), "r")
        insert_tags = insert.read()
        with open(working_xml_file, "r") as final_xml_file_pre:
            final_xml_file = tag_dict["wrapper-beg"] + insert_tags + \
                             final_xml_file_pre.read()
        with open(working_xml_file, "w") as final_step_xml_file:
            final_step_xml_file.write(final_xml_file)

    except TypeError:
        logging.exception("There was a problem inserting the xmlheader.")

    # TODO create a set of post process steps.
    # Post-process the file.
    # post_process.tag_cleanup(debug_dir=debug_dir)

    # TODO Create a snapshot of the working_xml_file to store in case of tag
    #  mismatch problems (the next step wipes out the working_xml_file while
    #  processing).

    xml_formatted_text = xmlformatter.xmlformatter_start(
        infile=working_xml_file, outfile=working_xml_file)

    with open(working_xml_file, "w") as new:
        new.write(xml_formatted_text)

    # Put the final XML file in the output directory and rename it per
    # the user's preference.
    output_dir = base_script_dir + "/output"
    copy(working_xml_file, output_dir)
    os.rename(output_dir + "/working_xml_file.xml",
              output_dir + f'/{output_file_name}')
