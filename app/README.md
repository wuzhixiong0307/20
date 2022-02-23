## 环境说明
# 此作业运行环境：python+pytest+allure+HUAWEI_P30_Pro+企业微信

## 运行文件说明
# run_all_case.py文件是运行所有用例的主文件

## 运行设备说明
# 手机设备信息写在config文件下的devices.yaml文件当中，如果设备不存在需要在文件中添加

## python运行命令说明
# 此代码支持指定设备运行，但运行命令需要按照定义的规范输入
# 运行命令规范：python run_all_case.py device=设备名称
# 如果运行命令没有带device参数，默认使用的设备是HUAWEI。如果想要修改默认运行设备，需要去修改base_page.py里面的device参数