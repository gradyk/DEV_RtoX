import Contents.Library.header_parser_step_one
import json
import os
import sys
import unittest


class TestDetermineHeaderStructure(unittest.TestCase):
    def test_determine_header_structure(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")

        Contents.Library.header_parser_step_one.determine_header_structure(
            debug_dir=test_dir,
            working_input_file=working_input_file)

        with open(os.path.join(test_dir, "header_tables_dict.json"), "r") as \
                header_tables_dict_pre:
            header_tables_dict = json.load(header_tables_dict_pre)

        header_tables_comparison = {"rtf": 1, "fonttbl": 1, "filetbl": 4}

        self.assertEqual(header_tables_dict, header_tables_comparison)


if __name__ == '__main__':
    unittest.main()
