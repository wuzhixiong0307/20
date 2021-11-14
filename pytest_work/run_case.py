"""
python在cmd命令行直接运行测试用例
"""
import os
import pytest


def run_test_case():
    """
    运行测试用例
    """
    # pytest运行用例，并指定运行结果存放路径
    pytest.main([r"D:\python_script\pytest_work\test_case","-vs","--alluredir=./result/"])

    # 调用os模块在cmd命令行执行allure命令，&&连接2条命令：&&前面是生成报告，&&后面打开报告
    os.system("allure generate ./result/ -o ./report/ --clean && allure open -h 127.0.0.1 -p 8883 ./report/")


if __name__ == "__main__":
    # 运行测试用例
    run_test_case()
