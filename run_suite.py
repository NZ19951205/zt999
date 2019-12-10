# 导包
import unittest


# 定义参数套件
from tools.HTMLTestReportCN import HTMLTestRunner

suite=unittest.defaultTestLoader.discover("./scripts")
# 获取报告文件流 并 实例化HtmlTestrunner 调用run
with open("./report/report.html","wb")as f:
    HTMLTestRunner(stream=f).run(suite)