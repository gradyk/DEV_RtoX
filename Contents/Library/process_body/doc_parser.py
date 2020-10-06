#  Copyright (c) 2020. Kenneth A. Grady
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
import json
import os

# From local application
import control_word_collections
import check_parse_text
from typing import Any


def body_parse_manager(main_dict: dict) -> dict:
    header_table_file = os.path.join(main_dict["debug_dir"],
                                     "header_tables_dict.json")
    parse_text, line_to_parse, parse_index = parse_starting_point(
        header_table_file=header_table_file, main_dict=main_dict)
    list_size = len(main_dict["working_input_file"])

    main_dict["parse_text"] = parse_text
    main_dict["list_size"] = list_size
    main_dict["line_to_parse"] = line_to_parse
    main_dict["parse_index"] = parse_index

    collections_dict = control_word_collections.cwc_processor()
    main_dict = check_parse_text.cpt_processor(
        main_dict=main_dict, collections_dict=collections_dict)
    return main_dict


def parse_starting_point(header_table_file: str, main_dict: dict) -> Any:
    with open(header_table_file) as htf_pre:
        header_table = json.load(htf_pre)
        line_to_parse = header_table["info"][2]
        parse_index = header_table["info"][3]
    parse_text, line_to_parse, parse_index = set_process_text(
        main_dict=main_dict, parse_index=parse_index,
        line_to_parse=line_to_parse)
    return parse_text, line_to_parse, parse_index


def set_process_text(main_dict: dict, parse_index: int,
                     line_to_parse: int) -> Any:
    line = main_dict["working_input_file"][main_dict["line_to_parse"]].rstrip()
    line = line[parse_index:]
    length = len(line)
    if parse_index > length - 2:
        parse_text = line[parse_index:] + main_dict["working_input_file"][
            main_dict["line_to_parse"] + 1].rstrip()
        line_to_parse += 1
        parse_index = 1
    else:
        parse_text = line
        parse_index = 1
    return parse_text, line_to_parse, parse_index
