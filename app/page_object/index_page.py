"""
首页建模
"""
from selenium.webdriver.common.by import By

from app.commons.base_page import Base
from app.page_object.address_book_page import AddressBookPage


class IndexPage(Base):
    # 首页的元素定位
    _address_book = (By.XPATH, "//*[@text='通讯录']")

    def goto_address_book(self):
        """去到通讯录页面"""
        self.element_click(self.driver, self._address_book)
        return AddressBookPage(self.driver)

if __name__ == "__main__":
    IndexPage().goto_address_book()
