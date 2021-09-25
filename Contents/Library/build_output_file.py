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

import logging

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    try:
        append_list = [main_dict["output_text"], main_dict["update_output"]]
        main_dict["output_text"] = ''.join(append_list)
        main_dict["update_output"] = ""
    except KeyError as error:
        msg = f"Problem with {'output_text'}"
        log.debug(error, msg)
    return main_dict
