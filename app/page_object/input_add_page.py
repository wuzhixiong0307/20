"""
手动输入添加成员页面建模
"""
import time

from selenium.webdriver.common.by import By

from app.commons.base_page import Base


class InputAddPage(Base):
    # 手动输入添加成员元素定位
    _name = (By.ID,"com.tencent.wework:id/bsm")
    _number = (By.ID,"com.tencent.wework:id/hgi")
    _save = (By.ID,"com.tencent.wework:id/at6")
    _save_add = (By.XPATH, "//*[@text='保存并继续添加']")
    _get_toast = (By.XPATH,'//*[@class="android.widget.Toast"]')

    def add_members(self,name,number):
        """添加单个成员"""
        self.element_send_keys(self.driver,self._name,name)
        self.element_send_keys(self.driver,self._number,number)
        self.element_click(self.driver,self._save)
        # 获取toast提示，并返回做断言依据
        toast_message = self.driver.find_element(*self._get_toast)
        return toast_message.text

    def save_and_add_members(self,name,number):
        """保存并继续添加"""
        self.element_send_keys(self.driver,self._name,name)
        self.element_send_keys(self.driver,self._number,number)
        self.element_click(self.driver,self._save_add)
        # 获取toast提示，并返回做断言依据
        toast_message = self.driver.find_element(*self._get_toast)
        return toast_message.text


