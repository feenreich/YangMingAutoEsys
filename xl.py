import xlrd
import pprint
import time

wb = xlrd.open_workbook('family_E.xlsx')
sheet = wb.sheet_by_name('sheet1')

def get_list_2d_all(sheet):
    return [sheet.row_values(row) for row in range(sheet.nrows)]

list = get_list_2d_all(sheet)

i = 0
district = sheet.cell_value(i,0)
name = sheet.cell_value(i,1)
date = sheet.cell_value(i,2)
stime = sheet.cell_value(i,3)
stime_h = stime[0:2]
stime_m = stime[3:5]
etime = sheet.cell_value(i,4)
etime_h = etime[0:2]
etime_m = etime[3:5]
job_title = sheet.cell_value(i,5)
way = sheet.cell_value(i,6)
objects = sheet.cell_value(i,7)
reason = sheet.cell_value(i,8)
content = sheet.cell_value(i,9)
memo = sheet.cell_value(i,10)

#xlrd.xldate_as_tuple(cell.value,0)
time.sleep(5.5)