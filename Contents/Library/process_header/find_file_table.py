#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
from collections import deque

# From local application
import file_table
import find_group_end
import flush_variables

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    try:
        table_search = main_dict["wif_string"].find("filetbl")
        if table_search != -1:
            main_dict["group_start"] = table_search - 4
            main_dict["index"] = main_dict["group_start"]
            deck = deque()
            main_dict = find_group_end.processor(main_dict=main_dict, deck=deck)
    except (IndexError, Exception) as error:
        msg = "A problem occurred searching for colortbl."
        log.debug(error, msg)
    """ Process the code settings for each color number and store the
    settings in a dictionary. """
    main_dict = file_table.trim_filetbl(main_dict=main_dict)
    main_dict, code_strings_list = file_table.split_code_strings(
        main_dict=main_dict)
    file_table.parse_code_strings(
        code_strings_list=code_strings_list, main_dict=main_dict)
    flush_variables.processor(main_dict=main_dict)
    return main_dict
