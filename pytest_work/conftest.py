import os,sys
import pytest
from selenium import webdriver

from api.calculator import Calculator
# 将当前文件路径添加到path变量
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# 创建calculation的fixtrue
@pytest.fixture()
def calculator():
    # 实例化类
    cal = Calculator()
    # 返回实例化类结果
    yield cal
    print("运算结束")


# 创建保存图片的fixture
@pytest.fixture()
def screenshot():
    # 实例化driver
    driver = webdriver.Chrome()
    return driver

