#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


def processor(temp_dict: dict) -> dict:
    temp_dict["group_contents"] = temp_dict["group_contents"] + "}"
    temp_dict["deck"].popleft()
    return temp_dict
