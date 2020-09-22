import Contents.Library.process_body.group_contents
import os
import sys
import unittest


class MyGroupTest(unittest.TestCase):
    def test_group_definition(self):
        group_info = {1_0:
                          ["{\\intro \\word{\\*\\thing {"
                           "\\nothing\\else}}\\given\\together {"
                           "\\speaking\\fast}\\hyper\\charged {\\terrible{"
                           "\\*\\awful\\lawyer}}\\game changer}",
                           1,
                           0,
                           1,
                           129]}

        self.maxDiff = None

        Contents.Library.process_body.group_contents.processor_settings(
            group_info=group_info)

        master_list = ['\\intro', '\\word', '{\\*\\thing {\\nothing\\else}}',
                '\\given',
         '\\together', '{\\speaking\\fast}', '\\hyper', '\\charged',
         '{\\terrible{\\*\\awful\\lawyer}}', '\\game', 'changer']

        self.assertEqual(contents_list, master_list)

if __name__ == '__main__':
    unittest.main()
