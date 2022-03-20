
import time

import pytest
import os,sys
# 将上级目录添加到path里，以解决报错：ModuleNotFoundError: No module named 'app2'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """按时间生成日志文件"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)

# def get_users():
#
