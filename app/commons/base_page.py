"""
基类，初始化设备信息及封装元素定位及操作方法
"""
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from app.commons.common_method import CommonMethod

# 接收命令行输入要运行的设备，默认使用HUAWEI手机
device = "HUAWEI"


class Base:
    # 实例化公共方法类
    methods = CommonMethod()

    def __init__(self, base_driver=None):
        """初始化运行设备"""
        if base_driver == None:
            # 读取设备配置文件，device接收pytest命令行输入的，运行设备信息
            device_message = self.methods.get_desired_caps(device)
            self.driver = webdriver.Remote("http://127.0.0.1:{}/wd/hub".format(device_message["port"]),
                                           device_message["desired_caps"])
            self.driver.implicitly_wait(3)

        else:
            self.driver = base_driver

    def element_find(self, driver, location, timeout=10):
        """
        单个元素定位方法二次封装

        driver：浏览器驱动
        location：定位方法及定位元素，以元组的形式传入。如：(By.ID, "username")
        timeout：元素查找超时等待时间
        """
        element = WebDriverWait(driver, timeout). \
            until(expected_conditions.element_to_be_clickable(location))
        return element

    def elements_find(self, driver, location, timeout=10):
        """
        多个元素定位方法二次封装

        driver：浏览器驱动
        location：定位方法及定位元素，以元组的形式传入，如（By.ID,"username")
        timeout：元素查找超时等待时间
        """
        elements = WebDriverWait(driver, timeout). \
            until(lambda x: x.find_elements(*location))
        return elements

    def element_click(self, driver, location, timeout=10, element=None, index=None):
        """
        元素点击操作二次封装
        """
        # 多个元素定位，点击
        if element:
            self.elements_find(driver, location, timeout)[index].click()
        # 单元素定位点击
        else:
            self.element_find(driver, location, timeout).click()

    def element_send_keys(self, driver, location, value, timeout=10, element=None, index=None):
        """
        内容输入二次封装
        """
        # 多元素定位输入
        if element:
            self.elements_find(driver, location, timeout)[index].send_keys(value)
        # 单元素定位输入
        else:
            self.element_find(driver, location, timeout).send_keys(value)

    def element_swipe(self, driver, location, count=5, timeout=3, element=None):
        """
        封装上下滑动查找元素方法
        """
        # 获取手机屏幕大小
        h_size = driver.get_window_size()
        start_x = h_size["width"] * 0.5  # 获取起始宽度
        start_y = h_size["height"] * 0.7  # 获取起始高度
        end_x = h_size["width"] * 0.5  # 获取终止宽度
        end_y = h_size["height"] * 0.3  # 获取终止高度

        for i in range(count):
            try:
                # 多个元素定位
                if element:
                    ele = self.elements_find(driver, location, timeout)
                # 单个元素定位
                else:
                    ele = self.element_find(driver, location, timeout)
                # 查找到元素，结束循环返回结果
                if ele:
                    return ele
            # 未找到元素，接收异常。滑动页面并进入下一次循环
            except Exception:
                driver.swipe(start_x, start_y, end_x, end_y)
                continue
        else:
            print(f"抱歉，未找到该元素：{location}")


if __name__ == "__main__":
    test = Base()
    # test.element_click(test.driver,(By.XPATH,"//*[@text='工作台']"))
    # test.element_swipe(test.driver,(By.XPATH,"//*[@text='上下游']"),count=1).click()
    test.element_click(test.driver, (By.XPATH, "//*[@text='通讯录']"))
    test.element_click(test.driver, (By.XPATH, "//*[@text='添加成员']"))
    test.element_click(test.driver, (By.XPATH, "//*[@text='手动输入添加']"))
    test.element_send_keys(test.driver, (By.ID, "com.tencent.wework:id/bsm"), test.methods.get_name())
    test.element_send_keys(test.driver, (By.ID, "com.tencent.wework:id/hgi"), test.methods.get_number())
    test.element_find(test.driver, (By.ID, "com.tencent.wework:id/at6")).click()
