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


def process_stylesheet(code_strings_to_process: list, main_dict: dict):
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
    code_strings_to_process = _trim_stylesheet(
        code_strings_to_process=code_strings_to_process)
    
    code_strings_to_process = _update_code_strings(
        code_strings_to_process=code_strings_to_process)
    
    _parse_code_strings(
        code_strings_to_process=code_strings_to_process,
        main_dict=main_dict)


def _trim_stylesheet(code_strings_to_process: list) -> list:
    for code_string in code_strings_to_process:
        if re.search(r'{\\stylesheet', code_string) is not None:
            place = code_strings_to_process.index(code_string)
            new_code_string = code_string.replace("{\\stylesheet{", "{\\s0")
            code_strings_to_process[place] = new_code_string
        else:
            pass
    return code_strings_to_process


def _update_code_strings(code_strings_to_process: list) -> list:
    for code_string in code_strings_to_process:
        # Change \*\cs to \cs and \*\ts to \ts.
        item = None
        test = re.search(r"^{\\\*\\", code_string)
        if test is not item:
            new_code_string = code_string.replace("\\*\\", "\\")
            code_strings_to_process[
                code_strings_to_process.index(code_string)] = \
                new_code_string
        else:
            pass
    return code_strings_to_process


def _parse_code_strings(code_strings_to_process: list, main_dict: dict) -> None:
    code_dict = {}
    for code_string in code_strings_to_process:
        code_string = code_string[1:-1]
        code_string, current_key = _check_stylecode(code_string=code_string,
                                                    code_dict=code_dict)
        item = None
        test = re.search(r"\\", code_string)
        while test is not item:
            code_string, current_key = _check_control_words(
                code_string=code_string, current_key=current_key,
                code_dict=code_dict)
            test = re.search(r"\\", code_string)
        _check_style_name(code_string=code_string, current_key=current_key,
                          code_dict=code_dict)

        dict_updater.json_dict_updater(
            dict_name="style_sheet_table_file.json",
            dict_update=code_dict,
            main_dict=main_dict)

        code_dict = {}


def _check_stylecode(code_string: str, code_dict: dict) -> tuple:
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
                code_dict.update({current_key: {"style_name": ""}})
                code_string = code_string.replace(test[0], "")
            else:
                pass
        except (ValueError, TypeError) as error:
            logging.exception(error, "A style does not have a style code.")
            pass
    return code_string, current_key


def _check_control_words(code_string: str, current_key: str,
                         code_dict: dict) -> tuple:
    item = None
    try:
        code_string = code_string.lstrip()
        test = re.search(r"^(\\[a-zA-Z]*[\-0-9]*)", code_string)
        if test is not item:
            test_clean = test[0].rstrip()
            control_word = "".join([i for i in test_clean if i.isalpha()])
            control_word_value = "".join(
                [i for i in test_clean if i.isdigit()])
            code_dict[current_key][control_word] = \
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


def _check_style_name(code_string: str, current_key: str,
                      code_dict: dict) -> None:
    """ Each style has a name, indicating where the style is used. """
    item = None
    code_string = code_string.lstrip()
    try:
        test = re.search(r'^([a-zA-Z\-\s()+0-9]*)', code_string)
        if test is not item:
            result = test[0].rstrip()
            code_dict[current_key]["style_name"] = result.lstrip()
        else:
            code_dict[current_key]["style_name"] = "None"
    except KeyError:
        logging.exception(msg="A style sheet KeyError occurred while "
                              f"processing code_string: {code_string}")
