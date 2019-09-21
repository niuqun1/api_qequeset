"""

======================

@author:niuqun

@time:2019/9/17:7:46 PM

@email:17689551930@163.com

======================

"""
import requests
import json


class RunMethod:
    def post_main(self, url, data, header=None):  # post请求
        res = None
        if header != None:  # 若果header不为空
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def get_main(self, url, data=None, header=None):  # get请求
        res = None
        if header != None:
            res = requests.get(url=url, params=data, headers=header)
            print(res.url)
        else:
            res = requests.get(url=url, params=data)
        return res.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':  # 判断请求方式
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)  # 格式化返回值


if __name__ == '__main__':
    url = 'https://test.duyaya.com/aienglish-course/api/v1/course/list'
    data = '{"kidId":615}'
    Headers = {
        "Content-Type": "application/json",
        'x-target-app': 'app_xiaomada_android',
        'Authorization': 'O3j9oo8P2q8yOdBSEvcbEyQX7D/9Su5B3UJKXR0OwoXfMGhsGOOAKCothsnD9FwB'
    }
    print(type(data))
    run = RunMethod()
    meder='get'
    if meder !='podt':
        datas=eval(data)
    print(run.run_main(meder, url, datas, Headers))
    print(Headers)
