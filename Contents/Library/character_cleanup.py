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

# From local applications
import array_select
import ignored_codes
import misc_char_cleanup
import unicode_cleanup

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    """ Cleanup characters ln the RTF file line-by-line. """
    array_codes = array_select.processor(main_dict=main_dict)
    main_dict = misc_char_cleanup.processor(
        array_codes=array_codes, main_dict=main_dict)
    main_dict = unicode_cleanup.processor(array_codes=array_codes,
                                          main_dict=main_dict)
    main_dict = ignored_codes.processor(main_dict=main_dict)
    return main_dict
