# coding=utf-8
"""
author:
date:
brief:
"""

import requests
import urllib3
import unittest
from common.logger import Log
import os

file_name = os.path.basename(__file__)

class TestLogin(unittest.TestCase):
    """测试登录"""

    def login(self, username, password, url):
        urllib3.disable_warnings()
        s = requests.session()
        data = {
            "username": username,
            "password": password
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
        }
        r = s.post(url, headers=headers, json=data, verify=False)
        result = r.json()
        s.close()
        return result

    @classmethod
    def setUpClass(cls):
        cls.file_name = os.path.basename(__file__)
        cls.log = Log()
        cls.log.info(u"%s：测试开始" % cls.file_name)

    @classmethod
    def tearDownClass(cls):
        cls.log.info(u"%s：测试结束" % cls.file_name)
        cls.log.info(u"=" * 60)

    def test_username_password_error(self):
        try:
            self.log.info(u"用户登录,错误的账号密码")
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
            username = "admin"
            password = "123456"
            json = self.login(username, password, url)
            self.assertEqual("Login Error!  Please try enter.", json['msg'])
            self.log.info(u"测试通过")
        except Exception as msg:
            self.log.info(u"测试未通过，原因：%s" % msg)
            raise

if __name__ == '__main__':
    unittest.main()
