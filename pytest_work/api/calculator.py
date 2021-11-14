"""
计算器功能
"""
from decimal import Decimal

class Calculator:

    def add(self,value_1,value_2):
        """
        加法运算
        :param value_1: 数字
        :param value_2: 数字
        :return: 加法计算结果
        """
        # 返回加法计算结果
        return value_1 + value_2

    def div(self,value_1,value_2):
        """
        除法运算
        :param value_1: 数字
        :param value_2: 数字
        :return: 除法计算结果
        """
        # 除法计算结果
        value = value_1 / value_2
        # 保留2位小数，不做四舍五入处理并将数据类型转换成float类型
        return float(Decimal(value).quantize(Decimal("0.00")))

if __name__ == "__main__":
    # 测试代码
    # 实例化类
    cal = Calculator()
    # 调用add方法，并打印结果
    add = cal.add(1,2)
    print(add)
    # 调用div方法，并打印结果
    div = cal.div(6,3)
    print(div)
