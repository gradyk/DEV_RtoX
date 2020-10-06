#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.process_body.group_boundaries"

# From standard libraries
from collections import deque
import logging
import sys


def define_boundaries(main_dict: dict) -> dict:
    """ Define the boundaries of an RTF group across multiple lines,
    while capturing the contents of the group. """
    main_dict["group_contents"] = ""
    deck = deque()
    working_index = main_dict["parse_index"]
    end_line = main_dict["line_to_parse"]

    ptext = main_dict["working_input_file"][end_line].rstrip(" ")
    ptext = ptext[working_index:]
    length = len(ptext)

    while working_index <= length - 1:
        try:
            if ptext[working_index] == "{":
                deck.append("{")
            elif ptext[working_index] == "}":
                deck.popleft()
            else:
                pass
        except IndexError as error:
            logging.exception(error, f"Working_index= {working_index}, "
                                     f"length= {length}.")
            sys.exit()
        main_dict["group_contents"] = ''.join([main_dict["group_contents"] +\
                                              ptext[working_index]])
        working_index += 1

        decklength = len(deck)
        if decklength == 0:
            main_dict["group_end_line"] = end_line
            main_dict["group_end_index"] = working_index
            main_dict["line_to_parse"] = end_line
            main_dict["parse_index"] = working_index + 1
            return main_dict
        else:
            if working_index > length - 1:
                end_line += 1
                ptext = main_dict["working_input_file"][end_line].rstrip()
                length = len(ptext)
                working_index = 0
            else:
                pass
    return main_dict
