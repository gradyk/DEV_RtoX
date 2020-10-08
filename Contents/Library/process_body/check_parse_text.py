#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_parse_text"

# From standard libraries
import re

# From local application
import check_group
import control_word
import backslash_text
import errant_space
import left_bracket_text
import check_text


def cpt_processor(main_dict: dict, collections_dict: dict) -> dict:
    main_dict["cw_regex"] = re.compile(r"^(\\[a-zA-Z\-0-9]*)")
    line = main_dict["line_to_parse"]
    while line < main_dict["list_size"] + 1:
        print(f"line: {line} -- text: {main_dict['parse_text']}")
        # Checks for a group.
        main_dict = check_group.cg_processor(
            main_dict=main_dict, collections_dict=collections_dict)
        # Checks for a backslash that should be treated as text.
        main_dict = backslash_text.bt_processor(main_dict=main_dict)
        # Checks for a left bracket that should be treated as text.
        # TODO Should there be a right bracket as text test?
        main_dict = left_bracket_text.lbt_processor(main_dict=main_dict)
        # Checks for a control word or destination.
        main_dict = control_word.cw_processor(
            main_dict=main_dict, collections_dict=collections_dict)
        # Checks for a space between control words.
        main_dict = errant_space.es_processor(main_dict=main_dict)
        # Checks for text.
        main_dict = check_text.ct_processor(main_dict=main_dict)
        line = main_dict["line_to_parse"]
    return main_dict
