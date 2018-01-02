import xlwt
import xlrd
from xlutils.copy import copy
'''修改一个已存在的excel中的某一单元格的值'''
# #使用xlrd读取指定excel工作中的指定表格的值并返回
# def excel_read(doc,table,x,y):
#      data = xlrd.open_workbook(doc)
#      table = data.sheet_by_name(table)
#      return table.cell(x,y).value
#
# #使用xlwt创建指定excel工作中的指定表格的值并保存
# def excel_create(sheet,value):
#      data = xlwt.Workbook()
#      table = data.add_sheet(sheet)
#      table.write(1,4,value)
#      data.save('demo.xls')

#三个结合操作同一个excel
rb = xlrd.open_workbook('demo.xls')
#管道作用
wb = copy(rb)
#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)  #1代表是写到第几个工作表里，从0开始算是第一个。
ws.write(1, 6, '2changed!')
wb.save('demo.xls')
