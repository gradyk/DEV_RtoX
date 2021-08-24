#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" An RTF file typically includes characters and control symbols that
should be replaced. This module updates the working version of the RTF file. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-27"
__name__ = "Contents.Library.character_cleanup"

# From standard libraries
import logging
from typing import Any

# From local applications
import array_select
import misc_char_cleanup
import unicode_cleanup

log = logging.getLogger(__name__)


def cc_processor(main_dict: dict) -> dict:
    """ Cleanup characters ln the RTF file line-by-line. """
    source_file = main_dict["working_input_file"]
    array_codes = array_select.processor(main_dict=main_dict)
    for line in source_file:
        place = source_file.index(line)
        new_line = misc_char_cleanup.processor(
            array_codes=array_codes, line=line)
        new_line = unicode_cleanup.processor(array_codes=array_codes,
                                             new_line=new_line)
        source_file[place] = new_line
    main_dict["working_input_file"] = source_file
    main_dict["working_input_file_bak"] = source_file
    return main_dict


def unicode_test(pattern: Any, new_line: str) -> Any:
    return pattern.search(new_line)
