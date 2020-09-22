#  Copyright (c) 2020. Kenneth A. Grady
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
from pathlib import Path

# From application library
import Contents.Library.input_file_prep


class CreateFile(object):
    def __init__(self):
        self.base_dir = Path.cwd()
        self.debug_dir = os.path.join(self.base_dir, "debugdir")

    @staticmethod
    def initiate_working_files(input_file: str) -> str:
        CreateFile.create_dict_files(self=CreateFile())
        working_input_file = \
            CreateFile.create_working_input_file(input_file=input_file)
        return working_input_file

    def create_dict_files(self) -> None:
        dict_library = (
            "header_tables_dict.json",
            "rtf_file_codes.json",
            "code_strings_file.json",
            "table_emptyorfull_dict.json",
            "font_table_file.json",
            "color_table_file.json",
            "style_sheet_table_file.json",
            "info_group_file.json",
            "tag_registry.json"
        )

        for file in dict_library:
            dict_path = os.path.join(self.debug_dir, file)
            with open(dict_path, "w+") as open_dict:
                json.dump({}, open_dict)

    @staticmethod
    def create_working_input_file(input_file: str) -> str:
        """ Copy of the input file for use during processing. """
        working_input_file = \
            Contents.Library.input_file_prep.processor(input_file=input_file)
        return working_input_file
