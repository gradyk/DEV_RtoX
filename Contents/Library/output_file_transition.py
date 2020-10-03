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
from typing import Any

# From application library
import build_output_file


def oft_processor(main_dict: dict, config_settings_dict: dict) -> Any:
    """ Insert the XML tags to start the document portion of the XML file
    (after the header). """
    start_tags = os.path.join(main_dict["dicts_dir"],
                              "start_tags.json")
    transition_tags = ""
    try:
        with open(start_tags, "r+") as start_tags_pre:
            start_tag_dict = json.load(start_tags_pre)
        if config_settings_dict["tag-set"] == "1":
            transition_tags = start_tag_dict["1"]
        elif config_settings_dict["tag-set"] == "2":
            transition_tags = start_tag_dict["2"]
        elif config_settings_dict["tag-set"] == "3":
            transition_tags = start_tag_dict["3"]
    except KeyError as error:
        logging.exception(error, "The tag-set number does not match an "
                                 "entry for transition tags.")
        transition_tags = start_tag_dict["1"]
    except FileNotFoundError as error:
        logging.exception(error, "The config_dict.json file is missing.")

    main_dict = build_output_file.bof_processor(
        main_dict=main_dict, update_output=transition_tags)

    return main_dict
