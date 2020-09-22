#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.control_word_to_build"

# From standard libraries
import importlib
import os
import sys

# From local application
import build_output_file
import tag_registry_update


def processor(tag_info: dict) -> None:
    tag_update = {}
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_dir, "debugdir")
    cws_dir = os.path.join(base_dir, "Library/control_words_symbols/")
    # Some modules are generic and some specific. For example, "toggle.py"
    # handles all emphasis tags (italic, bold, etc.) which toggle on or off.
    # "pard.py" only handles the \pard control word.
    tagging_mod = importlib.import_module(tag_info["func"], package=cws_dir)
    tag_action = tagging_mod.tagger(tag_info=tag_info)

    # If an opening tag, check to see if tag is already open. If yes,
    # skip adding the opening tag. If a closing tag check to see if tag is
    # open before closing it.

    if tag_action["tag_setting"] == "open":
        update_output = tag_action["open"]
        tag_update[tag_action["tag_name"]] = "open"
    else:
        update_output = tag_action["close"]
        name = tag_action["tag_name"]
        tag_update[name] = "open"
    build_output_file.processor(update_output=update_output)
    tag_registry_update.processor(debug_dir=debug_dir,
                                  tag_update=tag_update)
