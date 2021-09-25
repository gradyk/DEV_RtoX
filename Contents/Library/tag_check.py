#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" The tag registry maintains the status of tags. Check the status and
perform the appropriate operation based on the status. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-22"
__name__ = "Contents.Library.tag_check"

# From standard libraries
import logging
from typing import Tuple

import build_output_file

log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    """ Evaluate whether the tag is open. closed, or not in the registry.
    Options:
    open    and tag_action is open: do nothing
    open    and tag_action is close: close tag
    close   and tag_action is open: open tag
    close   and tag_action is close: do nothing
    absent  and tag_action is open: open tag
    absent  and tag_action is close: do nothing
    Finally, update the registry. """
    main_dict["update_output"] = ""
    try:  # is tag open or closed
        if tag_info["tag_status"] == "open":
            main_dict["update_output"] = tag_info["tag_close_str"]
    except (KeyError, Exception) as error:
        msg = "Problem closing open tags during process cleanup."
        log.debug(error, msg)
        # TODO For at least some toggles (aspalpha, aspanum) there isn't
        #  a close tag. Need to identify these situations and mark the
        #  status in the tag registry appropriately.
    main_dict = build_output_file.processor(main_dict=main_dict)
    return tag_info, main_dict
