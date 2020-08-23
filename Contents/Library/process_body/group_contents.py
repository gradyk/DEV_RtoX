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
#  with RtoX. If not, see <https://www.gnu.org/licenses/>.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

# From standard libraries
import logging
import pprint
import re
from collections import deque

# From local application
import check_parse_text


def processor_settings(group_info: dict, line_to_parse: int, group_dict: dict,
                       working_input_file: str, debug_dir: str,
                       control_word_dict: str,
                       num_lines: int) -> None:
    contents_list = []
    res = next(iter(group_info))
    working_parse_text = group_info[res][0][:-1].lstrip("{")
    parse_index = 0

    processor(parse_index=parse_index, contents_list=contents_list,
              working_parse_text=working_parse_text,
              line_to_parse=line_to_parse,
              group_dict=group_dict, working_input_file=working_input_file,
              debug_dir=debug_dir, control_word_dict=control_word_dict,
              num_lines=num_lines)


def processor(line_to_parse: int, contents_list: list, parse_index: int,
              working_parse_text: str, group_dict: dict,
              working_input_file: str, debug_dir: str, control_word_dict: str,
              num_lines: int):

    if working_parse_text != "":
        group_test(contents_list=contents_list,
                   line_to_parse=line_to_parse,
                   working_parse_text=working_parse_text,
                   group_dict=group_dict, working_input_file=working_input_file,
                   debug_dir=debug_dir, control_word_dict=control_word_dict,
                   num_lines=num_lines)
        post1987_destination_test(
            contents_list=contents_list, parse_index=parse_index,
            working_parse_text=working_parse_text, group_dict=group_dict,
            line_to_parse=line_to_parse, working_input_file=working_input_file,
            debug_dir=debug_dir, control_word_dict=control_word_dict,
            num_lines=num_lines)
        control_word_test(
            contents_list=contents_list, parse_index=parse_index,
            working_parse_text=working_parse_text, group_dict=group_dict,
            line_to_parse=line_to_parse, working_input_file=working_input_file,
            debug_dir=debug_dir, control_word_dict=control_word_dict,
            num_lines=num_lines)
        control_symbol_test(
            contents_list=contents_list, parse_index=parse_index,
            working_parse_text=working_parse_text, group_dict=group_dict,
            line_to_parse=line_to_parse, working_input_file=working_input_file,
            debug_dir=debug_dir, control_word_dict=control_word_dict,
            num_lines=num_lines)
        text_test(contents_list=contents_list, parse_index=parse_index,
                  working_parse_text=working_parse_text, group_dict=group_dict,
                  line_to_parse=line_to_parse,
                  working_input_file=working_input_file,
                  debug_dir=debug_dir, control_word_dict=control_word_dict,
                  num_lines=num_lines)
    else:
        print(contents_list)
        parser(contents_list=contents_list, group_dict=group_dict)
        for key, value in group_dict.items():
            if key == "children" and value != []:
                contents_list = group_dict["id"]
                # UPDATE OTHER VARIABLES???
                group_test(contents_list=contents_list,
                           line_to_parse=line_to_parse,
                           working_parse_text=working_parse_text,
                           group_dict=group_dict,
                           working_input_file=working_input_file,
                           debug_dir=debug_dir,
                           control_word_dict=control_word_dict,
                           num_lines=num_lines)
                group_dict_updater = {"children": [
                    {"id": "test"},
                    {"type": "group"},
                    {"children": []}
                ]}
                group_dict.update(group_dict_updater)
            else:
                pass


def group_test(contents_list: list, line_to_parse: int,
               working_parse_text: str, group_dict: dict,
               working_input_file: str, debug_dir: str,
               control_word_dict: str, num_lines: int) -> None:
    item = None
    try:
        test = re.search(r"^{", working_parse_text)
        if test is not item:
            group_contents, parse_index = group_boundaries(
                working_parse_text=working_parse_text, test=test)
            contents_list.append(group_contents)
            working_parse_text = working_parse_text[parse_index:]
            parse_index = 0
            processor(parse_index=parse_index, contents_list=contents_list,
                      working_parse_text=working_parse_text,
                      group_dict=group_dict, line_to_parse=line_to_parse,
                      working_input_file=working_input_file,
                      debug_dir=debug_dir, control_word_dict=control_word_dict,
                      num_lines=num_lines)
            check_parse_text.check_string_manager(
                parse_text=working_parse_text, line_to_parse=line_to_parse,
                parse_index=parse_index, working_input_file=working_input_file,
                debug_dir=debug_dir, control_word_dict=control_word_dict,
                num_lines=num_lines, group_dict=group_dict)
        else:
            pass
    except TypeError:
        logging.exception(f"Group_test: {contents_list}")
        pass


