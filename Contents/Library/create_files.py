#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Build files used during processing. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2030-03-19"
__name__ = "Contents.Library.create_files"

# From standard libraries
import os
import json


def create_dict_files(main_dict: dict) -> None:

    dict_library = (
        "header_tables_dict.json",
        "code_strings_file.json",
        "table_emptyorfull_dict.json",
        "font_table_file.json",
        "color_table_file.json",
        "style_sheet_table_file.json",
        "info_group_file.json",
        "xml_namespace_table_file.json"
    )
    for file in dict_library:
        dict_path = os.path.join(main_dict["debug_dir"], file)
        with open(dict_path, "w+") as open_dict:
            json.dump({}, open_dict)
