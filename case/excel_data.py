"""

======================

@author:niuqun

@time:2019/9/17:7:54 PM

@email:17689551930@163.com

======================

"""
#coding:utf-8
class global_var:
    id = "0"  # 用例id
    name = "1"  #接口昵称
    url = '2'  # 测试接口地址
    run = '3'  # 是否允许
    request_way = '4'  # 接口请求类型
    data_depend = "5"  # 依赖数据的data
    field_depend = "6"  # 数据依赖字段
    data = "7"  # 接口请求数据
    expect = "8"  # 预期结果
    resuit = "9"  # 实际结果
    data_depend_new = "10" #接受参数的接口数据
    api_return_data = "11"  # 接口返回数据
    # 用例id
# 返回id
def get_excel_id():
    return global_var.id
# 返回接口昵称
def get_excel_name():
    return global_var.name
# 返回接口地址
def get_excel_url():
    return global_var.url
# 返回是否运行
def get_excel_run():
    return global_var.run
# 返回请求方式
def get_excel_request_way():
    return global_var.request_way
# 返回依赖数据
def get_excel_data_depend():
    return global_var.data_depend
# 返回需要更换的字段
def get_excel_field_depend():
    return  global_var.field_depend
# 返回请求数据
def get_excel_data():
    return global_var.data
# 返回预期结果
def get_excel_expect():
    return global_var.expect
# 返回实际结果
def get_excel_resuit():
    return global_var.resuit
# 返回接口返回数据
def get_excel_aip_data():
    return global_var.api_return_data
def get_excel_data_depend_new():
    return global_var.data_depend_new



