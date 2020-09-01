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
import linecache
from collections import deque
import logging
import sys


def define_boundaries(processing_dict: dict) -> dict:
    """ Define the boundaries of an RTF group across multiple lines,
    while capturing the contents of the group. """
    processing_dict["group_contents"] = ""
    deck = deque()
    working_index = processing_dict["parse_index"]
    end_line = processing_dict["line_to_parse"]
    boundary_test(deck=deck, processing_dict=processing_dict,
                  working_index=working_index, end_line=end_line)
    return processing_dict


def boundary_test(processing_dict: dict, working_index: int, deck,
                  end_line: int) -> dict:

    ptext = linecache.getline(processing_dict["working_input_file"], end_line)
    ptext = ptext.rstrip("\n").rstrip(" ")
    ptext = ptext[working_index:]
    group_contents = ""
    length = len(ptext)
    processing_dict = boundary_loop(
        processing_dict=processing_dict,
        length=length,
        deck=deck, working_index=working_index,
        ptext=ptext, end_line=end_line,
        group_contents=group_contents)

    return processing_dict


def boundary_loop(processing_dict: dict, length: int, deck,
                  working_index: int, ptext: str, end_line: int,
                  group_contents: str) -> dict:
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
        group_contents = group_contents + ptext[working_index]
        working_index += 1

        decklength = len(deck)
        if decklength == 0:
            processing_dict["group_end_line"] = end_line
            processing_dict["group_end_index"] = working_index
            processing_dict["group_contents"] = group_contents
            processing_dict["line_to_parse"] = end_line
            processing_dict["parse_index"] = working_index + 1

            return processing_dict

        else:
            if working_index > length - 1:
                ptext, working_index, end_line, length, deck, group_contents = \
                    test_ptext(processing_dict=processing_dict,
                               end_line=end_line, group_contents=group_contents,
                               deck=deck)
            else:
                pass


def test_ptext(processing_dict: dict, end_line: int, deck,
               group_contents: str):
    end_line += 1
    ptext = linecache.getline(processing_dict["working_input_file"],
                              end_line).rstrip("\n").rstrip()
    length = len(ptext)
    working_index = 0
    return ptext, working_index, end_line, length, deck, group_contents
