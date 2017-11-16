import unittest
import requests
import json
class testAddClient(unittest.TestCase):
    url1="http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/auth/login"
    url2="http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/client"
    def testReturnOKWhenAddAnyClient(self):
        data1={"password":"Password is not right.","username":"test3@test.com"}
        data2={"fullname":"xiaohua","pCountry":"USA","producerGroup":"GPT3","status":"active"}
        session=requests.session()
        result1=session.post(self.url1,json=data1)
        token=result1.json()["data"]["token"]
        headers = {"Content-Type": "application/json;charset=UTF-8", "Authorization": token}
        result2=session.put(self.url2,json=data2,headers=headers)
        self.assertEqual("OK",result2.json()["msg"])
        session.close()
if (__name__=="__main__"):
    unittest.main(verbosity=2)
