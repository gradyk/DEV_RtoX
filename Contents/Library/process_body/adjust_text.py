#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def processor(parse_text: str, main_dict: dict, line_to_parse: int) -> tuple:
    # Since parse_text has 1 or fewer characters, increase parse_text by adding
    # the next string from working_input_file.
    line_to_parse += 1
    new_text = main_dict["working_input_file"][line_to_parse]
    parse_text = parse_text + new_text
    parse_index = 0
    return parse_text, line_to_parse, parse_index
