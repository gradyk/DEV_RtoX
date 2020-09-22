import Contents.Library.doc_parser
import os
import sys
import unittest


class GroupEndIndexSetProperly(unittest.TestCase):
    def test_group_end_index(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(
            test_dir, "working_input_file_group_end_index.txt")
        control_word_func_dict = os.path.join(test_dir,
                                              "control_word_func_dict.json")
        parse_index = 0
        line_to_parse = 1
        self.maxDiff = None

        line_to_parse, parse_index, group_count = \
            Contents.Library.group.group_processor(
                parse_index=parse_index,
                line_to_parse=line_to_parse,
                working_input_file=working_input_file,
                debug_dir=test_dir,
                control_word_func_dict=control_word_func_dict)

        compare_line = 6
        compare_index = 82
        compare_count = 0

        self.assertEqual(line_to_parse, compare_line)
        self.assertEqual(parse_index, compare_index)
        self.assertEqual(group_count, compare_count)


if __name__ == '__main__':
    unittest.main()
