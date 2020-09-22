import Contents.Library.font_table
import json
import os
import sys
import unittest


class TestFonttblParse(unittest.TestCase):

    def test_FonttblParse(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        new_font_file = os.path.join(test_dir, "font_file.json")
        self.maxDiff = None

        code_strings_to_process = [
            "{\\f0\\fbidi \\froman\\fcharset0\\fprq2{\\*\\panose "
            "02020603050405020304}Times New Roman;}", "{\\f1\\fbidi \\fswiss"
            "\\fcharset0\\fprq2{\\*\\panose 020b0604020202020204}Arial;}",
            "{\\f3\\fbidi \\fdecor\\fcharset2\\fprq2{\\*\\panose "
            "05050102010706020507}Symbol;}", "{\\f34\\fbidi \\froman"
            "\\fcharset0\\fprq2{\\*\\panose 02040503050406030204}"
            "Cambria Math;}"
            ]

        class FonttblParse(object):
            def __init__(self):
                self.debug_dir = test_dir
                self.code_strings_to_process = code_strings_to_process
                self.code_stack = []
                self.master_code_stack = []

        Contents.Library.font_table.FonttblParse.process_code_strings(
            self=FonttblParse())

        with open(new_font_file, "r") as font_file_pre:
            font_file_to_test = json.load(font_file_pre)

        comparison_file = [
            [
                ["fontnum", "f0"], ["fbidi", "Miriam"],
                ["froman", "Times New Roman"], ["fcharset", "0"], ["fprq", "2"],
                ["panose", "02020603050405020304"],
                ["fontname", "Times New Roman"], ["fname", "None"],
                ["altname", "None"],
                ["fontemb", False], ["cpg", "0"]
            ],
            [
                ["fontnum", "f1"], ["fbidi", "Miriam"], ["fswiss", "Arial"],
                ["fcharset", "0"], ["fprq", "2"],
                ["panose", "020b0604020202020204"],
                ["fontname", "Arial"], ["fname", "None"],
                ["altname", "None"],
                ["fontemb", False], ["cpg", "0"]
            ],
            [
                ["fontnum", "f3"], ["fbidi", "Miriam"],
                ["fdecor", "Old English"],
                ["fcharset", "2"], ["fprq", "2"],
                ["panose", "05050102010706020507"],
                ["fontname", "Symbol"], ["fname", "None"],
                ["altname", "None"],
                ["fontemb", False], ["cpg", "0"]
            ],
            [
                ["fontnum", "f34"], ["fbidi", "Miriam"],
                ["froman", "Times New Roman"],
                ["fcharset", "0"], ["fprq", "2"],
                ["panose", "02040503050406030204"],
                ["fontname", "Cambria Math"], ["fname", "None"],
                ["altname", "None"],
                ["fontemb", False], ["cpg", "0"]
            ]
            ]

        self.assertEqual(font_file_to_test, comparison_file)

    def tearDown(self) -> None:
        super(TestFonttblParse, self).tearDown()
        self.code_strings_to_process = []


if __name__ == '__main__':
    unittest.main()
