"""
conftest文件
"""

# conftest.py


import os,sys
# 将上级目录添加到path里，以解决报错：ModuleNotFoundError: No module named 'app'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

