#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import datetime
import json
import os
import sys


def open_processor():
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    time_tracker_file = os.path.join(dicts_dir, "time_tracker.json")
    d = {"begin_time": "", "end_time": ""}
    with open(time_tracker_file, "w+") as time_tracker_file_pre:
        json.dump(d, time_tracker_file_pre)
    d["begin_time"] = datetime.datetime.now()
    with open(time_tracker_file, "w+") as time_tracker_pre:
        json.dump(d, time_tracker_pre, default=myconverter)


def close_processor():
    close_time = datetime.datetime.now()
    base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    dicts_dir = os.path.join(base_dir, "Library/dicts")
    time_tracker_file = os.path.join(dicts_dir, "time_tracker.json")
    with open(time_tracker_file) as time_tracker_pre:
        d = json.load(time_tracker_pre)
    d["end_time"] = close_time
    with open(time_tracker_file, "r+") as time_tracker_pre:
        json.dump(d, time_tracker_pre, default=myconverter)
    print(f"Time to process file: \n"
          f"  Begin: {d['begin_time']}\n"
          f"  End:   {d['end_time']}")
    sys.exit(0)


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()