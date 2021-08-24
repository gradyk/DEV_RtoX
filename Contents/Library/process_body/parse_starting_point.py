#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import json

import set_process_text


def processor(header_table_file: str, main_dict: dict) -> tuple:
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
    parse_text, line_to_parse, parse_index = set_process_text.processor(
        main_dict=main_dict, parse_index=parse_index,
        line_to_parse=line_to_parse)
    return parse_text, line_to_parse, parse_index
