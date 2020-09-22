import Contents.Library.docinfo_read
import os
import sys
import unittest


class TestGetInfoContents(unittest.TestCase):

    def test_get_info_section_contents(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(
            test_dir, "working_input_file_info.rtf")
        self.table = "info"
        self.line_to_read = 1
        self.debug_dir = test_dir

        self.maxDiff = None

        table_boundaries_file_updater = \
            {"info": [1, 0, 3, 62]}

        class InfoParseController(object):
            def __init__(self):
                self.working_input_file = working_input_file
                self.debug_dir = test_dir

        self.InfoParseController = InfoParseController

        text_to_process \
            = Contents.Library.docinfo_read\
            .InfoParseController.get_info_section_contents(
                self=self, working_input_file=self.working_input_file,
                table_boundaries_file_updater=table_boundaries_file_updater)

        comparison_text = "{\\title IHLO Lean Law Chapter}" \
                          "{\\author Kenneth A. Grady}{\\operator Grady, " \
                          "Kenneth}{\\creatim\\yr2020\\mo2\\dy5\\hr16" \
                          "\\min55}{\\revtim\\yr2020\\mo2\\dy5\\hr16\\min55}" \
                          "{\\printim\\yr2019\\mo4\\dy1\\hr14\\min50}{" \
                          "\\version2}{\\edmins1}{\\nofpages37}" \
                          "{\\nofwords12283}{\\nofchars70017}{" \
                          "\\nofcharsws82136}{\\vern4227}"

        self.assertEqual(text_to_process, comparison_text)


if __name__ == '__main__':
    unittest.main()
