import unittest
import requests
import uuid
import json
import sys,os
sys.path.append('..')
sys.path.append('../function')
from my_excel import Excel
from mysql_db import DB
from logger import Log

class Repayment(unittest.TestCase):
    """匹配系统：还款"""
    def setUp(self):
        self.base_url = 'https://ebjrd.weshare.com.cn/pine2/loan/repayment'
        self.repayment_gid = str(uuid.uuid1())
        self.log = Log()
        self.el = Excel()
        self.sheet_name = 'repayment'
        self.table_name = 'creditor_registration'
        self.db = DB()
        #借款金额，借款记录gid，用户gid
        self.sql1 = {'fields':'max(id)','where':{'name':'张伟豪'}}
        self.sql2 = {'fields':'loan_amount,loan_record_gid,user_gid,due_time','where':{'id':'1234'}}

    def tearDown(self):
        self.log.info(self.result)

    def test_repayment_all(self):
        '''全部还款'''
        headers = self.el.GetDetialData(self.sheet_name,1,2)
        data = self.el.GetDetialData(self.sheet_name,1,3)
        headers = eval(headers)
        data = eval(data)
        #print(data)

        sql1 = self.db.select(self.table_name, self.sql1)
        sql2=self.sql2
        sql2['where']['id']=str(sql1[0]['max(id)'])
        mydata = self.db.select(self.table_name,sql2)

        data['repaymentCapital'] = str(mydata[0]['loan_amount'])
        data['repaymentAmount'] = str(mydata[0]['loan_amount'])
        data['loanGid'] = mydata[0]['loan_record_gid']
        data['userGid'] = mydata[0]['user_gid']
        data['endTime'] = mydata[0]['due_time']
        data['repaymentGid'] = self.repayment_gid     # repaymentGid赋唯一值

        #print(data)
        r = requests.post(url=self.base_url, data=json.dumps(data), headers=headers)
        self.result = r.json()

        self.assertEqual(self.result['returnCode'],'0000')
        self.assertEqual(self.result['returnDesc'],'成功')


if __name__ == "__main__":
    unittest.main()
