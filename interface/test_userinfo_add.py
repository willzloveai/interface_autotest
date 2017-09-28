import requests
import uuid
import json,sys,os
sys.path.append('../function')
from my_unit import MyUnit

base_url = 'https://ebjrd.weshare.com.cn/penguin/v1/userinfo/add?b=0'
bizOrderId = "166c1e87-a533-4c1f-9f5c-9a837b867920"
bizUserGid = "3a889059-fbdf-4550-9291-259c6a662016"
class UserInfo_Add(MyUnit):
    '''用户中心-用户信息上报'''

    def test_userinfo_add_mobile(self):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data_mobile = {"bizOrderId":bizOrderId,
                       "bizUserGid":bizUserGid,"dataTypeEm":"MOBILE",
                       "hashBody":"{\"mobile\":\"13350917565\",\"bizTypeEm\":\"sdjk\",\"bizUserGid\":"+ bizUserGid +",\"dataTypeEm\":\"MOBILE\",\"createTime\":1502940030,\"description\":\"init\"}"
                }
        r = requests.post(url=base_url, data=json.dumps(data_mobile), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['message'],'成功')

    def test_userinfo_add_userbase(self):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data_userbase = {"bizOrderId": bizOrderId,
                         "bizUserGid": bizUserGid, "dataTypeEm": "USER_BASE",
                         "hashBody": "{\"bizOrderId\":"+ bizOrderId+ ",\"name\":\"test47342\",\"idCard\":\"459358199309277549\",\"birthplace\":\"北京\",\"bizUserGid\":"+ bizUserGid +",\"dataTypeEm\":\"USER_BASE\",\"createTime\":1502939764,\"description\":\"init\"}"
                         }
        r = requests.post(url=base_url, data=json.dumps(data_userbase), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['message'],'成功')

    def test_userinfo_add_bankcard(self):
        headers = {"Content-Type": "application/json; charset=utf-8"}
        data_bankcard = {"bizOrderId": bizOrderId,
                         "bizUserGid": bizUserGid, "dataTypeEm": "BANK_CARD",
                         "hashBody": "{\"mobile\":\"13350917565\",\"name\":\"test47342\",\"idCard\":\"459358199301127549\",\"birthplace\":\"北京\",\"cardMobile\":\"13345647342\",\"cardNo\":\"6222600840000947342\",\"holderName\":\"test47342\",\"cardTypeEm\":\"DEBIT\",\"bankBinName\":\"中国交通银行\",\"bindTypeEm\":\"VERIFIED\",\"bizUserGid\":"+ bizUserGid +",\"dataTypeEm\":\"BANK_CARD\",\"createTime\":1502953346,\"bizOrderId\":"+bizOrderId+"}"
                         }
        r = requests.post(url=base_url, data=json.dumps(data_bankcard), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['message'],'成功')

if __name__=="__main__":
    MyUnit.main()