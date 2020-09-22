#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Module updates the tag registry after opening or  closing a tag. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-06"
__name__ = "Contents.Library.tag_registry_update"

# From standard libraries
import json
import os


def processor(debug_dir: str, tag_update: dict) -> None:
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)
        try:
            tag_registry.update(tag_update)
            with open(tag_registry_file, "w+") as tag_registry_prewrite:
                json.dump(tag_registry, tag_registry_prewrite, indent=4,
                          sort_keys=False, ensure_ascii=False)
        except KeyError:
            pass
