#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_parse_text"

# From standard libraries
import re
import sys

# From local application
import check_group
import control_word
import backslash_text
import left_bracket_text
import check_text
import script_timer


def check_string_manager(processing_dict: dict, line: int) -> None:
    control_word_regex = re.compile(r"^(\\[a-zA-Z\-\s0-9]*)")
    processing_dict.update({"cw_regex": control_word_regex})

    while line < processing_dict["num_lines"] + 1:
        # Checks for an RTF group.
        processing_dict = check_group.processor(processing_dict=processing_dict)
        # Checks for a backslash that should be treated as text.
        processing_dict = backslash_text.processor(
            processing_dict=processing_dict)
        # Checks for a left bracket that should be treated as text.
        processing_dict = left_bracket_text.processor(
            processing_dict=processing_dict)
        # Checks for a control word or destination.
        processing_dict = control_word.processor(
            processing_dict=processing_dict)
        # Checks for text.
        check_text.processor(
            processing_dict=processing_dict)

        line = processing_dict["line_to_parse"]

    # TODO This will actually go to modules that will close out the program.
    script_timer.close_processor()
