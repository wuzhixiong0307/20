"""
获取登录后的cookie信息
"""
from time import sleep
import yaml
from selenium import webdriver
from web.commons.common_method import CommonMethod


class GetCookie:

    def __init__(self,url):
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def get_login_cookies(self):
        """
        将cookie信息写入指定文件内
        """
        sleep(30)
        cookie = self.driver.get_cookies()
        # 获取文件存入路径
        cookie_file_path = CommonMethod().get_file_path(path=r"config\cookie.yaml")
        print(cookie_file_path)
        with open(cookie_file_path,"w") as f:
            yaml.safe_dump(cookie,f)
        self.driver.quit()

if __name__ == "__main__":
    # 获取登录cookie
    GetCookie("https://work.weixin.qq.com/wework_admin/loginpage_wx").get_login_cookies()

