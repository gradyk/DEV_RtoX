#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

# From standard libraries
import logging
import re

# From local applications
import build_output_file
import controlword_evaluator

log = logging.getLogger(__name__)


def processor(main_dict: dict, collections_dict: dict) -> dict:
    # Temp setup for testing
    for ele in main_dict["contents_list"]:
        if ele == "{" or ele == "}":
            pass
        elif re.search(main_dict["cw_regex"], ele):
            tag_info, main_dict, collections_dict = \
                controlword_evaluator.processor(
                    main_dict=main_dict, test=ele,
                    collections_dict=collections_dict)
        else:
            main_dict["update_output"] = ele
            build_output_file.processor(main_dict=main_dict)
    main_dict["contents_list"] = []
    return main_dict
