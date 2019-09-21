"""

======================

@author:niuqun

@time:2019/9/17:8:10 PM

@email:17689551930@163.com

======================

"""
import json
from case import data_config
from confing.operation_excel import OpenrationExcel
class GetData:
    def __init__(self):
        self.opera_excel=OpenrationExcel()
    def get_case_lines(self):
        return self.opera_excel.get_lines()#获取excel行数

    # 用例id
    def get_case_id(self,row):
        col=int(data_config.get_excel_id())
        case_id=self.opera_excel.get_cell_value(row,col)
        return case_id

    # 返回name
    def get_name(self, row):
        col = int(data_config.get_excel_name())
        name_Data = (self.opera_excel.get_cell_value(row, col))
        return name_Data

    # 获取url
    def get_url(self,row):
        col=int(data_config.get_excel_url())
        url_data=self.opera_excel.get_cell_value(row,col)
        return url_data

    # 判断是否运行
    def get_is_run(self, row):
        flag = None
        col = int(data_config.get_excel_run())
        run_model = self.opera_excel.get_cell_value(row, col)  # 获取是否运行内容
        if run_model == "yes":
            flag = True
        else:
            flag = False
        return flag
    #返回请求方式
    def git_method_way(self,row):
        col=int(data_config.get_excel_request_way())
        get_way=self.opera_excel.get_cell_value(row,col)
        return  get_way

    # 获取依赖数据


    def is_depend(self,row):
        col=int(data_config.get_excel_data_depend())
        api_data = self.opera_excel.get_cell_value(row, col)
        return api_data
    # 获取请求数据
    def get_api_data(self,row):
        col=int(data_config.get_excel_data())
        data=self.opera_excel.get_cell_value(row,col)
        return data
    # 获取实际结果
    def write_result(self,row,value):
        col=int(data_config.get_excel_resuit())
        result=(self.opera_excel.get_cell_value(row,col))
        return result
    # 获取预期结果
    def get_expcet_data(self,row):
        col=int(data_config.get_excel_expect())
        expect=self.opera_excel.get_cell_value(row,col)
        return expect
    # 获取接口返回数据

    def get_api_return_data(self,row):
        col=int(data_config.get_excel_aip_data())
        api_data=self.opera_excel.get_cell_value(row,col)
        return api_data

    #获取更换数据字段
    def get_field_depend(self,row):
        col=int(data_config.get_excel_field_depend())
        field=self.opera_excel.get_cell_value(row,col)
        return field
    # 将接口返回数据写入依赖接口数据中
    def write_api_return_data(self, row, value):
        col = int(data_config.get_excel_aip_data())
        self.opera_excel.write_value(row, col, value)
    # 将实际结果写入excel
    def write_resuit(self,row,value):
        col=int(data_config.get_excel_resuit())
        self.opera_excel.write_value(row,col,value)
        # 接受的参数
    def get_data_depend_new(self,row):
        col=int(data_config.get_excel_data_depend_new())
        new_data=self.opera_excel.get_cell_value(row,col)
        return new_data


