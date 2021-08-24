#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


import logging
import os
import posixpath

import read_configuration

log = logging.getLogger(__name__)


def retrieve(main_dict: dict) -> dict:
    config_settings_dict = read_configuration.get_system_arguments()
    config_settings_dict = read_configuration.get_configuration(
        main_dict=main_dict, config_settings_dict=config_settings_dict)
    try:
        file = config_settings_dict.get("output")
        main_dict["output_file_name"] = \
            posixpath.join(main_dict["base_dir"], "output", file)
        main_dict["output_file"] = file
    except (TypeError, Exception) as error:
        msg = "You did not provide the name of an output file. RtoX will " \
              "produce an output file with the name of your input file plus " \
              "the extension .xml."
        log.info(error, msg)
        final_output_file = \
            os.path.splitext(main_dict["input_file"])[0] + '.xml'
        main_dict["output_file_name"] = \
            posixpath.join(main_dict["base_dir"], "output",
                           final_output_file)
    return main_dict
