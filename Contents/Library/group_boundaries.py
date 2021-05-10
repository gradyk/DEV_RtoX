#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
    Module identifies and returns the start line and index, and end line
and index, for RTF tables and groups.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-16"
__name__ = "Contents.Library.group_boundaries"

# From standard libraries
import logging
import sys
from collections import deque
from typing import Any

log = logging.getLogger(__name__)


def define_boundaries(main_dict: dict) -> Any:
    deck = deque()
    line = main_dict["table_start_line"]
    start_index = main_dict["table_start_index"]
    parse_text = main_dict["parse_text"]
    group_string_start = parse_text
    # The first character in the string should be an opening bracket ({).
    # This starts the process of 1) counting brackets, and 2) adjusting the
    # parse text.
    deck.append("{")
    deck_length = len(deck)
    parse_text = parse_text[1:]
    end_index = start_index + 2
    text_length = len(parse_text)
    # Each time we advance one character we have to check if parse_text has
    # only one character remaining. If so, we need to add to parse_text.
    if text_length == 1:
        parse_text, line, text_length, end_index = _adjust_text(
            parse_text=parse_text, main_dict=main_dict, line=line)
    # Now that we have put the first character (a left bracket) in deck and
    # ensured that parse_text has at least two characters,
    # we start the loop to find the right (closing) bracket for the
    # group. A group may have 0 to n subgroups.
    while deck_length != 0:
        try:
            if parse_text[0] == "{":
                deck.append("{")
            elif parse_text[0] == "}":
                deck.popleft()
            deck_length = len(deck)
            parse_text = parse_text[1:]
            end_index += 1
            text_length -= 1
            if deck_length == 0:
                _close_out(main_dict, line, parse_text, start_index, end_index,
                           group_string_start)
            elif text_length == 1:
                parse_text, line, text_length, end_index, line = \
                    _adjust_text(parse_text=parse_text,
                                 main_dict=main_dict, line=line)
        except IndexError as error:
            log.debug(error, f"Parse_text: {parse_text}; Table_start_line: "
                             f"{line}; Table_start_index: {start_index}")
            sys.exit()
    return main_dict


def _adjust_text(parse_text: str, main_dict: dict, line: int) -> tuple:
    # Since parse_text has only 1 character, increase parse_text by adding
    # the next string from working_input_file.
    line += 1
    new_text = main_dict["working_input_file"][line]
    parse_text = parse_text + new_text
    text_length = len(parse_text)
    end_index = 0
    return parse_text, line, text_length, end_index, line


def _close_out(main_dict, line, parse_text, start_index, end_index,
               group_string_start) -> dict:
    # If deck_length = 0, then we found the right bracket that closes the main
    # group.
    if main_dict["table_start_line"] == line:
        main_dict["group_contents"] = parse_text[start_index:end_index]
        main_dict["group_end_line"] = line
        main_dict["group_end_index"] = end_index - 1
    else:
        row = main_dict["table_start_line"] + 1
        end_index += 1
        group_string_new = ""
        group_string_end = main_dict["working_input_file"][line][:end_index - 2]
        start = main_dict["table_start_line"]
        end = line
        while row in range(start, end):
            group_string_new = group_string_new + \
                               main_dict["working_input_file"][row]
            row += 1
        group_string = group_string_start + group_string_new + group_string_end
        main_dict["group_contents"] = group_string
        main_dict["group_end_line"] = line
        main_dict["group_end_index"] = end_index - 2
    return main_dict
