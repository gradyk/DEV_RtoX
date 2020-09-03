
#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# BASED ON USER'S SELECTION, GO TO LATEX OR XML FILE BUILDER AND ADD TEXT

# From standard libraries
import os
import sys


def processor(open_tag: str, close_tag: str, text: str) -> None:
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_script_dir, "debugdir")
    output_file_base = os.path.join(debug_dir, "output_file.xml")
    # THIS DOESN'T WORK B/C THERE MAY BE MORE TAGS TO OPEN BEFORE
    # ADDING TEXT AND CLOSING
    with open(output_file_base, "r") as output_file_pre:
        output_file = output_file_pre.read()
        update_list = [open_tag, text, close_tag]
        content_update = ''.join(update_list)
        output_file_updated = output_file + content_update

    with open(output_file_base, "w") as output_file_pre:
        output_file_pre.write(output_file_updated)
