import unittest
import Contents.Library.split_between_characters


class SplitCharactersTest(unittest.TestCase):

    def test_split_between_characters_pass(self):

        text_to_process = "{\\f0\\fbidi \\froman\\fcharset0\\fprq2" \
            "{\\*\\panose 02020603050405020304}Times New Roman;}" \
            "{\\f1\\fbidi \\fswiss\\fcharset0\\fprq2" \
            "{\\*\\panose 020b0604020202020204}Arial;}" \
            "{\\f3\\fbidi \\fdecor\\fcharset2\\fprq2" \
            "{\\*\\panose 05050102010706020507}Symbol;}" \
            "{\\f34\\fbidi \\froman\\fcharset0\\fprq2" \
            "{\\*\\panose 02040503050406030204}Cambria Math;}" \
            "{\\f37\\fbidi \\fswiss\\fcharset0\\fprq2" \
            "{\\*\\panose 020f0502020204030204}Calibri;}"

        split_characters = "}{"

        code_strings_list = \
            Contents.Library.split_between_characters.split_between(
                text_to_process=text_to_process,
                split_characters=split_characters)

        comparison_list = [
            "{\\f0\\fbidi \\froman\\fcharset0\\fprq2"
            "{\\*\\panose 02020603050405020304}Times New Roman;}",
            "{\\f1\\fbidi \\fswiss\\fcharset0\\fprq2"
            "{\\*\\panose 020b0604020202020204}Arial;}",
            "{\\f3\\fbidi \\fdecor\\fcharset2\\fprq2"
            "{\\*\\panose 05050102010706020507}Symbol;}",
            "{\\f34\\fbidi \\froman\\fcharset0\\fprq2"
            "{\\*\\panose 02040503050406030204}Cambria Math;}",
            "{\\f37\\fbidi \\fswiss\\fcharset0\\fprq2"
            "{\\*\\panose 020f0502020204030204}Calibri;}"]

        self.assertEqual(code_strings_list, comparison_list)


if __name__ == '__main__':
    unittest.main()
