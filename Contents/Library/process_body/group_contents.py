#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-12"
__name__ = "Contents.Library.process_body.group_contents"

# From standard libraries
import re

# From local applications
import build_output_file
import control_word_to_build
import csv_modifier
import tag_insert_missing_cw


def gc_processor(main_dict: dict, collections_dict: dict) -> dict:
    # Temp setup for testing
    for ele in main_dict["contents_list"]:
        if ele == "{" or ele == "}":
            pass
        elif re.search(main_dict["cw_regex"], ele):
            cw_text = "".join([i for i in ele if i.isalpha()])
            cw_value = "".join([i for i in ele if i.isdigit()])
            null_function = "null"
            try:
                cw_func = collections_dict[cw_text]
                if cw_func != null_function:
                    tag_set = main_dict["tag_set"]
                    tag_info = {
                        "func":      cw_func,
                        "cw_text":   cw_text,
                        "cw_value":  cw_value,
                        "name":      cw_text,
                        "tag_open":  "",
                        "tag_close": "",
                        "tag_set":   tag_set
                    }
                    main_dict = control_word_to_build.cwtb_processor(
                        tag_info=tag_info, main_dict=main_dict)
                else:
                    pass
            except KeyError:
                # Add missing control word to control_words_collections.csv
                # file.
                collections_dict = csv_modifier.csvm_processor(
                    main_dict=main_dict, cw_text=cw_text,
                    collections_dict=collections_dict)
                # Add control word that cannot be processed to XML build
                # file.
                tag_insert_missing_cw.ti_processor(main_dict=main_dict,
                                                   cw_text=cw_text)
        else:
            build_output_file.bof_processor(update_output=ele,
                                            main_dict=main_dict)
    return main_dict
