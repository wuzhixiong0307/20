"""
成员管理页面
"""
from selenium.webdriver.common.by import By

from app2.common.base import Base
from app2.page_object.edit_member_page import EditMember


class AddressBookManagement(Base):
    """成员管理页面"""

    # 定位方法
    # 第一个成员编辑页定位方法
    _edit_members = (By.ID, "com.tencent.wework:id/im1")

    def goto_edit_member(self, member=None):
        """
        进入成员编辑页
        member: 成员名字
        """
        # 指定成员编辑页定位方法
        _edit_member = (By.XPATH, f"//*[@text='{member}']/../../../..//*[@resource-id='com.tencent.wework:id/im1']")
        # 查找指定成员信息
        if member:
            # 滑动查找成员
            self.element_swipe(self.driver,_edit_member)
            # 点击编辑按钮
            self.element_click(self.driver,_edit_member)

        # 进入第一个成员编辑页
        else:
            self.element_click(self.driver,self._edit_members)

        # 返回成员编辑页
        return EditMember(self.driver)
