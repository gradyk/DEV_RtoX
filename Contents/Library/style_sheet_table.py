#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the stylesheet table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-04"
__name__ = "Contents.Library.style_sheet_table"

# From standard libraries
import logging
import re

# From local application
import dict_updater


class StyleSheetParse(object):
    """ An RTF file uses the following structure for a stylesheet (if present):
    <stylesheet>        '{' \\stylesheet <style>+ '}'
    <style>             '{' <styledef>?<keycode>? <formatting> <additivie>?
                            <based>? <next>? <autoupd>? <link>?
                            <stylename>?';''}'
    <styledef>          \\s |\\*\\cs | \\ds | \ts\tsrowd
    <keycode>           '{' \\keycode <keys> '}'
    <keys>              ( \\shift? & \\ctrl? & \alt?)
    <key>               \fn | #PCDATA
    <additive>          \additive
    <based>             \\sbasedon
    <next>              \\snext
    <autoupd>           \\sautoupd
    <hidden>            \\shidden
    <link>              \\slinkN
    <locked>            \\slocked
    <personal>          \\spersonal
    <compose>           \\scompose
    <reply>             \\sreply
    <formatting>        (<brdrder> | <parfmt> | <apoctl> | <tabdef> |
                        <shading> | <chrfmt>)+
    <styleid>           \\styrsidN
    <semihidden>        \\ssemihidden
    <stylename>         #PCDATA
    """
    def __init__(self, code_strings_to_process: list, main_dict: dict) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.main_dict = main_dict

    def trim_stylesheet(self) -> list:
        for code_string in self.code_strings_to_process:
            if re.search(r'{\\stylesheet', code_string) is not None:
                place = self.code_strings_to_process.index(code_string)
                new_code_string = code_string.replace("{\\stylesheet{", "{\\s0")
                self.code_strings_to_process[place] = new_code_string
            else:
                pass
        return self.code_strings_to_process

    def update_code_strings(self) -> list:
        for code_string in self.code_strings_to_process:
            # Change \*\cs to \cs and \*\ts to \ts.
            item = None
            test = re.search(r"^{\\\*\\", code_string)
            if test is not item:
                new_code_string = code_string.replace("\\*\\", "\\")
                self.code_strings_to_process[
                    self.code_strings_to_process.index(code_string)] = \
                    new_code_string
            else:
                pass
        return self.code_strings_to_process

    def parse_code_strings(self) -> None:
        code_dict = {}
        for code_string in self.code_strings_to_process:
            get_style_codes = StyleParser(code_dict=code_dict)
            code_string = code_string[1:-1]
            code_string, current_key = StyleParser.check_stylecode(
                self=get_style_codes, code_string=code_string)
            item = None
            test = re.search(r"\\", code_string)
            while test is not item:
                code_string, current_key = StyleParser.check_control_words(
                    self=StyleParser(code_dict=code_dict),
                    code_string=code_string, current_key=current_key)
                test = re.search(r"\\", code_string)
            StyleParser.check_style_name(
                self=get_style_codes, code_string=code_string,
                current_key=current_key)

            dict_updater.json_dict_updater(
                dict_name="style_sheet_table_file.json",
                dict_update=code_dict,
                main_dict=self.main_dict)

            code_dict = {}


class StyleParser(object):
    def __init__(self, code_dict: dict) -> None:
        self.code_dict = code_dict

    def check_stylecode(self, code_string: str) -> tuple:
        """ With the exception of the default style, each style has an
        identifying number. """
        current_key = ""
        code_styles = [
            "s",  # Paragraph style code
            "cs",  # Character style code
            "ds",  # Section style code
            'ts',  # Table style code
            "trowd",  # Table row (tables in RTF are contiguous paragraphs).
        ]

        for style in code_styles:
            item = None
            code_string = code_string.lstrip()
            try:
                test = re.search(rf"^\\{style}[0-9]*", code_string)
                if test is not item:
                    current_key = test[0].replace("\\", "")
                    self.code_dict.update({current_key: {"style_name": ""}})
                    code_string = code_string.replace(test[0], "")
                else:
                    pass
            except (ValueError, TypeError) as error:
                logging.exception(error, "A style does not have a style code.")
                pass
        return code_string, current_key

    def check_control_words(self, code_string: str, current_key: str) -> tuple:
        item = None
        try:
            code_string = code_string.lstrip()
            test = re.search(r"^(\\[a-zA-Z]*[\-0-9]*)", code_string)
            if test is not item:
                test_clean = test[0].rstrip()
                control_word = "".join([i for i in test_clean if i.isalpha()])
                control_word_value = "".join(
                    [i for i in test_clean if i.isdigit()])
                self.code_dict[current_key][control_word] = \
                    control_word_value
                code_string = code_string.replace(test_clean, "", 1)
                space_test = re.search(r"^ \\", code_string)
                if space_test is not item:
                    code_string = code_string.lstrip()
                else:
                    pass
            else:
                pass
        except (ValueError, TypeError) as error:
            logging.exception(error, "A style code word has created a problem.")
            pass
        return code_string, current_key

    def check_style_name(self, code_string: str, current_key: str) -> None:
        """ Each style has a name, indicating where the style is used. """
        item = None
        code_string = code_string.lstrip()
        test = re.search(r'^([a-zA-Z\-\s()+0-9]*)', code_string)
        if test is not item:
            result = test[0].rstrip()
            self.code_dict[current_key]["style_name"] = result.lstrip()
        else:
            self.code_dict[current_key]["style_name"] = "None"
