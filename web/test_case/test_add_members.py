"""
测试添加成员相关功能
"""

import pytest
from web.commons.common_method import CommonMethod
from web.page_object.index_page import IndexPage

class TestAddMembers:


    # 动态获时间戳，提高用例可复用性
    data = CommonMethod().get_int_timestamp(2)

    @pytest.mark.parametrize(["user_id","phone","username"],
                             [(data[0],"199%s" %str(data[0])[2:],"员工%s" %str(data[0])[2:]),
                              (data[1],"199%s" %str(data[1])[2:],"员工" + str(data[1])[2:])],
                             ids=["case_1","case_2"])
    @pytest.mark.success
    def test_add_members_success(self,user_id,phone,username):
        """
        测试添加成员
        """
        p_list = IndexPage().goto_add_members().\
            add_members(user_id,phone,username).get_user_list()
        # 断言添加的用户号码是否在列表中
        assert phone in p_list

    # 动态获时间戳，提高用例可复用性
    data = CommonMethod().get_int_timestamp()

    @pytest.mark.parametrize(["user_name","user_id","phone","assert_msg"],
                             [("员工","","199%s" %str(data)[2:],"请填写帐号"),
                              ("", data, "199", "请填写正确的手机号码"),
                              ("员工",data,"","手机和邮箱不能同时为空"),
                              ("员工",data,19960378307,"该手机号已被“嘿”占有")
                              ])
    @pytest.mark.fail
    def test_add_members_fail(self,user_name,user_id,phone,assert_msg):
        """
        测试添加成员失败
        """
        msg_list = IndexPage().goto_add_members()\
            .add_members_fail(user_name,user_id,phone)
        assert assert_msg in msg_list
    @pytest.mark.skip
    def test_1(self):
        import os, sys
        # a = sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        # print(os.path.join(os.path.dirname(__file__), '..\\'))
