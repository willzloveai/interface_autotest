from pymysql import connect,cursors
from pymysql.err import OperationalError
import os
import configparser as cparser
from logger import Log

base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/configuration/db_config.ini"


cf = cparser.ConfigParser()
cf.read(file_path)

host = cf.get("mysqlconf","host")
port = int(cf.get("mysqlconf","port"))
db = cf.get("mysqlconf","db_name")
user = cf.get("mysqlconf","user")
password = cf.get("mysqlconf","password")

class DB:
    def __init__(self):
        self.log = Log()
        try:
            self.conn = connect(
                host=host,
                port=port,
                user=user,
                password=password,
                db=db,
                charset='utf8',
                cursorclass=cursors.DictCursor
            )
        except OperationalError as e:
            self.log.error("Mysql Error %d: %s"(e.args[0],e.args[1]))
    #封装select语句
    def select(self,table_name,table_data):
        if table_data['where'] == '':
            #print("无where子句")
            real_sql = "select "+table_data['fields']+" from " + table_name
        else:
            keys = table_data['where']
            #print(keys)
            str='where'
            for key,value in keys.items():
                str = str+' '+key+' ='+' '+'\''+value+'\''+'and'
            str=str[:-3]
            real_sql = "select " + table_data['fields'] + " from " + table_name + ' '+str

        self.log.info(real_sql)
        #print(table_name)
        cur = self.conn.cursor()
        cur.execute(real_sql)
        results = cur.fetchall()
        return results

    #封装insert语句
    def insert(self,table_name,table_data):
        keys = table_data
        #print(keys)
        str1,str2='',''
        for key,value in keys.items():
            str1 = str1+key + ','
            str2 = str2+value + ','
        str1 = str1[:-1]
        str2 = str2[:-1]
        real_sql = "insert into "+table_name+" ("+str1+")"+" values "+"("+str2+")"
        self.log.info(real_sql)
        #print(table_name)
        cur = self.conn.cursor()
        cur.execute(real_sql)

#测试函数
if __name__=='__main__':
    db = DB()
    table_name = "log_loan_refund"
    data = {"fields":"process_status","where":{"repayment_amount":"500.0000","gid":"30540705-a3ac-4a7d-a596-455984f9c068"}}
    a=db.select(table_name,data)
    print(a[1])
    data1 = {"repayment_amount":"500.0000","gid":"30540705-a3ac-4a7d-a596-455984f9c068"}
    #db.insert(table_name,data1)
























