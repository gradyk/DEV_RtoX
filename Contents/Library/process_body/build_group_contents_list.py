#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-05-24"
__name__ = "Contents.Library.process_body.build_group_contents_list"

# From standard libraries
import logging
import re
import sys

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    try:
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
    except (TypeError, Exception) as error:
        msg = "main_dict is empty."
        log.debug(error, msg)
        sys.exit()

    while main_dict["contents_string"] != "":
        for key, value in pattern_dict.items():
            try:
                test1 = value.search(main_dict["contents_string"])
                if test1 is not item:
                    try:
                        if test1.span() != (0, 0):
                            main_dict["contents_list"].append(test1[0])
                            main_dict["contents_string"] = \
                                main_dict["contents_string"][0:test1.start()]\
                                + \
                                main_dict["contents_string"][test1.end():]
                            main_dict["contents_string"] = \
                                main_dict["contents_string"].lstrip()
                        elif test1.span() == (0, 0):
                            main_dict["contents_string"] = \
                                main_dict["contents_string"][0:test1.start()]\
                                + \
                                main_dict["contents_string"][test1.end():]
                            main_dict["contents_string"] = \
                                main_dict["contents_string"].lstrip()
                    except KeyError as error:
                        msg = f"Problem encountered with {main_dict}."
                        logging.exception(error, msg)
            except (KeyError, ValueError, TypeError, Exception) as error:
                msg = f"Problem encountered with " \
                      f"{main_dict['contents_list']}.append({test1[0]})"
                logging.exception(error, msg)
                sys.exit()
    return main_dict
