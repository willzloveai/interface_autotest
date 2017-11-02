from testlink import *
from logger import Log
import os
import configparser as cparser
#获取当前文件路径
base_dir = str(os.path.dirname(os.path.dirname(__file__)))
base_dir = base_dir.replace('\\','/')
file_path = base_dir + "/configuration/runmode_config.conf"


cf = cparser.ConfigParser()
cf.read(file_path,encoding='utf-8')
url = cf.get("TESTLINK","url")
key = cf.get("TESTLINK","key")

class TL:
    def __init__(self):
        self.tlc = TestlinkAPIClient(url,key)
        self.log = Log()

    #格式转化
    def __changeformat(self,oldformat):
        newformat = oldformat.replace('&quot;','"').replace('<p>','').replace('</p>','').replace('\n','').replace('\t','')
        return newformat

    #获取所有testsuite的id和name
    def get_testsuite_idname(self):
        projects = self.tlc.getProjects()
        animbus = projects[0]
        topSuites = self.tlc.getFirstLevelTestSuitesForTestProject(animbus['id'])
        suite = topSuites[0]
        for suite in topSuites:
            print('suite_id'+suite['id'],'suite_name'+suite['name'])

    #创建testsuite
    # def create_testsuite(self,project_id, test_suite_name, test_suite_describe, father_id):
    #     if father_id == "":
    #         self.tlc.createTestSuite(project_id, test_suite_name, test_suite_describe)
    #     else:
    #         self.tlc.createTestSuite(project_id, test_suite_name, test_suite_describe, parentid=father_id)


    #获取测试用例
    def get_testcase(self,testcase_id):
        self.log.info("开始获取测试用例")
        testcase_list=[]
        testcase = self.tlc.getTestCase(testcase_id)
        for i in testcase:
            self.log.info("获取信息头"+self.__changeformat(i.get('preconditions')))
            testcase_list.append(self.__changeformat(i.get('preconditions')))
            for m in i.get('steps'):
                expected_results = self.__changeformat(m.get("expected_results"))
                actions = self.__changeformat(m.get("actions"))
                step_number = self.__changeformat(m.get("step_number"))
                # testcase_list.append(step_number)
                testcase_list.append(actions)
                testcase_list.append(expected_results)
                self.log.info("步骤："+step_number+" 步骤动作："+actions+" 期望结果："+expected_results)
        return testcase_list

    #获取指定testplan下所有testcase的id
    def get_alltestcaseid_for_testplanid(self,testplanid):
        testcase_id = []
        testplan = self.tlc.getTestCasesForTestPlan(testplanid)
        for i in testplan.keys():
            self.log.info("testplanid等于"+str(testplanid)+"下【测试用例id:"+i+"】的testcase已加入列表")
            testcase_id.append(i)
        return testcase_id

    #获取指定testsuite下所有testcase的id
    def get_alltestcaseid_for_testsuiteid(self,testsuiteid):
        testcase_id = []
        testsuite = self.tlc.getTestCasesForTestSuite(testsuiteid,0,"")
        for i in testsuite:
            self.log.info("testsuiteid等于"+str(testsuiteid)+"下【测试用例id:"+i['id']+" name:"+i['name']+"】的testcase已加入列表")
            testcase_id.append(int(i['id']))
        return testcase_id


if __name__ == "__main__":
    tl = TL()
    # a = tl.get_testcase(4)
    # print(a)
    a = tl.get_alltestcaseid_for_testsuiteid(25)
    for i in a:
        b = tl.get_testcase(i)
        print(b)

    c = tl.get_alltestcaseid_for_testplanid(2)
    for i in c:
        d = tl.get_testcase(i)
        print(d)

