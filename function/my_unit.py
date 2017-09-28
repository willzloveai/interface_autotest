import unittest
from my_excel import Excel
from mysql_db import DB
from logger import Log

class MyUnit(unittest.TestCase):
    # def setUpClass(cls):
    #     cls.db = DB()
    #     # cls.log = Log()
    #     # cls.excel = Excel()
    #
    # def tearDownClass(cls):
    #     cls.log.info('success')

    def setUp(self):
        self.db = DB()
        self.log = Log()
        self.excel = Excel()

    def tearDown(self):
        self.log.info(self.result)
