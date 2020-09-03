#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def tagger(tag_set: int) -> tuple:
    # \b turns on bold; \b0 (or any other number) turns off bold
    tag_list = {
        "open":
            ['',
             '<ts:hiText rend="bold">',
             '',
             ''
            ],
        "close":
            ['',
             '</ts:hiText>',
             '',
             ''
            ]
    }
    open_tag = tag_list["open"][tag_set]
    close_tag = tag_list["close"][tag_set]
    return open_tag, close_tag
