import csv
import json
import os
import sys


def cw_csv_builder():
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))
    control_word_csv = os.path.join(base_script_dir, "control_words.txt")

    cw_dict_file = os.path.join(base_script_dir,
                                "../Library/dicts/control_word_dict.json")

    with open(cw_dict_file, "r+") as cw_dict_pre:
        cw_dict = json.load(cw_dict_pre)

        with open(control_word_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    key = f'{row[0]}'
                    if key[-1] == "N":
                        key = key.rstrip("N")
                    else:
                        pass
                    val1 = f'{row[1]}'
                    val2 = f'{row[2]}'
                    val3 = "null"
                    something = {key: [val1, val2, val3]}
                    cw_dict.update(something)
                    cw_dict_pre.seek(0)
                    json.dump(cw_dict, cw_dict_pre, indent=4)
                    line_count += 1


if __name__ == "__main__":
    cw_csv_builder()
