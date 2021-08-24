#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import xml_namespace_table


def processor(main_dict: dict, code_strings_to_process: list) -> None:
    """ Process the code settings for each xmlns entry and store
    the settings in a dictionary. """
    xml_namespace_table.trim_xmlnstbl(
        code_strings_to_process=code_strings_to_process)
    xml_namespace_table.parse_namespace(
        main_dict=main_dict,
        code_strings_to_process=code_strings_to_process)
