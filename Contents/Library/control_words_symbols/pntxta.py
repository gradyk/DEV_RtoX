#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

from typing import Tuple


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    main_dict["contents_list"] = ""
    main_dict["status"] = 1
    return tag_info, main_dict
