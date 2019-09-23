# """
#
# ======================
#
# @author:niuqun
#
# @time:2019/9/19:7:18 PM
#
# @email:17689551930@163.com
#
# ======================
#
# """
# coding:utf-8
import sys
import json

from confing.operation_excel import OpenrationExcel
from base.runmethod import RunMethod
from get_data.get_data import GetData
from jsonpath_rw import jsonpath, parse


class DependdentData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.opera_excel = OpenrationExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    # 返回依赖数据的data
    def run_dependent(self):
        # 获取依赖id所在的行
        row_num = self.opera_excel.get_row_num(self.case_id)
        # 获取依赖id的接口返回数据
        res = self.data.get_api_return_data(row_num)
        return json.loads(res)

    # 根据依赖的key去获取执行依赖测试case的响应,然后返回
    def get_data_for_key(self, row,new_data):
        """
        :param row: 传入行
        :param new_data:传入要修改的数据
        :return:
        """
        # 获取接受的字段
        if new_data !='':
            data_new=json.loads(new_data)
            depend_key = self.data.get_data_depend_new(row)
            depend_key_new = depend_key.split(';')
            if depend_key != '':
                for key in range(len(depend_key_new)):
                    # 获取数据依赖字段
                    depend_data = self.data.get_field_depend(row)
                    depend_data_new = depend_data.split(';')
                    # 获取依赖数据
                    response_data = self.run_dependent()
                    # 获取依赖字段
                    json_exe = parse(depend_data_new[key])
                    madle = json_exe.find(response_data)
                    new_data = [math.value for math in madle][0]
                    data_new[depend_key_new[key]] = new_data
                return json.dumps(data_new)
            else:
                return json.dumps(data_new)
        else:
            return None



if __name__ == '__main__':
    order = {
	"code": 10000,
	"message": "成功",
	"data": {
		"kidId": 615,
		"lessonId": 22,
		"timePosions": [{
			"sessionNo": 0,
			"startTime": 1569204000,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": 1681,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "true"
		}, {
			"sessionNo": 1,
			"startTime": 1569207600,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -1918,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 2,
			"startTime": 1569211200,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -5518,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 3,
			"startTime": 1569214800,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -9118,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 4,
			"startTime": 1569218400,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -12718,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 5,
			"startTime": 1569222000,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -16318,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 6,
			"startTime": 1569229200,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -23518,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 7,
			"startTime": 1569236400,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -30718,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 8,
			"startTime": 1569240000,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -34318,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 9,
			"startTime": 1569247200,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -41518,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}, {
			"sessionNo": 10,
			"startTime": 1569250800,
			"duration": 1382,
			"severTime": 1569205681,
			"timePos": -45118,
			"closeTimeBuffer": 60,
			"enterTimeBuffer": 180,
			"joinable": "false",
			"attended": "false"
		}]
	},
	"parameter": "null"
}
    res = "data.timePosions.1"

    json_exe = parse(res)
    madle = json_exe.find(order)
    print([math.value for math in madle][0])
