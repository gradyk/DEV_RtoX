#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import os
from typing import Any


def initialize(base_dir: Any) -> tuple:
    debug_dir = os.path.join(base_dir, "debugdir")
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    main_script = os.path.join(base_dir, "RtoX.py")
    config_ini = os.path.join(base_dir, "Config.ini")
    return debug_dir, dicts_dir, main_script, config_ini
