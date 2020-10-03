#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" The main body of an RTF document has four components assembled in a
variety of combinations: control symbols, groups containing destinations that
can be ignored, destinations that must be processed (within or outside of
groups), and groups (which also contain pieces of the core text of the
original document). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.process_body.doc_parser"

# From standard libraries
import json
import linecache
import os

# From local application
import control_word_collections
import check_parse_text
from typing import Any


class MainDocManager(object):
    def __init__(self, main_dict: dict) -> None:
        self.main_dict = main_dict
        self.processing_dict = self.main_dict
        self.main_dict = self.main_dict
        self.working_input_file = self.main_dict["working_file_name"]
        self.tag_set = self.processing_dict["tag_set"]
        self.length_parse_text = 0
        self.tag_registry = self.main_dict["tag_registry"]

    def body_parse_manager(self) -> dict:

        header_table_file = os.path.join(self.main_dict["debug_dir"],
                                         "header_tables_dict.json")
        main_doc_dir = MainDocManager(main_dict=self.main_dict)
        parse_text, line_to_parse, parse_index = \
            MainDocManager.parse_starting_point(
                self=main_doc_dir, header_table_file=header_table_file)
        list_size = len(self.main_dict["working_input_file"])

        processing_dict = {
            "parse_text":         parse_text,
            "list_size":          list_size,
            "line_to_parse":      line_to_parse,
            "parse_index":        parse_index,
            "working_input_file": self.working_input_file,
            "debug_dir":          self.main_dict["debug_dir"],
            "dicts_dir":          self.main_dict["dicts_dir"],
            "group_contents":     "",
            "group_end_line":     0,
            "group_end_index":    0,
            "contents_list":      [],
            "contents_string":    "",
            "tag_set":            self.tag_set
        }
        self.main_dict = processing_dict
        collections_dict = control_word_collections.cwc_processor()

        self.main_dict = check_parse_text.cpt_processor(
            main_dict=self.main_dict, collections_dict=collections_dict)

        self.main_dict = processing_dict
        return self.main_dict

    def parse_starting_point(self, header_table_file: str) -> Any:
        with open(header_table_file) as htf_pre:
            header_table = json.load(htf_pre)
            line_to_parse = header_table["info"][2]
            parse_index = header_table["info"][3]
        parse_text, line_to_parse, parse_index = \
            MainDocManager.set_process_text(
                self=MainDocManager(main_dict=self.main_dict),
                parse_index=parse_index,
                line_to_parse=line_to_parse)
        return parse_text, line_to_parse, parse_index

    def set_process_text(self, parse_index: int, line_to_parse: int) -> Any:
        line = linecache.getline(self.working_input_file, line_to_parse).\
            rstrip("\n").rstrip()
        line = line[parse_index:]
        length = len(line)
        if parse_index > length - 2:
            parse_text = line[parse_index:] + linecache.getline(
                self.working_input_file, line_to_parse + 1).\
                rstrip("\n").rstrip()
            line_to_parse += 1
            parse_index = 1
        else:
            parse_text = line
            parse_index = 1
        return parse_text, line_to_parse, parse_index
