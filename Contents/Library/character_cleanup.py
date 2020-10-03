#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" An RTF file typically uses Microsoft code page 1252 character encoding (
though it may use other encodings). Various MS1252 characters need to be
replaced with unicode characters. The first part of this module
makes the switch. The second part replaces miscellaneous
characters and formatting signals with acceptable unicode characters. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-27"
__name__ = "Contents.Library.convert_to_unicode"

# From standard libraries
import json
import re
import os
from pathlib import Path


def cc_processor(main_dict: dict) -> dict:
    # TODO this setup only works for cpg1252, figure out how to make it flex
    #  depending on cpg
    """ Convert miscellaneous characters to unicode. """
    source_file = main_dict["working_input_file"]

    pattern_list = [
        r"&",
        r"(\\'[A-Z0-9]{2})",
        r"HT\\tab",
        r"\\tab"
    ]
    item = None
    for line in source_file:
        place = source_file.index(line)
        for pattern in pattern_list:
            if re.search(pattern, line) is not item:
                new_line = re.sub(pattern, code_value, line)
                source_file[place] = new_line
            else:
                pass

    main_dict["working_input_file"] = source_file
    main_dict["working_input_file_bak"] = source_file
    return main_dict


def code_value(matchobj):
    base_dir = Path.cwd()
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    code_array = os.path.join(dicts_dir, "code_page_1252_array.json")
    supp_array = os.path.join(dicts_dir, "supp_code_page_array.json")
    with open(code_array, "r+") as code_dict_pre:
        code_dict = json.load(code_dict_pre)
    with open(supp_array, "r+") as supp_dict_pre:
        supp_dict = json.load(supp_dict_pre)
    merged_dict = {**code_dict, **supp_dict}
    match_text = matchobj.group(0).replace("\\'", "")
    value = merged_dict[match_text]
    return value
