"""
测试添加成员、删除成员
"""
import allure
import pytest
from app2.common.utils import Utils
from app2.common.app import App


class TestCase:

    def setup_class(self):
        """实例化app类"""
        self.app = App()

    def setup(self):
        """进入首页"""
        self.main = self.app.start().goto_main()

    def teardown(self):
        """回到首页"""
        self.app.start_activity_page()

    # 读取yaml文件用户数据
    user_data = Utils.read_file_yaml("datas/user.yaml")

    # 数据驱动
    @pytest.mark.parametrize("users",(user_data[0],user_data[1]))
    # @pytest.mark.skip
    @allure.title("添加成员")
    def test_add_member(self,users):
        """测试添加成员"""
        result = self.main.goto_address_book().goto_add_member(). \
            goto_manual_input_add().add_member(users["name"], users["number"])
        assert result == "添加成功"

    # 数据驱动
    @pytest.mark.parametrize("users",(user_data[0],user_data[1]))
    # @pytest.mark.skip
    @allure.title("删除成员")
    def test_del_member(self,users):
        """测试删除成员"""
        result = self.main.goto_address_book(). \
            goto_address_book_management().goto_edit_member(users["name"]).del_member()
        assert result == "管理通讯录"


if __name__ == "__main__":
    pass