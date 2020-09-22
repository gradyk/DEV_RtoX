import os
import sys
import unittest
import Contents.Library.header_parser_step_two


class EmptyTableCheck(unittest.TestCase):

    def test_empty_table_check(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")
        table_for_test = "filetbl"
        header_tables_dict = {"filetbl": 4}

        table, table_start_line, table_empty = \
            Contents.Library.header_parser_step_two.check_for_empty_table(
                table=table_for_test,
                header_tables_dict=header_tables_dict,
                working_input_file=working_input_file)

        test_function_results = [table, table_start_line, table_empty]
        comparison_results = ["filetbl", 4, True]

        self.assertEqual(test_function_results, comparison_results)


if __name__ == "__main__":
    unittest.main()
