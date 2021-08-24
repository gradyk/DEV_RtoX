#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def processor(main_dict: dict) -> dict:
    list_text = main_dict["working_input_file"]
    hold = ""
    main_dict["wif_string"] = hold.join(list_text)
    return main_dict
