#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2019. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Prepare csv files for use in processing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-29"
__name__ = "csv_prep"

import csv
import os


class CSVPrep:

    def __init__(self,
                 debug_dir
                ):
        self.__debug_dir = debug_dir

    def csv_file_prep(self):
        """
        Prepare csv files for table codes.
        """

        # Prepare font code csv file.
        font_file = os.path.join(self.__debug_dir, "fonts.csv")
        line = ["fontnum", "name", "fcharset", "fprq", "panose",
                "fontfamily", "altname", "fontemb", "cpg"]

        with open(font_file, 'w') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, delimiter=",",
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
            temp_file_writer.writerow(line)

        # Prepare style sheet code csv file.
        style_file = os.path.join(self.__debug_dir, "styles.csv")
        line = ["code", "additive", "para_next_style", "bold",
                "italic", "underline", "small_caps",
                "strikethrough", "style_name"]

        with open(style_file, 'w') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, delimiter=",",
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
            temp_file_writer.writerow(line)

        # Prepare info code csv file.
        info_file = os.path.join(self.__debug_dir, "info.csv")
        line = ["title", "subject", "author", "manager", "company",
                "operator", "category", "keywords", "comment" 
                "document_comments", "hyperlink_base_address", "count",
                "year", "month", "day", "minutes", "seconds", "version",
                "editing_time_minutes", "no_of_pages", "no_of_words",
                "no_of_characters_with_spaces",
                "no_of_characters_without_spaces", "internal_version_number"]

        with open(info_file, 'w') as temp_file:
            temp_file_writer = \
                csv.writer(temp_file, delimiter=",",
                           quotechar='"', quoting=csv.QUOTE_MINIMAL)
            temp_file_writer.writerow(line)


