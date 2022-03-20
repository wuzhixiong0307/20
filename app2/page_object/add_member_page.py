"""
添加成员页
"""
from selenium.webdriver.common.by import By

from app2.common.base import Base
from app2.page_object.manual_input_add import ManualInputAdd


class AddMember(Base):
    """添加成员页"""

    # 元素定位方法
    _manual_input_add = (By.XPATH,"//*[@text='手动输入添加']")

    def goto_manual_input_add(self):
        """进入手动添加成员页"""
        # 点击手动输入添加按钮
        self.element_click(self.driver,self._manual_input_add)
        # 返回手动输入添加页
        return ManualInputAdd(self.driver)