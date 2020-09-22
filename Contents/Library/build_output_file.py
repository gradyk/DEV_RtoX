#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Module adds tags and/or text to the output file RtoX builds. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.build_output_file"


# From standard libraries
import os
import sys


def processor(update_output: str) -> None:
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_dir = os.path.join(base_dir, "debugdir")
    output_file = os.path.join(file_dir, "output_file.xml")
    with open(output_file, "r+") as output_file_pre:
        output_file_text = output_file_pre.read()
    output_file_list = [output_file_text, update_output]
    update_output_file = ''.join(output_file_list)
    with open(output_file, "w+") as output_file_pre:
        output_file_pre.write(update_output_file)
