#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
import re
from read_log_config import logger_debug


def pre_process(main_dict: dict) -> dict:
    main_dict["contents_string"] = main_dict["group_contents"]
    item = None
    pattern_dict = {
        "lb": re.compile(r"^{"),
        "rb": re.compile(r"^[}]"),
        "dest": re.compile(r"^(\\\*\\[a-zA-Z-0-9]*)"),
        "cw": re.compile(r"^(\\[a-zA-Z-0-9]*)"),
        "cs": re.compile(r"^(\\['-:_|~])"),
        "text": re.compile(r"^([a-zA-Z0-9\s?.!,;:_%<>=@\-\[\]–/()\'\"“”‘’]*)")
    }
    while main_dict["contents_string"] != "":
        for key, value in pattern_dict.items():
            try:
                test = re.search(value, main_dict["contents_string"])
                if test is not item and test.span() != (0, 0):
                    main_dict["contents_list"].append(test[0])
                main_dict["contents_string"] = \
                    main_dict["contents_string"][0:test.start()] +\
                    main_dict["contents_string"][test.end():]
                main_dict["contents_string"] = \
                    main_dict["contents_string"].lstrip()
            except (KeyError, ValueError, TypeError, Exception) as error:
                error_report(error=error)
    return main_dict


# TODO Complete text for errors.
def error_report(error):
    if logger_debug.isEnabledFor(logging.ERROR):
        if error is KeyError:
            logger_debug(error, "__________")
        if error is ValueError:
            logger_debug(error, "__________")
        if error is TypeError:
            logger_debug(error, "__________")
        if error is Exception:
            logger_debug(error, "__________")
