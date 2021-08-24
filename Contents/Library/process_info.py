#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import information_group


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for the RTF document info and store the
    settings in a dictionary. """
    information_group.InfoGrpParse.process_code_strings(
        self=information_group.InfoGrpParse(
            main_dict=main_dict,
            code_strings_to_process=code_strings_to_process))
