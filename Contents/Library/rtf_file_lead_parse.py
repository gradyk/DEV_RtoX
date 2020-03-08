#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  1. Redistributions of source code must retain the above copyright notice,
#  this list of conditions and the following disclaimer.
#
#  2. Redistributions in binary form must reproduce the above copyright
#  notice, this list of conditions and the following disclaimer in the
#  documentation and/or other materials provided with the distribution.
#
#  3. Neither the name of the copyright holder nor the names of its
#  contributors may be used to endorse or promote products derived
#  from this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
Process the RTF file control words that precede the table definitions,
capturing codes in the rtf_file_codes dictionary.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-10"
__name__ = "Contents.Library.first_line"

# From standard libraries
import codecs
import json
import linecache
import logging
import os
import re

# From local application
from read_log_config import logger_basic
from read_log_config import logger_debug


def check_input_file_encoding(working_input_file: str, debug_dir: str):
    """ Check the working_input_file to make sure it is in utf-8 encoding. """
    working_input_file = os.path.join(debug_dir, working_input_file)
    try:
        codecs.open(working_input_file, encoding="utf-8",
                    errors="strict").readlines()
    except (UnicodeEncodeError, ValueError):
        logger_basic.critical(msg="There was a problem encoding the file "
                                  "as utf-8.")


def check_for_opening_brace(working_input_file: str, debug_dir: str):
    """ Check the working_input_file for an opening brace. """

    if linecache.getline(working_input_file, 1)[0] == "{":
        pass
    else:
        insert_opening_brace(working_input_file=working_input_file,
                             debug_dir=debug_dir)


def insert_opening_brace(working_input_file: str, debug_dir: str):
    """ If the file does not have an opening brace, insert one. """
    with open(os.path.join(working_input_file, debug_dir), "r") as \
            file_to_fix_pre:
        file_to_fix = "{" + file_to_fix_pre.read()
    with open(os.path.join(working_input_file, debug_dir), "w") as \
            file_to_fix_pre:
        file_to_fix_pre.write(file_to_fix)


def code_process(working_input_file: str):
    """ Test for the existence of each pretable controlword and,
    if present, capture the code. """
    pretable_controlword_replacementtext_list = [
        ("rtf[0-9]+", "rtf"),
        ("ansi", "ansi"),
        ("ansicpg1252", "ansicpg1252"),
        ("upr", "upr"),
        ("uc[0-9]+", "uc"),
        ("deflang[0-9]+", "deflang"),
        ("deflangfe[0-9]+", "deflangfe"),
        ("deff[0-9]+", "deff"),
        ("adeff[0-9]+", "adeff"),
        ("stshfdbch[0-9]+", "stshfdbch"),
        ("stshfloch[0-9]+", "stshfloch"),
        ("stshfhich[0-9]+", "stshfhich"),
        ("stshfbi[0-9]+", "stshfbi"),
        ("[a-z]+deflang[a-z]+", "deflang"),
        ("themelang[0-9]+", "themelang"),
        ("themelangfe[0-9]+", "themelangfe"),
        ("themelangcs[0-9]+", "themelangcs")
    ]
    rtf_file_codes_update = []
    line_to_search = linecache.getline(working_input_file, 1)

    for item in pretable_controlword_replacementtext_list:
        try:
            code_match = re.search(r'\\%s' % item[0],
                                   line_to_search)
            code = code_match[0].replace(f'\\{item[1]}', "")
            rtf_file_codes_update.append((item[1], code))
        except TypeError:
            if logger_basic.isEnabledFor(logging.INFO):
                logger_basic.info(f"No {item[1]} code.\n")

    return rtf_file_codes_update


def update_rtf_file_codes_dict(rtf_file_codes_update: dict, debug_dir: str):
    """ Update the rtf_file_codes dictionary with codes extracted from
    pretable controlwords. """
    rtf_file_codes_file = os.path.join(debug_dir, "rtf_file_codes.json")
    with open(rtf_file_codes_file) as rtf_file_codes_file_pre:
        rtf_file_codes = json.load(rtf_file_codes_file_pre)
        rtf_file_codes.update(rtf_file_codes_update)
    with open(rtf_file_codes_file, "w", encoding='utf-8') as \
            rtf_file_codes_file_pre:
        json.dump(rtf_file_codes, rtf_file_codes_file_pre,
                  ensure_ascii=False)

    # Used for debugging purposes.
    if logger_debug.isEnabledFor(logging.ERROR):
        logger_debug(msg=str(rtf_file_codes))
