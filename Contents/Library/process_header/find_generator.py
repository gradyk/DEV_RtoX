#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
from collections import deque

# From local application
import dict_updater
import find_group_end
import flush_variables

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    try:
        table_search = main_dict["wif_string"].find("generator")
        if table_search != -1:
            main_dict["group_start"] = table_search - 4
            deck = deque()
            find_group_end.processor(main_dict=main_dict, deck=deck)
            _trim_generator(main_dict=main_dict)
            _generator_settings(main_dict=main_dict)
    except (IndexError, Exception) as error:
        msg = "A problem occurred searching for generator."
        log.debug(error, msg)
    flush_variables.processor(main_dict=main_dict)
    return main_dict


def _trim_generator(main_dict: dict) -> dict:
    """ RTF wraps the generator information with {\\*\\generator ... }. This
    function removes the prefix and suffix. """
    main_dict["group_contents"] = main_dict["group_contents"].replace(
        "{\\*\\generator", "").rstrip("}")
    return main_dict


def _generator_settings(main_dict: dict) -> dict:
    """ Process the code settings for each generator entry and
    store the settings in a dictionary.
    '{' \\*\\generator <name> '}' """
    # \*\generator (emitter application stamps the doc with its name,
    # version and build number
    dict_update = {"doc_info": main_dict["group_contents"]}
    dict_updater.json_dict_updater(
        dict_name="generator.json",
        dict_update=dict_update,
        main_dict=main_dict)
    main_dict["group_contents"] = ""
    return main_dict
