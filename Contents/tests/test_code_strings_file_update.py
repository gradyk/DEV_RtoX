import Contents.Library.header_parser_step_two
import json
import os
import sys
import unittest


class TestCodeStringsFileUpdate(unittest.TestCase):

    def test_code_strings_file_update(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        table = "fonttbl"
        code_strings_list = "{\\f0\\fbidi \\froman\\fcharset0\\fprq2" \
                            "{\\*\\panose 02020603050405020304}Times New " \
                            "Roman;}"\
                            "{\\f1\\fbidi \\fswiss\\fcharset0\\fprq2" \
                            "{\\*\\panose 020b0604020202020204}Arial;}" \
                            "{f3\\fbidi \\fdecor\\fcharset2\\fprq2{" \
                            "\\*\\panose " \
                            "05050102010706020507}Symbol;}{\\f34\\fbidi " \
                            "\\froman\\fcharset0\\fprq2{\\*\\panose " \
                            "02040503050406030204}Cambria Math;}"

        with open(os.path.join(test_dir, "code_strings_file.json"), "w+") as \
                code_strings_file_pre:
            json.dump("{}", code_strings_file_pre)

        Contents.Library.header_parser_step_two.\
            code_strings_file_update(
                debug_dir=test_dir,
                code_strings_list=code_strings_list,
                table=table)

        with open(os.path.join(test_dir, "code_strings_file.json"), "r") as \
                code_strings_file_pre:
            code_strings_file = json.load(code_strings_file_pre)

        comparison_dict = {'fonttbl':
                               ['{\\f0\\fbidi \\froman\\fcharset0'
                                '\\fprq2{\\*\\panose '
                                '02020603050405020304}Times New Roman;}'
                                '{\\f1\\fbidi '
                                '\\fswiss\\fcharset0\\fprq2{\\*\\panose '
                                '020b0604020202020204}Arial;}{f3\\fbidi '
                                '\\fdecor\\fcharset2\\fprq2{\\*\\panose '
                                '05050102010706020507}Symbol;}{\\f34\\fbidi '
                                '\\froman\\fcharset0\\fprq2{\\*\\panose '
                                '02040503050406030204}Cambria Math;}']}

        self.assertEqual(code_strings_file, comparison_dict)


if __name__ == '__main__':
    unittest.main()
