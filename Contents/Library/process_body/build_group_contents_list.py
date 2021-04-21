#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.build_group_contents_list"

# From standard libraries
import logging
import re
import sys

log = logging.getLogger(__name__)


def pre_process(main_dict: dict) -> dict:
    if main_dict is None:
        log.debug(msg="Main dict is None.")
        sys.exit(1)
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
                test = value.search(main_dict["contents_string"])
                if test is not item and test.span() != (0, 0):
                    main_dict["contents_list"].append(test[0])
                    main_dict["contents_string"] = \
                        main_dict["contents_string"][0:test.start()] + \
                        main_dict["contents_string"][test.end():]
                    main_dict["contents_string"] = \
                        main_dict["contents_string"].lstrip()
                elif test is not item and test.span() == (0, 0):
                    main_dict["contents_string"] = \
                        main_dict["contents_string"][0:test.start()] + \
                        main_dict["contents_string"][test.end():]
                    main_dict["contents_string"] = \
                        main_dict["contents_string"].lstrip()
            # TODO Complete error text.
            except (KeyError, ValueError, TypeError, Exception) as error:
                if error is KeyError:
                    log.debug(msg="AAA")
                if error is ValueError:
                    log.debug(msg="BBB")
                if error is TypeError:
                    log.debug(msg="CCC")
                if error is Exception:
                    log.debug(msg="DDD")
                sys.exit("build_group_contents_list exit")
    return main_dict
