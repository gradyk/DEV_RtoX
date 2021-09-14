#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Add tags and/or text to the output file RtoX builds. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.build_output_file"


def processor(main_dict: dict, update_output: str) -> dict:
    append_list = [main_dict["output_text"], update_output]
    main_dict["output_text"] = ''.join(append_list)
    return main_dict
