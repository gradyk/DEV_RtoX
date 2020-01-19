#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  Copyright (c) 2020. Kenneth A. Grady
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
https://stackoverflow.com/questions/35761133/python-how-to-check-for-open-and-close-tags
"""


__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-12"
__name__ = "tag_closer"

# From standard libraries
import os


class TagCloser:
    def __init__(self,
                 debug_dir: str,
                 ):
        self.debug_dir = debug_dir

    def tag_closer(self):

        stack = []

        with open(os.path.join(self.debug_dir, "working_xml_file.xml"),
                               'r') as parse_file:
            for line in parse_file:
                print("INPUT LINE:", line)
                ltag = line.find('<')
                if ltag > -1:
                    rtag = line.find('>')
                    if rtag > -1:
                        # Found left and right brackets: grab tag
                        tag = line[ltag+1: rtag]
                        open_tag = tag[0] != '/'
                        if open_tag:
                            # Add tag to stack
                            stack.append(tag)
                            print("TRACE open", stack)
                        else:
                            tag = tag[1:]
                            if len(stack) == 0:
                                print("No blocks are open; tried to close", tag)
                            else:
                                if stack[-1] == tag:
                                    # Close the block
                                    stack.pop()
                                    print("TRACE close", tag, stack)
                                else:
                                    print("Tried to close", tag,
                                          "but most recent open "
                                          "block is", stack[0])
                                    if tag in stack:
                                        stack.remove(tag)
                                        print("Prior block closed; continuing")

        if len(stack):
            print("Blocks still open at EOF:", stack)
