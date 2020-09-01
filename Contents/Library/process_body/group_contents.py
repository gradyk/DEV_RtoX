#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

# From standard libraries
import linecache

# From local application
import check_parse_text


def processor(processing_dict: dict):
    item = None
    cw_dict = processing_dict["control_word_dict"]
    value = [ele for ele in processing_dict["contents_list"]]
    print("cl ", processing_dict["contents_list"])

    line = linecache.getline(processing_dict["working_input_file"],
                             processing_dict["line_to_parse"]).rstrip("\n").\
        rstrip()
    length = len(line)
    if processing_dict["parse_index"] > length:
        processing_dict["line_to_parse"] += 1
        processing_dict["parse_index"] = 0
        processing_dict["parse_text"] = \
            linecache.getline(
                processing_dict["working_input_file"],
                processing_dict["line_to_parse"]).\
            rstrip("\n").rstrip()
        processing_dict["contents_string"] = ""
        processing_dict["contents_list"] = []
    else:
        processing_dict["parse_text"] = linecache.getline(
            processing_dict["working_input_file"],
            processing_dict["line_to_parse"])
        processing_dict["parse_text"] = \
            processing_dict["parse_text"].rstrip("\n").rstrip(" ")
        processing_dict["group_contents"] = ""
        processing_dict["contents_string"] = ""
        processing_dict["contents_list"] = []

    return processing_dict
