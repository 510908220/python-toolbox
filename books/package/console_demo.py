# -*- encoding: utf-8 -*-

import time
import sys


def main():
    while 1:
        print("currenr timestamp:", time.time())
        time.sleep(5)


if __name__ == "__main__":
    sys.exit(main())
