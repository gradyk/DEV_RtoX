import Contents.Library.rtf_file_lead_parse
import os
import sys
import unittest


class InputFileEncoding(unittest.TestCase):
    def test_check_input_file_encoding(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(test_dir,
                                               "working_input_file.rtf")

        try:
            Contents.Library.rtf_file_lead_parse.check_input_file_encoding(
                debug_dir=test_dir,
                working_input_file=self.working_input_file)
        except (UnicodeEncodeError, ValueError) as etype:
            self.fail("rtf_file_lead_parse.check_input_file_encoding "
                      f"raised {etype} unexpectedly!")


if __name__ == '__main__':
    unittest.main()
