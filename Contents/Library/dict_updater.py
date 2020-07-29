#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

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
        json.dump(dict_new, dict_pre,
                  indent=4)
