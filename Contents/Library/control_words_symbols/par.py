#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Par marks the start of a new paragraph. It does not include any other
coding. When RtoX encounters par it: 1) checks for and closes relevant open
tags, 2) inserts a close paragraph tag, 3) inserts an open paragraph tag, and
4) updates the tag registry. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.control_words_symbols.par"

# Standard library imports
import logging

# From local application
import build_output_file
from read_log_config import logger_debug


def par_process(debug_dir: str, tag_dict: dict, line: str):

    open_emphasis_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict)

    paragraph_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict, line=line)

    tag_registry.update(____________)


def paragraph_tag_cleanup(debug_dir: str, tag_dict: dict, line: str):
    """ If the tag registry shows a closed paragraph, insert an open 
        paragraph tag. If it shows an open paragraph, close it and open a new
        paragraph. """

    if tag_registry["par"] == "closed":
        content_update = tag_dict["paragraph-beg"]
        build_output_file.content_append(debug_dir=debug_dir,
                                          content_update=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    else:
        content_update = tag_dict["paragraph-end"] + tag_dict["paragraph-beg"]
        output_file_update.content_append(debug_dir=debug_dir,
                                          content_update=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-end"] + tag_dict[
                         "paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")



    tag_registry["par"] = "open"
