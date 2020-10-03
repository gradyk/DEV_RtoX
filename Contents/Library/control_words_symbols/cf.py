#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import json
import os


def cw_cb(tag_set: int, value: int, debug_dir) -> tuple:
    color_table_file = os.path.join(debug_dir, "color_table_file.json")
    with open(color_table_file, "r+") as color_table_pre:
        color_table = json.load(color_table_pre)
    red = color_table[value]["red"]
    green = color_table[value]["green"]
    blue = color_table[value]["blue"]
    tag_list = {
        "open":
            ['',
             '<ts:colorVals',
             '',
             ''
            ],
        "close":
            ['',
             '</ts:colorVals>',
             '',
             ''
            ]
    }
    tag_elements = [tag_list["open"][tag_set], f'what="foreground',
                    f'red="{red}"', f'green="{green}"', f'blue="{blue}"']
    open_tag = ''.join(tag_elements)
    close_tag = tag_list["close"][tag_set]
    return open_tag, close_tag
