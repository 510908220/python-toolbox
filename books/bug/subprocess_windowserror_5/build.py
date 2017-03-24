import os
import shutil
import subprocess

CUR_DIR = os.path.abspath(os.path.dirname(__file__))

APP_DIR = os.path.join(CUR_DIR, "app")

pyinstaller_exe = r"C:\Python27\Scripts\pyinstaller.exe"

try:
    shutil.rmtree(os.path.join(CUR_DIR, "build"))
    shutil.rmtree(os.path.join(CUR_DIR, "dist"))
except:
    pass
subprocess.check_call("{pyinstaller} -w -F --onefile  --clean {script}".format(
    pyinstaller=pyinstaller_exe,
    script=os.path.join(CUR_DIR, "updater.py")
), shell=True, cwd=CUR_DIR)

shutil.copy(os.path.join(CUR_DIR, "dist", "updater.exe"),
                CUR_DIR)

try:
    shutil.rmtree(os.path.join(APP_DIR, "build"))
    shutil.rmtree(os.path.join(APP_DIR, "dist"))
except:
    pass
subprocess.check_call("{pyinstaller} -w -F --onefile  --clean {script}".format(
    pyinstaller=pyinstaller_exe,
    script=os.path.join(APP_DIR, "main.py")
), shell=True, cwd=APP_DIR)

shutil.copy(os.path.join(APP_DIR, "dist", "main.exe"),
                APP_DIR)
