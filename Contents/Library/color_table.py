#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Process the RTF file color table. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "Contents.Library.color_table"

# From standard libraries
import re

# From local application
import dict_updater

""" An RTF file uses the following structure for a colortbl (if present):
<colortbl>      '{' \\colortbl <colordef>+ '}'
<colordef>      <themecolor>? & \\ctintN? & \\cshadeN? & \\redN? &
                \\greenN? & \\blueN? ';'
<themecolor>    \\cmaindarkone | \\cmainlightone | \\cmaindarktwo |
                \\cmainlighttwo | \\caccentone | \\caccenttwo |
                \\caccentthree | \\caccentfour | \\caccentfive |
                \\caccentsix | \\chyperlink | \\cfollowedhyperlink |
                \\cbackgroundone | \\ctextone | \\cbackgroundtwo |
                \\ctexttwo
"""


def trim_colortbl(code_strings) -> iter:
    """
        RTF wraps the color table with {\\colortbl ... }. This function
    removes the prefix.
    """
    def _replace_tbl(rbg_string):
        return rbg_string.replace("{\\colortbl;", "") or rbg_string
    return map(_replace_tbl, code_strings)


def split_code_strings(code_strings_list: iter) -> iter:
    """
        An RTF color table includes rbg tuples which may be preceded by a
        control word. This function splits the table where each prefix + rbg
        tuple constitutes one string.
    """
    code_strings_list = [string.split(";") for string in code_strings_list]

    def _remove_bracket(working_list):
        """ Remove the trailing bracket from the color table
        wrapper, if present. """
        working_list = [x for x in working_list if x != "}"]
        return working_list
    return map(_remove_bracket, code_strings_list)


def parse_code_strings(code_strings_list: iter, main_dict: dict) -> None:
    """ Parse each color table string. """
    code_dict = {}
    cs_list = list(code_strings_list)[0]

    for code_string in cs_list:
        key = cs_list.index(code_string)
        code_dict.update({key: {}})
        code_dict = parse_control_word(
            code_string=code_string, code_dict=code_dict, key=key)
        code_dict = parse_theme_control_word(
            code_string=code_string, code_dict=code_dict, key=key)

        dict_updater.json_dict_updater(dict_name="color_table_file.json",
                                       dict_update=code_dict,
                                       main_dict=main_dict)

        code_dict = {}


def parse_control_word(code_string: str, code_dict: dict, key: str) -> dict:
    """ Parse the rgb portion of strings. """
    rgb_list = ["red", "green", "blue", "ctint", "cshade"]
    rgb_dict = {k: _color_vals(code_string, k) for k in rgb_list}
    code_dict[key].update(rgb_dict)
    return code_dict


def _color_vals(code_string, k) -> str:
    color = re.search(rf"\\{k}[0-9]*", code_string) or None
    if color is None:
        return "None"
    else:
        return color[0].replace(f"\\{k}", "")


def parse_theme_control_word(code_string: str, code_dict: dict,
                             key: str) -> dict:
    """ This function parses the rgb control word prefixes. """
    theme_list = [
        "cmaindarkone",
        "cmainlightone",
        "cmaindarktwo",
        "cmainlighttwo",
        "caccentone",
        "caccenttwo",
        "caccentthree",
        "caccentfour",
        "caccentfive",
        "caccentsix",
        "chyperlink",
        "cfollowedhyperlink",
        "cbackgroundone",
        "ctextone",
        "cbackgroundtwo",
        "ctexttwo"
    ]
    for theme in theme_list:
        result = re.search(rf"\\{theme}", code_string)
        if result is not None:
            code_dict[key][theme] = "True"
        else:
            code_dict[key][theme] = "False"
    return code_dict
