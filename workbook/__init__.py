#!/usr/bin/env python

from xlwt import Workbook as _WB_, Font, XFStyle, Borders, Alignment


def print_table(data, title="", bold=True):

    '''fancy ascii table'''

    maxs = []

    # convert table to all unicode, keep stuff simple later
    def convert(cell):
        if isinstance(cell, str):
            return unicode(cell, 'utf-8')
        elif not isinstance(cell, unicode):
            return u"%s" % str(cell)
        return cell

    data = [[convert(c) for c in row] for row in data]

    # find longest string for each column
    for row in data:
        for i, cell in enumerate(row):
            if len(maxs) <= i:
                maxs.append(0)

            l = len(cell)
            if l > maxs[i]:
                maxs[i] = l

    # row divider
    tb = "+-" + "-+-".join(["-" * m for m in maxs]) + "-+"
    print
    if title:
        if bold:
            print "*** \033[31m" + title + "\033[0m ***"
        else:
            print "*** " + title + " ***"
        print
        print tb

    for j, row in enumerate(data):

        text = []
        for i, cell in enumerate(row):

            # first column is always left, others are right justified
            if i > 0:
                cell = cell.rjust(maxs[i])
            else:
                cell = cell.ljust(maxs[i])

            if bold:
                # first column and first row are bold, if enabled
                if j == 0 or i == 0:
                    cell = '\033[32m%s\033[0m' % cell

            text.append(cell)

        print "| " + " | ".join(text) + " |"
        if j == 0:
            print tb
    print tb


class Workbook(_WB_):

    def write_sheet(self, data, sheet_name, print_to_screen=False):
        '''Write a very simple table to a new sheet in a spreadsheet,
           Optionally, print the table to the screen'''

        # most cells
        al = Alignment()
        al.horz = Alignment.HORZ_RIGHT
        al.vert = Alignment.VERT_CENTER
        font = Font()
        font.name = 'Arial'
        font.height = 9 * 20  # 9 pt
        style = XFStyle()
        style.font = font
        style.alignment = al

        # tops cells
        al = Alignment()
        al.horz = Alignment.HORZ_CENTER
        al.vert = Alignment.VERT_CENTER
        font = Font()
        font.name = 'Arial'
        font.bold = True
        font.height = 9 * 20  # 9 pt
        style_top = XFStyle()
        style_top.font = font
        style_top.alignment = al

        # left cells
        al = Alignment()
        al.horz = Alignment.HORZ_LEFT
        al.vert = Alignment.VERT_CENTER
        font = Font()
        font.name = 'Arial'
        font.bold = True
        font.italic = True
        font.height = 9 * 20  # 9 pt
        style_left = XFStyle()
        style_left.font = font
        style_left.alignment = al

        ws = self.add_sheet(sheet_name)

        for i, row in enumerate(data):
            for j, cell in enumerate(row):

                borders = Borders()

                if i == 0:
                    borders.top = 1
                    borders.bottom = 2

                if i == len(row) - 1:
                    borders.bottom = 1

                if j == 0:
                    borders.left = 1
                    borders.right = 1

                if j == len(row) - 1:
                    borders.right = 1

                if j == 0:
                    _style = style_left
                elif i == 0:
                    _style = style_top
                else:
                    _style = style

                _style.borders = borders

                # one of the libraries can get confused with plain strings
                if isinstance(cell, str):
                    cell = unicode(cell, 'utf-8')

                ws.write(i + 1, j + 1, cell, _style)

        if print_to_screen:
            print print_table(data, sheet_name, bold=True)

if __name__ == "__main__":

    wb = Workbook()
    wb.country_code = 61

    data = [["Acc", "b", "c"], [1, 2, 3], [4, 3, 5]]
    wb.write_sheet(data, "test_sheet", print_to_screen=True)

    wb.save("test.xls")
