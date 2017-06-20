from IPython.display import display
import pandas as pd
import pymysql.cursors
from collections import defaultdict


def print_table():
    db_result = []
    try:
        connection = get_connection()
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `auth_user` "
            cursor.execute(sql)
            db_result = cursor.fetchall()
    finally:
        connection.close()
    
    if not db_result:
        return
    if isinstance(db_result, dict):
        db_result = [db_result]
    data = defaultdict(list)
    for item in db_result:
        for key in item:
            data[key].append(item[key])
    df = pd.DataFrame(data)
    display(df)

def get_connection():
    connection = pymysql.connect(host='192.168.0.88',
                           user='root',
                           password='letmegoletmego',
                           db='db',
                           port=32768,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    return connection


def reset_table():
    connection = get_connection()
    table_sql = '''
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

    try:
        with connection.cursor() as cursor:
            cursor.execute(table_sql)
    finally:
        connection.close()