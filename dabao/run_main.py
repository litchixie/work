# coding:utf-8
import unittest
from common import HTMLTestRunner

# 存放用例的路径
# casepath = r"E:\\PyCharm 5.0.4\\dkdoo\\test_case"

import os
print(__file__)
basepath = os.path.realpath(os.path.dirname(__file__))
print(basepath)
test_casepath = os.path.join(basepath, "test_case")  # test_case 是放置用例的文件夹名称
test_reportpath = os.path.join(basepath, "test_report") # test_report 是放置测试报告的文件夹名称
print(test_casepath)
print(test_reportpath)
# 三要素：第一看有没用例，第二看用例的路径，第三看匹配规则
discover = unittest.defaultTestLoader.discover(test_casepath, "test*.py")
print(discover)  # 看有没找到用例

import time
nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
print(nowtime)

# 确定生成html报告的地址
htmlpath = os.path.join(test_reportpath, "内地QA环境测试报告.html")

print(htmlpath)

rp = open(htmlpath, "wb")  # 打开文件写入

# 运行器
runner = HTMLTestRunner.HTMLTestRunner(rp,
                                       title="内地QA环境接口测试报告",
                                       description="当前测试模块为登录接口"
                                       )
runner.run(discover)
rp.close()