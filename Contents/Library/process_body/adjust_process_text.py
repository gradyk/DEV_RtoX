#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import linecache


def processor(processing_dict: dict) -> dict:
    length = len(processing_dict["parse_text"])
    if length <= 2:
        processing_dict["line_to_parse"] = processing_dict["line_to_parse"] + 1
        line = linecache.getline(processing_dict["working_input_file"],
                                 processing_dict["line_to_parse"]).\
            rstrip("\n").rstrip()
        processing_dict["parse_text"] = ''.join((processing_dict["parse_text"],
                                                line))
        processing_dict["parse_index"] = 0
        return processing_dict
    else:
        return processing_dict
