import Contents.Library.style_sheet_table
import json
import os
import sys
import unittest


class TestStylesheetTableParse(unittest.TestCase):

    def test_process_code_strings(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        new_style_file = os.path.join(test_dir, "style_file.json")
        self.maxDiff = None
        
        code_strings_to_process = [
            "{\\s20\\ql \\li0\\ri0\\nowidctlpar\\wrapdefault"
            "\\faauto\\rin0\\lin0\\itap0 \\rtlch\\fcs1 \\af31507\\afs20"
            "\\alang1025 \\ltrch\\fcs0 \\fs20\\lang1033\\langfe1033"
            "\\loch\\f31506\\hich\\af31506\\dbch\\af43\\cgrid\\langnp1033"
            "\\langfenp1033 \\snext20 Footnote;}",
            "{\\s21\\ql \\li0\\ri0\\nowidctlpar\\wrapdefault\\faauto\\rin0"
            "\\lin0\\itap0 \\rtlch\\fcs1 \\af31507\\afs20\\alang1025 \\ltrch"
            "\\fcs0 \\fs20\\lang1033\\langfe1033\\loch\\f39\\hich\\af39"
            "\\dbch\\af43\\cgrid\\langnp1033\\langfenp1033 \\snext21 "
            "\\sqformat \\styrsid5263113 Endnote;}",
            "{\\*\\cs26 \\additive \\rtlch\\fcs1 \\af0 \\ltrch\\fcs0 "
            "\\sbasedon10 \\slink25 \\slocked \\styrsid13055681 Header Char;}"
            ]

        class StyleSheetParse(object):
            def __init__(self):
                self.debug_dir = test_dir
                self.code_strings_to_process = code_strings_to_process
                self.code_stack = []
                self.master_code_stack = []

        Contents.Library.style_sheet_table.StyleSheetParse.process_code_strings(
                    self=StyleSheetParse())

        with open(new_style_file, "r") as style_file_pre:
            style_file = json.load(style_file_pre)

        comparison_file = [[['stylecode', 's20'], ['italic', '0'],
                           ['bold', '0'], ['underline', '0'],
                           ['strikethrough', '0'], ['small_caps', '0'],
                           ['additive', False], ['style_name', 'Footnote'],
                           ['snext', '20'], ['font_align', 'faauto']],
                           [['stylecode', 's21'], ['italic', '0'],
                           ['bold', '0'], ['underline', '0'],
                           ['strikethrough', '0'], ['small_caps', '0'],
                           ['additive', False], ['style_name', 'Endnote'],
                           ['snext', '21'], ['font_align', 'faauto']]]

        self.assertEqual(style_file, comparison_file)

    def tearDown(self) -> None:
        super(TestStylesheetTableParse, self).tearDown()
        self.code_strings_to_process = []


if __name__ == '__main__':
    unittest.main()
