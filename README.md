workbook
==============

Print a simple data structure to a ASCII table, or to a Excel Spreedsheet

To print an ascii table out,

```python

from workbook import print_table

data = [['a','b','c'],[1,2,3],[4,5,6]]
print_table(data, "Title")

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

from workbook import Workbook, write_sheet

wb = Workbook()
wb.country_code = 61

data = [['a','b','c'],[1,2,3],[4,5,6]]
write_sheet(wb, data, "test_sheet", print_to_screen=True)  # add one sheet

*** test_sheet ***

  +---+---+----+
  | a | b |  c |
  +---+---+----+
  | 1 | 2 |  3 |
  | 4 | 5 | 60 |
  +---+---+----+

write_sheet(wb, data, "2nd_sheet", print_to_screen=False)  # add another

wb.save("test.xls")  # now, will have a xls spreadsheet
```

Installation
============

    pip install workbook

