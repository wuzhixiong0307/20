"""
公共方法类，提供一些数据生成及文件路径查找方法
"""
import os
import random
import time
import yaml


class CommonMethod:

    def get_desired_caps(self, devicesName="HUAWEI"):
        """
        获取设备配置信息
        """
        # 获取配置文件所在路径
        devices_file = self.get_file_path(r"config\devices.yaml")
        # 读取yaml文件内容
        with open(r"{}".format(devices_file), mode="rt", encoding="utf-8") as f:
            res = f.read()
            # 循环文件内容，并将文件内容转换成python数据类型
            for desc in yaml.load(res, Loader=yaml.FullLoader):
                # 判断输入的设备是否存在
                if devicesName in desc["desc"]:
                    return desc
            else:
                return {"error":"抱歉，该设备不存在"}

    def get_file_path(self, path=None):
        """
        获取文件路径
        """
        # 获取上级文件目录，并将路径格式进行转换
        dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 拼接文件路径
        if path:
            dir_name = os.path.join(dir_name, path)
        return dir_name

    def get_number(self):
        """
        获取号码
        """
        # 手机号头三位
        head = ["157", "199", "138", "135", "185"]
        # 获取毫秒级时间戳
        tail = time.time() * 1000
        # 拼接手机号
        number = random.choice(head) + str(tail).split(".")[0][-8::]
        print(number)
        return number

    def get_name(self):
        """
        获取名字
        """
        first = ["李", "张", "罗", "谢", "程", "廖", "蒋", "伍", "欧阳", "诸葛", "司马", "孤独", "皇甫"]
        last = ["冰冰", "慧慧", "思", "晨", "建国", "灵", "亮", "彩云", "明", "黎明", "荣", "瑞轩", "云"]
        # 随机选择一个姓跟名字，进行拼接
        name = random.choice(first) + random.choice(last)
        print(name)
        return name


if __name__ == "__main__":
    # a = CommonMethod().get_file_path(r"config\devices.yaml")
    # print(a)
    # CommonMethod().get_number()
    # CommonMethod().get_name()
    d = CommonMethod().get_desired_caps("雷电")
    print(d['desired_caps'])
