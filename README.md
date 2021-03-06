[![Build Status](https://secure.travis-ci.org/daleobrien/workbook.png)](http://travis-ci.org/daleobrien/workbook)

Workbook
==============

Print a simple data structure to a ASCII table, or to a Excel Spreedsheet

To print an ascii table out,

```python

from workbook import print_table

data = [['a','b','c'],[1,2,3],[4,5,6]]
print_table(data, "Title")
```
produces,
```
*** Title ***

+---+---+---+
| a | b | c |
+---+---+---+
| 1 | 2 | 3 |
| 4 | 5 | 6 |
+---+---+---+
```

To create an excel workbook,
```python

from workbook import Workbook

wb = Workbook()
wb.country_code = 61

data = [['a','b','c'],[1,2,3],[4,5,6]]
wb.write_sheet(data, "test_sheet", print_to_screen=True)  # add one sheet
```
produces,
```
*** test_sheet ***

  +---+---+----+
  | a | b |  c |
  +---+---+----+
  | 1 | 2 |  3 |
  | 4 | 5 | 60 |
  +---+---+----+
```

To save,
```python

wb.write_sheet(data, "2nd_sheet", print_to_screen=False)  # add another
wb.save("test.xls")  # now, will have a xls spreadsheet
```

Installation
============

    pip install workbook

