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

import logging
import re

import group_contents


def pre_process(processing_dict: dict):
    contents_string = processing_dict["group_contents"]
    contents_list = []
    print(contents_string)
    dict_update = {"contents_string": contents_string,
                   "contents_list": contents_list}
    processing_dict.update(dict_update)
    processor(processing_dict=processing_dict)


def processor(processing_dict: dict) -> None:
    while processing_dict["contents_string"] != "":
        try:
            left_bracket(processing_dict=processing_dict)
            post1987(processing_dict=processing_dict)
            control_word(processing_dict=processing_dict)
            control_symbol(processing_dict=processing_dict)
            right_bracket(processing_dict=processing_dict)
            text(processing_dict=processing_dict)
        except (ValueError, TypeError):
            logging.exception("_____________")
    group_contents.processor(processing_dict=processing_dict)


def left_bracket(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^{", processing_dict["contents_string"])
    if test is not item:
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
    test = re.search(r"^(\\\*\\)([a-zA-Z]*)(\s|-|[0-9]+)?",
                     processing_dict["contents_string"])
    if test is not item:
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].lstrip(test[0])
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        control_word(processing_dict=processing_dict)


def control_word(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^(\\\w+)", processing_dict["contents_string"])
    if test is not item:
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].\
            replace(test[0], "")
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        control_symbol(processing_dict=processing_dict)


def control_symbol(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^(\\)[^A-Za-z0-9]?", processing_dict["contents_string"])
    if test is not item:
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].\
            replace(test[0], "")
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        right_bracket(processing_dict=processing_dict)


def right_bracket(processing_dict: dict) -> None:
    item = None
    test = re.search(r"^}", processing_dict["contents_string"])
    if test is not item:
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
    test = re.search(r"^}", processing_dict["contents_string"])
    if test is not item:
        results = test[0]
        processing_dict["contents_list"].append(results)
        contents_string = processing_dict["contents_string"].lstrip(test[0])
        contents_string = contents_string.lstrip()
        processing_dict["contents_string"] = contents_string
        processor(processing_dict=processing_dict)
    else:
        processor(processing_dict=processing_dict)
