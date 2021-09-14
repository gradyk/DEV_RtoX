#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the file table (if the table exists in the document it means the
pre-RTF file included sub-documents). """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "Contents.Library.file_table"

# From standard libraries

from typing import Tuple

# From local application
import dict_updater

""" An RTF file uses the following structure for a filetbl (if present):
    <filetbl>       '{\\*'\\filetbl ('{' <fileinfo> '}')+ '}'
    <fileinfo>      \\file <filenum><relpath>?<osnum>? <filesource>+ <file
    name>
    <filenum>       \\fid
    <relpath>       \\frelative
    <osnum>         \\fosnum
    <filesource>    \\fvalidmac | \\fvaliddos | \\fvalidntfs | \\fvalidhpfs |
                    \\fnetwork | \\fnonfilesys
    <file name>     #PCDATA
    """


# TODO Complete file table analysis.
def trim_filetbl(main_dict: dict) -> iter:
    """ RTF wraps the file table with {\\filetbl ... }. This function
    removes the prefix. """
    main_dict["group_contents"] = main_dict["group_contents"].replace(
        "{\\*\\filetbl;", "").replace(";}", "")
    return main_dict


def split_code_strings(main_dict: dict) -> Tuple[dict, list]:
    """ An RTF file table includes ... """
    code_strings_list = main_dict["group_contents"].split(";")
    return main_dict, code_strings_list


def parse_code_strings(code_strings_list: iter, main_dict: dict) -> None:
    """ Parse each file table string. """
    code_dict = {}
    cs_list = list(code_strings_list)[0]
    for code_string in cs_list:
        key = cs_list.index(code_string)
        code_dict.update({key: {}})
        code_dict = parse_control_word(
            code_string=code_string, code_dict=code_dict, key=key)
        code_dict = parse_theme_control_word(
            code_string=code_string, code_dict=code_dict, key=key)
        dict_updater.json_dict_updater(dict_name="file_table_file.json",
                                       dict_update=code_dict,
                                       main_dict=main_dict)
        code_dict = {}


def parse_control_word(code_string: str, code_dict: dict, key: str):
    code_dict = code_dict
    return code_dict


def parse_theme_control_word(code_string: str, code_dict: dict, key: str):
    code_dict = code_dict
    return code_dict
