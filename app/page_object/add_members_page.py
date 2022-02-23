"""
添加成员页面建模
"""
from selenium.webdriver.common.by import By

from app.commons.base_page import Base
from app.page_object.input_add_page import InputAddPage


class AddMemberPage(Base):
    # 添加成员页面元素定位
    _input_add = (By.XPATH,"//*[@text='手动输入添加']")

    def goto_input_add(self):
        """去到手动输入添加页面"""
        self.element_click(self.driver,self._input_add)
        return InputAddPage(self.driver)