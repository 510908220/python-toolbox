
import sys
import time


def mock_download():
    for i in range(5):
        time.sleep(1)


def mock_database():
    for i in range(20):
        time.sleep(0.1)


def mock_calcate():
    for i in range(100000000):
        pass


def main():
    mock_download()
    mock_database()
    mock_calcate()


if __name__ == "__main__":
    sys.exit(main())