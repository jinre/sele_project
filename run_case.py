# coding:utf-8

import unittest
import os

# 测试用例地址
test_dir = os.path.dirname(os.path.realpath(__file__))

# 测试套件收集用例
test_case = unittest.TestSuite()

# discover加载测试用例
discover = unittest.defaultTestLoader.discover(start_dir=test_dir,
                                               pattern='test*.py')

test_case.addTests(discover)

# 批量运行多个用例
runner = unittest.TextTestRunner()
runner.run(test_case)
# runner.run(discover) # 效果同上

