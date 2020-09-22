import Contents.Library.header_parser_step_two
import os
import sys
import unittest


class TestTableContents(unittest.TestCase):

    def test_get_table_contents_as_code_strings(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")
        table = "fonttbl"
        table_boundaries_file_updater = {"fonttbl": [1, 174, 3, 155]}
        self.maxDiff = None

        text_to_process = Contents.Library.header_parser_step_two\
            .get_table_contents_as_text_string(
                table=table,
                table_boundaries_file_updater=table_boundaries_file_updater,
                working_input_file=working_input_file)

        comparison_text = "{\\f0\\fbidi \\froman\\fcharset0\\fprq2" \
                          "{\\*\\panose 02020603050405020304}Times New Roman;}"\
                          "{\\f1\\fbidi \\fswiss\\fcharset0\\fprq2" \
                          "{\\*\\panose 020b0604020202020204}Arial;}" \
                          "{f3\\fbidi \\fdecor\\fcharset2\\fprq2{\\*\\panose " \
                          "05050102010706020507}Symbol;}{\\f34\\fbidi " \
                          "\\froman\\fcharset0\\fprq2{\\*\\panose " \
                          "02040503050406030204}Cambria Math;}"

        self.assertEqual(text_to_process, comparison_text)


if __name__ == '__main__':
    unittest.main()
