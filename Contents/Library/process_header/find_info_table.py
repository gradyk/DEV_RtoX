#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
from collections import deque

# From local application
import find_group_end
import flush_variables
import information_group
import split_between_characters

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    deck = deque()
    try:
        table_search = main_dict["wif_string"].find("info")
        if table_search != -1:
            main_dict["group_start"] = table_search - 2
            main_dict["index"] = main_dict["group_start"]
            find_group_end.processor(main_dict=main_dict, deck=deck)
    except (IndexError, Exception) as error:
        msg = "A problem occurred searching for info."
        log.debug(error, msg)
    code_strings_list = split_between_characters.processor(main_dict=main_dict)
    _info_settings(main_dict=main_dict,
                   code_strings_to_process=code_strings_list)
    flush_variables.processor(main_dict=main_dict)
    return main_dict


def _info_settings(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for the RTF document info and store the
    settings in a dictionary. """
    information_group.InfoGrpParse.process_code_strings(
        self=information_group.InfoGrpParse(
            main_dict=main_dict,
            code_strings_to_process=code_strings_to_process))
