import unittest
import requests
import json

class TestLogin(unittest.TestCase):
    url="http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
    def testReturnLoginErrorWhenWrongUserOrPasswd(self):
        # headers={"Content-Type":"application/json;charset=UTF-8"}
        userinfo={"username":"user","password":"pass"}
        session = requests.session()
        result = session.post(self.url,json=userinfo)
        self.assertEqual("Login Error!",result.json()["msg"])
        session.close()


if(__name__ == "__main__"):
    unittest.main(verbosity=2)