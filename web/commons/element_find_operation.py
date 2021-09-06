"""
页面元素查找、操作等常用方法封装
"""
from selenium.webdriver.support.wait import WebDriverWait

class ElementOperation:

    def find(self, driver, location, timeout=30):
        """
        查找单个元素，driver：浏览器驱动，location：元素定位方法，timeout：超时时间
        """
        element = WebDriverWait(driver, timeout).until(lambda x: x.find_element(*location))
        return element

    def finds(self, driver, location, timeout=30):
        """
        查找多个元素，driver：浏览器驱动，location：元素定位方法，timeout：超时时间
        """
        elements = WebDriverWait(driver, timeout).until(lambda x: x.find_elements(*location))
        return elements

    def element_click(self, driver, location, timeout=30):
        """
        对元素进行点击操作
        """
        self.find(driver, location, timeout).click()

    def element_send_keys(self, driver, location, msg, timeout=30):
        """
        输入数据
        """
        self.find(driver, location, timeout).send_keys(msg)


if __name__ == "__main__":
    pass
