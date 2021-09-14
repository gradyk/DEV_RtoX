#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def processor(main_dict: dict) -> dict:
    main_dict["group_start"] = 0
    main_dict["group_contents"] = ""
    main_dict["group_end_found"] = False
    return main_dict
