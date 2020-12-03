import requests
import unittest
from common import test_get_post
from common.test_get_post import Method


class Case(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试环境搭建")

    def setUp(self):
        self.run = Method()
    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        print("测试用例导入完成")


    def test_case01(self):
        url='https://api.ximalaya.com/iot/openapi-smart-device-api/customized/recommend/guess-like?access_token=249e546c83c1465179e7bddb1ca83117&app_key=2e433f48db40f9e4fc4a371bd3cfb07b&app_version=4.0.0&client_os_type=2&device_id=api-caller&nonce=1606807796789&pack_id=com.ximalaya.ting.android.car.innertest&timestamp=1606807796789&sig=7e5d0c83b23d36feb2e1d43d20d01983'
        params={"access_token":"249e546c83c1465179e7bddb1ca83117","app_key":"2e433f48db40f9e4fc4a371bd3cfb07b",
                "app_version":"4.0.0","client_os_type":"2","device_id":"api-caller","nonce":"1606807796789","pack_id":
                "com.ximalaya.ting.android.car.innertest","timestamp":"1606807796789","sig":"48c0cd45ae761d369b9655ef6cd61853"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        res=self.run.run_main(url,None,None,None,'GET')
        print(res)



    def test_case02(self):
        url='https://api.ximalaya.com/iot/openapi-smart-device-api/subscribe/add?access_token=249e546c83c1465179e7bddb1ca83117&app_key=2e433f48db40f9e4fc4a371bd3cfb07b&app_version=4.0.0&client_os_type=2&device_id=api-caller&id=32988180&nonce=1606808672786&pack_id=com.ximalaya.ting.android.car.innertest&timestamp=1606808672786&sig=bcf5dae2924662d62969dab065987b8a'
        headers={"Content-Type":"application/x-www-form-urlencoded"}
        data = {"access_token": "249e546c83c1465179e7bddb1ca83117", "app_key": "2e433f48db40f9e4fc4a371bd3cfb07b",
                  "app_version": "4.0.0", "client_os_type": "2", "device_id": "api-caller", "id": "32988180",
                  "pack_id":"com.ximalaya.ting.android.car.innertest", "timestamp": "1606808672786",
                  "sig": "bcf5dae2924662d62969dab065987b8a"}

        res=self.run.run_main(url,data,None,headers,'POST')
        print(res)






