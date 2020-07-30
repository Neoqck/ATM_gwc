import os
import sys
from core import src

BASE_PATH = os.path.dirname(__file__)
#  添加到环境变量
sys.path.append(BASE_PATH)

if __name__ == '__main__':
    src.run()




