#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.control_words_symbols.toggle_emph"

# From standard libraries
import logging
from typing import Tuple

import build_output_file

log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    cw_text = tag_info["cw_text"]
    controlword = main_dict[cw_text]
    controlword_val = tag_info["cw_value"]
    tag_queue = main_dict["tag_queue"]

    if controlword == "open" and controlword_val == "" and not tag_queue:
        log.info(msg="1")
        main_dict["update_output"] = ""
        main_dict["tag_queue"].append(main_dict["tags"]["cw_text"][1])

    elif controlword == "open" and controlword_val == "" and tag_queue:
        log.info(msg="2")
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["tag_queue"] = []
        open_str_empty = main_dict["tags"]["toggle_emph"][0]
        open_str = open_str_empty.replace("zzz", tag_info["cw_text"])
        main_dict["update_output"] = main_dict["update_output"] + open_str
        main_dict["tag_queue"].append(main_dict["tags"]["toggle_emph"][1])

    elif controlword == "open" and controlword_val != "" and not tag_queue:
        log.info(msg="3")
        main_dict["update_output"] = main_dict["tags"]["toggle_emph"][1]
        main_dict["cw_text"] = "closed"

    elif controlword == "open" and controlword_val != "" and tag_queue:
        log.info(msg="4")
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["update_output"] = main_dict["tags"]["toggle_emph"][1]
        main_dict["tag_queue"] = []
        main_dict["cw_text"] = "closed"

    elif controlword == "closed" and controlword_val == "" and not tag_queue:
        log.info(msg="5")
        open_str_empty = main_dict["tags"]["toggle_emph"][0]
        open_str = open_str_empty.replace("zzz", tag_info["cw_text"])
        main_dict["update_output"] = open_str
        main_dict["tag_queue"].append(main_dict["tags"]["toggle_emph"][1])

    elif controlword == "closed" and controlword_val == "" and tag_queue:
        log.info(msg="6")
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["tag_queue"] = []
        open_str_empty = main_dict["tags"]["toggle_emph"][0]
        open_str = open_str_empty.replace("zzz", tag_info["cw_text"])
        main_dict["update_output"] = main_dict["update_output"] + open_str
        main_dict["tag_queue"].append(main_dict["tags"]["toggle_emph"][1])

    elif controlword == "closed" and controlword_val != "" and not tag_queue:
        log.debug(msg="7")
        main_dict["update_output"] = ""

    elif controlword == "closed" and controlword_val != "" and tag_queue:
        log.info(msg="8")
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["tag_queue"] = []

    build_output_file.processor(main_dict=main_dict)
    return tag_info, main_dict
