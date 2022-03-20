"""
app操作封装，如启动、退出等
"""
from appium import webdriver

from app2.common.base import Base
from app2.common.utils import Utils
from app2.page_object.main_page import Main

# 获取命令行输入运行设备名称,默认使用华为手机
_device_name = "HUAWEI_P30Pro"


class App(Base):

    def start(self,driver=None):
        """
        启动APP
        """
        if not driver:
            # 获取手机设备信息
            desc = Utils.get_desired_caps(_device_name)
            # 启动app
            self.driver = webdriver.Remote(f"http://127.0.0.1:{desc['port']}/wd/hub", desc["desired_caps"])
            # 等待3s
            self.driver.implicitly_wait(3)
        else:
            # 启动应用
            self.driver.launch_app()
        return self

    def stop(self):
        """退出app"""
        # 退出app
        self.driver.quit()

    def restart(self):
        pass

    def goto_main(self):
        """进入APP主页"""
        return Main(self.driver)
