Function to print ascii tables out.

```python

 wb = Workbook()
 wb.country_code = 61

 data = [['a','b','c'],[1,2,3],[4,5,6]]
 write_sheet(wb, data, "test_sheet", print_to_screen=True)  # add one sheet

  +---+---+----+
  | a | b |  c |
  +---+---+----+
  | 1 | 2 |  3 |
  | 4 | 5 | 60 |
  +---+---+----+

 wb.save("test.xls")
 # now, will have a xls spreadsheet
```

Code
```python

#pip install xlutils
#pip install xlwt
from xlwt import Workbook, Font, XFStyle, Borders, Alignment


def print_table(data, title="", bold=True):

    '''fancy ascii table'''

    maxs = []

    for row in data:
        for i, cell in enumerate(row):
            if len(maxs) <= i:
                maxs.append(0)
            if len(str(cell)) > maxs[i]:
                maxs[i] = len(str(cell))

    tb = "+-" + "-+-".join(["-" * m for m in maxs]) + "-+"
    print
    if title:
        if bold:
            print "*** \033[31m" + title + "\033[0m ***"
        else:
            print "*** " + title + " ***"
        print
        print tb

                #_row = ['\033[1m%s\033[0m' % r for r in row]
    for j, row in enumerate(data):

        text = []
        for i, cell in enumerate(row):

            if i > 0:
                cell = str(cell).rjust(maxs[i])
            else:
                cell = str(cell).ljust(maxs[i])

            if bold:
                if j == 0 or i == 0:
                    cell = '\033[32m%s\033[0m' % str(cell)

            text.append(cell)

        print "| " + " | ".join(text) + " |"
        if j == 0:
            print tb
    print tb


def write_sheet(wb, data, sheet_name, print_to_screen=False):
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

    ws = wb.add_sheet(sheet_name)

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
            ws.write(i + 1, j + 1, cell, _style)

    if print_to_screen:
        print print_table(data, sheet_name, bold=True)

if __name__ == "__main__":

    wb = Workbook()
    wb.country_code = 61

    data = [["Acc", "b", "c"], [1, 2, 3], [4, 3, 5]]
    write_sheet(wb, data, "test_sheet", print_to_screen=True)

    wb.save("test.xls")

```