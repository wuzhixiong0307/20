"""
基类，封装一些元素操作方法
"""
import logging
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from app2.common.utils import Utils


class Base:

    def __init__(self, driver: WebDriver = None):
        """初始化构造方法"""
        self.driver = driver

    def start_activity_page(self,app_package="com.tencent.wework",app_activity=".launch.LaunchSplashEduActivity"):
        """
        进入指定Activity页面
        app_package：被启动的APP包名
        app_activity：被启动的activity页面
        """
        self.driver.start_activity(app_package,app_activity)

    def log_info(self,message):
        """
        打印日志信息
        message：日子输出的内容
        """
        logging.info(message)

    def find_element(self, driver, location, timeout=15):
        """
        封装元素查找方法
        driver：驱动
        location：定位方法，以元组形式传入，格式：(By.ID,"idxxx")
        timeout：超时等待时间，默认15s
        """
        # 获取指定的调用信息，并打印输出日志
        caller_message = Utils.get_caller()
        self.log_info(f"调用链路信息：{caller_message[36:-1]}")
        # 打印日志，并输出定位操作信息
        self.log_info(f"查找元素：{location}")

        # 循环查找元素，判断元素是否可点击
        element = WebDriverWait(driver, timeout). \
            until(EC.element_to_be_clickable(location))
        # 返回元素信息
        return element

    def element_click(self, driver, location, timeout=15):
        """
        点击指定元素
        driver：驱动
        location：定位方法，以元组形式传入，格式：(By.ID,"idxxx")
        timeout：超时等待时间，默认15s
        """
        # 获取指定调用信息，并打印输出日志
        caller_message = Utils.get_caller()
        self.log_info(f"调用链路信息：{caller_message[36:-1]}")
        # 打印日志，并输出定位操作信息
        self.log_info(f"点击元素：{location}")

        # 调用元素查找方法，执行点击操作
        self.find_element(driver, location, timeout).click()

    def element_send_keys(self, driver, location, value, timeout=15):
        """
        输入文本信息
        driver：驱动
        location：定位方法，以元组形式传入，格式：(By.ID,"idxxx")
        value：要输入的文本
        timeout：超时等待时间，默认15s
        """
        # 获取指定调用信息，并打印输出日志
        caller_message = Utils.get_caller()
        self.log_info(f"调用链路信息：{caller_message[36:-1]}")
        # 打印日志，并输出定位操作信息
        self.log_info(f"输入文本信息：{location}")

        # 调用元素查找方法，执行输入文本操作
        self.find_element(driver, location, timeout).send_keys(value)

    def element_swipe(self, driver, location, count=5, timeout=3):
        """
        封装上下滑动查找元素方法
        driver：驱动
        location：定位方法，以元组形式传入，格式：(By.ID,"idxxx")
        count：滑动查找的次数
        timeout：超时等待时间，默认3s
        """
        # 获取指定调用信息，并打印输出日志
        caller_message = Utils.get_caller()
        self.log_info(f"调用链路信息：{caller_message[36:-1]}")

        # 获取手机屏幕大小
        h_size = driver.get_window_size()
        start_x = h_size["width"] * 0.5  # 获取起始宽度
        start_y = h_size["height"] * 0.7  # 获取起始高度
        end_x = h_size["width"] * 0.5  # 获取终止宽度
        end_y = h_size["height"] * 0.3  # 获取终止高度

        for i in range(count):
            try:
                ele = self.find_element(driver, location, timeout)
                # 查找到元素，结束循环返回结果
                return ele
            # 未找到元素，接收异常。滑动页面并进入下一次循环
            except Exception:
                # 打印日志，并输出定位操作信息
                self.log_info(f"滑动页面查找元素：{location}")
                # 滑动页面
                driver.swipe(start_x, start_y, end_x, end_y)
                # continue
        else:
            print(f"抱歉，未找到该元素：{location}")

    def get_toast(self):
        """获取toast提示信息"""
        toast = self.driver.find_element(By.XPATH, '//*[@class="android.widget.Toast"]')
        return toast.text


if __name__ == "__main__":
    Base().log_info("11111")
    Base().find_element(1,2)