#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" The main body of an RTF document has four components assembled in a
variety of combinations: control symbols, groups containing destinations that
can be ignored, destinations that must be processed (within or outside of
groups), and groups (which also contain pieces of the core text of the
original document). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.process_body.doc_parser"

# From standard libraries
from collections import deque

# From local application
import control_words_collections
import check_string


def body_parse_manager(main_dict: dict) -> None:
    collections_dict = control_words_collections.cwc_processor()
    main_dict["parse_text"] = ""
    deck = deque()
    check_string.pre_processor(
        main_dict=main_dict, collections_dict=collections_dict)
    check_string.processor(main_dict=main_dict,
                           collections_dict=collections_dict,
                           deck=deck)
