#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def tagger(processing_dict: dict, cw_value: str) -> tuple:
    # \i turns on italic; \i0 (or any other number) turns off italic
    # See Word2007RTFSpec9 Font (Character) Formatting Properties, p.130.
    tag_set = processing_dict["tag_set"]
    if cw_value ==

    tag_list = {
        "open":
            ['',
             '<ts:hiText rend="italic">',
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
