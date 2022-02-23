"""
测试添加成员
"""
import time

import allure
import pytest

import os,sys
# 将上级目录添加到path里，以解决报错：ModuleNotFoundError: No module named 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from app.page_object.index_page import IndexPage
from app.commons.common_method import CommonMethod


@allure.feature("添加成员用例")
class TestAddMembers:
    data = CommonMethod()

    # @pytest.mark.skip
    @allure.title("单个成员添加成功")
    def test_add_members(self):
        """添加单个成员用例"""
        result = IndexPage().goto_address_book().goto_add_members().\
            goto_input_add().add_members(self.data.get_name(),self.data.get_number())
        assert result == "添加成功"

    # @pytest.mark.skip
    @allure.title("多个成员添加成功")
    def test_save_and_add_members(self):
        """保存并继续添加，添加多个成员用例"""
        res = IndexPage().goto_address_book().goto_add_members().\
            goto_input_add()
        # 循环2次添加2个成员
        for i in range(2):
            result = res.save_and_add_members(self.data.get_name(),self.data.get_number())
            time.sleep(1)
            assert result == "添加成功"


if __name__ == "__main__":
    TestAddMembers().test_add_members()
    # print(sys.argv)