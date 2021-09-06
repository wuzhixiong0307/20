"""
系统文件相关操作方法
"""
import os
import time

class CommonMethod:

    def get_file_path(self, path=None):
        """
        获取文件目录
        """
        # 获取上级文件目录，并将路径格式进行转换
        dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # 拼接文件路径
        if path:
            dir_name = os.path.join(dir_name, path)
        return dir_name

    def get_int_timestamp(self, count=1):
        """
        获取整型时间戳
        1、count参数为1时，返回单个int时间戳
        2、count参数大于1时，返回一个list
        """
        if count <= 1:
            timestamp = str(int(time.time()))
        else:
            timestamp = []
            for i in range(count):
                time.sleep(1)
                timestamp.append(str(int(time.time())))

        return timestamp


if __name__ == "__main__":
    a = CommonMethod().get_int_timestamp(0)
    print(a)
