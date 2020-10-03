#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.


def apt_processor(main_dict: dict) -> dict:
    processing_dict = main_dict["processing_dict"]
    control_info = main_dict["control_info"]
    length = len(processing_dict["parse_text"])
    if length <= 2:
        processing_dict["line_to_parse"] = processing_dict["line_to_parse"] + 1
        line = control_info["working_input_file"][processing_dict[
            "line_to_parse"]].rstrip()
        processing_dict["parse_text"] = ''.join((processing_dict["parse_text"],
                                                line))
        processing_dict["parse_index"] = 0
        main_dict["processing_dict"] = processing_dict
        return main_dict
    else:
        main_dict["processing_dict"] = processing_dict
        return main_dict
