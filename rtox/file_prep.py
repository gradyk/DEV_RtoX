#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2019. Kenneth A. Grady
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
Do some basic checking (e.g., is it really an RTF file) and configuration
prior to processing.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-10-26"
__name__ = "file_prep"

import os
import re
import sys
from rtox.dictionaries.language_dict import language_dict
from log_config import logger


class FilePrep:
    """
    Prepare file to process and do preliminary checks.
    """

    def __init__(
                 self,
                ):
        self.__init__()

    @staticmethod
    def check_file_rtf(working_rtf_file, debug_file_dir):
        """
        Check first lin of input file to see if it starts with keywords:
        "rtf1", "ansi", "ansicpg1252", "uc1".
        Then check for language keywords. Then check for style codes.
        """

        read_obj = open(working_rtf_file, "r")
        line_to_read = read_obj.readline()
        token = line_to_read.rstrip()
        rtf_file_codes = {}

        try:
            token.encode(encoding="us-ascii")
        except UnicodeEncodeError:
            logger.critical(msg="RTF file is not ASCII encoded. This "
                                "version of the program needs an ASCII "
                                "encoded file. The program will now "
                                "quit.\n")
            sys.exit(1)

        # Split line into tokens based on \.
        first_line_list = token.split("\\")
        fll_length = len(first_line_list)
        fll_index = 0

        # Check for opening bracket.
        if first_line_list[fll_index] == "{":
            fll_index += 1
            pass
        else:
            logger.critical(msg="Document does not start with '{'. "
                                "This version of the program will not "
                                "be able to convert it to an XML file. "
                                "The program will now exit.")
            sys.exit(1)

        # Check for keyword rtfN.
        pattern_rtf = re.compile(r'rtf[0-9]+')
        if pattern_rtf.match(first_line_list[fll_index]):
            fll_index += 1
            pass
        else:
            logger.critical(msg="Document does not start with 'rtfN'. "
                                "This version of the program will not "
                                "be able to convert it to an XML file. "
                                "The program will now exit.\n")
            sys.exit(1)

        # Check for keyword ansi.
        pattern_ansi = re.compile(r'ansi')
        if pattern_ansi.match(first_line_list[fll_index]):
            fll_index += 1
            pass
        else:
            logger.critical(msg="Document does not use the ANSI "
                                "character set. This version of "
                                "the program does not handle "
                                "Macintosh (\\mac), IBM PC code page 437 "
                                "(\\pc), IBM PC code page 850 (\\pca) "
                                "character sets. The program will "
                                "not be able to convert the file "
                                "to an XML file. The program will "
                                "now exit.\n")
            sys.exit(1)

        # Check for keyword ansicpg1252.
        pattern_cpg = re.compile(r'ansicpg1252')
        if pattern_cpg.match(first_line_list[fll_index]):
            fll_index += 1
            pass
        else:
            logger.critical(msg="Document did not use ANSI code page 1252 "
                                "when writing the Unicode to ANSI "
                                "conversion. This version of the program "
                                "does not handle other code page "
                                "conversions. The program will now exit.")
            sys.exit(1)

        # Check for destination coding: \\upr, \\ud, \\ucN, \\uN.
        # Check for language keywords.
        if fll_index <= fll_length:
            pattern_upr = re.compile(r'upr')
            if pattern_upr.match(first_line_list[fll_index]):
                logger.critical(msg="This version of RtoX does not support "
                                    "conversion of mixed ANSI and Unicode "
                                    "in RTF files. The program will now "
                                    "exit.\n")
                sys.exit(1)
            else:
                pass

        pattern_uc = re.compile(r'uc[0-9]+')
        if pattern_uc.match(first_line_list[fll_index]):
            fll_index += 1
            pass
        else:
            logger.critical(msg="This version of RtoX does not support "
                                "ANSI characters without Unicode "
                                "equivalents. The program will now "
                                "quit.\n")
            sys.exit(1)

        while fll_index < fll_length:

            pattern_lang = re.compile(r'deflang[0-9]+')
            if pattern_lang.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].replace("deflang", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            pattern_alt_lang = re.compile(r'adeflang[0-9]+')
            if pattern_alt_lang.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].replace("adeflang", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            pattern_fe_lang = re.compile(r'deflangfe[0-9]+')
            if pattern_fe_lang.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].replace(
                    "deflangfe", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            # pattern_other_lang = re.compile(r'[a-z]+deflang[a-z]+')
            # if pattern_other_lang.match(first_line_list[fll_index]):
            #     temp_key = first_line_list[fll_index].replace(____, "")
            #     lang_value = language_dict[temp_key]
            #     pkl_file = open('rtf_file_codes.pkl', 'rb')
            #     codesdict2 = pickle.load(pkl_file)
            #     codesdict2.update(temp_key=lang_value)
            #     pkl_file.close()
            #     pass
            # else:
            #     pass

            pattern_lang_code = re.compile(r'deff[0-9]+')
            if pattern_lang_code.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].replace("deff", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            # Set default fonts.
            pattern_ea_default = re.compile(r'stshfdbch[0-9]+')
            if pattern_ea_default.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].\
                    replace("stshfdbch", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            pattern_ascii_default = re.compile(r'stshfloch[0-9]+')
            if pattern_ascii_default.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].\
                    replace("stshfloch", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            pattern_highansi_default = re.compile(r'stshfhich[0-9]+')
            if pattern_highansi_default.match(first_line_list[fll_index]):
                temp_key = first_line_list[fll_index].\
                    replace("stshfhich", "")
                lang_value = language_dict[temp_key]
                rtf_file_codes.update({temp_key: lang_value})
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

            pattern_bidi_default = re.compile(r'stshfbi')
            if pattern_bidi_default.match(first_line_list[fll_index]):
                fll_index += 1
                if fll_index == fll_length:
                    return
                else:
                    pass
            else:
                pass

        with open(os.path.join(debug_file_dir, "rtf_file_codes.data"),
                  "w+") as rtf_dict:
            rtf_dict.write(str(rtf_file_codes))
            rtf_dict.close()

        return rtf_dict

    # def head_from_body(self, working_input_file):
    #     """
    #     Using the working_input_file.data, split the header section from the
    #     rest of the file.
    #     :param: working_input_file:
    #     :return:
    #     """
    #
    #     with open(working_input_file, "r") as read_object:
