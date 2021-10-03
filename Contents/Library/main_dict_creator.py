#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" RtoX uses the main dict to pass variables among modules when parsing the
body of the RTF document. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.main_dict_creator"

import json
import os
from typing import Any


def processor(base_dir: Any, debug_dir: Any, dicts_dir: Any,
              main_script: Any, config_ini: Any) -> dict:
    main_dict_file = os.path.join(base_dir, dicts_dir, "main_dict.json")
    with open(main_dict_file) as mdf_pre:
        main_dict = json.load(mdf_pre)
    main_dict["base_dir"] = base_dir
    main_dict["debug_dir"] = debug_dir
    main_dict["dicts_dir"] = dicts_dir
    main_dict["main_script"] = main_script
    main_dict["config_ini"] = config_ini
    return main_dict
