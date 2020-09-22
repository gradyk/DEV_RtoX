#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
An RTF file typically uses Microsoft code page 1252 character encoding (
though it may use other encodings). Various MS1252 characters need to be
replaced with unicode characters. The first part of this module
makes the switch. The second part replaces miscellaneous
characters and formatting signals with acceptable unicode characters.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-27"
__name__ = "Contents.Library.convert_to_unicode"

# From standard libraries
import codecs
import json
import linecache
import re
import os
from pathlib import Path

# From local application
import file_stats


def processor():
    block_size = 1048576  # or some other, desired size in bytes
    base_dir = Path.cwd()
    debug_dir = os.path.join(base_dir, "debugdir")
    source_file = os.path.join(debug_dir, "working_input_file_pre.txt")
    target_file = os.path.join(debug_dir, "working_input_file_new.txt")
    with codecs.open(source_file, "r+") as source_file_open:
        with codecs.open(target_file, "w+", "utf-8") as target_file_open:
            while True:
                contents = source_file_open.read(block_size)
                if not contents:
                    break
                target_file_open.write(contents)

    os.remove(source_file)


def character_cleanup():
    """ Convert miscellaneous characters to unicode. """
    base_dir = Path.cwd()
    debug_dir = os.path.join(base_dir, "debugdir")
    source_file = os.path.join(debug_dir, "working_input_file_new.txt")
    target_file = os.path.join(debug_dir, "working_input_file.txt")
    file_length = file_stats.processor(working_input_file=source_file)

    pattern_list = [
        r"&",
        r"(\\'[A-Z0-9]{2})",
        r"HT\\tab",
        r"\\tab"
    ]

    line = 1
    with open(target_file, "a+") as target_file_open:
        while line <= file_length + 1:
            file_string = linecache.getline(source_file, line)
            for pattern in pattern_list:
                file_string = re.sub(pattern, code_value, file_string)
            target_file_open.write(file_string)
            line += 1

    os.remove(source_file)


def code_value(matchobj):
    base_dir = Path.cwd()
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    code_array = os.path.join(dicts_dir, "code_page_1252_array.json")
    supp_array = os.path.join(dicts_dir, "supp_code_page_array.json")
    with open(code_array, "r+") as code_dict_pre:
        code_dict = json.load(code_dict_pre)
    with open(supp_array, "r+") as supp_dict_pre:
        supp_dict = json.load(supp_dict_pre)
    merged_dict ={**code_dict, **supp_dict}
    match_text = matchobj.group(0).replace("\\'", "")
    value = merged_dict[match_text]
    return value
