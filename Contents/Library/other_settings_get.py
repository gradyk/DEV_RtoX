#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

import logging

import read_configuration

log = logging.getLogger(__name__)


def retrieve(main_dict: dict) -> dict:
    config_settings_dict = read_configuration.get_system_arguments()
    config_settings_dict = read_configuration.get_configuration(
        main_dict=main_dict, config_settings_dict=config_settings_dict)
    # These settings come from the Config.ini file.
    tag_set = config_settings_dict.get("tag-set")
    output_header = config_settings_dict.get("output-file-header")
    convert_symbol = config_settings_dict.get("convert-symbol")
    convert_caps = config_settings_dict.get("convert-caps")
    report_level = config_settings_dict.get("problem-report-level")
    xml_indenting = config_settings_dict.get("xml-indenting")
    create_lists = config_settings_dict.get("create-lists")

    # TODO These need to reflect user input rather than be hard-coded.
    user_input_choices_dict = {
        tag_set:        f'XML tags: {tag_set}',
        output_header:  f'Header setting: {output_header}',
        convert_symbol: f"All symbols converted will be converted "
                        f"to UTF-8 characters.",
        convert_caps:   f'Caps setting: {convert_caps}',
        report_level:   f"Problem report level: {report_level}.",
        xml_indenting:  f"XML indenting turned on.",
        create_lists:   "Create lists turned on."
    }
    for menu_item in user_input_choices_dict:
        log.info(msg=user_input_choices_dict[menu_item])
    return config_settings_dict