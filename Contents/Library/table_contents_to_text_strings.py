#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

def processor(table_boundaries: dict, working_input_file: list):
    # TODO PROBLEM: This doesn't work when everything in the group is on the
    #  same line. Need a solution for 1) everything on the same line, and 2)
    #  everything on 2 or more lines.
    table_start_line = table_boundaries[0]
    table_last_line = table_boundaries[2]
    controlword_line = table_start_line
    initial_string = working_input_file[controlword_line]
    string_to_slice = initial_string[table_boundaries[1]:]
    if table_start_line == table_last_line:
        text_to_process = working_input_file[controlword_line][
            table_boundaries[1]:table_boundaries[3]]
    else:
        controlword_line += 1
        while controlword_line < table_last_line:
            string_list = \
                [string_to_slice, working_input_file[controlword_line]]
            string_to_slice = ''.join(string_list)
            controlword_line += 1
        last_string = working_input_file[controlword_line]
        last_string = last_string[:table_boundaries[3]]
        text_list = [string_to_slice, last_string]
        text_to_process = ''.join(text_list)
    return text_to_process
