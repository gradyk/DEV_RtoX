import Contents.Library.group_boundaries_capture_contents
import os
import sys
import unittest


class TestGroupBoundariesCapture(unittest.TestCase):

    def test_group_boundaries_one(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(
            test_dir, "working_input_file_slash_star.txt")
        self.maxDiff = None

        group_list = Contents.Library.group_boundaries_capture_contents.\
            define_boundaries_capture_contents(
                working_input_file=working_input_file,
                group_start_line=14,
                group_start_index=0)

        comparison_list = {"14_0":
                           ["{{\\pard\\plain \\ltrpar\\s2\\qc "
                            "}\\ltrpar\\s2\\qc "
                            "{\\*\\pnseclvl1\\pnucrm\\pnstart1\\pnindent720"
                            "\\pnhang{\\pntxta .}}", 14, 0, 16, 12]}

        self.assertEqual(group_list, comparison_list)

    def test_group_boundaries_two(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(
            test_dir, "working_input_file_slash_star.txt")
        self.maxDiff = None

        group_list = Contents.Library.group_boundaries_capture_contents.\
            define_boundaries_capture_contents(
                working_input_file=working_input_file,
                group_start_line=1,
                group_start_index=0)

        comparison_list = {"1_0":
                           ['{\\*\\ftnsep \\ltrpar \\pard\\plain '
                            '\\ltrpar\\ql\\li0\\ri0\\widctlpar'
                            '\\wrapdefault\\aspalpha\\aspnum\\n'
                            '\\faauto\\adjustright\\rin0\\lin0'
                            '\\itap0 '
                            '\\rtlch\\fcs1 \\af0\\afs24\\alang1025 '
                            '\\ltrch\\fcs0\\n\\fs24\\lang1033'
                            '\\langfe1033\\cgrid\\langnp1033'
                            '\\langfenp1033 '
                            '{\\rtlch\\fcs1 \\af0 \\ltrch\\fcs0'
                            '\\insrsid10764137 '
                            '\\chftnsep\\par }\\insrsid10764137 '
                            '\\chftnsep\\par }',
                            1, 0, 7, 32]}

        self.assertEqual(group_list, comparison_list)


if __name__ == '__main__':
    unittest.main()
