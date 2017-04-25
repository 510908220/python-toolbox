
import sys
import time

@profile
def mock_download():
    for i in range(5):
        time.sleep(1)

@profile
def mock_database():
    for i in range(20):
        time.sleep(0.1)


@profile
def main():
    mock_download()
    mock_database()

if __name__ == "__main__":
    sys.exit(main())