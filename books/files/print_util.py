import os


def print_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path.replace(dir_path, ""))


