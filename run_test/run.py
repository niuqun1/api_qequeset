"""

======================

@author:niuqun

@time:2019/9/17:8:29 PM

@email:17689551930@163.com

======================

"""
# coding:utf-8
from base.base import RunMethod
from get_data.get_data import GetData
from confing.comonutil import CommonUtil
from confing.dependdent_data import DependdentData
from get_data import tonkes
import json
host_test='https://test.duyaya.com'
class RunTest:
    def __init__(self):
        self.run_method=RunMethod()
        self.data=GetData()
        self.com_util=CommonUtil()
    # 程序执行流程
    def go_on_run(self):
        res=None
        # 获取所有行
        roes_count=self.data.get_case_lines()
        # 跳过1在行里循环
        for i in range(1,roes_count):
            is_run = self.data.get_is_run(i)
            if is_run:#执行
                urls=self.data.get_url(i)#接口地址
                url=host_test+urls
                method=self.data.git_method_way(i)#请求方
                former=self.data.get_api_data(i)#请求数据
                expect=self.data.get_expcet_data(i)#预期结果
                header=tonkes.gain_herder()#获取header
                depend_case=self.data.is_depend(i)#获取是否有数据依赖
                if depend_case !=None:#判断数据依赖不是空
                    self.depend_data=DependdentData(depend_case)#实列化depend_data
                    data=self.depend_data.get_data_for_key(i,former)#获取依赖返回data
                res=self.run_method
                if is_run:#判断是否执行
                    res=self.run_method.run_main(method,url,data,header)
                    self.data.write_api_return_data(i,res)
                    if self.com_util.is_contain(expect,res):#判断预期结果
                        self.data.write_resuit(i,"测试通过")
                    else:
                        self.data.write_resuit(i,"测试失败")

if __name__=="__main__":
    run=RunTest()
    print(run.go_on_run())



