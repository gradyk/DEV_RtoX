
#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

from typing import Tuple


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    tag_info["cw_value"] = ""
    main_dict["contents_list"][2:-1] = ""
    return tag_info, main_dict
