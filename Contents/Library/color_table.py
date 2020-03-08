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


class ColortblParse(object):
    """ An RTF file uses the following structure for a colortbl (if present):
    <colortbl>      '{' \\colortbl <colordef>+ '}'
    <colordef>      \red ? & \\green ? & \blue ? '}'
    """
    def __init__(self, code_strings_to_process: list) -> None:
        self.code_strings_to_process = code_strings_to_process

        code_string = ColortblParse.process_code_strings(self=ColortblParse(
            code_strings_to_process=self.code_strings_to_process))

        ColortblParse.process_color_codes(
            self=ColortblParse(
                code_strings_to_process=self.code_strings_to_process),
            code_string=code_string)

    def process_code_strings(self):

        for code_string in self.code_strings_to_process:

            ColortblParse.process_color_codes(
                self=ColortblParse(
                    code_strings_to_process=self.code_strings_to_process),
                code_string=code_string)

            return code_string

    def process_color_codes(self, code_string: str):
        pass
