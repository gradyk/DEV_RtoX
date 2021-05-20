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
import json
import os

# From local application
import control_words_collections
import check_parse_text
from typing import Any


def body_parse_manager(main_dict: dict) -> dict:
    header_table_file = os.path.join(main_dict["debug_dir"],
                                     "header_tables_dict.json")
    parse_text, line_to_parse, parse_index = parse_starting_point(
        header_table_file=header_table_file, main_dict=main_dict)

    main_dict["parse_text"] = parse_text
    main_dict["line_to_parse"] = line_to_parse
    main_dict["parse_index"] = parse_index

    collections_dict = control_words_collections.cwc_processor()
    main_dict = check_parse_text.cpt_processor(
        main_dict=main_dict, collections_dict=collections_dict)
    return main_dict


def parse_starting_point(header_table_file: str, main_dict: dict) -> Any:
    with open(header_table_file) as htf_pre:
        header_table = json.load(htf_pre)
        first = list(header_table.keys())[0]
        starting_line = header_table[first][2]
        starting_index = header_table[first][3]
        for table in header_table:
            if header_table[table][2] > starting_line:
                starting_line = header_table[table][2]
                starting_index = header_table[table][3]
            elif header_table[table][3] > starting_index and \
                    header_table[table][2] == starting_line:
                starting_index = header_table[table][3]
            else:
                pass
    line_to_parse = starting_line
    parse_index = starting_index
    parse_text, line_to_parse, parse_index = set_process_text(
        main_dict=main_dict, parse_index=parse_index,
        line_to_parse=line_to_parse)
    return parse_text, line_to_parse, parse_index


def set_process_text(main_dict: dict, parse_index: int,
                     line_to_parse: int) -> tuple:
    line_text = main_dict["working_input_file"][line_to_parse].rstrip()
    parse_text = line_text[parse_index:]
    length = len(parse_text)
    if length <= 1:
        parse_text, line_to_parse, parse_index = _adjust_text(
            parse_text=parse_text, main_dict=main_dict,
            line_to_parse=line_to_parse)
    else:
        parse_index = 1
    return parse_text, line_to_parse, parse_index


def _adjust_text(parse_text: str, main_dict: dict, line_to_parse: int) -> tuple:
    # Since parse_text has 1 or fewer characters, increase parse_text by adding
    # the next string from working_input_file.
    line_to_parse += 1
    new_text = main_dict["working_input_file"][line_to_parse]
    parse_text = parse_text + new_text
    parse_index = 0
    return parse_text, line_to_parse, parse_index
