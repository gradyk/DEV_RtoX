#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import re


def processor(main_dict: dict, array_codes: dict) -> dict:
    """ Convert miscellaneous characters to unicode. """
    item = None
    pattern_list = [r"&", r"(HT\tab)", r"\tab"]
    for pattern in pattern_list:
        test = re.search(pattern, main_dict["wif_string"])
        if test is not item:
            cleaned_test = "".join([i for i in test[0] if i.isalnum()])
            if cleaned_test is not '':
                sub_string = array_codes[cleaned_test]
                main_dict["wif_string"] = re.sub(pattern, sub_string,
                                                 main_dict["wif_string"])
    return main_dict
