import mysql.connector
from mysql.connector import Error
import pandas as pd

try:
    my_db = mysql.connector.connect(host='172.16.105.37',
                                 database='av_datamaintenance',
                                 user='JavaUser',
                                 password='Pwd_W3b',
                                 auth_plugin ='mysql_native_password'
                                 )
    if my_db.is_connected():
        db_info = my_db.get_server_info()
        print("Connected to UFone ", db_info)
        cursor = my_db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database is connected to: ", record)
except Error as e:
    print("No connection established", e)




# advances = pd.read_sql_query('''SELECT *
#                               FROM advance_log
#                               WHERE runid = 198;''', con=my_db)


advances = pd.read_sql_query('''SELECT *
                              FROM advance_log
                              WHERE runid IN (select max(runid) 
                                 and co ;''', con=my_db)
payments = pd.read_sql_query('''SELECT *
      FROM payment_log
      WHERE runid = (select 
         MAX(runid) 
         FROM run_detail 
         WHERE runtype LIKE '%Payment Run%');''', con=my_db)

recharges = pd.read_sql_query('''SELECT *
                              FROM payment_log
                              WHERE runid IN (select max(runid) 
                                 from ;''', con=my_db)