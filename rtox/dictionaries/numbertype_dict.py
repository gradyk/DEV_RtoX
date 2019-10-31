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

number_type_dict = {
    0:    'Arabic',
    1:    'uppercase Roman numeral',
    2:    'lowercase Roman numeral',
    3:    'uppercase letter',
    4:    'lowercase letter',
    5:    'ordinal number',
    6:    'cardinal text number',
    7:    'ordinal text number',
    10:   'Kanji numbering without the digit character',
    11:   'Kanji numbering with the digit character',
    1246: 'phonetic Katakana characters in aiueo order',
    1346: 'phonetic katakana characters in iroha order',
    14:   'double byte character',
    15:   'single byte character',
    16:   'Kanji numbering 3',
    17:   'Kanji numbering 4',
    18:   'Circle numbering',
    19:   'double-byte Arabic numbering',
    2046: 'phonetic double-byte Katakana characters',
    2146: 'phonetic double-byte katakana characters',
    22:   'Arabic with leading zero',
    23:   'bullet',
    24:   'Korean numbering 2',
    25:   'Korean numbering 1',
    26:   'Chinese numbering 1',
    27:   'Chinese numbering 2',
    28:   'Chinese numbering 3',
    29:   'Chinese numbering 4',
    30:   'Chinese Zodiac numbering 1',
    31:   'Chinese Zodiac numbering 2',
    32:   'Chinese Zodiac numbering 3',
    33:   'Taiwanese double-byte numbering 1',
    34:   'Taiwanese double-byte numbering 2',
    35:   'Taiwanese double-byte numbering 3',
    36:   'Taiwanese double-byte numbering 4',
    37:   'Chinese double-byte numbering 1',
    38:   'Chinese double-byte numbering 2',
    39:   'Chinese double-byte numbering 3',
    40:   'Chinese double-byte numbering 4',
    41:   'Korean double-byte numbering 1',
    42:   'Korean double-byte numbering 2',
    43:   'Korean double-byte numbering 3',
    44:   'Korean double-byte numbering 4',
    45:   'Hebrew non-standard decimal',
    46:   'Arabic Alif Ba Tah',
    47:   'Hebrew Biblical standard',
    48:   'Arabic Abjad style',
    255:  'No number',
}