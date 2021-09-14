#  Copyright (c) 2021. Kenneth A. Grady
#  See BSD-2-Clause-Patent license in LICENSE.txt
#  Additional licenses are in the license folder.

""" Parse the list table and pass the values to a dictionary. """

__author__ = "Kenneth A. Grady"
__version__ = "0.1.0a0"
__maintainer__ = "Kenneth A. Grady"
__email__ = "gradyken@msu.edu"
__date__ = "2021-05-13"
__name__ = "Contents.Library.list_table"

""" An RTF file uses the following structure for a list table (if present):
(p.30)

<listtable>	    '{\\*' \\listtable <listpicture>? <list>+ '}'
<listpicture>	'{\\*' \\listpicture <shppictlist> '}'
<list>	        \\list \\listemplateid & (\\listsimple | \\listhybrid)? &
                <listlevel>+ & \\listrestarthdn & \\listidN & (\\listname
                #PCDATA ';') \\liststyleidN? \\liststylename?
<listlevel>	    '{' \\listlevel <number> <justification> & \\levelfollowN
                & \\levelstartatN & \\lvltentative? (\\leveloldN &
                \\levelprevN? & \\levelprevspaceN? & \\levelspaceN? &
                \\levelindentN?)? & <leveltext> & <levelnumbers> &
                \\levellegalN? & \\levelnorestartN? & <chrfmt>? &
                \\levelpictureN & \\liN? & \fiN? & (\\jclisttab \txN)? &
                \\linN? '}'
<number>	    \\levelnfcN | \\levelnfcnN | (\\levelnfcN & \\levelnfcnN)
<justification>	\\leveljcN | \\leveljcnN | (\\leveljcN & \\leveljcnN)
<leveltext>	    '{' \\leveltext \\leveltemplateid? #SDATA ';}'
<levelnumbers>	'{' \\levelnumbers #SDATA ';}'
"""


def processor(main_dict: dict, code_strings_to_process: list) -> dict:
    for code_string in code_strings_to_process:
        pass
    return main_dict
