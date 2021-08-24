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
import os

# From local application
import control_words_collections
import check_parse_text
import parse_starting_point


def body_parse_manager(main_dict: dict) -> dict:
    header_table_file = os.path.join(main_dict["debug_dir"],
                                     "header_tables_dict.json")
    parse_text, line_to_parse, parse_index = parse_starting_point.processor(
        header_table_file=header_table_file, main_dict=main_dict)
    main_dict["parse_text"] = parse_text
    main_dict["line_to_parse"] = line_to_parse
    main_dict["parse_index"] = parse_index
    collections_dict = control_words_collections.cwc_processor()
    main_dict = check_parse_text.cpt_processor(
        main_dict=main_dict, collections_dict=collections_dict)
    return main_dict