def post1987_destination_test(contents_list: list, parse_index: int,
                              working_parse_text: str,
                              group_dict: dict, line_to_parse: int,
                              working_input_file: str, debug_dir: str,
                              control_word_dict: str,
                              num_lines: int) -> None:
    item = None
    try:
        test = re.search(r"^(\\\*\\)([a-zA-Z]*)(\s|-|[0-9]+)?",
                         working_parse_text)
        if test is not item:
            control_word = test[0]
            parse_index = parse_index + len(control_word)
            control_word = control_word.replace("\\*", "").rstrip()
            contents_list.append(control_word)
            working_parse_text = working_parse_text[parse_index:]
            parse_index = 0
            processor(parse_index=parse_index, contents_list=contents_list,
                      working_parse_text=working_parse_text,
                      group_dict=group_dict, line_to_parse=line_to_parse,
                      working_input_file=working_input_file,
                      debug_dir=debug_dir, control_word_dict=control_word_dict,
                      num_lines=num_lines)
        else:
            pass
    except TypeError:
        logging.exception(f"Post1987_destination_test: {contents_list}")
        pass


def control_word_test(contents_list: list, parse_index: int,
                      working_parse_text: str, group_dict: dict,
                      line_to_parse: int,
                      working_input_file: str, debug_dir: str,
                      control_word_dict: str,
                      num_lines: int) -> None:
    item = None
    try:
        test = re.search(r"^(\\\w+)", working_parse_text)
        if test is not item:
            control_word = test.group()
            control_word = control_word.rstrip()
            parse_index = parse_index + test.end()
            contents_list.append(control_word)
            print(control_word)
            working_parse_text = working_parse_text[parse_index:]
            parse_index = 0
            processor(parse_index=parse_index, contents_list=contents_list,
                      working_parse_text=working_parse_text,
                      group_dict=group_dict, line_to_parse=line_to_parse,
                      working_input_file=working_input_file,
                      debug_dir=debug_dir, control_word_dict=control_word_dict,
                      num_lines=num_lines)
        else:
            pass
    except TypeError:
        logging.exception(f"Control_word_test: {contents_list}")
        pass


def control_symbol_test(contents_list: list, parse_index: int,
                        working_parse_text: str, group_dict: dict,
                        line_to_parse: int,
                        working_input_file: str, debug_dir: str,
                        control_word_dict: str, num_lines: int) -> None:
    item = None
    try:
        test = re.search(r"^(\\)[^A-Za-z0-9]?", working_parse_text)
        if test is not item:
            control_symbol = test.group()
            control_symbol = control_symbol.rstrip()
            parse_index = parse_index + test.end()
            contents_list.append(control_symbol)
            working_parse_text = working_parse_text[parse_index:]
            parse_index = 0
            processor(parse_index=parse_index, contents_list=contents_list,
                      working_parse_text=working_parse_text,
                      group_dict=group_dict, line_to_parse=line_to_parse,
                      working_input_file=working_input_file,
                      debug_dir=debug_dir, control_word_dict=control_word_dict,
                      num_lines=num_lines)
        else:
            pass
    except TypeError:
        logging.exception(f"Control_symbol_test: {contents_list}")
        pass


def text_test(contents_list: list, parse_index: int,
              working_parse_text: str, group_dict: dict,
              line_to_parse: int,
              working_input_file: str, debug_dir: str, control_word_dict: str,
              num_lines: int) -> None:
    # TODO What if the text is a { or \ or includes one or
    #  both characters?
    item = None
    try:
        test = re.search(r"^(\w+|\s|\W)*(?<!})", working_parse_text)
        if test is not item:
            control_word = test.group()
            parse_index = parse_index + test.end()
            contents_list.append(control_word)
            working_parse_text = working_parse_text[parse_index:]
            parse_index = 0
            processor(parse_index=parse_index, contents_list=contents_list,
                      working_parse_text=working_parse_text,
                      group_dict=group_dict, line_to_parse=line_to_parse,
                      working_input_file=working_input_file,
                      debug_dir=debug_dir, control_word_dict=control_word_dict,
                      num_lines=num_lines)
        else:
            # TODO If you arrive at this point, something is wrong - raise an
            #  error.
            pass
    except TypeError:
        logging.exception(f"Text_test: {contents_list}")
        pass


def group_boundaries(working_parse_text: str, test) -> tuple:
    deck = deque()
    group_contents = ""

    working_index = test.start()
    length = len(working_parse_text)
    while working_index < length + 1:

        if working_parse_text[working_index] == "{":
            deck.append(working_parse_text[working_index])
            group_contents = group_contents + \
                working_parse_text[working_index]
            working_index += 1
        elif working_parse_text[working_index] == "}":
            group_contents = group_contents + \
                working_parse_text[working_index]
            deck.popleft()

            if not deck:  # If deck is empty ...
                deck.clear()
                return group_contents, working_index + 1
            else:
                working_index += 1

        else:
            group_contents = group_contents + \
                             working_parse_text[working_index]
            working_index += 1


def parser(contents_list: list, group_dict: dict):

    for ele in contents_list:
        if re.search(r"^(\\\w+)", ele) is not None:
            child = {"id": ele,
                     "type": "cw"}

            group_dict["children"].append(child)
        elif re.search(r"^{", ele):
            child = {"id": ele,
                     "type": "group",
                     "children": []}

            group_dict["children"].append(child)

    pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)
    pp.pprint(group_dict)
