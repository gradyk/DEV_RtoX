import Contents.Library.docinfo_read
import json
import os
import sys
import unittest


class TestFindInfoBoundaries(unittest.TestCase):

    def test_find_info_section_boundaries(self):
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        test_dir = os.path.join(base_dir, "data")
        self.working_input_file = os.path.join(
                    test_dir, "working_input_file_info.rtf")
        self.table = "info"
        self.line_to_read = 1

        self.maxDiff = None

        class InfoParseController(object):
            def __init__(self):
                self.working_input_file = working_input_file
                self.debug_dir = test_dir

        self.InfoParseController = InfoParseController

        table_boundaries_file_updater = \
            Contents.Library.docinfo_read.InfoParseController\
            .find_info_section_boundaries(self=self)

        comparison_list = {"info": [1, 0, 3, 62]}

        self.assertEqual(table_boundaries_file_updater, comparison_list)


if __name__ == '__main__':
    unittest.main()
