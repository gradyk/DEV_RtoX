#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Perform several clean up operations on the output_file.xml:
1) Removing empty tag pairs (e.g., <p></p>).
2) Post-processing the file. [TO BE ADDED]
3) Formatting the output_file.xml.
6) Copying the output_file.xml to the output directory and changing the file
name to the name specified in the user's preferences. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-01-09"
__name__ = "Contents.Library.final_step"

# From standard libraries
import json
import ntpath
import os
import sys
from shutil import copy

# From local application
import xmlformatter


def fs_processor(main_dict: dict) -> None:
    xml_tags_file = os.path.join(main_dict["dicts_dir"],
                                 "xml_tags.json")
    with open(xml_tags_file, "r+") as tag_dict_pre:
        tag_dict_options = json.load(tag_dict_pre)
    tag_dict = tag_dict_options[str(main_dict["tag_set"])]

    # Converting to XML creates instances of empty tag pairs.
    # Run through the file twice looking for empty pairs (deleting
    # empty tags on the first run through may create new empty tag pairs).
    tag_pairs = tag_dict["tag_pairs"]
    i = 1
    while i < 3:
        for item in tag_pairs:
            main_dict["output_text"] = \
                        main_dict["output_text"].\
                        replace(item, "")
        i += 1

    # Create a backup of the output_file.xml.
    main_dict["output_text_bak"] = main_dict["output_text"]
    output_file = os.path.join(main_dict["debug_dir"], "output_file.xml")
    with open(output_file, "w+") as output_file_pre:
        output_file_pre.write(main_dict["output_text"])
    with open(output_file, "r+") as output_file_byte:
        output_file_str = output_file_byte.read()

    xml_formatted_text = xmlformatter.xmlformatter_start(
        infile=output_file_str,
        outfile=main_dict["output_file_name"])

    if xml_formatted_text is tuple:
        print("Tuple")
        sys.exit(0)
    else:
        with open(output_file, "w+") as output_xml_file_pre:
            output_xml_file_pre.write(xml_formatted_text[0])

    # Put the final XML file in the output directory and rename it per
    # the user's preference.
    final_file = ntpath.basename(main_dict["output_file_name"])
    output_dir = os.path.join(main_dict["base_dir"], "output")

    copy(main_dict["output_file_name"], output_dir)

    orig_output_list = [output_dir, "/output_file.xml"]
    final_output_list = [output_dir, f'/{final_file}']
    orig_output = ''.join(orig_output_list)
    final_output = ''.join(final_output_list)
    os.rename(orig_output, final_output)
