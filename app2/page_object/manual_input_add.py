"""
手动输入添加成员页
"""
import time

from selenium.webdriver.common.by import By

from app2.common.base import Base


class ManualInputAdd(Base):
    """手动输入添加页"""

    # 定位方法
    _name = (By.XPATH,"//*[@text='姓名　']/..//*[@text='必填']")
    _number = (By.XPATH,"//*[@text='手机　']/..//*[@text='必填']")
    _save = (By.XPATH,"//*[@text='保存']")

    def add_member(self,name,number):
        """
        添加成员
        name：成员名字
        number：成员电话号码
        """
        # 输入成员姓名
        self.element_send_keys(self.driver,self._name,name)
        # 输入成员号码
        self.element_send_keys(self.driver,self._number,number)
        # 保存成员信息
        self.element_click(self.driver,self._save)
        # 获取toast信息做断言依据
        time.sleep(1)
        return self.get_toast()