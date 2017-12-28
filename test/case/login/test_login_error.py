# coding=utf-8
"""
author:
date:
brief:
"""

import requests
import urllib3
import os
import unittest
from common.logger import Log


urllib3.disable_warnings()

class TestLong(unittest.TestCase):
    """username, password error"""

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
        result = r.json()
        return result

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

    def test_username_error(self):
        try:
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
            username = "test2@test1.com"
            password = "111111"
            result_json = self.login(url, username, password, self.s)
            self.log.info("错误的用户名，登录")
            self.assertEqual("Login Error!  Please try enter.", result_json['msg'])
            self.log.info("通过测试")
        except Exception as msg:
            self.log.info("没有通过该测试，原因为：%s" % msg)
            raise

    def test_password_error(self):
        try:
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
            username = "test2@test.com"
            password = "1111111"
            result_json = self.login(url, username, password, self.s)
            self.log.info("错误的密码，登录")
            self.assertEqual("Login Error!  Please try enter.", result_json['msg'])
            self.log.info("通过测试")
        except Exception as msg:
            self.log.info("没有通过该测试，原因为：%s" % msg)
            raise

    def test_login(self):
        try:
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
            username = "test2@test.com"
            password = "111111"
            result_json = self.login(url, username, password, self.s)
            self.log.info("正确是用户名和密码，登录")
            self.assertEqual("test2@test.com", result_json['data']["username"])
            self.log.info("通过测试")
        except Exception as msg:
            self.log.info("没有通过该测试，原因为：%s" % msg)
            raise


if __name__ == '__main__':
    unittest.main()

