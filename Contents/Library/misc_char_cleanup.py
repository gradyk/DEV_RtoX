#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import re


def processor(line: str, array_codes: dict) -> str:
    """ Convert miscellaneous characters to unicode. """
    item = None
    new_line = line
    pattern_list = [r"&", r"(HT\tab)", r"\tab"]
    for pattern in pattern_list:
        test = re.search(pattern, new_line)
        if test is not item:
            cleaned_test = "".join([i for i in test[0] if i.isalnum()])
            sub_string = array_codes[cleaned_test]
            new_line = re.sub(pattern, sub_string, new_line)
    return new_line
