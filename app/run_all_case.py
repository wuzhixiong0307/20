"""
2022/2/21 0:19  加油呀，少年！
"""

import os
import sys

import pytest
# 解决命令行运行报错问题：ModuleNotFoundError: No module named 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



def run_all_case():
    """
    运行所有测试用例
    """
    from app.commons.common_method import CommonMethod
    from app.commons import base_page
    # 获取测试用例存放路径
    case_path = CommonMethod().get_file_path("test_case")
    # 循环命令行输入的内容
    for i in sys.argv:
        # 判断是否输入了device字段，如果输入了就以“=”分隔并将设备名称赋值给base_page.py文件里device变量
        if "device" in i:
            base_page.device = i.split("=")[1]
    # 执行测试用例，并生成allure结果
    pytest.main([case_path, "-vs","--alluredir=./result/"])
    # 将allure结果生成allure报告
    os.system("allure generate ./result/ -o ./report/ --clean && allure open -h 127.0.0.1 -p 8883 ./report/")

if __name__ == "__main__":
    run_all_case()
    # run_test()
