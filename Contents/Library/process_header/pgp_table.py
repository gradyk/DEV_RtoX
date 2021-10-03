#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the pgp table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-05-06"
__name__ = "Contents.Library.pgp_table"

# From standard libraries
import logging
import re

# From local application
import dict_updater

log = logging.getLogger(__name__)


def trim_pgptbl(code_strings_to_process: list) -> list:
    item = None
    for code_string in code_strings_to_process:
        if re.search(r'^{\\\*\\pgptbl', code_string) is not item:
            place = code_strings_to_process.index(code_string)
            new_code_string = code_string.replace("{\\*\\pgptbl ", "")
            code_strings_to_process[place] = new_code_string
        else:
            pass
    return code_strings_to_process


def parse_pgp_string(code_strings_to_process: list, main_dict: dict) -> None:
    counter = 1000
    for code_string in code_strings_to_process:
        code_string, current_key, code_dict = pgp_parse(
            code_string=code_string, code_dict={})
        code_dict, current_key, code_string = ipgpn_parse(
            code_string=code_string, counter=counter,
            current_key=current_key, code_dict=code_dict)
        item = None
        test = re.search(r"\\", code_string)
        while test is not item:
            code_string, current_key, code_dict = check_control_words(
                code_string=code_string, current_key=current_key,
                code_dict=code_dict)
            test = re.search(r"\\", code_string)
        dict_updater.json_dict_updater(
            dict_name="pgp_table_file.json",
            dict_update=code_dict,
            main_dict=main_dict)


def pgp_parse(code_string: str, code_dict: dict) -> tuple:
    """ An RTF file may have a paragraph formatting table with the following
    structure:
    <pgptbl>    '{\\*' \\pgptbl <entry>+ '}'
    <entry>	    '{' \\pgp <value> '}'
    <value>	    \\ipgpN <parfmt>+
    """
    code_string = code_string[1:-1]
    current_key = ""
    item = None
    try:
        test = re.search(r"^\\pgp", code_string)
        if test is not item:
            # Trim \\pgp and pass remainder of code_string to processing.
            code_string = code_string.replace(test[0], "")
        else:
            pass
    except (ValueError, TypeError) as error:
        msg = "A problem was encountered with a paragraph formatting table."
        log.debug(error, msg)
    return code_string, current_key, code_dict


def ipgpn_parse(code_string: str, current_key: str,
                code_dict: dict, counter: int) -> tuple:
    code_string = code_string.lstrip()
    item = None
    counter += 1
    try:
        test = re.search(r"^\\ipgp[0-9]*", code_string)
        if test is not item:
            current_key = test[0].replace("\\", "")
            # For some odd reason, RTF reuses ipgp identifiers. That is,
            # e.g., there can be two "\\ipgp0" groups. So, you will always
            # get the last group of two or more groups coded with the same
            # \\ipgpN identifier.
        else:
            current_key = "ipgp" + str(counter)
        code_dict.update({current_key: {}})
        code_string = code_string.replace(test[0], "")
    except (ValueError, TypeError) as error:
        msg = "A paragraph table ipgp identifier has caused a problem."
        log.debug(error, msg)
    return code_dict, current_key, code_string


def check_control_words(code_dict: dict, code_string: str,
                        current_key: str) -> tuple:
    item = None
    try:
        code_string = code_string.lstrip()
        test = re.search(r"^(\\[a-zA-Z]*[\-0-9]*)", code_string)
        if test is not item:
            test_clean = test[0].rstrip()
            control_word = "".join([i for i in test_clean if i.isalpha()])
            control_word_value = "".join(
                [i for i in test_clean if i.isdigit()])
            code_dict[current_key][control_word] = control_word_value
            code_string = code_string.replace(test_clean, "", 1)
            space_test = re.search(r"^ \\", code_string)
            if space_test is not item:
                code_string = code_string.lstrip()
            else:
                pass
        else:
            pass
    except (ValueError, TypeError) as error:
        msg = "A paragraph table code word has created a problem."
        log.debug(error, msg)
    return code_string, current_key, code_dict
