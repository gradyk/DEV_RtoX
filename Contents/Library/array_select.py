#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import importlib
import logging
import os

# From local applications
from Contents.Library.dicts.code_array import array_files


log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    """ Select the code page dictionary based on the ansicpg setting. """
    try:
        array_num = main_dict["file_codes"]["ansicpg"]
        if array_num == "":
            log.debug("RTF file code array number missing, using number 1252.")
            array_num = "1252"
    except KeyError:
        array_num = "1252"
    array_name = array_files[array_num]
    try:
        array_mod = importlib.import_module(array_name,
                                            package="Contents.Library.dicts")
        array_codes = getattr(array_mod, "codes")
    except ModuleNotFoundError as error:
        msg = f"Unable to locate code_array {array_num}. Using array (1252)."
        log.debug(error, msg)
        array_codes = getattr(os.path.join(main_dict["dicts_dir"],
                              "Western_European_code_array.py"), "codes")
    return array_codes
