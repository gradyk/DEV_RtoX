#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging
from typing import Any, Tuple

import control_word_to_build
import csv_modifier

log = logging.getLogger(__name__)


def processor(main_dict: dict, test: Any, collections_dict: dict) -> \
        Tuple[dict, dict, dict]:
    tag_info = {}
    cw_text = "".join([i for i in test if i.isalpha()])
    cw_value = "".join([i for i in test if i.isdigit()])
    null_function = "null"
    try:
        cw_func = collections_dict[cw_text]
        if cw_func != null_function:
            tag_info = {
                "func":             cw_func,
                "cw_text":          cw_text,
                "cw_value":         cw_value,
                "tag_status":       "",
                "tag_open_str":     "",
                "tag_close_str":    "",
                "tag_set":          main_dict["tag_set"]
            }
            main_dict = control_word_to_build.processor(
                tag_info=tag_info, main_dict=main_dict)
    except KeyError:
        # Add missing control word to control_words_collections.csv file.
        collections_dict = csv_modifier.processor(
            main_dict=main_dict, collections_dict=collections_dict,
            cw_text=cw_text)
        # TODO Fix
        # Add control word that cannot be processed to XML build file.
        # tag_insert_missing_cw.ti_processor(main_dict=main_dict,
        # cw_text=cw_text)
    return tag_info, main_dict, collections_dict
