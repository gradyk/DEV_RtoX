#  Copyright (c) 2020. Kenneth A. Grady
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
import os

# From local application
import build_output_file
import tag_check


def cwtb_processor(tag_info: dict, main_dict: dict) -> dict:
    base_dir = main_dict["base_dir"]
    cws_dir = os.path.join(base_dir, "Library/control_words_symbols/")
    tagging_mod = importlib.import_module(tag_info["func"], package=cws_dir)
    tag_info = tagging_mod.cw_func_processor(tag_info=tag_info)
    # Check whether tag is already open or closed.
    results = tag_check.tc_processor(tag_info=tag_info,
                                     main_dict=main_dict)
    main_dict["tag_registry"] = results[1]
    update_output = results[2]
    if update_output == "":
        pass
    else:
        build_output_file.bof_processor(update_output=update_output,
                                        main_dict=main_dict)
    return main_dict
