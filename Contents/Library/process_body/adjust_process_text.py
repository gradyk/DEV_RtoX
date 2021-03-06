#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


def apt_processor(main_dict: dict) -> dict:
    length = len(main_dict["parse_text"])
    if length <= 2:
        main_dict["line_to_parse"] += 1
        if main_dict["line_to_parse"] < main_dict["list_size"]:
            line = main_dict["working_input_file"][main_dict["line_to_parse"]]
            main_dict["parse_text"] = ''.join((main_dict["parse_text"], line))
            main_dict["parse_index"] = 1
        else:
            pass
    else:
        pass
    return main_dict
