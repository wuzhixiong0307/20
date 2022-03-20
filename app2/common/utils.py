"""
工具类，辅助测试工作
"""
import os
import sys
import traceback
import yaml
from faker import Faker


class Utils:

    @classmethod
    def get_file_path(cls, path=None):
        """
        获取文件路径
        path：文件路径信息
        """
        # 获取上上级文件目录
        file_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # print(file_path)
        if path:
            # 拼接文件路径
            file_path = os.path.join(file_path, path)
            # print(file_path)

        # 返回文件路径
        return file_path

    @classmethod
    def get_desired_caps(cls, devicesName="HUAWEI_P30Pro"):
        """
        获取配置文件设备信息
        devicesName：设备名称，默认设备huawei
        """
        # 读取配置文件信息
        devices_msg = cls.read_file_yaml(r"config\devices.yaml")
        # 循环配置信息，判断设备是否存在
        for desc in devices_msg:
            if devicesName in desc.get("desc"):
                return desc
        else:
            return {"error": "抱歉，该设备不存在"}

    @classmethod
    def get_caller(cls):
        """
        获取调用方信息
        """
        # 返回方法调用者信息
        return traceback.extract_stack()

    @classmethod
    def get_name(cls):
        """
        随机获取姓名
        """
        return Faker("zh_CN").name()

    @classmethod
    def get_number(cls):
        """
        随机获取号码
        """
        return Faker("zh_CN").phone_number()

    @classmethod
    def write_file_yaml(cls,path_file,data,mode="wt"):
        """
        yaml文件写入操作
        path_file: 要写入的文件路径
        data：要写入的数据
        mode：写入的模式，默认wt
        """
        # 获取文件路径
        file_path = cls.get_file_path(path_file)

        # 将python数据格式转换为yaml数据格式写入文件
        with open(file_path,mode=mode,encoding="utf-8") as f:
            yaml.dump(data,f,allow_unicode=True)


    @classmethod
    def read_file_yaml(cls,path_file):
        """
        yaml文件读取操作
        path_file: 文件路径
        """
        # 获取文件路径
        file_path = cls.get_file_path(path_file)

        # 将yaml数据格式转换为python数据格式取出
        with open(file_path,mode="rt",encoding="utf-8") as f:
            r = f.read()
            return yaml.load(r,Loader=yaml.FullLoader)


if __name__ == "__main__":
    # Utils().get_file_path("config")
    # Utils().get_desired_caps()
    # a = Utils.get_desired_caps()
    # print(a['port'],a['desired_caps'])
    # b = Utils.get_caller()
    # print(b)
    # n = Utils.get_name()
    # h = Utils.get_number()
    # print(n)
    # print(h)
    user_data = [{"name":"张三","number":"13566907788"},{"name":"李四","number":"13566907799"}]
    Utils.write_file_yaml("datas/user.yaml",user_data)
    print(Utils.read_file_yaml("datas/user.yaml"))
