#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
    Process the RTF file control words that precede the table definitions,
capturing codes in the rtf_file_codes dictionary.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-10"
__name__ = "Contents.Library.rtf_file_lead_parse"

# From standard libraries
import logging
import re
from rtf_file_codes import file_codes

log = logging.getLogger(__name__)


def check_for_opening_brace(main_dict: dict) -> dict:
    """
        Check for and, if necessary, add an opening brace to the working
    version of the RTF file.
    """
    working_input_file = main_dict["working_input_file"]
    if working_input_file[0][0] != "{":
        working_input_file[0] = "{" + working_input_file[0]
        main_dict["working_input_file"] = working_input_file
    return main_dict


def code_process(main_dict: dict) -> dict:
    """
        Test for the existence of each pre-table control word and,
    if present, capture the code.
    """
    pretable_controlword_replacementtext_list = [
        "rtf[0-9]+",
        "ansi",
        "ansicpg[0-9]+",
        "upr",
        "uc[0-9]+",
        "deflang[0-9]+",
        "deflangfe[0-9]+",
        "deff[0-9]+",
        "adeff[0-9]+",
        "stshfdbch[0-9]+",
        "stshfloch[0-9]+",
        "stshfhich[0-9]+",
        "stshfbi[0-9]+",
        "([a-z]+deflang[a-z]+)",
        "themelang[0-9]+",
        "themelangfe[0-9]+",
        "themelangcs[0-9]+",
    ]
    rtf_file_codes_update = []
    working_input_file = main_dict["working_input_file"]
    line_to_search = working_input_file[0]
    for item in pretable_controlword_replacementtext_list:
        try:
            code_match = re.search(rf'\\{item}', line_to_search)
            code_text = "".join([i for i in code_match[0] if i.isalpha()])
            code_value = "".join([i for i in code_match[0] if i.isdigit()])
            rtf_file_codes_update.append((code_text, code_value))
        except TypeError:
            log.debug(f"No {item} code.")
    file_codes_update = {code: value for (code, value) in rtf_file_codes_update}
    file_codes.update(file_codes_update)
    main_dict["file_codes"] = file_codes
    return main_dict
