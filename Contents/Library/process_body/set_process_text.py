#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import adjust_text


def processor(main_dict: dict, parse_index: int, line_to_parse: int) -> tuple:
    line_text = main_dict["working_input_file"][line_to_parse].rstrip()
    parse_text = line_text[parse_index:]
    length = len(parse_text)
    if length <= 1:
        parse_text, line_to_parse, parse_index = adjust_text.processor(
            parse_text=parse_text, main_dict=main_dict,
            line_to_parse=line_to_parse)
    else:
        parse_index = 1
    return parse_text, line_to_parse, parse_index
