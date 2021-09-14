#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the font table and pass the values to a dictionary. An RTF file
uses the following structure for a fonttbl (if present):
<fonttbl>       '{' \\fonttbl (<fontinfo> | ('{' <fontinfo> '}'))+ '}'
<fontinfo>      <fontnum> <fontfamily> <fcharset>? <fprq>? <panose>?
                <nontaggedname>? <fontemb>? <codepage>? <fontname>
                <fontaltname>?';'
<themefont>     \\flomajor | \\fhimajor | \\fdbmajor | \\flominor | \\fdbminor |
                \\fbiminor
<fontnum>       \\f
<fontfamily>    \\fnil | \\froman | \\fswiss | \\fmodern | fscript | \\fdecor
                | \\ftech | \\fbidi
<fcharset>      \\fcharset
<fprq>          \\fprq
<panose>        <data>
<nontaggedname> \\*\\fname
<fontname>      #PCDATA
<fontaltname>   '{\\*' \\falt #PCDATA '}'
<fontemb>       '{\\*' \\fontemb <fonttype> <fontfname>? <data>? '}'
<fonttype>      \\ftnil | \\fttruetype
<fontfname>     '{\\*' \\fontfile <codepage>? #PCDATA '}'
<codepage>      \\cpg
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-31"
__name__ = "Contents.Library.font_table"

# From standard libraries
import json
import logging
import os
import re
from collections import deque
from typing import Any, Tuple

# From local application
import dict_updater
import find_group_end

log = logging.getLogger(__name__)


def trim_fonttbl(main_dict: dict) -> dict:
    """ RTF wraps the font table with {\\fonttbl ... }. This function
    removes the prefix and suffix. """
    main_dict["group_contents"] = main_dict["group_contents"].replace(
        "{\\fonttbl", "").rstrip("}")
    return main_dict


def split_code_strings(main_dict: dict) -> Tuple[dict, list]:
    """ An RTF font table includes a string for each font code number. """
    main_dict["group_contents"] = main_dict["group_contents"].replace(
        "}{", "}|{")
    code_strings_list = main_dict["group_contents"].split("|")
    return main_dict, code_strings_list


def remove_code_strings(code_strings_list: list) -> list:
    """ RtoX ignores strings that begin with \\*\\."""
    remove_list = []
    for code_string in code_strings_list:
        pattern = re.compile(r"^{\\\*\\")
        place = code_strings_list.index(code_string)
        if re.search(pattern, code_string) is not None:
            remove_list.append(place)
    for ele in sorted(remove_list, reverse=True):
        del code_strings_list[ele]
    return code_strings_list


def parse_code_strings(main_dict: dict, code_strings_list: list):
    index = 0
    code_dict = {}
    current_key = ""
    deck = deque()
    for code_string in code_strings_list:
        code_string = delete_themes(code_string=code_string)
        if code_string is not None:
            code_string, code_dict, current_key, index = check_fontnum(
                code_string=code_string, code_dict=code_dict)
        if code_string is not None:
            code_string, code_dict, index = check_fontfamily(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key, index=index, main_dict=main_dict)
        if code_string is not None:
            code_string, code_dict = check_fcharset(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key)
        if code_string is not None:
            code_string, code_dict = check_fprq(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key)
        if code_string is not None:
            code_string, code_dict = check_panose(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key)
        if code_string is not None:
            code_string, code_dict = check_fname(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key)
        if code_string is not None:
            code_string, code_dict = check_altname(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key)
        if code_string is not None:
            code_string, code_dict = check_fontemb(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key, main_dict=main_dict, deck=deck)
        if code_string is not None:
            code_string, code_dict = check_fontname_tagged(
                code_string=code_string, code_dict=code_dict,
                current_key=current_key, index=index)
        if code_string is not None:
            check_cpg(code_string=code_string, code_dict=code_dict,
                      current_key=current_key)

            dict_updater.json_dict_updater(
                dict_name="font_table_file.json",
                dict_update=code_dict,
                main_dict=main_dict)
            code_dict = {}


def delete_themes(code_string: str) -> str:
    """ Starting with Microsoft Word 2007, Word introduced themes. Some
    font definitions may include theme names. However, the definitions
    also include related font information (e.g., font name). RtoX,
    ignores theme names. """
    theme_list = ["flomajor", "fhimajor", "fdbmajor", "fbimajor",
                  "flominor", "fhiminor", "fdbminor", "fbiminor"]
    for ele in theme_list:
        try:
            test = re.search(fr'\\{ele}', code_string)
            code_string = code_string.replace(test[0], "")
        except TypeError:
            pass
    return code_string


def check_fontnum(code_dict: dict, code_string: str) \
        -> Tuple[str, dict, str, int]:
    """ Each font code has a unique font number (e.g., fontnum = f0). """
    index = 1
    current_key = ""
    item = None
    try:
        test = re.search(r'\\f[0-9]+', code_string[1:])
        if test is not item:
            current_key = test[0].replace("\\", "")
            code_dict.update({current_key: {}})
            index = index + len(test[0])
    except TypeError as error:
        # TODO Check that the program continues even if it encounters
        #  this problem.
        msg = "The font table is missing a font number."
        log.debug(error, msg)
    return code_string, code_dict, current_key, index


