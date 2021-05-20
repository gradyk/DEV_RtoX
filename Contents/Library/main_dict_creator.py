#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" RtoX uses the main dict to pass variables among modules when parsing the
body of the RTF document. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2019-12-21"
__name__ = "Contents.Library.main_dict_creator"


def mdc_processor(base_dir, debug_dir: str, dicts_dir: str,
                  main_script: str, config_ini: str) -> dict:
    main_dict = {
        "contents_list":            [],
        "contents_string":          "",
        "cw_regex":                 "",
        "group_contents":           "",
        "group_end_index":          0,
        "group_end_line":           0,
        "group_counter":            0,
        "group_log":                {},
        "line_to_parse":            "",
        "list_size":                "",
        "parse_index":              "",
        "parse_text":               "",
        "group_start_index":        "",
        "group_start_line":         "",
        "tag_set":                  "",
        "base_dir":                 base_dir,
        "debug_dir":                debug_dir,
        "dicts_dir":                dicts_dir,
        "main_script":              main_script,
        "config_ini":               config_ini,
        "input_file":               "",  # Name of the RTF file
        "working_file_name":        "",  # Path + name of the working
                                         # input file
        "working_input_file":       "",  # Text of input file line by line
                                         # accessible
        "working_input_file_bak":   "",  # Backup for working_input_file
        "output_file":              "",  # Name of output file
        "output_file_name":         "",  # Path + name of the final XML file
        "output_text":              "",  # Location where new XML text is
                                         # stored during processing
        "output_text_bak":          "",  # Used while formatting
                                         # tempt_output_text
        "i":                        "close",
        "b":                        "close",
        "ul":                       "close",
        "strike":                   "close",
        "scaps":                    "close",
        "footnote":                 "close",
        "header":                   "close",
        "section":                  "open",
        "par":                      "open",
        "body":                     "open",
        "bodytext":                 "open",
        "wrapper":                  "open",
        "pard":                     "close",
        "intbl":                    "close",
        "itap":                     "close",
        "level":                    "close",
        "noline":                   "close",
        "outlinelevel":             "close",
        "sbys":                     "close",
        "s":                        "close"
        }
    return main_dict
