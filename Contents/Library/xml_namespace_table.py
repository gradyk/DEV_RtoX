#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the XML namespace table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "Contents.Library.xml_namespace_table"

# From standard libraries
import logging
import re

# From local application
import dict_updater


def trim_xmlnstbl(code_strings_to_process: list) -> list:
    item = None
    for code_string in code_strings_to_process:
        if re.search(r'^{\\\*\\xmlnstbl', code_string) is not item:
            place = code_strings_to_process.index(code_string)
            new_code_string = code_string.replace("{\\*\\xmlnstbl ", "")
            code_strings_to_process[place] = new_code_string
        else:
            pass
    return code_strings_to_process


def parse_namespace(code_strings_to_process: list,
                    main_dict: dict) -> None:
    for code_string in code_strings_to_process:
        code_string, current_key, code_dict = namespace_code_parse(
            code_string=code_string, code_dict={})

        code_dict = namespace_parse(
            code_string=code_string,
            current_key=current_key, code_dict=code_dict)

        dict_updater.json_dict_updater(
            dict_name="xml_namespace_table_file.json",
            dict_update=code_dict,
            main_dict=main_dict)


def namespace_code_parse(code_string: str, code_dict: dict) -> tuple:
    """ An RTF file may have an XML namespace table with the following
    structure:
    <xmlnstbl>	'{\\*' \\xmlnstbl <xmlnsdecl>* '}'
    <xmlnsdecl>	'{' \\xmlnsN #PCDATA '}'
    """
    code_string = code_string[1:-1]
    current_key = ""
    item = None
    try:
        test = re.search(rf"^\\xmlns[0-9]*", code_string)
        if test is not item:
            current_key = test[0].replace("\\", "")
            code_dict.update({current_key: {}})
            code_string = code_string.replace(test[0], "")
        else:
            pass
    except (ValueError, TypeError) as error:
        logging.exception(error, "An XML namespace does not have a code.")
        pass
    return code_string, current_key, code_dict


def namespace_parse(code_string: str, current_key: str,
                    code_dict: dict) -> dict:
    code_string = code_string.lstrip()
    item = None
    try:
        test = re.search(r"^([a-zA-Z0-9/:_.-?]*)", code_string)
        if test is not item:
            result = test[0].rstrip()
            code_dict[current_key]["namespace"] = result.lstrip()
        else:
            code_dict[current_key]["namespace"] = "None"
    except (ValueError, TypeError):
        logging.exception(msg="_______________")
    return code_dict
