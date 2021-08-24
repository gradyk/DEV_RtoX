#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import font_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each font number and store the
    settings in a dictionary. """
    font_table.FonttblParse.trim_fonttbl(
        self=font_table.FonttblParse(
            code_strings_to_process=code_strings_to_process,
            main_dict=main_dict))
    font_table.FonttblParse.remove_code_strings(
        self=font_table.FonttblParse(
            code_strings_to_process=code_strings_to_process,
            main_dict=main_dict))
    font_table.FonttblParse.parse_code_strings(
        self=font_table.FonttblParse(
            main_dict=main_dict,
            code_strings_to_process=code_strings_to_process))
