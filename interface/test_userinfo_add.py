import requests
import uuid
import json,sys,os
sys.path.append('../function')
from my_unit import MyUnit

base_url = ''
class UserInfo_Add(MyUnit):

    def test_userinfo_add_mobile(self):
        headers = {}
        data_mobile = {}
        r = requests.post(url=base_url, data=json.dumps(data_mobile), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['status'],0)
        self.assertEqual(self.result['message'],'成功')



if __name__=="__main__":
    MyUnit.main()