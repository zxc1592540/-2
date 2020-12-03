import shutil
import unittest
from common import HTMLTestRunner
from test_case.testcase import Case
import  os
from common.send_mail import email


class Runmain():
    def __init__(self):
        self.send = email()
    def run_case(self):
        suite=unittest.TestSuite()
        suite.addTest(Case('test_case01'))
        suite.addTest(Case('test_case02'))
        report_path="D:\\pycharm\\MyRequests\\report"
        if os.path.isdir(report_path):
            shutil.rmtree(report_path)
            os.mkdir(report_path)
        else:
            os.mkdir(report_path)

        fp = open(report_path+'\\'+'result.html', 'wb')
        HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口自动化测试报告', description=u'测试者：李子实').run(suite)
        #self.send_mail.send_report(fp)
        self.send.send_report()
        print('ok')


if __name__== '__main__':
    run=Runmain()
    run.run_case()


