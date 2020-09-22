import Contents.Library.rtf_file_lead_parse
import os
import sys
import unittest


class TableCodeProcess(unittest.TestCase):
    def test_code_process(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")

        rtf_file_codes_update \
            = Contents.Library.rtf_file_lead_parse.code_process(
                working_input_file=working_input_file)

        comparison_dict = [('rtf', '1'),
                           ('ansi', ''),
                           ('ansicpg1252', ''),
                           ('uc', '1'),
                           ('deflang', '1033'),
                           ('deflangfe', '1033'),
                           ('deff', '0'),
                           ("adeff", "0"),
                           ('stshfdbch', '43'),
                           ('stshfloch', '31506'),
                           ('stshfhich', '31506'),
                           ('stshfbi', '31507'),
                           ("themelang", '1033'),
                           ("themelangfe", '0'),
                           ("themelangcs", '0')]

        self.assertEqual(rtf_file_codes_update, comparison_dict)


if __name__ == '__main__':
    unittest.main()
