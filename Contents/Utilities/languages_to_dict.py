import csv
import json
import os
import sys


def languages_to_dict():
    base_script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    language_source = os.path.join(base_script_dir, "languages.csv")
    language_dict = os.path.join(base_script_dir, "language_dict.json")
    lang_new = {}
    with open(language_dict, "w+") as language_dict_pre:
        with open(language_source) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                lang_new.update({row[0]: [row[1], row[2]]})
                language_dict_pre.seek(0)
                json.dump(lang_new, language_dict_pre, indent=4)
                line_count += 1


if __name__ == "__main__":
    languages_to_dict()
