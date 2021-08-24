#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Check header for existence and location of sections: <first line>,
    <font table>, <file table>, <color table>, <stylesheet>, <list table>,
    <rev table>, <rsid table>, <generator>, <info>, <xmlnstbl>. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "Contents.Library.header_structure"

# Standard library imports
import json
import os
import re

# From local application
import dict_updater
import group_boundaries


def build_header_tables_dict(main_dict: dict) -> None:
    tables = os.path.join(main_dict["dicts_dir"], "tables_dict.json")
    with open(tables, "r+") as tables_dict_pre:
        tables_dict = json.load(tables_dict_pre)
    working_input_file = main_dict["working_input_file"]
    for table in tables_dict:
        listpos = 0
        while listpos in range(len(working_input_file)):
            line = working_input_file[listpos].strip()
            # line = line.strip()
            item = None
            factor = tables_dict[table]["factor"]
            term = re.compile(rf".{table}")
            table_search = re.search(term, line)
            if table_search is not item:
                table_start_line = working_input_file.index(line)
                table_start_index = line.find(table) - factor
                main_dict["group_start_line"] = table_start_line
                main_dict["group_start_index"] = table_start_index
                main_dict["parse_text"] = line[main_dict["group_start_index"]:]
                main_dict["parse_index"] = main_dict["group_start_index"]
                main_dict["line_to_parse"] = main_dict["group_start_line"]
                temp_dict = group_boundaries.initialize(main_dict=main_dict)
                main_dict = group_boundaries.process(
                    main_dict=main_dict, temp_dict=temp_dict)
                table_boundaries_info = {table: [
                        main_dict["group_start_line"],
                        main_dict["group_start_index"],
                        main_dict["group_end_line"],
                        main_dict["group_end_index"]]
                }
                dict_updater.json_dict_updater(
                    dict_name="header_tables_dict.json",
                    dict_update=table_boundaries_info,
                    main_dict=main_dict)
                listpos = len(working_input_file) + 1
            else:
                listpos += 1
                pass
