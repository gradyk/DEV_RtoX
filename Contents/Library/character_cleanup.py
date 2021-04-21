#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
    An RTF file typically includes characters and control symbols that
should be replaced. This module updates the working version of the RTF file.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-27"
__name__ = "Contents.Library.character_cleanup"

# From standard libraries
import importlib
import logging
import re
import os
from typing import Any

# From local applications
from Contents.Library.dicts.code_array import array_files

log = logging.getLogger(__name__)


def cc_processor(main_dict: dict) -> dict:
    """ Cleanup characters ln the RTF file line-by-line. """
    source_file = main_dict["working_input_file"]
    array_codes = array_select(main_dict=main_dict)
    for line in source_file:
        place = source_file.index(line)
        new_line = misc_cleanup(array_codes=array_codes, line=line)
        new_line = unicode_cleanup(array_codes=array_codes, new_line=new_line)
        source_file[place] = new_line
    main_dict["working_input_file"] = source_file
    main_dict["working_input_file_bak"] = source_file
    return main_dict


def array_select(main_dict: dict) -> dict:
    """
        Select the correct code page dictionary based on the ansicpg setting.
    """
    try:
        array_num = main_dict["file_codes"]["ansicpg"]
        if array_num == "":
            log.debug("No code array number was found in the RTF file. Using "
                      "array number 1252.")
            array_num = "1252"
    except KeyError:
        array_num = "1252"
    array_name = array_files[array_num]
    dicts_dir = main_dict["dicts_dir"]
    codes = "codes"
    try:
        array_mod = importlib.import_module(array_name,
                                            package="Contents.Library.dicts")
        array_codes = getattr(array_mod, codes)
    except ModuleNotFoundError:
        log.debug(f"Unable to locate a code_array matching the code page "
                  f"specified in the RTF file ({array_num}). Using the default "
                  f"array: Western_European_code_array (1252).")
        array_codes = getattr(
            os.path.join(dicts_dir, "Western_European_code_array.py"), codes)
    return array_codes


def misc_cleanup(line: str, array_codes: dict) -> str:
    """ Convert miscellaneous characters to unicode. """
    item = None
    new_line = line
    pattern_list = [r"&", r"(HT\tab)", r"\tab"]
    for pattern in pattern_list:
        test = re.search(pattern, new_line)
        if test is not item:
            cleaned_test = "".join([i for i in test[0] if i.isalnum()])
            sub_string = array_codes[cleaned_test]
            new_line = re.sub(pattern, sub_string, new_line)
    return new_line


def unicode_cleanup(new_line: str, array_codes: dict) -> str:
    """ Convert unicode codes to characters. """
    item = None
    pattern = re.compile(r"(\'[A-Z0-9]{2})")
    while unicode_test(pattern=pattern, new_line=new_line) is not item:
        try:
            test = pattern.search(new_line)
            test_string = new_line[test.start():test.end()]
            cleaned_string = test_string.replace("\'", "").upper()
            replacement_string = array_codes[cleaned_string]
            new_line = new_line.replace(new_line[test.start():test.end()],
                                        replacement_string)
        except KeyError as error:
            log.debug(error, f"{new_line}")
    return new_line


def unicode_test(pattern: Any, new_line: str) -> Any:
    return pattern.search(new_line)
