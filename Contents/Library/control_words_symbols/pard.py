#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" \\pard resets any paragraph formatting.
    When RtoX encounters \\pard it: 1) checks for and closes relevant open
    paragraph formatting tags, 2) opens default paragraph formatting tags,
    and 3) updates the tag registry. The following list contains paragraph
    formatting control words. RtoX ignores those control words preceded by an *.
    \\par	        New paragraph.
    \\pard	        Resets to default paragraph properties.
    *\\spv	        Style separator feature that causes the paragraph mark to
                    not appear even in ShowAll. Used to nest paragraphs within
                    the document view or outline without generating a new
                    heading.
    *\\hyphpar	    Switches automatic hyphenation for the paragraph. Append 1
                    or nothing to toggle property on; append 0 to turn it off.
    \\intbl	        Paragraph is part of a table.
    \\itapN	        Paragraph nesting level, where 0 is the main document, 1
                    is a table cell, 2 is a nested table cell, 3 is a doubly
                    nested table cell, and so forth (default is 1).
    *\\keep	        Keep paragraph intact (completely on one page if possible).
    *\\keepn	        Keep paragraph with the next paragraph.
    \\levelN	    N is the outline level of the paragraph.
    \\noline	    No line numbering.
    *\\nowidctlpar	No widow/orphan control. This is a paragraph-level
                    property and is used to override the document-level
                    \\widowctrl.
    *\\widctlpar	Widow/orphan control is used for the current
                    paragraph. This is a paragraph property used to override
                    the absence of the document-level \\widowctrl.
    \\outlinelevelN	Outline level of paragraph. The N argument is a value
                    from 0 to 8 representing the outline level of the
                    paragraph. In the default case, no outline level is
                    specified (same as body text).
    *\\pagebb	    Break page before the paragraph.
    \\sbys	        Side-by-side paragraphs.
    \\sN	        Designates paragraph style. If a paragraph style is
                    specified, style properties must be specified with the
                    paragraph. N references an entry in the style sheet.
    """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-02-13"
__name__ = "Contents.Library.control_words_symbols.pard"

# Standard library imports
import json
import logging
import os

# From local application
import build_output_file
import tag_check
import tag_registry_update
from read_log_config import logger_debug


def pard_tag_process(debug_dir: str, tag_dict: dict, line: str):

    open_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict)

    paragraph_tag_cleanup(debug_dir=debug_dir, tag_dict=tag_dict, line=line)

    update_tag_registry(debug_dir=debug_dir)


def open_tag_cleanup(debug_dir: str, tag_dict: dict):
    """ Check the tag registry to see whether an emphasis tag needs closing
    and close them. """
    # Check the tag registry to see whether a paragraph formatting tag needs
    # closing and, if so, close it.
    status_list = [
        "par",
        "pard",
        "intbl",
        "itap",
        "level",
        "noline",
        "outlinelevel",
        "sbys",
        "s"  # Drop
    ]
    tag_check.tag_check(debug_dir=debug_dir, status_list=status_list,
                        tag_dict=tag_dict)


def paragraph_tag_cleanup(debug_dir: str, tag_dict: dict, line: str):
    """ If the tag registry shows a closed paragraph, insert an open
    paragraph tag. If it shows an open paragraph, close it and open a new
    paragraph. """
    tag_registry_file = os.path.join(debug_dir, "tag_registry.json")
    with open(tag_registry_file) as tag_registry_pre:
        tag_registry = json.load(tag_registry_pre)

    tag_closed = "0"

    if tag_registry["paragraph"] == tag_closed:
        content_update = tag_dict["paragraph-beg"]

        build_output_file.processor(update_output=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")

    else:
        content_update = tag_dict["paragraph-end"] + tag_dict["paragraph-beg"]
        build_output_file.processor(update_output=content_update)
        try:
            if logger_debug.isEnabledFor(logging.DEBUG):
                msg = str(tag_dict["paragraph-end"] + tag_dict[
                         "paragraph-beg"] + f"{line}")
                logger_debug.error(msg)
        except AttributeError:
            logging.exception("Check setLevel for logger_debug.")


def update_tag_registry(debug_dir: str, tag_open="1"):
    content_update_dict = {"paragraph": tag_open}
    tag_registry_update.processor(debug_dir=debug_dir,
                                  tag_update_dict=content_update_dict)
