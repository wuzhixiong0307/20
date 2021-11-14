"""
测试calculation功能
"""
import allure
import pytest


@allure.feature("测试计算器功能")
@allure.title("计算器测试类")
class TestCalculator:


    # 参数化用例，分别测试2种情况相加：整数相加，小数相加
    @pytest.mark.parametrize(["value_1","value_2","result"],[(1,2,3),(0.5,0.5,1)],
                             ids=["整数相加成功","小数相加成功"])
    @allure.title("加法测试用例")  # 添加用例标题
    @pytest.mark.run(order=2)        # 控制用例执行顺序
    @allure.story("测试加法功能")       # 添加功能名称
    def test_add(self,value_1,value_2,result,calculator):
        """
        测试加法运算
        """
        # 添加测试步骤，实例化Calculator类
        with allure.step("第一步：实例化Calculator类"):
            cal = calculator
        # 添加测试步骤，调用add方法，进行相加计算
        with allure.step(f"第二步：调用add方法，进行相加计算：{value_1}+{value_2}"):
            add_result = cal.add(value_1, value_2)
        print(add_result)
        # 添加测试步骤，上传图片
        with allure.step("第三步：上传图片"):
            allure.attach.file(r"D:\python_script\pytest_work\img\test.png","测试图片",attachment_type=allure.attachment_type.PNG)
        # 添加测试步骤，断言计算结果是否与预期一致
        with allure.step(f"第四步：断言计算结果是否与预期一致：{add_result}=={result}"):
            assert add_result == result

    # 参数化用例，分别测试2种情况相除：整数相除，小数相除
    @pytest.mark.parametrize(["value_1","value_2","result"],[(6,3,2),(3.3,9.9,0.33)],
                             ids=["整数相除成功","小数相除成功"])
    @allure.title("除法测试用例")     # 添加用例标题
    @pytest.mark.run(order=1)        # 控制用例执行顺序
    @allure.story("测试除法功能")     # 添加功能名称
    def test_div(self,value_1,value_2,result,calculator):
        """
        测试除法运算
        """
        # 添加测试步骤，实例化类
        with allure.step("第一步：实例化计算器类：calculator"):
            cal = calculator
        # 添加测试步骤，调用div方法，进行相除计算
        with allure.step(f"第二步：调用div方法，进行相除计算:{value_1} / {value_2}"):
            div_result = cal.div(value_1,value_2)
        print(div_result)
        # 添加测试步骤，上传图片
        with allure.step("第三步：上传图片"):
            allure.attach.file(r"D:\python_script\pytest_work\img\test.png","测试图片",attachment_type=allure.attachment_type.PNG)
        # 添加测试步骤，断言相除结果是否与预期结果一致
        with allure.step(f"第四步：断言相除结果是否与预期结果一致:{div_result} == {result}"):
            assert div_result == result
