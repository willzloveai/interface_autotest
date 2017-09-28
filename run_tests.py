import time,sys,os,unittest
sys.path.append('./interface')
sys.path.append('./function')
from HTMLTestRunner import HTMLTestRunner
from send_email import SendEmail

test_dir = './interface'
test_report = './report'
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

def new_report(testreport):
        lists = os.listdir(testreport)
        #查找最新报告
        lists.sort(key=lambda fn: os.path.getmtime(testreport + "\\" + fn))
        file_new = os.path.join(testreport,lists[-1])
        #print(file_new)
        return file_new

if __name__ == "__main__":
        em = SendEmail()
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = './report/'+now+'_result.html'
        fp = open(filename,'wb')
        runner = HTMLTestRunner(stream=fp,title='Test Report',description='Implementation Example with:')
        runner.run(discover)
        fp.close()

        new_report = new_report(test_report)
        em.sendemail(new_report)