def check_fontfamily(code_string: str, code_dict: dict,
                     current_key: str, index: int,
                     main_dict: dict) -> Tuple[str, dict, int]:
    """ Each font code may define its font family. """
    font_families_dict = os.path.join(main_dict["dicts_dir"],
                                      "font_families_dict.json")
    with open(font_families_dict) as ffd:
        font_families = json.load(ffd)
    item = None
    for key in font_families:
        test = re.search(r"\\"+key, code_string[index:])
        if test is not item:
            code_dict[current_key][key] = font_families[key]["sub"]
            value = str(test.end())
            font_families[key]["temp_index"] = value
        else:
            pass
    for key in font_families:
        if font_families[key]["temp_index"] == "":
            font_families[key]["temp_index"] = 0
        index = max(index, int(font_families[key]["temp_index"]))
    return code_string, code_dict, index


def check_fcharset(code_string: str, code_dict: dict,
                   current_key: str) -> Tuple[str, dict]:
    """ Each font code may define the character set it uses. """
    item = None
    try:
        test = re.search(r'\\fcharset([0-9])+', code_string)
        if test is not item:
            value = test[0].replace("\\fcharset", "")
            code_dict[current_key]["fcharset"] = value
        else:
            code_dict[current_key]["fcharset"] = 0
    except TypeError:
        code_dict[current_key]["fcharset"] = 0
    return code_string, code_dict


def check_fprq(code_string: str, code_dict: dict,
               current_key: str) -> Tuple[str, dict]:
    """ Each font code have a font pitch (default, fixed or variable). """
    item = None
    try:
        test = re.search(r'\\fprq([0-9])+', code_string)
        if test is not item:
            value = test[0].replace("\\fprq", "")
            code_dict[current_key]["fprq"] = value
    except TypeError:
        code_dict[current_key]["fprq"] = 0
    return code_string, code_dict


def check_panose(code_string: str, code_dict: dict,
                 current_key: str) -> Tuple[str, dict]:
    """ If present, panose contains a 10-byte Panose 1 number. """
    item = None
    try:
        test = re.search(r'{\\\*\\panose\s[0-9a-zA-Z]+}', code_string)
        if test is not item:
            result = test[0].replace("{\\*\\panose ", "").replace("}", "")
            code_dict[current_key]["panose"] = result
    except TypeError:
        code_dict[current_key]["panose"] = 0
    return code_string, code_dict


def check_fname(code_string: str, code_dict: dict, current_key: str
                ) -> Tuple[str, dict]:
    """ Each code may have a non-tagged name. RtoX ignores this control word."""
    item = None
    try:
        test = re.search(r'(\}|\s)[a-zA-Z\s\(\);]+', code_string)
        if test is not item:
            result = test[0].replace("}", "").replace(";", "")
            code_dict[current_key]["fname"] = result
    except TypeError:
        code_dict[current_key]["fname"] = "None"
    return code_string, code_dict


def check_altname(code_string: str, code_dict: dict,
                  current_key: str) -> Tuple[str, dict]:
    """ Each font code may use an alternative name. """
    item = None
    try:
        test = re.search(r'\{\\\*\\falt\s[\s\'0-9A-Za-z]+\}', code_string)
        if test is not item:
            result = test[0][:-1].replace(r"{\*\falt ", "")
            code_dict[current_key]["altname"] = result
    except TypeError:
        code_dict[current_key]["altname"] = "None"
    return code_string, code_dict


def check_fontemb(code_string: str, code_dict: dict,
                  current_key: str, main_dict: dict,
                  deck: Any) -> Tuple[str, dict]:
    """ Each code may contain an embedded font, which RtoX ignores. """
    item = None
    try:
        test = re.search(r'{\\\*\\fontemb', code_string)
        if test is not item:
            main_dict = find_group_end.processor(main_dict=main_dict, deck=deck)
            code_dict[current_key]["fontemb"] = main_dict["group_contents"]
            code_string = code_string.replace(
                main_dict["group_contents"], "")
    except TypeError:
        code_dict[current_key]["fontemb"] = False
    return code_string, code_dict


def check_fontname_tagged(code_string: str, code_dict: dict,
                          current_key: str, index: int) -> Tuple[str, dict]:
    """ A tagged fontname means that the "bytes in runs tagged with the
    associated\\fN are character codes in the codepage corresponding to
    the charset N. If \\cpgN appears, it supersedes the codepage given by
    \\fcharsetN. """
    item = None
    try:
        test = re.search(r"[\w|\s()\-]+", code_string[index:])
        if test is not item:
            result = test[0].lstrip()
            code_dict[current_key]["fontname"] = result
        else:
            code_string = check_fontname_nontagged(code_string=code_string)
    except TypeError:
        code_dict[current_key]["fontname"] = None
    return code_string, code_dict


def check_fontname_nontagged(code_string: str) -> str:
    return code_string


def check_cpg(code_string: str, code_dict: dict,
              current_key: str) -> Tuple[str, dict]:
    """ Each font code may use a specified code page (e.g. Microsoft 1252).
    """
    item = None
    try:
        test = re.search(r'{\\cpg([0-9])+', code_string)
        if test is not item:
            value = "".join([i for i in test[0] if i.isdigit()])
            code_dict[current_key]["cpg"] = value
        else:
            code_dict[current_key]["cpg"] = "0"
    except (KeyError, TypeError):
        code_dict[current_key]["cpg"] = "0"
    return code_string, code_dict
