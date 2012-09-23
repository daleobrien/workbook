# -*- coding: utf-8 -*-

import unittest
from workbook import Workbook, print_table
from StringIO import StringIO
import sys


class TestWorkbook(unittest.TestCase):

    def setUp(self):
        self.saved_stdout = sys.stdout
        self.out = StringIO()
        sys.stdout = self.out

        self.wb = Workbook()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_write_to_excel(self):

        wb = self.wb

        wb.country_code = 61  # Australia

        # 2D data
        data = [['a', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        # add one sheet
        wb.write_sheet(data, "test_sheet", print_to_screen=True)

        # add another sheet
        data = [['o', 'b', 'x'],
                [0, 0, 1],
                [1, 1, 0]]
        wb.write_sheet(data, "another", print_to_screen=True)

        wb.save('test.xls')

        # TODO: add a test to check the xls file is as expected

    def test_unicode_excel(self):
        sys.stdout = self.saved_stdout
        wb = self.wb

        # 2D data, mix of unicode and such like
        data = [[u'Ö', u'b', 'Ö'],
                [1, 2, 3],
                [4, 5, 6]]

        # just don't through any exceptions
        wb.write_sheet(data, "another", print_to_screen=True)
        wb.save('test.xls')

    def test_unicode_table(self):

        # 2D data
        data = [['Ö', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        print_table(data, "title", bold=False)

        output = self.out.getvalue().strip()

        expected_table = u'*** title ***\n\n' +\
                         u'+---+---+---+\n' +\
                         u'| Ö | b | c |\n' +\
                         u'+---+---+---+\n' +\
                         u'| 1 | 2 | 3 |\n' +\
                         u'| 4 | 5 | 6 |\n' +\
                         u'+---+---+---+'

        self.assertEqual(output, expected_table)

    def test_text_table(self):

        # 2D data
        data = [['a', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        print_table(data, "title", bold=False)

        output = self.out.getvalue().strip()

        expected_table = u'*** title ***\n\n' +\
                         u'+---+---+---+\n' +\
                         u'| a | b | c |\n' +\
                         u'+---+---+---+\n' +\
                         u'| 1 | 2 | 3 |\n' +\
                         u'| 4 | 5 | 6 |\n' +\
                         u'+---+---+---+'

        self.assertEqual(output, expected_table)

    def test_bold_text_table(self):
        # bold version
        data = [['a', 'Ä'],
                [1, 2]]
        print_table(data, "title", bold=True)
        output = self.out.getvalue().strip()

        # includes control chars
        expected_table = u'*** \x1b[31mtitle\x1b[0m ***\n\n' +\
                         u'+---+---+\n' +\
                         u'| \x1b[32ma\x1b[0m | \x1b[32mÄ\x1b[0m |\n' +\
                         u'+---+---+\n' +\
                         u'| \x1b[32m1\x1b[0m | 2 |\n' +\
                         u'+---+---+'

        self.assertEqual(output, expected_table)

#
