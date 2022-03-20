"""
编辑成员页
"""
import time

from selenium.webdriver.common.by import By

from app2.common.base import Base


class EditMember(Base):
    """编辑成员"""

    # 定位方法
    _del = (By.ID,"com.tencent.wework:id/gb0")
    _confirm = (By.ID,"com.tencent.wework:id/cfq")
    _management_page = (By.XPATH,"//*[@text='管理通讯录']")

    def del_member(self):
        """删除成员"""
        # 滑动查找成员
        self.element_swipe(self.driver,self._del)
        # 点击删除按钮
        self.element_click(self.driver,self._del)
        # 点击确认按钮
        self.element_click(self.driver,self._confirm)
        # 获取管理通讯录页面元素，做断言依据
        time.sleep(1)
        msg = self.driver.find_element(*self._management_page)

        return msg.text
