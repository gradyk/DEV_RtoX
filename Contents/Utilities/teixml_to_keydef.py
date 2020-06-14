import csv
import os
import sys


def tei_to_tpres_keydefs():
    base_script_dir = os.path.dirname(os.path.abspath(
        sys.argv[0]))
    all_types = os.path.join(base_script_dir,
                             "TEICombinedList.csv")

    combined_file = os.path.join(base_script_dir,
                                 "combined_tpres.txt")

    with open(combined_file, "w") as combined_file_pre:
        with open(all_types) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if row[2] == "Element":
                    something = f'\t<keydef keys="{row[1]}" ' \
                                f'href="Topics/el-{row[1]}.dita" ' \
                                f'format="dita"/>\n'
                    combined_file_pre.write(something)
                    line_count += 1
                elif row[2] == "Datatype":
                    something = f'\t<keydef keys="{row[1]}" ' \
                                f'href="Topics/dt-{row[1]}.dita" ' \
                                f'format="dita"/>\n'
                    combined_file_pre.write(something)
                    line_count += 1
                elif row[2] == "Macro":
                    something = f'\t<keydef keys="{row[1]}" ' \
                                f'href="Topics/macro-{row[1]}.dita" ' \
                                f'format="dita"/>\n'
                    combined_file_pre.write(something)
                    line_count += 1
                elif row[2] == "Class":
                    something = f'\t<keydef keys="{row[1]}" ' \
                                f'href="Topics/at-{row[1]}.dita" ' \
                                f'format="dita"/>\n'
                    combined_file_pre.write(something)
                    line_count += 1
                    
                elif row[2] == "Model":
                    something = f'\t<keydef keys="{row[1]}" ' \
                                f'href="Topics/model-{row[1]}.dita" ' \
                                f'format="dita"/>\n'
                    combined_file_pre.write(something)
                    line_count += 1

    # Need to do cleanup (remove extra text, dots to dashes, etc.)
    with open(combined_file) as combined_file_pre:
        combined_file = combined_file_pre.read()
        combined_file = combined_file.replace(".", "-")
        combined_file = combined_file.replace("model-model-", "model-")
        combined_file = combined_file.replace("dt-tsdata-", "dt-")
        combined_file = combined_file.replace("-dita", ".dita")
        combined_file = combined_file.replace("-attributes.dita", ".dita")

        print(combined_file)


if __name__ == "__main__":
    tei_to_tpres_keydefs()
