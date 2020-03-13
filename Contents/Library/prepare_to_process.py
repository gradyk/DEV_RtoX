#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
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
This module performs preparatory housekeeping steps before the RTF file can
be processed.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.prepare_to_process"

# From standard libraries
import json
import os

# From local application
import input_file_prep
import prelim_routine
import rtf_codes_file_prep
from opening_tag_registry_dict import opening_tag_registry_dict


class PrepareToProcess:

    def __init__(self, base_script_dir: str, config_file: str,
                 debug_dir: str, input_file_name: str, output_file_name: str
                 ) -> None:
        self.base_script_dir = base_script_dir
        self.config_file = config_file
        self.debug_dir = debug_dir
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def extract_config_settings(self):
        """ Extract command line and Config.ini settings to run RtoX. Store
        the settings in the config_dict.py (config_dictionary). """
        self.base_script_dir, self.debug_dir, self.config_file = \
            prelim_routine.Prelim.prelim_settings(
                prelim_routine.Prelim(config_file=self.config_file,
                                      base_script_dir=self.base_script_dir,
                                      debug_dir=self.debug_dir))

        self.input_file_name, self.output_file_name = \
            prelim_routine.Prelim.create_config_dict(
                self=prelim_routine.Prelim(config_file=self.config_file,
                                           base_script_dir=self.base_script_dir,
                                           debug_dir=self.debug_dir))

        return self.base_script_dir, self.debug_dir, self.input_file_name, \
            self.output_file_name

    @staticmethod
    def extract_users_preferred_xml_tag_style():
        """ Extract the user's preference for XML tag style. """
        from config_dict import config_dictionary as rtf_settings_dict

        try:
            xml_tag_num = rtf_settings_dict.get("tag-style")
        except TypeError:
            xml_tag_num = 1

        return xml_tag_num

    def create_working_tag_registry(self):
        """ Dictionary for tracking open and closed XML tags. """
        tag_registry_file = os.path.join(self.debug_dir, "tag_registry.json")
        with open(tag_registry_file, "w", encoding='utf-8') as \
                tag_registry:
            json.dump(opening_tag_registry_dict, tag_registry)

    def create_header_table_dict(self):
        """ Dictionary for storing which tables are in the RTF file header
        and the line number on which each table starts. """
        header_tables_dict = os.path.join(self.debug_dir,
                                          "header_tables_dict.json")
        with open(header_tables_dict, "w+", encoding="utf-8") as \
                header_tables:
            json.dump({}, header_tables)

    def prepare_working_input_file(self):
        """ Create a copy of the input file for use during processing (
        working_input_file). """
        working_input_file = input_file_prep.InputPrep.input_file_prep(
            input_file_prep.InputPrep(input_file_name=self.input_file_name,
                                      debug_dir=self.debug_dir,
                                      base_script_dir=self.base_script_dir))

        return working_input_file

    def prepare_working_xml_file(self, xml_tag_num: str):
        """Create an XML file to hold tags during processing (
        working_xml_file)."""
        rtf_codes_file_prep.RTFCodesPrep.rtf_codes_to_xml_prep(
            self=rtf_codes_file_prep.RTFCodesPrep(
                debug_dir=self.debug_dir, xml_tag_num=xml_tag_num))
