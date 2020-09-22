import Contents.Library.header_parser_step_two
import unittest


class TestTableToCodeStrings(unittest.TestCase):

    def test_get_code_strings_from_text(self):

        self.maxDiff = None
        text_to_process = "{\\f0\\fbidi \\froman\\fcharset0\\fprq2" \
                          "{\\*\\panose 02020603050405020304}Times New Roman;}"\
                          "{\\f1\\fbidi \\fswiss\\fcharset0\\fprq2" \
                          "{\\*\\panose 020b0604020202020204}Arial;}" \
                          "{f3\\fbidi \\fdecor\\fcharset2\\fprq2{\\*\\panose " \
                          "05050102010706020507}Symbol;}{\\f34\\fbidi " \
                          "\\froman\\fcharset0\\fprq2{\\*\\panose " \
                          "02040503050406030204}Cambria Math;}"

        code_strings_list = Contents.Library.header_parser_step_two.\
            get_code_strings_from_text(text_to_process=text_to_process)

        comparison_list = ['{\\f0\\fbidi \\froman\\fcharset0\\fprq2'
                           '{\\*\\panose 02020603050405020304}Times New '
                           'Roman;}', '{\\f1\\fbidi \\fswiss\\fcharset0'
                           '\\fprq2{\\*\\panose 020b0604020202020204}Arial;}',
                           '{f3\\fbidi \\fdecor\\fcharset2\\fprq2{'
                           '\\*\\panose 05050102010706020507}Symbol;}',
                           '{\\f34\\fbidi \\froman\\fcharset0\\fprq2'
                           '{\\*\\panose 02040503050406030204}Cambria Math;}']

        self.assertEqual(code_strings_list, comparison_list)


if __name__ == '__main__':
    unittest.main()
