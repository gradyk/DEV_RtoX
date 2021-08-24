#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import color_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each color number and store the
    settings in a dictionary. """
    code_strings_list = color_table.trim_colortbl(
        code_strings=code_strings_to_process)
    code_strings_list = color_table.split_code_strings(
        code_strings_list=code_strings_list)
    color_table.parse_code_strings(
        code_strings_list=code_strings_list, main_dict=main_dict)
