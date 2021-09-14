#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    # If deck_length = 0, then we found the right bracket that closes the main
    # group.
    main_dict["group_end_line"] = temp_dict["line"]
    main_dict["group_end_index"] = temp_dict["end_index"]

    text_phrase = "{" + temp_dict["group_contents"] + "}"
    main_dict["parse_text"] = temp_dict["parse_text"].replace(
        text_phrase, "", 1)
    main_dict["group_counter"] += 1
    return main_dict
