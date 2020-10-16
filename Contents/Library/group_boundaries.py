#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Module that identifies and returns the start line and index, and end line 
and index, for RTF tables or groups. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.group_boundaries"

# From standard libraries
import logging
from collections import deque
from typing import Any


def define_boundaries(main_dict: dict) -> dict:
    """ Define the boundaries of an RTF table or group. """
    deck = deque()
    end_line = main_dict["table_start_line"]
    contents = main_dict["parse_text"]
    length = len(contents)
    group_contents = ""
    working_index = 0
    main_dict = boundary_loop(
        main_dict=main_dict, length=length, deck=deck,
        working_index=working_index, contents=contents, end_line=end_line,
        group_contents=group_contents)
    return main_dict


def boundary_loop(main_dict: dict, length: int, deck, working_index: int,
                  contents: str, end_line: int, group_contents: str) -> dict:
    while working_index <= (length - 1):
        deck = bracket_test(contents=contents,
                            deck=deck, working_index=working_index)
        group_contents = group_contents + contents[working_index]
        contents, working_index, end_line, length = adjust_working_index(
            main_dict=main_dict, end_line=end_line, contents=contents,
            working_index=working_index, length=length)
        decklength = len(deck)
        if decklength == 0:
            main_dict["group_end_line"] = end_line
            main_dict["group_end_index"] = working_index
            main_dict["group_contents"] = group_contents
            main_dict["line_to_parse"] = end_line
            main_dict["parse_index"] = working_index + 1
            return main_dict


def bracket_test(contents: str, deck: Any, working_index: int):
    try:
        if contents[working_index] == "{":
            deck.append("{")
        if contents[working_index] == "}":
            deck.popleft()
        return deck
    except IndexError as error:
        logging.exception(error, f"Working_index exceeds length.")


def adjust_working_index(main_dict: dict, end_line: int,
                         working_index: int, length: int,
                         contents: str) -> tuple:
    working_index += 1
    try:
        if working_index > (length - 1):
            end_line += 1
            contents = main_dict["working_input_file"][end_line].rstrip()
            length = len(contents)
            working_index = 0
            return contents, working_index, end_line, length
    except IndexError:
        working_index -= 1
    return contents, working_index, end_line, length
