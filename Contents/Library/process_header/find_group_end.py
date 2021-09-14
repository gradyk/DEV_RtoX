#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging
import sys
from typing import Any

import check_deck_status

log = logging.getLogger(__name__)


def processor(main_dict: dict, deck: Any) -> dict:
    length = len(main_dict["wif_string"])
    while main_dict["index"] <= length:
        if main_dict["wif_string"][main_dict["index"]] == "{":
            main_dict["group_contents"] = \
                main_dict["group_contents"] + \
                main_dict["wif_string"][main_dict["index"]]
            deck.append("{")
            main_dict["index"] = main_dict["index"] + 1
        elif main_dict["wif_string"][main_dict["index"]] == "}":
            main_dict["group_contents"] = \
                main_dict["group_contents"] + \
                main_dict["wif_string"][main_dict["index"]]
            try:
                deck.popleft()
            except IndexError as error:
                msg = f"Something went wrong with the bracket count. " \
                      f"Location: {main_dict['wif_string'][main_dict['index']:main_dict['index']+30]}"
                log.debug(error, msg)
                sys.exit(1)
            main_dict["index"] = main_dict["index"] + 1
            main_dict = check_deck_status.processor(
                main_dict=main_dict, deck=deck)
            if main_dict["group_end_found"] is True:
                main_dict["index_ptr"] = max(main_dict["index_ptr"],
                                             main_dict["index"])
                return main_dict
        else:
            main_dict["group_contents"] = \
                main_dict["group_contents"] + \
                main_dict["wif_string"][main_dict["index"]]
            main_dict["index"] = main_dict["index"] + 1
    return main_dict
