"""
通讯录页面功能建模
"""
from selenium.webdriver.common.by import By
from web.commons.base_page import BasePage
from web.commons.element_find_operation import ElementOperation

class ContactPage(BasePage):

    def get_user_list(self):
        """
        获取phone，返回phone_list
        """
        # 获取用户列表电话信息，添加到列表
        phone = ElementOperation().finds(self.driver,(By.XPATH,"//*[@id='member_list']//td[5]"))
        phone_list = []
        for p in phone:
            phone_list.append(p.text)
        return phone_list