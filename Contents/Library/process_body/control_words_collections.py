#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-9-22"
__name__ = "Contents.Library.process_body.control_words_collections"


# From standard libraries
import csv
import os
from pathlib import Path


def processor():
    # TODO Need a func to check csv for duplicates and remove them. Also,
    #  should check for and remove incomplete entries (e.g., name,,,) which
    #  would cause problems.
    collection_dict = dict()
    util_dir = Path.cwd()
    control_word_csv = os.path.join(util_dir,
                                    "Utilities/control_words_collections.csv")
    with open(control_word_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                # ctw=row[0], typ=row[1], cat=row[2], fnc=row[3]
                entry = {f'{row[0]}': f'{row[3]}'}
                if entry == {}:
                    pass
                else:
                    collection_dict.update(entry)

    return collection_dict
