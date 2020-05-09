import Contents.Library.group_boundaries
import os
import sys
import unittest


class TestGroupBoundaries(unittest.TestCase):

    def test_group_boundaries_one(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(
            test_dir, "working_input_file_full.txt")
        self.maxDiff = None

        group_list = Contents.Library.group_boundaries.define_group_boundaries(
            working_input_file=self.working_input_file,
            group_start_line=3,
            group_start_index=0)

        comparison_list = [
            ("{\\headerl \\ltrpar \\pard\\plain \\ltrpar\\s25\\ql \\li0\\ri0"
             "\\nowidctlpar\\tqc\\tx4680\\tqr\\tx9360\\wrapdefault\\faauto"
             "\\rin0\\lin0\\itap0 \\rtlch\\fcs1 \\af31507\\afs20\\alang1025 "
             "\\ltrch\\fcs0 \\fs20\\lang1033\\langfe1033\\loch\\af31506"
             "\\hich\\af31506\\dbch\\af43\\cgrid\\langnp1033\\langfenp1033"
             "{\\rtlch\\fcs1 \\af31507 \\ltrch\\fcs0 "
             "\\insrsid15734229 \\par }}", 3, 0, 4, 233)]

        self.assertEqual(group_list, comparison_list)

    def test_group_boundaries_two(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(
            test_dir, "working_input_file_full.txt")
        self.maxDiff = None

        group_list = Contents.Library.group_boundaries.define_group_boundaries(
            working_input_file=self.working_input_file,
            group_start_line=5,
            group_start_index=0)

        comparison_list = [
            ("{\\headerr \\ltrpar \\pard\\plain \\ltrpar\\ql \\li0\\ri0"
             "\\widctlpar\\tqr\\tx9359\\wrapdefault\\aspalpha\\aspnum"
             "\\faauto\\adjustright\\rin0\\lin0\\itap0 \\rtlch\\fcs1 "
             "\\af0\\afs24\\alang1025 \\ltrch\\fcs0 \\fs24\\lang1033"
             "\\langfe1033\\cgrid\\langnp1033\\langfenp1033{\\rtlch\\fcs1 "
             "\\af43 \\ltrch\\fcs0 \\f44\\insrsid8351756 October 2, 2019}"
             "{\\rtlch\\fcs1 \\af43 \\ltrch\\fcs0 \\f44\\insrsid15734229 \t "
             "Back Matter Page }{\\field{\\*\\fldinst{\\rtlch\\fcs1 \\af43 "
             "\\ltrch\\fcs0 \\f44\\insrsid15734229 PAGE}}{\\fldrslt {\\rtlch"
             "\\fcs1 \\af43 \\ltrch\\fcs0 \\f44\\insrsid15734229 30}}}\\sectd "
             "\\ltrsect\\linex0\\endnhere\\sectdefaultcl\\sftnbj {"
             "\\rtlch\\fcs1 \\af43 \\ltrch\\fcs0 \\f44\\insrsid15734229\\par "
             "}}", 5, 0, 11, -1)]

        self.assertEqual(group_list, comparison_list)


if __name__ == '__main__':
    unittest.main()
