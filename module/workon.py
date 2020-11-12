from base import Arguments
import os
import sys
import signal
from manual import manual as man
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def signal_handler(sig, frame):
    print('  Bye!')
    sys.exit(1)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    if sys.argv[1] == 'man' and len(sys.argv) == 2:
        man()
        os._exit(1)
    Arguments.limit_argumeent() #limit workon and -
    Arguments.argument_chkr()
    os._exit(1)
    signal.pause()

if __name__ == '__main__':
    if os.path.join(BASE_DIR,'paths.txt'):
        main()