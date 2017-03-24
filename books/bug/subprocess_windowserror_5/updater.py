# -*- encoding: utf-8 -*-
import logging
import os
import sys
import zipfile

CUR_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))

CACHE_DIR = os.path.join(CUR_DIR, "cache")
NEW_PACKAGE = os.path.join(CUR_DIR, "app.zip")

logging.basicConfig(filename=os.path.join(CUR_DIR, "updater.log"), filemode="w", level=logging.INFO,
                    format='%(asctime)s  [%(levelname)s]- %(message)s')


def update_files():
    logging.info(u"删除缓存目录:%s", CACHE_DIR)
    with zipfile.ZipFile(NEW_PACKAGE) as zip:
        zip.extractall(CACHE_DIR)
    
    app_cache_dir = os.path.join(CUR_DIR, "cache", "app")
    app_dir = os.path.join(CUR_DIR, "app")
    app_old_dir = os.path.join(CUR_DIR, "old_app")
    logging.info(u"替换目录%s 为 %s", app_dir, app_old_dir)
    os.rename(app_dir, app_old_dir)


if __name__ == "__main__":
    
    try:
        update_files()
    
    except Exception as e:
        logging.exception(e)
