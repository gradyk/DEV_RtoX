#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import rsid_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each RSID entry and store the
    settings in a dictionary. """
    new_code_string = rsid_table.trim_rsidtbl(
        code_strings_to_process=code_strings_to_process)
    rsid_table.parse_rsid_string(
        main_dict=main_dict,
        code_string=new_code_string)
