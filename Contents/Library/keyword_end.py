#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#
#
#
"""
Find keyword closing }. Note-this test only works where the closing bracket
is of the form: }
                }
and both brackets are at the beginning of their respective lines. Suitable
keywords: par, pard, sect, sectd, header, footnote.
"""

# From standard library
import linecache
import re


def keyword_end(working_file: str,
                line_number: str
                ) -> str:

    close_test = 0
    keyword_close = line_number

    while close_test == 0:
        search_area = linecache.getline(working_file,
                                        line_number)
        search_area_plus = linecache.getline(working_file,
                                             int(line_number) + 1)

        test_close_bracket = re.search("}", search_area[0]) and \
            re.match("}", search_area_plus[0])
        if test_close_bracket is not None:
            keyword_close = line_number
            close_test = 1
        else:
            line_number += 1

    return keyword_close
