#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
from collections import deque

# From local application
import find_group_end
import flush_variables
import list_table
import split_between_characters

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    deck = deque()
    try:
        table_search = main_dict["wif_string"].find("listtable")
        if table_search != -1:
            main_dict["group_start"] = table_search - 4
            main_dict["index"] = main_dict["group_start"]
            find_group_end.processor(main_dict=main_dict, deck=deck)
            code_strings_list = split_between_characters.processor(
                main_dict=main_dict)
            main_dict = list_table.processor(
                main_dict=main_dict, code_strings_to_process=code_strings_list)
    except (IndexError, Exception) as error:
        msg = "A problem occurred searching for listtable."
        log.debug(error, msg)
    flush_variables.processor(main_dict=main_dict)
    return main_dict
