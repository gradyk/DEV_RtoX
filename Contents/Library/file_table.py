#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
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

""" Parse the file table (if the table exists in the document it means the
pre-RTF file included sub-documents). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "Contents.Library.file_table"

# From standard libraries

# From local application


class FiletblParse(object):
    """ An RTF file uses the following structure for a filetbl (if present):
    <filetbl>       '{\\*'\filetbl ('{' <fileinfo> '}')+ '}'
    <fileinfo>      \file <filenum><relpath>?<osnum>? <filesource>+ <file name>
    <filenum>       \fid
    <relpath>       \frelative
    <osnum>         \fosnum
    <filesource>    \fvalidmac | \fvaliddos | \fvalidntfs | \fvalidhpfs |
                    \fnetwork | \fnonfilesys
    <file name>     #PCDATA
    """

    def __init__(self, code_strings_to_process: list) -> None:
        self.code_strings_to_process = code_strings_to_process

        code_string = FiletblParse.process_code_strings(self=FiletblParse(
            code_strings_to_process=self.code_strings_to_process))

        FiletblParse.process_file_table_codes(self=FiletblParse(
            code_strings_to_process=self.code_strings_to_process),
            code_string=code_string)

    def process_code_strings(self):

        for code_string in self.code_strings_to_process:
            FiletblParse.process_file_table_codes(
                self=FiletblParse(
                    code_strings_to_process=self.code_strings_to_process),
                code_string=code_string)

            return code_string

    def process_file_table_codes(self, code_string: str):
        pass
