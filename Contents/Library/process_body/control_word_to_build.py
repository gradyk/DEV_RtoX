#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Some modules processing control words are generic and some specific. For
example, "toggle_emph.py" handles all emphasis tags (italic, bold,
etc.) which toggle on or off. "pard.py" only handles the \\pard control
word. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word_to_build"

# From standard libraries
import importlib
import logging
import os


log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> dict:
    cws_dir = os.path.join(main_dict["base_dir"],
                           "Library/control_words_symbols/")
    try:
        tagging_mod = importlib.import_module(tag_info["func"], package=cws_dir)
    except ValueError as error:
        msg = f"Module name: {tag_info['name']} is missing."
        log.debug(error, msg)
    tag_info, main_dict = tagging_mod.processor(
        tag_info=tag_info, main_dict=main_dict)
    return main_dict
