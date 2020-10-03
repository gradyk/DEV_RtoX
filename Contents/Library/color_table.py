#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Process the RTF file color table. The current version of RtoX notes the
existence of the table in the codes dictionary, but does not parse the table.
"""

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


class ColortblParse(object):
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
    def __init__(self, code_strings_to_process: list, main_dict: dict) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.main_dict = main_dict

    def trim_colortbl(self):
        for code_string in self.code_strings_to_process:
            item = None
            test = re.search(r"^{\\colortbl;", code_string)
            if test is not item:
                place = self.code_strings_to_process.index(code_string)
                new_code_string = code_string[:-2].replace("{\\colortbl;", "")
                self.code_strings_to_process[place] = new_code_string
            else:
                pass

    def parse_code_strings_to_process(self) -> list:
        code_string_list = []
        for string in self.code_strings_to_process:
            code_string_list = string.split(";")
        return code_string_list

    def parse_code_strings(self, code_string_list: list):
        code_dict = {}
        count = len(code_string_list)
        keys = [*range(0, count, 1)]
        place = 0
        for code_string in code_string_list:
            code_dict, current_key = ColorParser.assign_key(
                code_dict=code_dict,
                keys=keys, place=place)
            code_dict = ColorParser.parse_control_word(
                code_string=code_string,
                current_key=current_key, code_dict=code_dict)
            code_dict = ColorParser.parse_theme_control_word(
                code_string=code_string,
                current_key=current_key, code_dict=code_dict)

            dict_updater.json_dict_updater(dict_name="color_table_file.json",
                                           dict_update=code_dict,
                                           main_dict=self.main_dict)

            place += 1
            code_dict = {}


class ColorParser(object):
    def __init__(self, code_dict: dict) -> None:
        self.code_dict = code_dict

    @staticmethod
    def assign_key(code_dict: dict, keys: list, place: int) -> tuple:
        current_key = keys[place]
        code_dict.update({current_key: {}})
        return code_dict, current_key

    @staticmethod
    def parse_control_word(code_string: str, current_key: int,
                           code_dict: dict) -> dict:
        control_word_list = [
            "red",
            "green",
            "blue",
            "ctint",
            "cshade"
        ]

        for cw in control_word_list:
            item = None
            try:
                test = re.search(r"(\\)" + f"{cw}" + r"[0-9]*", code_string)
                if test is not item:
                    value = test[0].replace(f"\\{cw}", "")
                    code_dict[current_key][f"{cw}"] = value
                    code_string = code_string.replace(test[0], "")
                else:
                    pass
            except ValueError:
                pass
        return code_dict

    @staticmethod
    def parse_theme_control_word(code_string: str, current_key: int,
                                 code_dict: dict) -> dict:
        control_word_list = [
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

        for cw in control_word_list:
            item = None
            try:
                test = re.search(r"(\\)" + f"{cw}" + r"[0-9]*", code_string)
                if test is not item:
                    value = test[0].replace(f"\\{cw}", "")
                    code_dict[current_key][f"{cw}"] = value
                    code_string = code_string.replace(test[0], "")
                else:
                    pass
            except ValueError:
                pass
        return code_dict
