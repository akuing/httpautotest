# coding=utf-8
"""
author:
date:
brief:
"""

import requests
import urllib3
import unittest
import os
from common.logger import Log

urllib3.disable_warnings()

def forgot(url, username):
    s = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36"
    }
    data = {
        "username": username
    }
    r = s.post(url, json=data, headers=headers, verify=False)
    result = r.json()
    s.close()
    return result

class TestForgot(unittest.TestCase):
    """测试找回密码"""
    @classmethod
    def setUpClass(cls):
        cls.file_name = os.path.basename(__file__)
        cls.log = Log()
        cls.log.info(r"%s:测试开始" % cls.file_name)

    @classmethod
    def tearDownClass(cls):
        cls.log.info(u"%s:测试结束" % cls.file_name)
        cls.log.info(u"=" * 60)


    def test_username_error(self):
        try:
            self.log.info(u"没有注册的用户名")
            url = "http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/forget"
            username = "admin"
            result = forgot(url, username)
            self.assertEqual('Account Invalid!', result['msg'])
            self.log.info(r"测试结束，与预期的相同")
        except Exception as msg:
            self.log.info(u'测试结果，两者不相等 %s' % msg)
            raise

if __name__ == '__main__':
    unittest.main()
