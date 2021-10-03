#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import re


def processor(main_dict: dict) -> dict:
    ignored_code_dict = {
        "loch": r"\loch\f[0-9]*"
    }
    for code in ignored_code_dict:
        while re.search(code, main_dict["wif_string"]) is not None:
            test = re.search(code, main_dict["wif_string"])
            main_dict["wif_string"] = \
                main_dict["wif_string"].replace(
                    main_dict["wif_string"][test.start():test.end()], "")
    return main_dict
