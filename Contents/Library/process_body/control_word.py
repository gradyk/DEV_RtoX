#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word"

# From standard libraries
import logging
import re

# From local application
import controlword_evaluator
import plain_text

log = logging.getLogger(__name__)


def processor(main_dict: dict, collections_dict: dict) -> dict:
    # Test for control word (backslash followed by a combination of text,
    # character (optional), and numbers (optional).
    item = None
    try:
        test = re.search(main_dict["cw_regex"],
                         main_dict["wif_string"][main_dict["index"]:])
        if test is not item:
            length = test.end() - test.start()
            main_dict["index"] = main_dict["index"] + length
            main_dict["index_ptr"] = main_dict["index"]
            main_dict, collections_dict = controlword_evaluator.processor(
                main_dict=main_dict,
                test=test[0], collections_dict=collections_dict)
        else:
            main_dict = plain_text.processor(main_dict=main_dict)
    except (TypeError, IndexError, Exception) as error:
        msg = f"Check " \
              f"{main_dict['wif_string'][main_dict['index']:main_dict['index'] + 50]}"
        log.debug(error, msg)
    return main_dict
