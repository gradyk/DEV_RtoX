import os
import sys
import unittest
import Contents.Library.rtf_file_lead_parse


class OpeningBraceTest(unittest.TestCase):

    def test_check_opening_brace(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        working_input_file = os.path.join(test_dir, "working_input_file.rtf")

        try:
            Contents.Library.rtf_file_lead_parse.check_for_opening_brace(
                debug_dir=test_dir,
                working_input_file=working_input_file)
        except (ValueError, TypeError, RuntimeError, SyntaxError) as etype:
            self.fail("rtf_file_lead_parse.check_for_opening_brace raised "
                      f"{etype} unexpectedly!")


if __name__ == "__main__":
    unittest.main()