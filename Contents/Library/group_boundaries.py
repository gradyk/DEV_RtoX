#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Module identifies and returns the start line and index, and end line
and index, for RTF tables and groups.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-05-22"
__name__ = "Contents.Library.group_boundaries"

# From standard libraries
import logging
from collections import deque
from typing import Tuple

log = logging.getLogger(__name__)


def initialize(main_dict: dict) -> dict:
    temp_dict = {
        "deck":             deque(),
        "text_length":      0,
        "line":             main_dict["group_start_line"],
        "start_index":      main_dict["group_start_index"],
        "end_index":        0,
        "parse_text":       main_dict["parse_text"],
        "group_contents":   "",
        "character":        ""
    }
    temp_dict = _remove_lead_bracket(temp_dict=temp_dict)
    return temp_dict


def _remove_lead_bracket(temp_dict: dict) -> dict:
    # These steps start the process of 1) counting brackets, and 2) adjusting
    # the parse text.
    temp_dict["deck"].append("{")
    temp_dict["deck_length"] = len(temp_dict["deck"])
    temp_dict["parse_text"] = temp_dict["parse_text"][1:]
    temp_dict["end_index"] = temp_dict["start_index"] + 1
    temp_dict["text_length"] = len(temp_dict["parse_text"])
    return temp_dict


def process(main_dict: dict, temp_dict: dict) -> dict:
    main_dict, temp_dict = _adjust_text(
        main_dict=main_dict, temp_dict=temp_dict)
    main_dict, temp_dict = _eval_parse_text(
        main_dict=main_dict, temp_dict=temp_dict)
    main_dict, temp_dict = _adjust_text(
        main_dict=main_dict, temp_dict=temp_dict)
    return main_dict


def _adjust_text(main_dict: dict, temp_dict: dict) -> Tuple[dict, dict]:
    # If parse_text has only 1 character, increase parse_text by adding
    # the next string from working_input_file.
    if temp_dict["text_length"] == 1:
        temp_dict["line"] += 1
        new_text = main_dict["working_input_file"][temp_dict["line"]]
        temp_dict["parse_text"] = temp_dict["parse_text"] + new_text
        main_dict["parse_text"] = temp_dict["parse_text"]
        main_dict["group_end_line"] = temp_dict["line"]
        temp_dict["text_length"] = len(temp_dict["parse_text"])
        temp_dict["end_index"] = 0
    else:
        pass
    return main_dict, temp_dict


def _eval_parse_text(main_dict: dict, temp_dict: dict) -> Tuple[dict, dict]:
    # Loop through parse text until deck length equals zero (boundaries have
    # been found).
    while temp_dict["deck_length"] != 0:
        temp_dict = _process_parse_text_character(
            command=temp_dict["parse_text"][0], temp_dict=temp_dict)
        temp_dict = _adjust_variables(temp_dict=temp_dict)
        # Test for group end. If not, test whether parse text needs more
        # text.
        main_dict, temp_dict = _check_deck_status(
            main_dict=main_dict, temp_dict=temp_dict)
        main_dict, temp_dict = \
            _adjust_text(main_dict=main_dict, temp_dict=temp_dict)
    return main_dict, temp_dict


def _process_parse_text_character(command, temp_dict) -> dict:
    choice = {
        "{":        _left_bracket,
        "}":        _right_bracket,
        "other":   _other_character
    }
    try:
        if command == "{" or command == "}":
            code_function = choice[command]
        else:
            code_function = choice["other"]
        temp_dict["character"] = command
        code_function(temp_dict=temp_dict)
    except (AttributeError, TypeError):
        logging.exception(msg="The program encountered a processing "
                              "problem in group_boundaries.")
    return temp_dict


def _left_bracket(temp_dict: dict) -> dict:
    temp_dict["group_contents"] = temp_dict["group_contents"] + "{"
    temp_dict["deck"].append("{")
    return temp_dict


def _right_bracket(temp_dict: dict) -> dict:
    temp_dict["group_contents"] = temp_dict["group_contents"] + "}"
    temp_dict["deck"].popleft()
    return temp_dict


def _other_character(temp_dict: dict) -> dict:
    temp_dict["group_contents"] = temp_dict["group_contents"] + temp_dict[
        "character"]
    return temp_dict


def _adjust_variables(temp_dict: dict) -> dict:
    temp_dict["deck_length"] = len(temp_dict["deck"])
    temp_dict["parse_text"] = temp_dict["parse_text"][1:]
    temp_dict["end_index"] += 1
    temp_dict["text_length"] -= 1
    return temp_dict


def _check_deck_status(main_dict: dict, temp_dict: dict) -> Tuple[dict, dict]:
    if temp_dict["deck_length"] == 0:
        temp_dict["group_contents"] = temp_dict["group_contents"][:-1]
        main_dict, temp_dict = _close_out(
            main_dict=main_dict, temp_dict=temp_dict)
    return main_dict, temp_dict


def _close_out(main_dict, temp_dict: dict) -> Tuple[dict, dict]:
    # If deck_length = 0, then we found the right bracket that closes the main
    # group.
    main_dict["group_end_line"] = temp_dict["line"]
    main_dict["group_end_index"] = temp_dict["end_index"]

    text_phrase = "{" + temp_dict["group_contents"] + "}"
    main_dict["parse_text"] = temp_dict["parse_text"].replace(
        text_phrase, "", 1)

    main_dict["group_counter"] += 1
    return main_dict, temp_dict
