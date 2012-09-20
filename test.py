
import unittest
from workbook import Workbook


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.wb = Workbook()

    def test_write_to_excel(self):

        wb = self.wb

        wb.country_code = 61  # Australia

        # 2D data
        data = [['a', 'b', 'c'],
                [1, 2, 3],
                [4, 5, 6]]

        # add one sheet
        wb.write_sheet(data, "test_sheet", print_to_screen=True)

        wb.save('test.xls')

        #
    def test_unicode_table(self):
        pass

    def test_bold_and_not(self):
        pass
