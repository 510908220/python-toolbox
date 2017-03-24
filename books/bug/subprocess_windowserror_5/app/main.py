# encoding: utf-8
import logging
import os
import subprocess
import sys

CUR_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

logging.basicConfig(filename=os.path.join(CUR_DIR, "app.log"),
                    filemode="w",level=logging.INFO,
                    format='%(asctime)s  [%(levelname)s]- %(message)s')
UPDATER = os.path.abspath(os.path.join(CUR_DIR, "..", "updater.exe"))


def main():
    subprocess.Popen([UPDATER])
    sys.exit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pass
