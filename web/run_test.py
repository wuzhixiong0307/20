import pytest
import os,sys

# 解决命令行运行报错问题：ModuleNotFoundError: No module named 'web'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def run_all_test():
    """
    运行所有测试用例
    """
    from web.commons.common_method import CommonMethod
    # 获取测试用例存放路径
    case_path = CommonMethod().get_file_path("test_case")
    pytest.main([case_path, "-vs"])

if __name__ == "__main__":
    run_all_test()