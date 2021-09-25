#  Copyright (c) 2021. Kenneth A. Grady
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
__name__ = "Contents.Library.control_words_symbols.par"

# Standard library imports
import logging
from typing import Tuple

# From local application
import build_output_file

log = logging.getLogger(__name__)


def processor(tag_info: dict, main_dict: dict) -> Tuple[dict, dict]:
    """ If the tag registry shows a closed paragraph, insert an open
        paragraph tag. If it shows an open paragraph, close it and open a new
        paragraph. """
    if main_dict["tag_queue"]:
        main_dict["update_output"] = ''.join(main_dict["tag_queue"][::-1])
        main_dict["tag_queue"] = []
        main_dict["pard"] = "closed"
    if main_dict["pard"] == "closed":
        main_dict["update_output"] = main_dict["update_output"] + \
            main_dict["tags"]["pard"][0]
        main_dict["tag_queue"].append(main_dict["tags"]["pard"][1])
    elif main_dict["pard"] == "open":
        main_dict["update_output"] = main_dict["update_output"] + \
            main_dict["tags"]["pard"][1] + main_dict["tags"]["pard"][0]
        main_dict["tag_queue"].append(main_dict["tags"]["pard"][1])
    build_output_file.processor(main_dict=main_dict)
    main_dict["pard"] = "open"
    return tag_info, main_dict
