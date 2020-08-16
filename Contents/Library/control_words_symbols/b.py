def cw_b(tag_set: int) -> tuple:
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
