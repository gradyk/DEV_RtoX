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
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

"""

"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.header_parser_step_one"

# From local application
import rtf_file_lead_parse
import header_structure


class PretableController(object):

    def __init__(self, working_input_file: str, debug_dir: str) -> None:
        self.working_input_file = working_input_file
        self.debug_dir = debug_dir
        PretableController.determine_header_structure(self)
        PretableController.process_pretable_controlwords(self)

    def determine_header_structure(self):
        """
        Determine what tables are in the RTF header and store the table name
        and its line location in a dictionary.
        """
        header_structure.build_header_tables_dict(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir)

    def process_pretable_controlwords(self):
        """
        Process the control words that precede tables (rtf <charset> <deffont>
        \\deff).
        """

        rtf_file_lead_parse.check_input_file_encoding(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir)

        rtf_file_lead_parse.check_for_opening_brace(
            working_input_file=self.working_input_file,
            debug_dir=self.debug_dir)

        rtf_file_codes_update = \
            rtf_file_lead_parse.code_process(
                working_input_file=self.working_input_file)

        rtf_file_lead_parse.update_rtf_file_codes_dict(
            rtf_file_codes_update=rtf_file_codes_update,
            debug_dir=self.debug_dir)
