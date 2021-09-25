#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the RSID table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-05-06"
__name__ = "Contents.Library.rsid_table"

# From standard libraries
import logging
import re

# From local application
import dict_updater

log = logging.getLogger(__name__)


def trim_rsidtbl(code_strings_to_process: list) -> str:
    code_string = code_strings_to_process[0]
    new_code_string = ""
    try:
        new_code_string = \
            code_string.replace("{\\*\\rsidtbl ", "").replace("}", "")
    except (ValueError, TypeError) as error:
        msg = "A problem was encountered processing the rsid table."
        log.debug(error, msg)
    return new_code_string


def parse_rsid_string(code_string: str, main_dict: dict) -> None:
    code_dict = rsid_parse(
        code_string=code_string, code_dict={})

    dict_updater.json_dict_updater(
        dict_name="rsid_table_file.json",
        dict_update=code_dict,
        main_dict=main_dict)


def rsid_parse(code_string: str, code_dict: dict) -> dict:
    """ An RTF file may have an RSID (Revision Save IDs) table with the
    following structure:
    <rsidtable>	'{\\*' \\rsidtbl \\rsidN+ '}'
    """
    counter = 0
    current_key = "rsid" + str(counter)
    item = None
    while code_string != "":
        try:
            test = re.search(r"^\\rsid[0-9]*", code_string)
            test_clean = test[0].rstrip()
            control_word_value = "".join(
                [i for i in test_clean if i.isdigit()])
            code_dict[current_key] = control_word_value
            code_string = code_string.replace(test_clean, "", 1)
            space_test = re.search(r"^ \\", code_string)
            if space_test is not item:
                code_string = code_string.lstrip()
            counter += 1
            current_key = "rsid" + str(counter)
        except (ValueError, TypeError) as error:
            msg = "An rsid table entry has caused a problem."
            log.debug(error, msg)
    return code_dict


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
    except (ValueError, TypeError) as error:
        msg = "An RSID table code word has created a problem."
        log.exception(error, msg)
    return code_string, current_key, code_dict
