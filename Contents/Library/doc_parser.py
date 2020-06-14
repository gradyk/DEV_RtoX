#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

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
__name__ = "Contents.Library.doc_parser"

# From standard libraries
import json
import linecache
import os
import re

# From local application
import Contents.Library.destination
import file_stats
import contents_group_parse
import Contents.Library.group
import Contents.Library.slash_star
import working_xml_file_update


def main_doc_parser(working_input_file: str, debug_dir: str,
                    control_word_func_dict: str) -> None:
    file_metrics = file_stats.file_stats_calculator(
        working_input_file=working_input_file)
    length_working_input_file = file_metrics[0]

    header_table_file = os.path.join(debug_dir, "header_tables_dict.json")
    with open(header_table_file, "r") as header_table_dict_pre:
        header_table_dict = json.load(header_table_dict_pre)

    line_to_parse = header_table_dict["info"][2]
    parse_index = header_table_dict["info"][3]
    shift_text = ""

    while line_to_parse < (length_working_input_file + 1):
        reset_line_to_parse = line_to_parse
        parse_text = linecache.getline(working_input_file, line_to_parse)
        parse_text = parse_text.rstrip("\n").rstrip(" ")
        parse_text = shift_text + parse_text
        length_parse_text = len(parse_text)

        while parse_index <= (length_parse_text - 1):
            if parse_index > (length_parse_text - 3):
                shift_length = length_parse_text - parse_index
                shift_text = parse_text[-shift_length]
                line_to_parse += 1
                parse_index = 0
                break
            else:
                pass
            character = parse_text[parse_index]
            character_plus_one = parse_text[parse_index+1]
            character_plus_two = parse_text[parse_index+2]

            if character == " ":
                line_to_parse, parse_index = blank_space(
                    line_to_parse=line_to_parse,
                    parse_index=parse_index)

            elif character + character_plus_one + character_plus_two == "{\\*":

                reset_line_to_parse, parse_index = bracket_slash_star(
                    line_to_parse=line_to_parse,
                    parse_index=parse_index,
                    working_input_file=working_input_file,
                    shift_text=shift_text)

                if reset_line_to_parse > line_to_parse:
                    line_to_parse = reset_line_to_parse
                    break
                else:
                    pass

                if parse_index >= length_parse_text:
                    reset_line_to_parse = line_to_parse + 1
                    parse_index = 0
                else:
                    pass

            elif character == "{":

                reset_line_to_parse, parse_index = group(
                    line_to_parse=line_to_parse,
                    parse_index=parse_index,
                    working_input_file=working_input_file,
                    shift_text=shift_text, debug_dir=debug_dir,
                    control_word_func_dict=control_word_func_dict)

            elif character == "\\":

                line_to_parse, parse_index = destination(
                    line_to_parse=line_to_parse,
                    parse_index=parse_index,
                    working_input_file=working_input_file,
                    debug_dir=debug_dir,
                    control_word_func_dict=control_word_func_dict)

                if parse_index >= length_parse_text:
                    reset_line_to_parse = line_to_parse + 1
                    parse_index = 0
                else:
                    pass

            elif character == "}":
                parse_index += 1

                if parse_index >= length_parse_text:
                    reset_line_to_parse = line_to_parse + 1
                    parse_index = 0
                else:
                    pass

            else:
                line_to_parse, parse_index = contents(
                    line_to_parse=line_to_parse,
                    working_input_file=working_input_file,
                    parse_index=parse_index,
                    debug_dir=debug_dir)

            if reset_line_to_parse != line_to_parse:
                line_to_parse = reset_line_to_parse
                break
            else:
                pass

            shift_text = ""


def blank_space(line_to_parse: int, parse_index: int) -> tuple:
    parse_index += 1
    return line_to_parse, parse_index


def bracket_slash_star(line_to_parse: int, parse_index: int,
                       working_input_file: str, shift_text: str) -> tuple:
    line_to_parse, parse_index \
        = Contents.Library.slash_star.slash_star_processor(
            working_input_file=working_input_file,
            parse_index=parse_index,
            line_to_parse=line_to_parse,
            shift_text=shift_text)
    return line_to_parse, parse_index


def group(line_to_parse: int, parse_index: int, working_input_file: str,
          shift_text: str, debug_dir: str, control_word_func_dict: str) \
        -> tuple:
    group_id, group_info, reset_line_to_parse, parse_index = \
        Contents.Library.group.group_processor(
            line_to_parse=line_to_parse,
            parse_index=parse_index,
            working_input_file=working_input_file,
            shift_text=shift_text)

    contents_group_parse.contents_group_processor(
        debug_dir=debug_dir,
        group_id=group_id, group_info=group_info,
        control_word_func_dict=control_word_func_dict)
    return reset_line_to_parse, parse_index


def destination(line_to_parse: int, parse_index: int, debug_dir: str,
                control_word_func_dict: str, working_input_file: str) -> tuple:
    line_to_parse, parse_index = \
        Contents.Library.destination.destination_processor(
            line_to_parse=line_to_parse,
            parse_index=parse_index,
            working_input_file=working_input_file,
            control_word_func_dict=control_word_func_dict,
            debug_dir=debug_dir)
    return line_to_parse, parse_index


def contents(line_to_parse: int, working_input_file: str, parse_index: int,
             debug_dir: str) -> tuple:
    try:
        parse_text = linecache.getline(working_input_file, line_to_parse)
        parse_text = parse_text.rstrip("\n").rstrip(" ")
        regex = r"^((?!\}|\\).)*"
        matches = re.search(regex, parse_text[parse_index:])
        working_xml_file_update.tag_append(
            debug_dir=debug_dir,
            tag_update=matches.group(0))
        end = matches.end()
        parse_index = parse_index + end
        return line_to_parse, parse_index
    except TypeError:
        # TODO Replace next line
        print("STRING DOES NOT MATCH", line_to_parse, parse_index)
        return line_to_parse, parse_index
