import os
import sys
import unittest
import table_boundaries


class TableBoundaries(unittest.TestCase):

    def text_braces_count_match(self):
        table = "fonttbl"
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")
        table_start_line = 1

        matched_brace_count = table_boundaries.find_table_start_end(
            table=table, working_input_file=working_input_file,
            table_start_line=table_start_line)

        self.assertEqual(matched_brace_count, 6)


if __name__ == "__main__":
    unittest.main()
