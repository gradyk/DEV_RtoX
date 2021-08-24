#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import pgp_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each pgp (_____) entry and store the
    settings in a dictionary. """
    code_strings_to_process = pgp_table.trim_pgptbl(
        code_strings_to_process=code_strings_to_process)
    pgp_table.parse_pgp_string(
        main_dict=main_dict,
        code_strings_to_process=code_strings_to_process)
