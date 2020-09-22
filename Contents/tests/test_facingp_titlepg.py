import Contents.Library.facingp_titlepg
import os
import sys
import unittest


class TestFacingTitlePage(unittest.TestCase):

    def test_facingp_titlepg(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(test_dir,
                                               "working_input_file_full.txt")

        face_title = \
            Contents.Library.facingp_titlepg.search_for_facingp(
                working_input_file=self.working_input_file)

        comparison_list = [
            ("facingp", 1),
            ("titlepg", 1),
            ("titlepg", 2)
        ]

        self.assertEqual(face_title, comparison_list)


if __name__ == '__main__':
    unittest.main()
