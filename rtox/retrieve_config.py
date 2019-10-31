# #############################################################################
#  Copyright (c) 2019 Kenneth A. Grady                                        #
#                                                                             #
#  Redistribution and use in source and binary forms, with or without         #
#  modification, are permitted provided that the following conditions are met:#
#                                                                             #
#  1. Redistributions of source code must retain the above copyright          #
#  notice, this list of conditions and the following disclaimer.              #
#                                                                             #
#  2. Redistributions in binary form must reproduce the above copyright       #
#  notice, this list of conditions and the following disclaimer in the        #
#  documentation and/or other materials provided with the distribution.       #
#                                                                             #
#  3. Neither the name of the copyright holder nor the names of its           #
#  contributors may be used to endorse or promote products derived            #
#  from this software without specific prior written permission.              #
#                                                                             #
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS    #
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,  #
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR     #
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR          #
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,      #
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,        #
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR         #
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF     #
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING       #
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF              #
#  THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.          #
# #############################################################################

# Retrieves the user-selected options from the configuration file and returns
# the config_setting_dict.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-23"
__name__ = "retrieve_config"


import sys
import os
import rtox.read_configuration
import rtox.options_trem
from log_config import logger


class RetrieveConfig:

    def __init__(self, 
                 system_arguments,
                 bug_handler,
                 configuration_file=None,
                 ):
        self.__system_arguments = system_arguments
        self.__configuration_file = configuration_file
        self.__bug_handler = bug_handler
    
    def get_options(self):
        # Return valid, output, help, show_warnings, debug, file.

        return_options = self.__get_config_options() 

        config_setting_dict = {
                                "dir":              [1],
                                "help":             [0, "h"],
                                "show-warnings":    [0],
                                "xml-tags":          [0],
                                "tei-tags":          [0],
                                "tpres-tags":        [0],
                                "caps":                     [0],
                                "no-caps":                  [0],
                                "symbol":                   [0],
                                "no-symbol":                [0],
                                "font":                     [0],
                                "no-font":                  [0],
                                "version":                  [0],
                                "output":                   [1, "o"],
                                "no-namespace":             [0],
                                "level":                    [1],
                                "indent":                   [1],
                                "no-lists":                 [0],
                                "lists":                    [0],
                                "format":                   [1, "f"],
                                "config":                   [0],
                }
                
        options_obj = rtox.options_trem.ParseOptions(
                        system_string=self.__system_arguments,
                        config_setting_dict=config_setting_dict
                    )
        options, arguments = options_obj.parse_options()

        if options == 0:
            return_options["valid"] = 0
            return return_options 
        the_keys = options.keys()

        return_options["help"] = 0
        if "help" in the_keys:
            return_options["help"] = 1
            return return_options

        return_options["config"] = 0
        if "config" in the_keys:
            return_options["config"] = 1
            return return_options

        return_options["version"] = 0
        if "version" in the_keys:
            return_options["version"] = 1
            return return_options

        return_options["out-file"] = 0
        if "output" in the_keys:
            return_options["out-file"] = options["output"]
        else:
            logger.debug(
                'You must provide an output file with the "-o" option.\n')
            return_options["valid"] = 0
            pass

        if "level" in the_keys:
            return_options["level"] = options["level"]

        the_level = return_options.get("level")
        if the_level:
            try:
                return_options["level"] = int(the_level)
            except ValueError:
                logger.debug('The options "--level" must be a number.\n')
                return_options["valid"] = 0
                return return_options

        acceptable = ["sdoc", "raw", "tpres"]
        if "format" in the_keys:
            formatted = options["format"]
            if formatted not in acceptable:
                logger.debug('--format must take either "sdoc" or '
                             '"tpres".\n')
                return_options["valid"] = 0
                return return_options
            else:
                return_options["format"] = options["format"]

        return_options["show-warnings"] = 0
        if "show-warnings" in the_keys:
            return_options["show-warnings"] = 1

        if "no-font" in the_keys:
            return_options["convert-symbol"] = 0

        if "font" in the_keys:
            return_options["convert-symbol"] = 1

        if "symbol" in the_keys:
            return_options["convert-symbol"] = 1
        if "no-symbol" in the_keys:
            return_options["convert-symbol"] = 0

        if "caps" in the_keys:
            return_options["convert-caps"] = 1
        if "no-caps" in the_keys:
            return_options["convert-caps"] = 0

        return_options["no-ask"] = 0
        if "no-ask" in the_keys:
            return_options["no-ask"] = 1
            logger.debug("You can also permanently set the no-ask option "
                         "in the .rtf2xml36 file.\n")

        if "no-namespace" in the_keys:
            return_options["no-namespace"] = 1

        if "no-lists" in the_keys:
            return_options["form-lists"] = 0
        elif "lists" in the_keys:
            return_options["form-lists"] = 1

        if len(arguments) == 0:
            logger.debug("You must provide a file to convert.\n")
            return_options["valid"] = 0
            return return_options
        elif len(arguments) > 1:
            logger.debug("You can only convert one file at a time.\n")
            return_options["valid"] = 0
        else:
            return_options["in-file"] = arguments[0]

        # check for out file

        smart_output = return_options.get("smart-output")
        if smart_output == "false":
            smart_output = 0

        if smart_output and not return_options["out-file"]:
            in_file = return_options["in-file"]
            the_file_name, ext = os.path.splitext(in_file)
            if ext != ".rtf":
                logger.debug('Sorry, but this file does not have an "rtf" \n'
                             'extension, so the script will not attempt to \n'
                             'convert it. If it is in fact an rtf file, use \n'
                             'the "-o" option.\n')
                return_options["valid"] = 0
            else:
                return_options["out-file"] = f"{the_file_name}.xml"

        if not smart_output and not return_options["out-file"]:
            logger.debug("Please provide a file to output with the -o option.\n"
                         "Or, set '<smart-output value = true/>' \n"
                         "in the configuration file.\n"
                         )
            return_options["valid"] = 0
            pass

        if "indent" in the_keys:
            try:
                value = int(options["indent"])
                return_options["indent"] = value
            except ValueError:
                logger.debug("--indent must take an integer")
                return_options["valid"] = 0

        return return_options

    def __get_config_options(self):
        #

        configure_obj = rtox.read_configuration.Configure(
            bug_handler=self.__bug_handler,
            configuration_file=self.__configuration_file)

        config_setting_dict = configure_obj.get_configuration()

        if config_setting_dict == 1:
            sys.exit(1)

        config_setting_dict["valid"] = 1

        convert_caps = config_setting_dict.get("convert-caps")
        if convert_caps == "false":
            config_setting_dict["convert-caps"] = 0

        convert_symbol = config_setting_dict.get("convert-symbol")
        if convert_symbol == "false":
            config_setting_dict["convert-symbol"] = 0

        form_lists = config_setting_dict.get("lists")
        if form_lists == "true" or form_lists == "1":
            config_setting_dict["form-lists"] = 1
        elif form_lists == "false" or form_lists == "0":
            config_setting_dict["form-lists"] = 0
        else:
            config_setting_dict["form-lists"] = 0

        return config_setting_dict
