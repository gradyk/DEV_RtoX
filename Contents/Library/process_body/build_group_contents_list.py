#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
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

# From standard libraries
import logging
import re

# From local applications
import group_contents


def pre_process(processing_dict: dict):
    contents_string = processing_dict["group_contents"]
    processing_dict["contents_string"] = contents_string
    print("cs ", contents_string)
    processor(processing_dict=processing_dict)


def processor(processing_dict: dict) -> None:
    string_length = len(processing_dict["contents_string"])
    print("cs length ", string_length)
    while processing_dict["contents_string"] != "":
        try:
            left_bracket(processing_dict=processing_dict)
            post1987(processing_dict=processing_dict)
            control_word(processing_dict=processing_dict)
            control_symbol(processing_dict=processing_dict)
            right_bracket(processing_dict=processing_dict)
            text(processing_dict=processing_dict)
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")
    else:
        group_contents.processor(processing_dict=processing_dict)


def left_bracket(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^{", processing_dict["contents_string"])
    if test is not item:
        print("left_bracket: ", test[0])
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"][1:]
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        post1987(processing_dict=processing_dict)


def post1987(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^(\\\*\\[a-zA-Z\-\s0-9]*)",
                     processing_dict["contents_string"])
    if test is not item:
        print("post1987: ", test[0])
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].\
            replace(test[0], "", 1)
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        control_word(processing_dict=processing_dict)


def control_word(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^(\\[a-zA-Z\-0-9]*)", processing_dict[
        "contents_string"])
    if test is not item:
        print("control_word ", test[0])
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].\
            replace(test[0], "", 1)
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        control_symbol(processing_dict=processing_dict)


def control_symbol(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^(\\)[^A-Za-z0-9]?", processing_dict["contents_string"])
    if test is not item:
        print("control_symbol: ", test[0])
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].\
            replace(test[0], "", 1)
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        right_bracket(processing_dict=processing_dict)


def right_bracket(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^}", processing_dict["contents_string"])
    if test is not item:
        print("right_bracket: ", test[0])
        results = test.group()
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"][1:]
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        text(processing_dict=processing_dict)


def text(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^([a-zA-Z\-\s0-9]*)", processing_dict["contents_string"])
    if test is not item:
        print("text: ", test[0])
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].lstrip(test[0])
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        processor(processing_dict=processing_dict)
