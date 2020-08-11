def cw_i(selector: int):
    tag_list = {
        1: "",
        2: '<ts:hiText rend="italic">',
        3: '',
        4: ""
    }
    return tag_list[selector]
