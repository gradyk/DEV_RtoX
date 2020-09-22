#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-9-22"
__name__ = "Contents.Library.process_body.control_word_collections"


# From standard libraries
import csv
import os
from pathlib import Path
from collections import defaultdict


def cw_dict(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def processor():
    util_dir = Path.cwd()
    control_word_csv = os.path.join(util_dir,
                                    "control_words_collections.csv")
    collectionlist = []
    with open(control_word_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # ctw=row[0], typ=row[1], cat=row[2], fnc=row[3]
                entry = (f'{row[0]}', f'{row[1]}', f'{row[2]}', f'{row[3]}')
                if entry == ():
                    pass
                else:
                    collectionlist.append(entry)

    collection_dict = defaultdict()
    for idx, (ctw, typ, cat, fnc) in enumerate(collectionlist):
        val = ctw, typ, cat, fnc
        collection_dict[(idx, ctw)] = val
        collection_dict[(idx, typ)] = val
        collection_dict[(idx, cat)] = val
        collection_dict[(idx, fnc)] = val

    return collection_dict


if __name__ == "Contents.Library.process_body.control_word_collections":
    cw_dict()