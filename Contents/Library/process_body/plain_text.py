#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging

import build_output_file

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:

    try:
        text = main_dict["wif_string"][main_dict["index"]]
        main_dict["index"] = main_dict["index"] + 1
        main_dict = build_output_file.processor(
            update_output=text, main_dict=main_dict)
    except (TypeError, Exception) as error:
        msg = f"Check_text: " \
              f"{main_dict['wif_string'][main_dict['index']:main_dict['index']+50]}"
        log.debug(error, msg)
    return main_dict
