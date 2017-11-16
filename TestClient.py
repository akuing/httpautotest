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
#
# 1.接口的请求地址：http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/client
# 2.该接口的功能描述：增加client信息
# 3.该接口请求是：put
# 4.该接口需要在登陆情况下才有用吗？需要登录
# 5.该接口有上送数据吗？上送的数据是什么？有
# fullname "xiaohua"
# pCountry "USA"
# producerGroup "GPT3"
# status "active"
# 6.该接口返回的状态码是多少？200
# 7.该接口返回报文体的格式和编码是什么？
# application/json;charset=UTF-8
# 8.该接口返回的内容是什么？{"code":0,"msg":"OK","data":null}
#
# 1.接口的请求地址：http://ecsystemtestjava-env.us-east-2.elasticbeanstalk.com/api/client/
# 2.该接口的功能描述：返回所有client列表信息
# 3.该接口请求是：post
# 4.该接口需要在登陆情况下才有用吗？需要登录
# 5.该接口有上送数据吗？上送的数据是什么？有
# page 1
# 6.该接口返回的状态码是多少？200
# 7.该接口返回报文体的格式和编码是什么？application/json;charset=UTF-8
# 8.该接口返回的内容是什么？
# {"code":0,"msg":null,"data":{"items":[{"id":1,"producerGroup":"JD Farms","accountId":"17-1014-","fullname"
# :"full name","shortname":"xx","contactName":"contact person","contactPhone":"phone number","contactEmail"
# :"email","pStreet":"street","pCity":"city","pState":"aa","pPostal":"1111111","pCountry":"country","status"
# :"active","inactiveReason":null,"lastExpiry":null,"renewReady":null,"notes":"notes","created":1507964512000
# },{"id":4,"producerGroup":"JD Farms","accountId":"17-1015-","fullname":"fsd","shortname":null,"contactName"
# :"fds","contactPhone":"ffds","contactEmail":"fds","pStreet":null,"pCity":"fds","pState":null,"pPostal"
# :null,"pCountry":null,"status":"active","inactiveReason":"fff","lastExpiry":null,"renewReady":null,"notes"
# :null,"created":1508056778000},{"id":5,"producerGroup":"Pineland","accountId":"17-1023-","fullname":"qqqq"
# ,"shortname":null,"contactName":"qqq","contactPhone":"qq","contactEmail":"qq","pStreet":"qqq","pCity"
# :null,"pState":null,"pPostal":null,"pCountry":null,"status":"active","inactiveReason":"qqqqqq","lastExpiry"
# :null,"renewReady":null,"notes":null,"created":1508760052000},{"id":6,"producerGroup":"JD Farms","accountId"
# :"17-1026-","fullname":"sunn","shortname":null,"contactName":null,"contactPhone":"12345675554","contactEmail"
# :null,"pStreet":null,"pCity":null,"pState":null,"pPostal":null,"pCountry":null,"status":"active","inactiveReason"
# :"switched certifier","lastExpiry"