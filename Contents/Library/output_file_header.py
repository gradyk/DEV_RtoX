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
import json
import logging
import os
import sys

# From local application
import build_output_file


def processor():
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_dir = os.path.join(base_script_dir, "debugdir")
    config_file = os.path.join(file_dir, "config_dict.json")

    try:
        with open(config_file, "r+") as config_dict_pre:
            config_dict = json.load(config_dict_pre)

        if config_dict["output-file-header"] == 0:
            header_file_dir = os.path.join(base_script_dir, "input")
            header_file = os.path.join(header_file_dir, "defaultheader.xml")
            with open(header_file, "r+") as header_file_pre:
                header_file_text = header_file_pre.read()
        else:
            header_file_dir = os.path.join(base_script_dir, "input")
            header_file = os.path.join(header_file_dir, "tpresheader.xml")
            with open(header_file, "r+") as header_file_pre:
                header_file_text = header_file_pre.read()
        build_output_file.processor(update_output=header_file_text)
    except FileNotFoundError as error:
        logging.exception(error, "An XML header file cannot be found or "
                                 "opened.")
