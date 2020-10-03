#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


def apt_processor(main_dict: dict) -> dict:
    length = len(main_dict["parse_text"])
    if length <= 2:
        main_dict["line_to_parse"] = main_dict["line_to_parse"] + 1
        line = main_dict["working_input_file"][main_dict[
            "line_to_parse"]].rstrip()
        main_dict["parse_text"] = ''.join((main_dict["parse_text"],
                                                line))
        main_dict["parse_index"] = 0
        return main_dict
    else:
        return main_dict
