#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

from typing import Tuple

import build_output_file


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    main_dict["update_output"] = "‘"
    build_output_file.processor(main_dict=main_dict)
    return tag_info, main_dict
