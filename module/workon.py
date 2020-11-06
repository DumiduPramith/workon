from base import Arguments, File
import os
import sys

BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def main():
    Arguments.limit_argumeent()
    Arguments.argument_chkr()

if __name__ == '__main__':
    if os.path.join(BASE_DIR,'paths.txt'):
        main()