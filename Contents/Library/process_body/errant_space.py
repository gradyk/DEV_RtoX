#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

"""  """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2020-8-17"
__name__ = "Contents.Library.process_body.check_parse_text"


def es_processor(main_dict: dict) -> dict:
    try:
        if main_dict["parse_text"].startswith(" \\"):
            main_dict["parse_text"] = main_dict["parse_text"].lstrip()
        else:
            pass
    except IndexError:
        pass
    return main_dict
