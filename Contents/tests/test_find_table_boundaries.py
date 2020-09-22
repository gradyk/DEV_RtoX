import header_parser_step_two
import os
import sys
import unittest


class TableBoundaries(unittest.TestCase):

    def test_find_table_boundaries(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")

        table_updater = ({"fonttbl": [1, False]})
        table = "fonttbl"

        table_list = header_parser_step_two.find_table_boundaries(
            table=table, table_updater=table_updater,
            working_input_file=working_input_file)

        compare_list = {"fonttbl": [1, 174, 3, 155]}

        self.assertEqual(table_list, compare_list)


if __name__ == '__main__':
    unittest.main()
