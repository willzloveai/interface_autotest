"""
Testlink API Sample Python Client implementation
"""
from testlink import *

# url = 'http://192.168.118.140/testlink/lib/api/xmlrpc/v1/xmlrpc.php'
# key = '4bcb8726dbfcde68ee45888f73691f09'
# class TestlinkAPIClient:
#     # substitute your server URL Here
#
#     def __init__(self, key):
#         self.tlc = TestlinkAPIClient(url, key)
#         # print("key in init: %s" %key)
#     def getTestCaseIDByName(self,key):
#         data = {"key":key, "testcasename":"Test Case 1", "testsuitename":"Test Suite 1"}
#         return self.tlc.getTestCaseIDByName(data)
#
#     def reportTCResult(self, tcid, tpid, status):
#         data = {"key":self.key, "tcid":tcid, "tpid":tpid, "status":status}
#         return self.tlc.reportTCResult(data)
#
#     def getInfo(self):
#         return self.tlc.about()
#
#     def sayHello (self):
#         return self.tlc.sayHello()
#
#     def getProjects (self, key):
#         print("key: %s" %key)
#         data = {"key":key}
#         return self.tlc.getProjects(data)

if __name__ == '__main__':
    # key = "abc04556463cd813a1ea05caf042d42f"
    # # substitute your Dev Key Here
    # client = TestlinkAPIClient (key)
    # # get info about the server
    # print(client.getInfo())
    #
    # # retval = client.sayHello()
    #
    # #retval = client.getProjects(key)
    # retval = client.getTestCaseIDByName(key)
    #
    # print('retval: ', retval)

    import sys

    args = sys.argv[1]
    print(args)