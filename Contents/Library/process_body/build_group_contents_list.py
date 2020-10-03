#  Copyright (c) 2020. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

# From standard libraries
import logging
import re


def pre_process(main_dict: dict) -> dict:
    contents_string = main_dict["processing_dict"]["group_contents"]
    main_dict["processing_dict"]["contents_string"] = contents_string
    main_dict = processor(main_dict=main_dict)
    return main_dict


def processor(main_dict: dict) -> dict:
    # TODO Complete text for logging.exceptions.
    item = None
    while main_dict["processing_dict"]["contents_string"] != "":

        try:
            # Left bracket
            test = re.search(r"^{",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                results = test[0]
                main_dict["processing_dict"]["contents_list"].append(results)
                contents_string = \
                    main_dict["processing_dict"]["contents_string"][1:]
                contents_string = contents_string.lstrip()
                main_dict["processing_dict"]["contents_string"] = \
                    contents_string
            else:
                pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

        try:
            # Destination (\*\...)
            test = re.search(r"^(\\\*\\[a-zA-Z\-0-9]*)",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                results = test[0]
                main_dict["processing_dict"]["contents_list"].append(results)
                contents_string = \
                    main_dict["processing_dict"]["contents_string"].\
                    replace(test[0], "", 1)
                contents_string = contents_string.lstrip()
                main_dict["processing_dict"]["contents_string"] = \
                    contents_string
            else:
                pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

        try:
            # Control word
            test = re.search(r"^(\\[a-zA-Z\-0-9]*)",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                results = test[0]
                main_dict["processing_dict"]["contents_list"].append(results)
                contents_string = \
                    main_dict["processing_dict"]["contents_string"].\
                    replace(test[0], "", 1)
                contents_string = contents_string.lstrip()
                main_dict["processing_dict"]["contents_string"] = \
                    contents_string
            else:
                pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

        try:
            # Control symbol \x where x is ', -, :, _, |, or ~.
            test = re.search(r"^(\\['-:_|~])",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                results = test[0]
                main_dict["processing_dict"]["contents_list"].append(results)
                contents_string = \
                    main_dict["processing_dict"]["contents_string"].\
                    replace(test[0], "", 1)
                contents_string = contents_string.lstrip()
                main_dict["processing_dict"]["contents_string"] = \
                    contents_string
            else:
                pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

        try:
            # Right bracket
            test = re.search(r"^}",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                results = test.group()
                main_dict["processing_dict"]["contents_list"].append(results)
                contents_string = \
                    main_dict["processing_dict"]["contents_string"][1:].\
                    lstrip()
                main_dict["processing_dict"]["contents_string"] = \
                    contents_string
            else:
                pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

        try:
            # Text
            test = re.search(r"^[{\\]",
                             main_dict["processing_dict"]["contents_string"])
            if test is not item:
                pass
            else:
                test = \
                    re.search(r"^([^}]*)",
                              main_dict["processing_dict"]["contents_string"])
                if test is not item and test[0] != '':
                    results = test.group()
                    main_dict["processing_dict"]["contents_list"].\
                        append(results)
                    contents_string = \
                        main_dict["processing_dict"]["contents_string"].\
                        lstrip(test.group())
                    contents_string = contents_string.lstrip()
                    main_dict["processing_dict"]["contents_string"] = \
                        contents_string
                else:
                    pass
        except ValueError as error:
            logging.exception(error, "_____________")
        except TypeError as error:
            logging.exception(error, "_____________")
        except Exception as error:
            logging.exception(error, "_____________")

    return main_dict
