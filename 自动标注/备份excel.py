import time
import openpyxl


xlsx_address = r'C:\Users\温柔的小茶花\Desktop\样本9\算法挖掘数据样本9-王二-00-00.xlsx'
new_xlsx_address_1 = r'C:\Users\温柔的小茶花\Desktop\样本9\备份\time'
new_xlsx_address_2 = time.strftime('%m-%d__%H_%M')
new_xlsx_address_3 = '.xlsx'
new_xlsx_address = new_xlsx_address_1 + new_xlsx_address_2 + new_xlsx_address_3
print(new_xlsx_address)
# 1.打开文件
workbook = openpyxl.load_workbook(xlsx_address)
# 2.保存文件
workbook.save(new_xlsx_address)
