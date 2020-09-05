#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.tag_to_build"

# From standard libraries
import os
import sys


def processor(tag: str):
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_script_dir, "debugdir")
    output_file_base = os.path.join(debug_dir, "output_file.xml")

    with open(output_file_base, "r+") as output_file_pre:
        output_file_old = output_file_pre.read()
        output_file_list = [output_file_old, tag]
        output_file_update = ''.join(output_file_list)
    with open(output_file_base, "w+") as output_file_pre:
        output_file_pre.write(output_file_update)
