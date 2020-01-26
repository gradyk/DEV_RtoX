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
This script covers some preparatory work before the input file can be processed.
1.
2. Empty the tables in the rtox_db from the last time a file was processed.
3. Copy the input file to "working_file" in the debugdir directory and use
that new file for processing (to avoid inadvertent corruption of the input
file).
4. Determine the user's preference for XML tags (plain, TEI, TPRES --
xml_tag_num) so the proper tags can be applied during processing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "prepare_to_process"

# From standard libraries
import json
import os

# From local application
import rtox.databases.database_clean
import rtox.input_file_prep
import rtox.prelim_routine
import rtox.rtf_codes_file_prep
from rtox.dicts.tag_registry import tag_registry_dict


class PrepareToProcess:

    def __init__(self,
                 base_script_dir="",
                 config_file="",
                 debug_dir="",
                 input_file_name="",
                 output_file_name=""
                 ):
        self.base_script_dir = base_script_dir
        self.config_file = config_file
        self.debug_dir = debug_dir
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name

    def file_structure(self):
        base_script_dir_pass = self.base_script_dir
        config_file_pass = self.config_file
        debug_dir_pass = self.debug_dir
        input_file_name_pass = self.input_file_name
        output_file_name_pass = self.output_file_name

        return base_script_dir_pass, config_file_pass, debug_dir_pass,\
            input_file_name_pass, output_file_name_pass

    def prelim_routine(self):
        """
        1. Gather command line and Config.ini settings to run RtoX.
        2. Store the settings in the config_dict.py (config_dictionary).
        """
        prelim_vars = rtox.prelim_routine.Prelim.prelim_settings(
            rtox.prelim_routine.Prelim(
                config_file=self.config_file,
                base_script_dir=self.base_script_dir,
                debug_dir=self.debug_dir))
        self.base_script_dir = prelim_vars[0]
        self.debug_dir = prelim_vars[1]
        self.config_file = prelim_vars[2]

        config_vars = rtox.prelim_routine.Prelim.create_config_dict(
            self=rtox.prelim_routine.Prelim(
                config_file=self.config_file,
                base_script_dir=self.base_script_dir,
                debug_dir=self.debug_dir))
        self.input_file_name = config_vars[0]
        self.output_file_name = config_vars[1]

        return self.base_script_dir, self.debug_dir, self.input_file_name, \
            self.output_file_name

    @staticmethod
    def rtox_db_clean():
        """
        Remove all rows from the rtox_db database tables. (They aren't
        removed at the end of the prior RtoX run in case they are needed for
        debugging purposes.)
        """
        from debugdir.config_dict import config_dictionary
        host_pass = config_dictionary.get("host")
        database_pass = config_dictionary.get("database")
        user_pass = config_dictionary.get("user")
        password_pass = config_dictionary.get("password")

        rtox.databases.database_clean.DBClean.db_clean(
            self=rtox.databases.
            database_clean.DBClean(host=host_pass, database=database_pass,
                                   user=user_pass, password=password_pass))

    def xml_tag_pref(self):
        """
        Determine user's preference for XML tag style and use the appropriate
        dictionary.
        """

        from debugdir.config_dict import config_dictionary as rtf_settings_dict

        xml_tag_num = rtf_settings_dict.get("tag-style")
        if xml_tag_num is None:
            xml_tag_num = 4
        else:
            pass

        file_list = [[1, "xml_tags.py"], [2, "tei_tags.py"],
                     [3, "tpres_tags.py"], [4, "xml_tags.py"]]

        tag_file = file_list[int(xml_tag_num)-1][1]
        tag_dict = os.path.join(self.debug_dir, tag_file)

        return tag_dict, xml_tag_num

    def create_working_tag_registry(self):
        with open(os.path.join(self.debug_dir, "tag_registry.txt"), "w+") as \
                tag_registry_working_file:
            json.dump(tag_registry_dict, tag_registry_working_file)

    def prep_rtf_file(self, xml_tag_num):
        """
        1. Create a copy of the input file for use during processing.
        2. Create an XML file to hold tags (it will become the output file).
        """
        working_file = rtox.input_file_prep.InputPrep.input_file_prep(
            rtox.input_file_prep.
            InputPrep(input_file_name=self.input_file_name,
                      debug_dir=self.debug_dir,
                      base_script_dir=self.base_script_dir))

        rtox.rtf_codes_file_prep.RTFCodesPrep.rtf_codes_to_xml_prep(
            self=rtox.rtf_codes_file_prep.RTFCodesPrep(
                debug_dir=self.debug_dir, xml_tag_num=xml_tag_num))

        return working_file
