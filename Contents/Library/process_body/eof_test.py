#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Test whether the end of the input file has been reached. If yes,
do post-processing. If no, continue processing. """

from collections import deque

import check_string
import final_step


def processor(main_dict: dict, collections_dict: dict) -> None:
    deck = deque()
    if not main_dict["wif_string"]:
        final_step.processor(main_dict=main_dict)
    else:
        main_dict["index"] += 1
        check_string.processor(main_dict=main_dict,
                               collections_dict=collections_dict, deck=deck)
