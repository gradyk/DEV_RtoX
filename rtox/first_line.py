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
Process the first line of the RTF file, capturing codes.
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-11-10"
__name__ = "first_line"

import linecache
import os
import re
import sys
from log_config import logger


class FirstLine:
    """
    Process Header first line settings.
    """

    def __init__(
                 self,
                 working_file,
                 debug_dir,
                 base_script_dir
                 ):
        self.__working_file = working_file
        self.__debug_dir = debug_dir
        self.__base_script_dir = base_script_dir

    def line_parse(self):
        """
        Parse first line of input file with keywords:
        "rtf1", "ansi", "ansicpg1252", "uc1".
        Check for language keywords; check for style codes.
        """

        line_to_read = linecache.getline(self.__working_file, 1)
        rtf_file_codes = {}

        try:
            line_to_read.encode(encoding="us-ascii")
        except UnicodeEncodeError:
            logger.critical(msg="RTF file is not ASCII encoded. This "
                                "version of the program needs an ASCII "
                                "encoded file. RtoX will now quit.\n")
            sys.exit(1)

        # Check for opening bracket.
        if line_to_read[0] == "{":
            pass
        else:
            logger.critical(msg="Document does not start with '{'. "
                                "This version of RtoX cannot convert it to an "
                                "XML file. RtoX will now quit.")
            sys.exit(1)

        # Record keyword rtfN.
        pattern_rtf = re.search(r'rtf[0-9]+', line_to_read)
        if pattern_rtf:
            rtf_code = pattern_rtf[0].replace('rtf', "")
            rtf_file_codes.update({"rtf": rtf_code})
            pass
        else:
            logger.critical(msg="Document does not start with 'rtfN'. "
                                "This version of RtoX cannot convert it to an "
                                "XML file. RtoX will now quit.")
            sys.exit(1)

        # Check for keyword ansi.
        pattern_ansi = re.search(r'ansi', line_to_read)
        if pattern_ansi:
            rtf_code = pattern_ansi[0].replace('ansi', "")
            rtf_file_codes.update({"ansi": rtf_code})
            pass
        else:
            logger.critical(msg="Document does not use the ANSI "
                                "character set. This version of "
                                "RtoX does not handle "
                                "Macintosh (\\mac), IBM PC code page 437 "
                                "(\\pc), or IBM PC code page 850 (\\pca) "
                                "character sets. RtoX will "
                                "now quit.\n")
            sys.exit(1)

        # Check for keyword ansicpg1252.
        pattern_cpg = re.search(r'ansicpg1252', line_to_read)
        if pattern_cpg:
            rtf_code = pattern_cpg[0].replace("ansicpg", "")
            rtf_file_codes.update({"code_pg": rtf_code})
            pass
        else:
            logger.critical(msg="Document did not use ANSI code page 1252 "
                                "when writing the Unicode to ANSI "
                                "conversion. RtoX will now quit.")
            sys.exit(1)

        # Check for destination coding: \\upr, \\ud, \\ucN, \\uN.
        # Check for language keywords.
        pattern_upr = re.search(r'upr', line_to_read)
        if pattern_upr:
            logger.critical(msg="This version of RtoX does not support "
                                "conversion of mixed ANSI and Unicode "
                                "in RTF files. RtoX will now quit.\n")
            sys.exit(1)
        else:
            pass

        pattern_uc = re.search(r'uc[0-9]+', line_to_read)
        if pattern_uc[0]:
            rtf_code = pattern_uc[0].replace("uc", "")
            rtf_file_codes.update({"uc": rtf_code})
            pass
        else:
            logger.critical(msg="This version of RtoX does not support "
                                "ANSI characters without Unicode "
                                "equivalents. RtoX will now quit.\n")
            sys.exit(1)

        pattern_lang = re.search(r'deflang[0-9]+', line_to_read)
        if pattern_lang:
            rtf_code = pattern_lang[0].replace("deflang", "")
            rtf_file_codes.update({"deflang": rtf_code})
        else:
            pass

        pattern_alt_lang = re.search(r'adeflang[0-9]+', line_to_read)
        if pattern_alt_lang:
            rtf_code = pattern_alt_lang[0].replace("adeflang", "")
            rtf_file_codes.update({"adeflang": rtf_code})
        else:
            pass

        pattern_fe_lang = re.search(r'deflangfe[0-9]+', line_to_read)
        if pattern_fe_lang:
            rtf_code = pattern_fe_lang[0].replace(
                "deflangfe", "")
            rtf_file_codes.update({"deflangfe": rtf_code})
        else:
            pass

        pattern_lang_code = re.search(r'deff[0-9]+', line_to_read)
        if pattern_lang_code:
            rtf_code = pattern_lang_code[0].replace("deff", "")
            rtf_file_codes.update({"deff": rtf_code})
        else:
            pass

        # Set default fonts.
        pattern_ea_default = re.search(r'stshfdbch[0-9]+', line_to_read)
        if pattern_ea_default:
            rtf_code = pattern_ea_default[0].replace("stshfdbch", "")
            rtf_file_codes.update({"stshfdbch": rtf_code})
        else:
            pass

        pattern_ascii_default = re.search(r'stshfloch[0-9]+', line_to_read)
        if pattern_ascii_default:
            rtf_code = pattern_ascii_default[0].replace("stshfloch", "")
            rtf_file_codes.update({"stshfloch": rtf_code})
        else:
            pass

        pattern_highansi_default = re.search(r'stshfhich[0-9]+', line_to_read)
        if pattern_highansi_default:
            rtf_code = pattern_highansi_default[0].replace("stshfhich", "")
            rtf_file_codes.update({"stshfhich": rtf_code})
        else:
            pass

        pattern_bidi_default = re.search(r'stshfbi', line_to_read)
        if pattern_bidi_default:
            rtf_code = pattern_bidi_default[0].replace("stshfbi", "")
            rtf_file_codes.update({"stshfbi": rtf_code})
        else:
            pass

        match = re.compile(r'[a-z]+deflang[a-z]+')
        pattern_other_lang = re.search(match, line_to_read)
        if pattern_other_lang:
            rtf_code = pattern_other_lang[0].replace(str(match), "")
            rtf_file_codes.update({'other_lang': rtf_code})
        else:
            pass
