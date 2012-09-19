print_to_table
==============

Print a simple data structure to a ASCII table, or to a Excel Spreedsheet

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

Requirements
============

    pip install xlutils
    pip install xlwt
