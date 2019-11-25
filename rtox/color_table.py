#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
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
Process color table (version 0.1.0a0 notes the existence of the table in the
XML file and the codes dictionary).
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "color_table"

import rtox.xml_color_tags


class ColortblParse:
    """
    Process Header color table.
    """

    def __init__(
                 self,
                 working_file,
                 line_to_check,
                 debug_dir
                 ):
        self.__working_file = working_file
        self.__line_to_read = line_to_check
        self.__debug_dir = debug_dir

    def color_table(self, xml_tag_num):
        """
        Record a tag about the color table, but do not save all color table
        settings (typically not relevant for XML applications).
        """

        rtox.xml_color_tags.XMLTagSets.xml_color_tags(
            self=rtox.xml_color_tags.XMLTagSets(
                debug_dir=self.__debug_dir,
                xml_tag_num=xml_tag_num))

        # TODO this needs to get written to a dictionary here - call
        #  update_rtf_file_codes??
        color_code_list = {"colortbl": 'Skipped'}

        return color_code_list
