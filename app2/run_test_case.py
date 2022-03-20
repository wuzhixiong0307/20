"""
运行所有用例
"""
import os
import sys
import pytest
# 解决命令行运行报错问题：ModuleNotFoundError: No module named 'app2'


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from app2.common.utils import Utils
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def run_test_case():
    """运行用例"""
    from app2.common.utils import Utils
    from app2.common import app
    # 获取用例路径
    case_path = Utils.get_file_path("test_case")
    # 循环命令行输入的内容
    for i in sys.argv:
        # 判断是否输入了device字段，如果输入了就以=号分隔，将设备名称赋值给app文件里面的_device_name
        if "device" in i:
            app._device_name = i.split("=")[1]
    # 执行用例，并生成allure结果
    pytest.main([case_path,"-vs","--alluredir=./result/"])
    # 将结果生成allure报告
    os.system("allure generate ./result/ -o ./report/ --clean && allure open -h 127.0.0.1 -p 8883 ./report/")

if __name__ == "__main__":
    run_test_case()