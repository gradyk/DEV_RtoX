#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import dict_updater


def trim_xmlnstbl(main_dict: dict) -> dict:
    """ RTF wraps the xmlns table with {\\xmlnstbl ... }. This function
    removes the prefix and suffix. """
    main_dict["group_contents"] = main_dict["group_contents"].replace(
        "{\\*\\xmlnstbl", "")
    main_dict["group_contents"] = main_dict["group_contents"][:-1]
    return main_dict


def parse_xmlns_string(main_dict: dict):
    # TODO This only works if there is 1 xmlns (e.g., \\xmlns1).
    main_dict["group_contents"] = main_dict["group_contents"].lstrip('{')
    main_dict["group_contents"] = \
        main_dict["group_contents"].replace(r"{\xmlns1 ", "")
    code_dict = {"xmlns": main_dict["group_contents"][:-1]}
    dict_updater.json_dict_updater(
        dict_name="xmlns_table_file.json",
        dict_update=code_dict,
        main_dict=main_dict)
