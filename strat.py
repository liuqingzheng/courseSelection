import os,sys
path=os.path.dirname(__file__)

sys.path.append(path)
from core import src

if __name__ == '__main__':
    src.run()