#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-9-15"
__name__ = "Contents.Library.process_body.find_body_group_end"

import logging
import sys
from typing import Any

import check_deck_status
import flush_variables
import build_group_contents_list
import group_contents

log = logging.getLogger(__name__)


def processor(main_dict: dict, deck: Any, collections_dict: dict) -> dict:
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
                main_dict = build_group_contents_list.processor(
                    main_dict=main_dict)
                main_dict = group_contents.processor(
                    main_dict=main_dict, collections_dict=collections_dict)
                flush_variables.processor(main_dict=main_dict)
                return main_dict
        else:
            main_dict["group_contents"] = \
                main_dict["group_contents"] + \
                main_dict["wif_string"][main_dict["index"]]
            main_dict["index"] = main_dict["index"] + 1
    return main_dict
