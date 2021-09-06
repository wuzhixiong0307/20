"""
初始化基类
"""

import yaml
from selenium import webdriver
from web.commons.common_method import CommonMethod

class BasePage:

    # 声明类的私有属性变量，用来接收需要访问的网址
    _base_url = ""
    def __init__(self,base_driver=None):

        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get(self._base_url)
            self.driver.implicitly_wait(30)
            self.driver.maximize_window()
            # 获取cookie存放的路径
            cookie_path = CommonMethod().get_file_path("config\cookie.yaml")
            # 循环读取添加cookie
            cookies = yaml.safe_load(open(cookie_path))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get(self._base_url)
        else:
            self.driver = base_driver

