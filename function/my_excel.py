import xlrd,os,itertools
import xlwt
from logger import Log

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
# file_path = base_dir + "/data/interface.xlsx"
file_path = "e:/interface.xlsx"
mylist = []
class Excel:
    def __init__(self):
        self.log = Log()
        try:
            self.el = xlrd.open_workbook(file_path)
        except Exception as e:
            self.log.error('[Excel]filepath is wrong:%s'%e)



    #获取指定sheet所有值,行循环
    def GetAllExcelData(self,sheet_name):
        try:
            table = self.el.sheet_by_name(sheet_name)
            #获取总行数
            nrows = table.nrows
            for i in range(nrows):
                #print(table.row_values(i))
                return table.row_values(i)
        except Exception as e:
            self.log.error('[Excel]GetAllExcelData:%s'%e)

    #获取某一行所有值
    def GetRowsData(self,sheet_name,row_num):
        try:
            table = self.el.sheet_by_name(sheet_name)
            try:
                #print(table.col_values(row_num))
                return table.row_values(row_num)
            except Exception as e:
                self.log.error('[Excel]GetRowsData:%s'%e)
        except Exception as e:
            self.log.error('[Excel]GetRowsData:%s'%e)

    #获取某一列所有值
    def GetColsData(self,sheet_name,col_num):
        try:
            table = self.el.sheet_by_name(sheet_name)
            try:
                #print(table.col_values(col_num))
                return table.col_values(col_num)
            except Exception as e:
                self.log.error('[Excel]GetColsData:%s'%e)
        except Exception as e:
            self.log.error('[Excel]GetColsData:%s'%e)

    def GetDetialData(self,sheet_name,row_num,col_num):
        try:
            table = self.el.sheet_by_name(sheet_name)
            try:
                nrows = table.row(row_num)[col_num].value
                #print(table.row(row_num)[col_num])
                return nrows
            except Exception as e:
                self.log.error('[Excel]GetDetialData:%s'%e)
        except Exception as e:
            self.log.error('[Excel]GetDetialData:%s'%e)

class MyExcel:
    def __init__(self):
        # self.log = Log()
        try:
            self.el = xlrd.open_workbook(file_path)
        except Exception as e:
            self.log.error('[Excel]filepath is wrong:%s'%e)

    def myexcel(self):
        global mylist
        for sheet in self.el.sheets():
            try:
                mykeys = sheet.row_values(0)
                nrows = sheet.nrows
                for i in range(1,nrows):
                    myvalues = sheet.row_values(i)
                    mydict = dict(zip(mykeys,myvalues))
                    mylist.append(mydict)
            except Exception as e:
                self.log.error('myexcel' % e)
        return(mylist)
    #测试功能
if __name__ == '__main__':
    el = MyExcel()
    als = el.myexcel()
    # print(als)
    # print(als[1]['描述'])
    for i in range(len(als)):
        print(als[i]['header'],als[i]['json'])
