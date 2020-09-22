import Contents.Library.doc_parser
import Contents.Library.slash_star
import os
import sys
import unittest


class DocParseSlashStar(unittest.TestCase):
    def test_slash_star_processor(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir,
                                          "working_input_file_slash_star.txt")

        start_index = 0
        line_to_parse = 1

        ssp_metrics = Contents.Library.slash_star.slash_star_processor(
            working_input_file=working_input_file,
            start_index=start_index,
            line_to_parse=line_to_parse)

        line_to_parse = ssp_metrics[0]
        parse_index = ssp_metrics[1]

        line_to_parse_compare = 7
        parse_index_compare = 36

        self.assertEqual(line_to_parse_compare, line_to_parse)
        self.assertEqual(parse_index_compare, parse_index)


if __name__ == '__main__':
    unittest.main()
