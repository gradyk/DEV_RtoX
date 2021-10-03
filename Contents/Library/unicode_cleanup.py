#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging
import re

log = logging.getLogger(__name__)


def processor(main_dict: dict, array_codes: dict) -> dict:
    """ Convert unicode codes to characters. """
    pattern = re.compile(r"(\'[a-zA-Z0-9]{2})")
    while re.search(pattern, main_dict["wif_string"]) is not None:
        test = re.search(pattern, main_dict["wif_string"])
        result = main_dict["wif_string"][test.start():test.end()]
        result = result.upper()
        cleaned_string = result.replace("\'", "").upper()
        replacement_string = array_codes[cleaned_string]
        main_dict["wif_string"] = \
            main_dict["wif_string"].replace(
                main_dict["wif_string"][test.start():test.end()],
                replacement_string)
    return main_dict
