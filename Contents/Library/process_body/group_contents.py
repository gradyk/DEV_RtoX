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

import re
import sys
from collections import deque


def processor_settings(group_info: dict) -> None:
    contents_list = []
    res = next(iter(group_info))
    working_parse_text = group_info[res][0][:-1].lstrip("{")
    parse_index = 0
    processor(contents_list=contents_list, parse_index=parse_index,
              working_parse_text=working_parse_text)


def processor(contents_list: list, parse_index: int,
              working_parse_text: str):
    if working_parse_text == "":
        pass
    else:
        group_test(parse_index=parse_index,
                   working_parse_text=working_parse_text,
                   contents_list=contents_list)
        destination_test(
            parse_index=parse_index,
            working_parse_text=working_parse_text,
            contents_list=contents_list)
        control_word_test(
            parse_index=parse_index,
            working_parse_text=working_parse_text,
            contents_list=contents_list)
        control_symbol_test(
            parse_index=parse_index,
            working_parse_text=working_parse_text,
            contents_list=contents_list)
        text_test(
            parse_index=parse_index,
            working_parse_text=working_parse_text,
            contents_list=contents_list)

    print(contents_list)
    sys.exit()


def group_test(parse_index: int, working_parse_text: str, contents_list: list):
    # Group
    test = re.search(r"^{", working_parse_text)
    if test is not None:
        group_contents = group_boundaries(
            working_parse_text=working_parse_text, test=test)
        contents_list.append(group_contents)
        working_parse_text = working_parse_text[parse_index:]
        working_parse_text = working_parse_text[:-1].lstrip("{")
        parse_index = 0
        processor(parse_index=parse_index, contents_list=contents_list,
                  working_parse_text=working_parse_text)
    else:
        pass


def destination_test(working_parse_text: str, parse_index: int,
                     contents_list: list):
    # Destination
    test = re.search(r"^(\\\*\\)([a-zA-Z]*)(\s|-|[0-9]+)?",
                     working_parse_text)
    if test is not None:
        control_word = test[0]
        parse_index = parse_index + len(control_word)
        control_word = control_word.replace("\\*", "").rstrip()
        contents_list.append(control_word)
        working_parse_text = working_parse_text[parse_index:]
        parse_index = 0
        processor(parse_index=parse_index, contents_list=contents_list,
                  working_parse_text=working_parse_text)
    else:
        pass


def control_word_test(working_parse_text: str, parse_index: int,
                      contents_list: list):
    # Control word
    test = re.search(r"^(\\)([a-zA-Z]*)(\s|-|[0-9]+)?", working_parse_text)
    if test is not None:
        control_word = test.group()
        control_word = control_word.rstrip()
        parse_index = parse_index + test.end()
        contents_list.append(control_word)
        working_parse_text = working_parse_text[parse_index:]
        parse_index = 0
        processor(parse_index=parse_index, contents_list=contents_list,
                  working_parse_text=working_parse_text)
    else:
        pass


def control_symbol_test(working_parse_text: str, parse_index: int,
                        contents_list: list):
    # Control symbol
    test = re.search(r"^(\\)[^A-Za-z0-9]?", working_parse_text)
    if test is not None:
        control_symbol = test.group()
        control_symbol = control_symbol.rstrip()
        parse_index = parse_index + test.end()
        contents_list.append(control_symbol)
        working_parse_text = working_parse_text[parse_index:]
        parse_index = 0
        processor(parse_index=parse_index, contents_list=contents_list,
                  working_parse_text=working_parse_text)
    else:
        pass


def text_test(working_parse_text: str, parse_index: int, contents_list: list):
    # TODO What if the text is a { or \ or includes one or
    #  both characters?
    # Text
    test = re.search(r"^([A-Za-z0-9.?!,;:\-()\[\]'\"/]*)", working_parse_text)
    if test is not None:
        control_word = test.group()
        parse_index = parse_index + test.end()
        contents_list.append(control_word)
        working_parse_text = working_parse_text[parse_index:]
        parse_index = 0
        processor(parse_index=parse_index, contents_list=contents_list,
                  working_parse_text=working_parse_text)
    else:
        pass


def group_boundaries(working_parse_text: str, test) -> str:
    deck = deque()
    group_contents = ""

    working_index = test.start()
    while working_index < len(working_parse_text) + 1:

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
                return group_contents
            else:
                working_index += 1

        else:
            group_contents = group_contents + \
                             working_parse_text[working_index]
            working_index += 1
