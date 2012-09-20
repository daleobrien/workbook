# -*- coding: utf-8 -*-

import unittest
from workbook import Workbook, print_table
from StringIO import StringIO
import sys


class TestSequenceFunctions(unittest.TestCase):

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
        data = [['Ö', 'b', 'x'],
                [0, 0, 1],
                [1, 1, 0]]
        wb.write_sheet(data, "another", print_to_screen=True)

        wb.save('test.xls')

        # TODO: add a test to check the xls file is as expected

    def test_unicode_table(self):

        # 2D data
        data = [['Ö', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        print_table(data, "title", bold=False)

        output = self.out.getvalue().strip()

        expected_table = '*** title ***\n\n' +\
                         '+---+---+---+\n' +\
                         '| Ö | b | c |\n' +\
                         '+---+---+---+\n' +\
                         '| 1 | 2 | 3 |\n' +\
                         '| 4 | 5 | 6 |\n' +\
                         '+---+---+---+'

        self.assertEqual(output, expected_table)

    def test_text_table(self):

        # 2D data
        data = [['a', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        print_table(data, "title", bold=False)

        output = self.out.getvalue().strip()

        expected_table = '*** title ***\n\n' +\
                         '+---+---+---+\n' +\
                         '| a | b | c |\n' +\
                         '+---+---+---+\n' +\
                         '| 1 | 2 | 3 |\n' +\
                         '| 4 | 5 | 6 |\n' +\
                         '+---+---+---+'

        self.assertEqual(output, expected_table)

    def test_bold_text_table(self):
        # bold version
        data = [['a', 'Ä'],
                [1, 2]]
        print_table(data, "title", bold=True)
        output = self.out.getvalue().strip()

        # includes control chars
        expected_table = '*** \x1b[31mtitle\x1b[0m ***\n\n' +\
                         '+---+---+\n' +\
                         '| \x1b[32ma\x1b[0m | \x1b[32mÄ\x1b[0m |\n' +\
                         '+---+---+\n' +\
                         '| \x1b[32m1\x1b[0m | 2 |\n' +\
                         '+---+---+'

        self.assertEqual(output, expected_table)

#
