import csv
import json
import os
import sys


def cw_csv_builder():
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))
    control_word_csv = os.path.join(base_script_dir,
                                    "control_words.txt")

    cw_info_dict_file = os.path.join(base_script_dir,
                                     "control_word_info_dict.json")
    cw_func_dict_file = os.path.join(base_script_dir,
                                     "control_word_func_dict.json")

    with open(cw_info_dict_file, "r") as cw_info_dict_pre:
        cw_dict = json.load(cw_info_dict_pre)
        with open(control_word_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    key = f'{row[0]}'
                    val1 = f'{row[1]}'
                    val2 = f'{row[2]}'
                    something = {key: [val1, val2]}
                    cw_dict.update(something)
                    line_count += 1

    with open(cw_info_dict_file, "w") as cw_info_dict_pre:
        json.dump(cw_dict, cw_info_dict_pre, ensure_ascii=False)

    with open(cw_func_dict_file, "r") as cw_func_dict_pre:
        cw_dict = json.load(cw_func_dict_pre)
        with open(control_word_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
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
                    cw_not_coded = None
                    something = {key: cw_not_coded}
                    cw_dict.update(something)
                    line_count += 1

    with open(cw_func_dict_file, "w") as cw_dict_pre:
        json.dump(cw_dict, cw_dict_pre, ensure_ascii=False)


if __name__ == "__main__":
    cw_csv_builder()
