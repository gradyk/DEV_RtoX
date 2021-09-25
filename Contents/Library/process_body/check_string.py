#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_string"

# From standard libraries
import logging
import re
import sys
from collections import deque

# From local application
import control_word
import eof_test
import find_body_group_end
import plain_text

log = logging.getLogger(__name__)


def pre_processor(main_dict: dict, collections_dict: dict) -> None:
    main_dict["cw_regex"] = re.compile(r"^\\[*]?[\\]?[a-zA-Z\-0-9]*")
    if collections_dict is None:
        sys.exit("Collections_dict is empty.")
    main_dict["index"] = main_dict["index_ptr"]
    eof_test.processor(main_dict=main_dict, collections_dict=collections_dict)


def processor(main_dict: dict, collections_dict: dict) -> None:
    deck = deque()
    length = len(main_dict["wif_string"])
    while main_dict["index"] < length:
        try:
            if main_dict["wif_string"][main_dict["index"]] == "{":
                main_dict = find_body_group_end.processor(
                    main_dict=main_dict, deck=deck,
                    collections_dict=collections_dict)
                main_dict["group_end_found"] = False
            elif main_dict["wif_string"][main_dict["index"]] == "\\":
                control_word.processor(
                    main_dict=main_dict, collections_dict=collections_dict)
            else:
                plain_text.processor(main_dict=main_dict)
        except (KeyError, IndexError, Exception) as error:
            msg = f"Issue in input file: {main_dict['index']: }" \
                  f"{main_dict['wif_string'][main_dict['index']:main_dict['index']+50]}"
            log.debug(error, msg)
