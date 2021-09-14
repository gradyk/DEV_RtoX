#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "Contents.Library.header_structure"

# Standard library imports
import logging

# From local application
import find_color_table
import find_file_table
import find_font_table
import find_generator
import find_info_table
import find_list_table
import find_list_override_table
import find_pgp_table
import find_rsid_table
import find_style_sheet_table
import find_track_changes_table
import find_xmlns_table

log = logging.getLogger(__name__)


def processor(main_dict: dict) -> dict:
    try:
        main_dict = find_color_table.processor(main_dict=main_dict)
        main_dict = find_file_table.processor(main_dict=main_dict)
        main_dict = find_font_table.processor(main_dict=main_dict)
        main_dict = find_generator.processor(main_dict=main_dict)
        main_dict = find_info_table.processor(main_dict=main_dict)
        main_dict = find_list_table.processor(main_dict=main_dict)
        main_dict = find_list_override_table.processor(main_dict=main_dict)
        main_dict = find_pgp_table.processor(main_dict=main_dict)
        main_dict = find_rsid_table.processor(main_dict=main_dict)
        main_dict = find_style_sheet_table.processor(main_dict=main_dict)
        main_dict = find_track_changes_table.processor(main_dict=main_dict)
        main_dict = find_xmlns_table.processor(main_dict=main_dict)
    except ModuleNotFoundError as error:
        msg = "The module needed to process one of the file tables is missing."
        log.debug(error, msg)
    return main_dict
