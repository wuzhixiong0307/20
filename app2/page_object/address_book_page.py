"""
通讯录页
"""
from selenium.webdriver.common.by import By

from app2.common.base import Base
from app2.page_object.add_member_page import AddMember
from app2.page_object.address_book_management_page import AddressBookManagement


class AddressBook(Base):
    """通讯录页面"""

    # 定位方法
    _add_member = (By.XPATH,"//*[@text='添加成员']")
    _management = (By.ID,"com.tencent.wework:id/kkn")

    def goto_add_member(self):
        """进入添加成员页面"""
        # 滑动查找添加成员按钮，并点击
        self.element_swipe(self.driver,self._add_member).click()
        # 返回添加成员页
        return AddMember(self.driver)

    def goto_address_book_management(self):
        """进入管理成员页面"""
        # 点击管理图标按钮
        self.element_click(self.driver,self._management)
        # 返回成员管理页面
        return AddressBookManagement(self.driver)