#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
import re
from typing import Any


def pre_process(main_dict: dict) -> dict:
    main_dict["contents_string"] = main_dict["group_contents"]
    item = None
    pattern_dict = {
        "lb": re.compile(r"^{"),
        "rb": re.compile(r"^[}]"),
        "dest": re.compile(r"^(\\\*\\[a-zA-Z-0-9]*)"),
        "cw": re.compile(r"^(\[a-zA-Z-0-9]*)"),
        "cs": re.compile(r"^(\['-:_|~])"),
        "text": re.compile(r"^([a-zA-Z0-9\s?.!,;:_%<>=@\-\[\]–/()\'\"“”‘’]*)")
    }
    while main_dict["contents_string"] != "":
        for key, value in pattern_dict.items():
            try:
                test = re.search(value, main_dict["contents_string"])
                if test is not item:
                    main_dict["contents_list"].append(test[0])
                    switcher(main_dict=main_dict, test=test, key=key)
            except (KeyError, ValueError, TypeError, Exception) as error:
                error_report(error=error)
    return main_dict


def switcher(main_dict: dict, test: Any, key: Any) -> Any:
    switch = {
        "lb":   lb_change,
        "rb":   rb_change,
        "dest": other_change,
        "cw":   other_change,
        "cs":   other_change,
        "text": other_change
    }
    func_name = switch.get(key, lambda: "Unidentifiable character in "
                                        "contents string.")
    main_dict = func_name(main_dict=main_dict, test=test)
    return main_dict


def lb_change(main_dict: dict, test: Any) -> dict:
    main_dict["contents_string"] = main_dict["contents_string"][1:].lstrip()
    return main_dict


def rb_change(main_dict: dict, test: Any) -> dict:
    main_dict["contents_string"] = main_dict["contents_string"][:-1].rstrip()
    return main_dict


def other_change(main_dict: dict, test: Any) -> dict:
    main_dict["contents_string"] = \
        main_dict["contents_string"].replace(test[0], "", 1).lstrip()
    return main_dict


# TODO Complete text for logging.exceptions.
def error_report(error):
    if error is KeyError:
        logging.exception(error, "__________")
    if error is ValueError:
        logging.exception(error, "__________")
    if error is TypeError:
        logging.exception(error, "__________")
    if error is Exception:
        logging.exception(error, "__________")
