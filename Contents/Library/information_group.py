#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""
Each RTF file, after the header section, may have an "info" section that
captures metadata about the document. This module controls the processing of
the "info" section.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-29"
__name__ = "Contents.Library.docinfo_read"

# From standard libraries
import re

# From local applications
import dict_updater


class InfoGrpParse(object):
    """ An RTF file uses the following basic structure for an information group:
    <info>       '{' \\info <title>? & <subject>? & <author>? &
                     <manager>? & <company>? & <operator>? &
                     <<category>? & <keywords>? & <comment>? & \\version? &
                     <doccomm>? & \\vern? & <creatim>? & <revtim>? &
                     <printim>? & <buptim>? & \\edmins? & \\nofpages? &
                     \\nofwords? \\nofchars? & \\id? '}'
    <title>      '{' \\title #PCDATA '}'
    <subject>    '{" \\subject #PCDATA '}'
    <author>     '{' \\author #PCDATA '}'
    <manager>    '{' \\manager #PCDATA '}'
    <company>    "[" \\company #PCDATA '}'
    <operator>   '{' \\operator #PCDATA '}'
    <category>   '{' \\category #PCDATA '}'
    <keywords>   '{' \\keywords #PCDATA '}'
    <comment>    '{' \\comment #PCDATA '}'
    <doccomm>    '{' \\doccomm #PCDATA '}'
    <hlinkbase>  '{' \\hlinkbase #PCDATA '}'
    <creatim>    '{' \\creatim <time> '}'
    <revtim>     '{' \\revtim <time> '}'
    <printim>    '{' \\printim <time> '}'
    <buptim>     '{' \\buptim <time> '}'
    <time>       \\yr? \\mo? \\dy? \\hr? \\min? \\sec?
    """

    # TODO Add \\userprops parsing (see p. 30 RTF Spec 2003).
    def __init__(self, main_dict: dict, code_strings_to_process: list) -> None:
        self.code_strings_to_process = code_strings_to_process
        self.main_dict = main_dict
        self.code_dict = {}

    def process_code_strings(self) -> None:

        for code_string in self.code_strings_to_process:

            GetInfoCodes.check_info_code(
                self=GetInfoCodes(main_dict=self.main_dict,
                                  code_string=code_string))

            GetInfoCodes.check_nofchars(
                self=GetInfoCodes(main_dict=self.main_dict,
                                  code_string=code_string))

            GetInfoCodes.check_stat_code(
                self=GetInfoCodes(main_dict=self.main_dict,
                                  code_string=code_string))

            GetInfoCodes.check_time_components(
                self=GetInfoCodes(main_dict=self.main_dict,
                                  code_string=code_string))


class GetInfoCodes(object):

    def __init__(self, main_dict: dict, code_string: str) -> None:
        self.code_string = code_string
        self.main_dict = main_dict
        self.code_dict = {}
        self.current_key = ""
        self.beg_index = 0
        self.end_index = 0

    def check_info_code(self):
        """ Parse each code string. """
        info_part_list = [
                "title",
                "subject",
                "author",
                "manager",
                "company",
                "operator",
                "category",
                "comment",
                "doccomm",
                "hlinkbase",
                "keywords"
            ]

        for info_part in info_part_list:
            pattern = rf"{info_part}"
            try:
                test = re.search(re.escape(pattern), self.code_string)
                if test is not None:
                    pattern = re.compile(r'\s(\w+|\s|\W)+')
                    info_text = re.search(pattern, self.code_string)
                    pre_result = info_text[0].lstrip()
                    self.code_dict.update({info_part: pre_result[:-1]})
                else:
                    pass
            except (ValueError, TypeError):
                pass

        dict_updater.json_dict_updater(dict_name="info_group_file.json",
                                       dict_update=self.code_dict,
                                       main_dict=self.main_dict)
        self.code_dict = {}

    def check_nofchars(self):
        test = re.search(fr'\\nofchars[0-9]+', self.code_string)
        if test is not None:
            value = int(test[0].replace('\\nofchars', ""))
            self.code_dict.update({"nofchars": value})
            dict_updater.json_dict_updater(dict_name="info_group_file.json",
                                           dict_update=self.code_dict,
                                           main_dict=self.main_dict)
        else:
            pass

        self.code_dict = {}

    def check_stat_code(self):
        stat_code_list = [
                "version",
                "edmins",
                "nofpages",
                "nofwords",
                "nofcharsws",
                "vern"
            ]

        for stat in stat_code_list:
            test = re.search(fr'\\{stat}[0-9]*', self.code_string)
            if test is not None:
                value = int(test[0].replace('\\'+stat, ""))
                self.code_dict.update({stat: value})
                dict_updater.json_dict_updater(dict_name="info_group_file.json",
                                               dict_update=self.code_dict,
                                               main_dict=self.main_dict)
            else:
                pass

        self.code_dict = {}

    def check_time_components(self):

        time_part_list = [
            "creatim",
            "revtim",
            "printim",
            "buptim"
        ]

        for time_part in time_part_list:

            test = re.search(time_part, self.code_string)
            if test is not None:
                time_data_list = ["yr", "mo", "dy", "hr", "min", "sec"]
                for ele in time_data_list:
                    pattern = re.compile(fr'{ele}[0-9]*')
                    measure = re.search(pattern, self.code_string)
                    if measure is not None:
                        value = int(measure[0].replace(ele, ""))
                        key = time_part + "_" + ele
                        self.code_dict.update({key: value})
                        dict_updater.json_dict_updater(
                            dict_name="info_group_file.json",
                            dict_update=self.code_dict,
                            main_dict=self.main_dict)
                    else:
                        pass
            else:
                pass

        self.code_dict = {}
