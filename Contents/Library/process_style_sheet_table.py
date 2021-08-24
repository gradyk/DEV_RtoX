#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import style_sheet_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each style number and store the
    settings in a dictionary. """
    style_sheet_table.process_stylesheet(
        code_strings_to_process=code_strings_to_process,
        main_dict=main_dict)

    # TODO sf_restrictions (style and formatting restrictions) is part of
    #  style sheet table
