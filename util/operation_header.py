"""

======================

@author:niuqun

@time:2019/9/20:9:49 PM

@email:17689551930@163.com

======================

"""
from jsonpath_rw import parse
import json
from confing.operation_excel import OpenrationExcel
def gain_herder():
    herder = {
        "Content-Type": "application/json",
        'x-target-app': 'app_xiaomada_android',
        'Authorization':''

    }
    opera_excel = OpenrationExcel()
    d=opera_excel.get_cell_value(1,11)
    data=json.loads(d)
    res = "data.accessToken"
    json_exe = parse(res)
    madle = json_exe.find(data)
    new=[math.value for math in madle][0]
    token='Authorization'
    herder[token] = new
    return herder