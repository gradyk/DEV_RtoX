#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

# From standard library
import json
import os


def json_dict_updater(dict_name: str, dict_update: dict, debug_dir: str):
    dict_to_update = os.path.join(debug_dir, dict_name)
    with open(dict_to_update, "r+") as dict_pre:
        dict_new = json.load(dict_pre)
        dict_new.update(dict_update)
        dict_pre.seek(0)
        json.dump(dict_new, dict_pre, indent=4, sort_keys=False)
