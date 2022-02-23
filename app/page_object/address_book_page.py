"""
通讯录页面建模
"""
from selenium.webdriver.common.by import By

from app.commons.base_page import Base
from app.page_object.add_members_page import AddMemberPage


class AddressBookPage(Base):
    # 通讯录页面元素定位
    _add_members = (By.XPATH,"//*[@text='添加成员']")

    def goto_add_members(self):
        """去到添加成员页面"""

        # 滚动查找元素，并执行点击操作
        self.element_swipe(self.driver,self._add_members).click()
        return AddMemberPage(self.driver)