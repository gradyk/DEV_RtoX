#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" A properly formed XML file requires certain tags prior to the main body
of the file (where the main document test resides). The specific tags
needed depend on the tag set chosen by the user. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.output_file_header"

# From standard libraries
import logging
import os

# From local application
import build_output_file


def ofh_processor(main_dict: dict, config_settings_dict: dict) -> dict:
    header_file_dir = os.path.join(main_dict["base_dir"], "input")
    try:
        if config_settings_dict["output-file-header"] == 0:
            header_file_name = "defaultheader.xml"
        else:
            header_file_name = "tpresheader.xml"
        header_file = os.path.join(header_file_dir, header_file_name)
        with open(header_file, "r+") as header_file_pre:
            header_file_text = header_file_pre.read()
        main_dict = build_output_file.bof_processor(
            main_dict=main_dict, update_output=header_file_text)
    except FileNotFoundError as error:
        logging.exception(error, "An XML header file cannot be found or "
                                 "opened.")
    return main_dict
