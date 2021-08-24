#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging
import re

import character_cleanup

log = logging.getLogger(__name__)


def processor(new_line: str, array_codes: dict) -> str:
    """ Convert unicode codes to characters. """
    item = None
    pattern = re.compile(r"(\'[A-Z0-9]{2})")
    while character_cleanup.unicode_test(pattern=pattern, new_line=new_line) \
            is not item:
        try:
            test = pattern.search(new_line)
            test_string = new_line[test.start():test.end()]
            cleaned_string = test_string.replace("\'", "").upper()
            replacement_string = array_codes[cleaned_string]
            new_line = new_line.replace(new_line[test.start():test.end()],
                                        replacement_string)
        except KeyError as error:
            msg = f"{new_line}"
            log.debug(error, msg)
    return new_line
