"""

======================

@author:niuqun

@time:2019/9/19:7:14 PM

@email:17689551930@163.com

======================

"""
# 判断实际结果与预期做对比
class CommonUtil:
    def is_contain(self,str_one=None,str_two=None):# 判断预期跟实际是否一致
        if str_one=="":
            print("没有预期结果无法对比")
        else:
            flag=None
            if str_one in str_two:
                flag =True
            else:
                flag=False
            return flag
if __name__ == '__main__':
    abc=CommonUtil