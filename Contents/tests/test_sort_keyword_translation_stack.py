import Contents.Library.doc_parser
import json
import os
import sys
import unittest


class TestSortKeywordTransactionStack(unittest.TestCase):

    def test_sort_keyword_transaction_stack(self):

        self.maxDiff = None

        self.keyword_translation_stack = [
            (True, "cs_beg", "10"),
            (True, "cs_end", "15"),
            (True, "par", "12"),
            (True, "par", "16"),
            (True, "pard", "17"),
            (True, "sectd", "21"),
            (True, "sect", "20"),
            (True, "footnote_beg", "25"),
            (True, "footnote_end", "31"),
            (True, "cs_beg", "27"),
            (True, "cs_end", "30"),
            (True, "par", "28"),
            (True, "pard", "29")
        ]

        keyword_translation_stack = \
            Contents.Library.doc_parser.sort_keyword_translation_stack(
                keyword_translation_stack=self.keyword_translation_stack)

        comparison_list = [
            (True, "cs_beg", "10"),
            (True, "par", "12"),
            (True, "cs_end", "15"),
            (True, "par", "16"),
            (True, "pard", "17"),
            (True, "sect", "20"),
            (True, "sectd", "21"),
            (True, "footnote_beg", "25"),
            (True, "cs_beg", "27"),
            (True, "par", "28"),
            (True, "pard", "29"),
            (True, "cs_end", "30"),
            (True, "footnote_end", "31"),

        ]

        self.assertEqual(keyword_translation_stack, comparison_list)


if __name__ == '__main__':
    unittest.main()
