#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#   RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Process the RTF file color table. The current version of RtoX notes the
existence of the table in the codes dictionary, but does not parse the table.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "Contents.Library.color_table"

# From standard libraries
import re

# From local application
import dict_updater


class ColortblParse(object):
    """ An RTF file uses the following structure for a colortbl (if present):
    <colortbl>      '{' \\colortbl <colordef>+ '}'
    <colordef>      \red ? & \\green ? & \blue ? '}'
    """
    def __init__(self,
                 code_strings_to_process: list,
                 debug_dir: str) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.debug_dir = debug_dir

    def color_process_controller(self):
        code_string = ColortblParse.process_code_strings(
            self=ColortblParse(
                code_strings_to_process=self.code_strings_to_process,
                debug_dir=self.debug_dir))

        ColortblParse.process_color_codes(
            self=ColortblParse(
                code_strings_to_process=self.code_strings_to_process,
                debug_dir=self.debug_dir),
            code_string=code_string)

    def process_code_strings(self):
        code_string = ""
        for ele in self.code_strings_to_process:
            code_string += ele
        return code_string

    def process_color_codes(self, code_string: str):
        color_codes = code_string.split(";")
        for ele in color_codes:
            try:
                test = re.search(r'{\\colortbl;', ele)
                color_codes[0] = "\\red255\\green255\\blue255"
            except ValueError:
                pass

        for ele in color_codes:
            try:
                test = re.search(r'}', ele)
                color_codes.remove(ele)
            except ValueError:
                pass

        i = 0
        for code in color_codes:
            color_code_updater = {i: code}
            dict_updater.json_dict_updater(dict_name="color_table_file.json",
                                           dict_update=color_code_updater,
                                           debug_dir=self.debug_dir)
            i += 1
