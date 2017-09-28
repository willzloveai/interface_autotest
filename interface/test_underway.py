import unittest
import requests
import uuid
import json
import sys,os
sys.path.append('..')
sys.path.append('../function')
from my_excel import Excel
# from mysql_db import DB
from logger import Log

class UnderWay(unittest.TestCase):
    """匹配系统：借款"""
    def setUp(self):
        self.base_url = 'https://ebjrd.weshare.com.cn/pine2/loan/underway'
        self.loan_gid = str(uuid.uuid1())               #使用uuid库生成唯一ID
        self.sheet_name = 'underway'
        self.el = Excel()
        self.log = Log()

    def tearDown(self):
        self.log.info(self.result)

    def test_underway_success(self):
        '''借款成功'''
        headers = self.el.GetDetialData(self.sheet_name,1,2)
        data = self.el.GetDetialData(self.sheet_name,1,3)
        headers = eval(headers)
        data = eval(data)
        #loanRecordGid赋唯一值
        data['loanRecordGid'] = self.loan_gid
        #self.log.info(data)
        r = requests.post(url=self.base_url, data=json.dumps(data), headers=headers)
        self.result = r.json()
        self.assertEqual(self.result['returnCode'],'0000')
        self.assertEqual(self.result['returnDesc'],'成功')

if __name__ == "__main__":
    unittest.main()
