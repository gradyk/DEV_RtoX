import Contents.Library.doc_parser
import Contents.Library.group
import os
import sys
import unittest


class DocParseGroup(unittest.TestCase):
    def test_group_processor(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        debug_dir = test_dir
        working_input_file = os.path.join(test_dir,
                                          "working_input_file_slash_star.txt")
        control_word_func_dict = os.path.join(test_dir,
                                              "control_word_func_dict.json")

        line_to_parse = 9
        parse_index = 0

        gp_metrics = Contents.Library.group.group_processor(
            working_input_file=working_input_file,
            parse_index=parse_index,
            line_to_parse=line_to_parse,
            control_word_func_dict=control_word_func_dict,
            debug_dir=debug_dir)

        line_to_parse = gp_metrics[0]
        parse_index = gp_metrics[1]

        line_to_parse_compare = 9
        parse_index_compare = 1

        self.assertEqual(line_to_parse, line_to_parse_compare)
        self.assertEqual(parse_index, parse_index_compare)


if __name__ == '__main__':
    unittest.main()
