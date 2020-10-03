#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-10"
__name__ = "Contents.Library.header_parser_step_one"

# From local application
import rtf_file_lead_parse
import header_structure


def determine_header_structure(main_dict: dict) -> None:
    """ Determine what tables are in the RTF header and store the table name
    and its line location in a dictionary. """
    header_structure.build_header_tables_dict(main_dict=main_dict)


def process_pretable_controlwords(main_dict: dict) -> dict:
    """ Process the control words that precede tables (rtf <charset>
    \\deff). """
    main_dict = rtf_file_lead_parse.check_for_opening_brace(main_dict=main_dict)

    rtf_file_codes_update = \
        rtf_file_lead_parse.code_process(main_dict=main_dict)

    rtf_file_lead_parse.update_rtf_file_codes_list(
        rtf_file_codes_update=rtf_file_codes_update, main_dict=main_dict)

    return main_dict
