
""" Prepare the input file for processing. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "Contents.Library.input_file_prep"

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import os
from pathlib import Path

# From local application
import convert_to_unicode


def processor(input_file: str):
    """ Copy the input_file to a working file in the debug directory. Create a
    working xml file where tags will be placed. """
    base_dir = Path.cwd()
    debug_dir = os.path.join(base_dir, "debugdir")
    # TODO input_file should come from a diff director determined by the
    #  user.
    input_file = os.path.join(base_dir, input_file)
    working_input_file_pre = os.path.join(debug_dir,
                                          "working_input_file_pre.txt")

    # Copy input file to working_input_file.data in debugdir.
    with open(input_file) as input_file_copy:
        read_file = input_file_copy.read()

    with open(working_input_file_pre, "w+") as working_rtf_file_pre:
        working_rtf_file_pre.write(read_file)

    # Convert text to unicode and cleanup miscellaneous characters.
    convert_to_unicode.processor()
    convert_to_unicode.character_cleanup()

    working_input_file = os.path.join(debug_dir, "working_input_file.txt")

    # Create the file in which the appropriate tags and text will be
    # added as the conversion progresses.
    output_file = open(os.path.join(debug_dir, "output_file.xml"), "w+")
    output_file.close()

    return working_input_file
