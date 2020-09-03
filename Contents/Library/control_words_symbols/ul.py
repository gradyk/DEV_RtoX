#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def tagger(processing_dict: dict, cw_value: str) -> tuple:
    # \ul turns on continuous underlining; \ul0 (or any other number) turns
    # off continuous underlining
    tag_set = processing_dict["tag_set"]
    if cw_value ==

    tag_list = {
        "open":
            ['',
             '<ts:hiText rend="caps">',
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

