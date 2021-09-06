"""
首页功能模块建模
"""
from time import sleep

# from selenium import webdriver
from selenium.webdriver.common.by import By
from web.commons.base_page import BasePage
from web.commons.element_find_operation import ElementOperation
from web.page_object.add_members_page import AddMembersPage


class IndexPage(BasePage):

    # 需要打开的网址
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"

    def goto_add_members(self):
        """
        点击添加成员，return添加成员页面
        """
        ElementOperation().element_click(self.driver,(By.LINK_TEXT,"添加成员"))
        return AddMembersPage(self.driver)

if __name__ == "__main__":
    IndexPage().goto_add_members()