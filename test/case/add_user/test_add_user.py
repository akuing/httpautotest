# coding=utf-8
"""
author:
date:
brief:
"""

import requests
import unittest
from common.logger import Log
import urllib3
import os

urllib3.disable_warnings()
class Test_add_user(unittest.TestCase):

    def login(self, url, username, password, s):
        """登录"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/62.0.3202.94 Safari/537.36",
            "Cookie": "JSESSIONID=2DCC3BC8B087AA0E0256F084EB77B3E8"
        }
        data = {
            "username": username,
            "password": password
        }

        r = s.post(url, json=data, headers=headers, verify=False)
        token = r.json()['data']['token']
        return token

    @classmethod
    def setUpClass(cls):
        cls.file_name = os.path.basename(__file__)
        cls.log = Log()
        cls.log.info(r"%s:测试开始" % cls.file_name)

    @classmethod
    def tearDownClass(cls):
        cls.log.info(u"%s:测试结束" % cls.file_name)
        cls.log.info(u"=" * 60)

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        self.s.close()

    def test_add_user(self):
        url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
        username = "test2@test.com"
        password = "111111"
        token = self.login(url, username, password, self.s)
        try:
            self.log.info(u"添加用户")
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/client"
            data = {
                "fullname": "1",
                "producerGroup": "Pineland",
                "status": "active",
                "pCountry": "USA",
                "shortname": "1",
                "species": "C",
                "pPostal": "1",
                "pState": "1",
                "pCity": "1",
                "pStreet": "1",
                "contactEmail": "1",
                "contactPhone": "1",
                "contactName": "1",
                "inactiveReason": "failed inspection",
                "lastExpiry": "11"
            }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/62.0.3202.94 Safari/537.36",
                "Authorization": token,
                "Content-Type": "application/json;charset=UTF-8"}
            url1 = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/client"
            result = self.s.put(url1, json=data, headers=headers)
            self.assertEqual("OK", result.json()['msg'])
            self.log.info("通过测试")
        except Exception as msg:
            self.log.info("未通过测试，原因为：%s" % msg)
            raise

if __name__ == '__main__':
    unittest.main()