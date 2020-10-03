#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

#  !/usr/bin/env python3
#   -*- coding: utf-8 -*-
#
#
#  This file is part of RtoX.
#
#  RtoX is free software: you can redistribute it and / or modify it under
#  the terms of the GNU General Public License as published by the Free
#  Software Foundation, either version 3 of the License, or (at your option)
#  any later version.
#
#  RtoX is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE. See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along
#  with RtoX. If not, see < https://www.gnu.org / licenses / >.

""" Headers and footers have the following format;
    <hdrftr>        '{' <hdrctl> <pap>+ '}' <hdrftr>?
    <hdrctl>        \\header | \\footer | \\headerderl | \\headerr |
                    \\headerf | \\footer | \\footerr | \\footerf
"""

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.footer_cwd"

footer_cwd_list = {  # Spec Page 45
    "\\footer": ["Coded", "Footer on all pages.", "Destination"],
    "\\footerl": ["Coded","Footer on left pages only.", "Destination"],
    "\\footerr": ["Coded", "Footer on right pages only.", "Destination"],
    "\\footerf": ["Coded", "Footer on first page only.", "Destination"]
}

