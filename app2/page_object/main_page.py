"""
企业微信首页
"""
from selenium.webdriver.common.by import By

from app2.common.base import Base
from app2.page_object.address_book_page import AddressBook


class Main(Base):
    """企业微信首页"""

    # 定位方法
    _address_book = (By.XPATH,"//*[@text='通讯录']")

    def goto_address_book(self):
        """进入通讯录页面"""
        # 点击通讯录按钮
        self.element_click(self.driver,self._address_book)
        # 返回添加通讯录页面
        return AddressBook(self.driver)

