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
__date__ = "2020-06-01"
__name__ = "Contents.Library.contents_group_parse"

# From standard library
import re

# From local application
import Contents.Library.contents_group
import Contents.Library.contents_destination
import Contents.Library.contents_slash_star
import working_xml_file_update


def contents_group_processor(group_id: str, group_info: dict,
                             debug_dir: str, control_word_func_dict: str):
    contents = group_info[group_id][0]
    contents = contents.lstrip("{").rstrip("}")
    parse_index = 0
    length_of_contents = len(contents)

    while parse_index < length_of_contents:
        character, character_plus_one, character_plus_two = define_character(
            parse_index=parse_index,
            length_of_contents=length_of_contents,
            contents=contents)

        if character + character_plus_one + character_plus_two == "{\\*":
            parse_index, character, character_plus_one, character_plus_two = \
                contents_bracket_slash_star(
                    contents=contents,
                    parse_index=parse_index,
                    length_of_contents=length_of_contents)

        elif character == "{":
            parse_index += 1
            pass

        elif character == " ":
            parse_index = contents_blank_space(
                parse_index=parse_index,
                character_plus_one=character_plus_one,
                debug_dir=debug_dir)
            pass

        elif character == "\\":
            parse_index = contents_destination(
                contents=contents,
                parse_index=parse_index,
                control_word_func_dict=control_word_func_dict,
                debug_dir=debug_dir)
            pass

        elif character == "}":
            parse_index = close_bracket(parse_index=parse_index)
            pass

        else:
            contents_to_xml(contents=contents,
                            parse_index=parse_index,
                            debug_dir=debug_dir)
            parse_index = length_of_contents


def define_character(parse_index: int, length_of_contents: int,
                     contents: str) -> tuple:
    character_plus_one = ""
    character_plus_two = ""

    if length_of_contents - parse_index <= 1:
        character = contents[parse_index]
        pass
    elif length_of_contents - parse_index <= 2:
        character = contents[parse_index]
        character_plus_one = contents[parse_index + 1]
        pass
    else:
        character = contents[parse_index]
        character_plus_one = contents[parse_index + 1]
        character_plus_two = contents[parse_index + 2]

    return character, character_plus_one, character_plus_two


def contents_blank_space(parse_index: int, character_plus_one: str,
                         debug_dir: str) -> int:
    if character_plus_one == " ":
        text = " "
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=text[0])
        print("    TEXT", text[0])
        parse_index = parse_index + 2
    else:
        parse_index += 1
    return parse_index


def contents_bracket_slash_star(contents: str, parse_index: int,
                                length_of_contents: int) -> tuple:
    parse_index \
        = Contents.Library.contents_slash_star.contents_slash_star_processor(
            parse_index=parse_index,
            contents=contents)
    character, character_plus_one, character_plus_two = define_character(
        parse_index=parse_index,
        length_of_contents=length_of_contents,
        contents=contents)
    return parse_index, character, character_plus_one, character_plus_two


def contents_group(parse_index: int, contents: str):
    parse_index = \
        Contents.Library.contents_group.contents_group_processor(
            contents=contents,
            parse_index=parse_index)
    return parse_index


def contents_destination(contents: str, parse_index: int,
                         control_word_func_dict: str,
                         debug_dir: str) -> int:
    parse_index = \
        Contents.Library.contents_destination.destination_content_processor(
            contents=contents,
            parse_index=parse_index,
            control_word_func_dict=control_word_func_dict,
            debug_dir=debug_dir)
    return parse_index


def close_bracket(parse_index: int) -> int:
    parse_index += 1
    return parse_index


def contents_to_xml(contents: str, parse_index: int, debug_dir: str):
    try:
        regex = r"^((?!\}|\\).)*"
        text = re.search(regex, contents[parse_index:])
        end = text.end()
        working_xml_file_update.tag_append(debug_dir=debug_dir,
                                           tag_update=text[0])
        print("    TEXT", text[0])
        print("      ", contents[parse_index])
    # TODO Replace what happens in error situations.
    except TypeError:
        print("NONETYPE", parse_index)
    except IndexError:
        print(contents[-1])
