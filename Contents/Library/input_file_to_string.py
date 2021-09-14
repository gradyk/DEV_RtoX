#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import os


def processor(main_dict: dict) -> dict:
    hold = ""
    main_dict["wif_string"] = hold.join(main_dict["working_input_file"])
    input_file_as_string = os.path.join(main_dict["debug_dir"],
                                        "input_file_as_string.txt")
    with open(input_file_as_string, "w+") as ifas:
        ifas.write(main_dict["wif_string"])
    return main_dict
