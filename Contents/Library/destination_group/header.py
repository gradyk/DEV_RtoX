#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse text and settings in the RTF file wrapped by the header keyword ({
\\header ...}). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-11"
__name__ = "Contents.Library.header"

# From standard libraries
import linecache
import logging

# From local application
import tag_check
import tag_registry_update
import output_file_update
from read_log_config import logger_debug


def find_header_close_boundary(working_input_file: list,
                               line_to_search: int) -> str:
    """ A header is bounded by an opening brace and keyword ({\\header)
        and a closing brace (}). The opening is easy to identify. The closing
        can be determined by counting opening and closing braces until the count
        matches. """
    left_brace = 0
    right_brace = 0
    header_end_line = "0"
    while header_end_line == "0":
        search_text = linecache.getline(working_input_file, line_to_search)
        for character in search_text:
            if character == "{":
                left_brace += 1
            elif character == "}":
                right_brace += 1
            else:
                pass
            if left_brace == right_brace:
                header_end_line = line_to_search
            else:
                pass
        line_to_search += 1

    linecache.clearcache()
    return header_end_line


def open_emphasis_tag_cleanup_start(debug_dir: str, tag_dict: dict):
    """ Check for open tags and close them. """
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph"
    ]

    tag_check.processor(tag_info=tag_info, main_dict=main_dict)


def insert_opening_header_tag(debug_dir: str, tag_dict: dict,
                              line_to_read: str) -> None:
    content_update = tag_dict["header-beg"]

    output_file_update.content_append(debug_dir=debug_dir,
                                  content_update=content_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            logger_debug.error(msg=str(tag_dict["header-beg"] +
                                       f"{line_to_read}"))
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")


def update_tag_registry_start(debug_dir: str, tag_open="1") -> None:
    content_update_dict = {"header": tag_open}
    tag_registry_update.processor(tag_info, )


def header_process_controller_end(debug_dir: str, tag_dict: dict,
                                  line: str) -> None:

    open_emphasis_tag_cleanup_end(debug_dir=debug_dir, tag_dict=tag_dict)

    insert_closing_header_tag(debug_dir=debug_dir, tag_dict=tag_dict,
                              line=line)

    update_tag_registry_end(debug_dir=debug_dir)


def open_emphasis_tag_cleanup_end(debug_dir: str, tag_dict: dict) -> None:
    """ Check for open tags and close them. """
    status_list = [
        "small_caps",
        "strikethrough",
        "underline",
        "bold",
        "italic",
        "paragraph"
    ]

    tag_check.processor(tag_info=tag_info, main_dict=main_dict)


def insert_closing_header_tag(debug_dir: str, tag_dict: dict,
                              line: str) -> None:
    # TODO At least in TPRES, a header may be embedded in a paragraph or fall
    #  at the end or beginning of a paragraph. See also footnote.
    """ Insert the header closing tag. Note that a header ending is
        different than a footnote ending. Headers are separate blocks and need
        a paragraph opening tag afterwards. """
    content_update = tag_dict["header-end"] + tag_dict["paragraph-beg"]

    output_file_update.content_append(debug_dir=debug_dir,
                                  content_update=content_update)
    try:
        if logger_debug.isEnabledFor(logging.DEBUG):
            msg = str(tag_dict["header-end"] +
                      tag_dict["paragraph-beg"] + f"{line}")
            logger_debug.error(msg)
    except AttributeError:
        logging.exception("Check setLevel for logger_debug.")


def update_tag_registry_end(debug_dir: str, tag_closed="0",
                            tag_open="1") -> None:
    content_update_dict = {"header": tag_closed, "paragraph": tag_open}
    tag_registry_update.processor(tag_info, )
