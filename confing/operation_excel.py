"""

======================

@author:niuqun

@time:2019/9/17:8:04 PM

@email:17689551930@163.com

======================

"""
import xlrd
from xlutils.copy import copy
class OpenrationExcel:
    def __init__(self,file_name=None,sheet_id=None):
        """

        :param file_name: excel的存储路径
        :param sheet_id:
        """
        if file_name:
            self.file_name=file_name
            self.sheet_id=sheet_id
        else:
            self.file_name='/Users/edz/Desktop/python_requese/data/data_test_api.xlsx'
            self.sheet_id=0
        self.data=self.get_data()
    # 获取sheets内容
    def get_data (self):
        data = xlrd.open_workbook(self.file_name,)
        tables = data.sheets()[self.sheet_id]
        return tables
    # 获取总行数
    def get_lines(self):
        tables=self.data
        return tables.nrows
    # 获取单元格内容
    def get_cell_value(self,row,col):
        """

        :param row: excel行
        :param col: excel列
        :return:
        """
        return self.data.cell_value(row,col)
    # 将数据写入excel
    def write_value(self,row,col,vale):
        """

        :param row:
        :param col:
        :param vale: 数据
        :return:
        """
        read_data=xlrd.open_workbook(self.file_name)
        write_data=copy(read_data)
        sheet_data=write_data.get_sheet(0)
        sheet_data.write(row,col,vale)
        write_data.save(self.file_name)
    # 根据csse_id 找到对应行的内容
    def get_rows_data(self,casr_id):
        row_num=self.get_row_num(casr_id)
        rows_data=self.get_row_values(row_num)
        return rows_data

   # 根据data找到对应行
    def get_row_num(self,case_id):
        num= 0
        clols_data=self.get_cols_data()#返回一行内容
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num=num+1
   # 获取一行内容
    def get_row_values(self,row):
        tables=self.data
        row_data=tables.row_values(row)
        return row_data
    # 获取某一列内容
    def get_cols_data(self,col_id=None):
        if col_id!=None:
            cols=self.data.col_values(col_id)
        else:
            cols=self.data.col_values(0)
        return cols
if __name__=='__main__':
    Opers=OpenrationExcel()
    b=Opers.get_row_num("a11")
    print(b,"b")


