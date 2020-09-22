#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-9-22"
__name__ = "Contents.Library.process_body.create_control_word_collections"


# From standard libraries
import csv
import json
import os
import sys
from pathlib import Path
from collections import defaultdict


def cw_dict(func):
    cache = dict()

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
                    key = f'{row[0]}'
                    val0 = f'{row[1]}'
                    val1 = f'{row[2]}'
                    val2 = f'{row[3]}'
                    entry = (key, val0, val1, val2)
                    if entry == ():
                        pass
                    else:
                        collectionlist.append(entry)

        collection_dict = dict()
        for idx, (sym, typ, cat, fnc) in enumerate(collectionlist):
            idx = str(idx)
            val = sym, typ, cat, fnc
            collection_dict[(idx, sym)] = val
            collection_dict[(idx, typ)] = val
            collection_dict[(idx, cat)] = val
            collection_dict[(idx, fnc)] = val

        return collection_dict

    return processor
