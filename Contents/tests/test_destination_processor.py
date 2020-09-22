import Contents.Library.doc_parser
import Contents.Library.destination
import os
import sys
import unittest


class DocParseDestination(unittest.TestCase):
    def test_destination_processor(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir,
                                          "working_input_file_slash_star.txt")
        control_word_func_dict = os.path.join(test_dir,
                                              "control_word_func_dict.json")

        line_to_parse = 8
        parse_index = 0

        dp_metrics = Contents.Library.destination.destination_processor(
            working_input_file=working_input_file,
            parse_index=parse_index,
            line_to_parse=line_to_parse,
            control_word_func_dict=control_word_func_dict)

        line_to_parse = dp_metrics[0]
        parse_index = dp_metrics[1]

        line_to_parse_compare = 8
        parse_index_compare = 11

        self.assertEqual(line_to_parse_compare, line_to_parse)
        self.assertEqual(parse_index_compare, parse_index)


if __name__ == '__main__':
    unittest.main()
