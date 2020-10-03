#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.facingp_titlepg"

# From standard libraries
import re


def search_for_facingp_titlepg(main_dict: dict) -> list:
    face_title = []
    cwd_list_two = {  # Spec Page 45
        "facingp": ["Coded", "", "Flag"],
        "titlepg": ["Coded", "", "Flag"]
    }

    for key in cwd_list_two:
        item = None
        count = 0
        for line in main_dict["working_input_file"]:
            match = re.search(r"\\"+f"{key}", line)
            if match is not item:
                face_title.append((key, line))
                count += 1
            else:
                pass
        if count > 0:
            pass
        else:
            face_title.append((key, None))
    return face_title
