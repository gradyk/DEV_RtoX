#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" The output_file transition from header to body requires inserting
certain tags. RTF, for example, does not mark the start of a paragraph
whereas XML requires a tag to mark the beginning of a paragraph. The
specific tags depend on the user's tag set preference. The generic tag
types needed are:
<text>
    <body>
        <section>
            <paragraph>. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-18"
__name__ = "Contents.Library.output_file_transition"

# From standard libraries
import json
import logging
import os
import sys

# From application library
import build_output_file
import tag_registry_update


def processor():
    """ Insert the XML tags to start the document portion of the XML file
    (after the header). """
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    debug_dir = os.path.join(base_script_dir, "debugdir")
    config_file = os.path.join(debug_dir, "config_dict.json")
    dicts_dir = os.path.join(base_script_dir, "Library/dicts")
    start_tags = os.path.join(dicts_dir, "start_tags.json")
    try:
        with open(config_file, "r+") as config_dict_pre:
            config_dict = json.load(config_dict_pre)
        with open(start_tags, "r+") as start_tags_pre:
            start_tag_dict = json.load(start_tags_pre)
        if config_dict["tag-set"] == 1:
            start_tags = start_tag_dict["1"]
        elif config_dict["tag-set"] == 2:
            start_tags = start_tag_dict["2"]
        elif config_dict["tag-set"] == 3:
            start_tags = start_tag_dict["3"]

    except KeyError as error:
        logging.exception(error, "The tag-set number does not match an "
                                 "entry for transition tags.")
        start_tags = start_tag_dict["1"]
    except FileNotFoundError as error:
        logging.exception(error, "The config_dict.json file is missing.")

    build_output_file.processor(update_output=start_tags)

    # Update the tag registry.
    content_update_dict = {"bodytext":  "1",
                           "section":   "1",
                           "paragraph": "1",
                           "body":      "1"}
    tag_registry_update.tag_registry_update(
        debug_dir=debug_dir, content_update_dict=content_update_dict)
