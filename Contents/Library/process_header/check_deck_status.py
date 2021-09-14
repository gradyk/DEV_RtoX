#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
from typing import Any

# From local application
import find_group_end

log = logging.getLogger(__name__)


def processor(main_dict: dict, deck: Any) -> dict:
    try:
        if deck:
            find_group_end.processor(main_dict=main_dict, deck=deck)
    except (TypeError, Exception) as error:
        msg = "Problem evaluating end of group."
        log.debug(error, msg)
    main_dict["group_end_found"] = True
    return main_dict
