"""
添加成功页面功能建模
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webdriver
import time
from web.commons.base_page import BasePage
from web.commons.element_find_operation import ElementOperation
from web.page_object.contact_page import ContactPage



class AddMembersPage(BasePage):

    # 实例化元素定位操作类
    element = ElementOperation()
    # 将重复的定位方法提取出来
    _user_name = (By.ID, "username")
    _user_id = (By.ID,"memberAdd_acctid")
    _phone = (By.ID,"memberAdd_phone")
    _save = (By.LINK_TEXT,"保存")

    def add_members(self,user_id,phone,user_name="员工"):
        """
        成员添加成功，return通讯录页面
        """
        print("添加成员页面")
        self.element.element_send_keys(self.driver,self._user_name,user_name)
        self.element.element_send_keys(self.driver,self._user_id,user_id)
        self.element.element_send_keys(self.driver, self._phone, phone)
        self.element.element_click(self.driver,self._save)
        return ContactPage(self.driver)

    def add_members_fail(self,user_name,user_id,phone):
        """
        成员添加失败，返回失败提示信息列表
        """
        self.element.element_send_keys(self.driver,self._user_name,user_name)
        self.element.element_send_keys(self.driver,self._user_id,user_id)
        self.element.element_send_keys(self.driver, self._phone, phone)
        self.element.element_click(self.driver,self._save)
        # 获取页面提示信息，添加到列表
        time.sleep(2)
        msg = self.element.finds(self.driver,(By.XPATH,"//div[@class='ww_inputWithTips_tips']"))
        error_message = []
        for i in msg:
            error_message.append(i.text)
        return error_message

