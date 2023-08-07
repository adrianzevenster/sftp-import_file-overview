import mysql.connector
from mysql.connector import Error
import pandas as pd

try:
    my_db = mysql.connector.connect(host='10.0.44.20',
                                 database='av_microservice_finance',
                                 user='JavaUser',
                                 password='Pwd_W3b',
                                 auth_plugin ='mysql_native_password'
                                 )
    if my_db.is_connected():
        db_info = my_db.get_server_info()
        print("Connected to DigiCel ", db_info)
        cursor = my_db.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("Database is connected to: ", record)
except Error as e:
    print("No connection established", e)




query = pd.read_sql_query('''SELECT s.msisdn, a.externalref, p.*
                                FROM   payment p, advance a, subscriber s
                                WHERE  a.advanceid = p.advanceid
                                AND    s.subscriberid = a.subscriberid
                                and    p.amount > 0
                                AND    p.COMMENT LIKE '%manual - overclaw%'
                                AND    p.paymentdate >= '2023-05-01'
                                AND    p.paymentdate < '2023-05-02'
                                ORDER BY p.paymentdate;''', con=my_db)
def report_headers(info):
    minDate, maxDate = info.timestamp.dt.date.min(), info.timestamp.dt.date.max()
    minDate = pd.to_datetime(minDate)
    maxDate = pd.to_datetime(maxDate)
    cnt = info.shape[0]
    coalesce = [[minDate,
                maxDate,
                cnt]]
    reportFrame = pd.DataFrame(coalesce, columns=['minDate', 'maxDate', 'cnt'])
    return reportFrame
print(query)

for i in range(len(query)):
        print(f'{query.loc[i, "msisdn"]}\n'
              f'curl -v "http://10.0.44.22:8080/av_integration_momo_vcl/reverseTransaction?msisdn={query.loc[i, "msisdn"]}&externalRef={query.loc[i, "transactionid"]}&amount={query.loc[i, "amount"]}"\n')


for j in range(len(query)):
# print(f'INSERT INTO `payment` (`advanceid`, `transtypeid`, `paymentdate`, `transactionid`, `amount`,`timestamp`, `statusid`, `sourceid`, comment)'
#         f'VALUES ((SELECT advanceid FROM   av_microservice_finance.advance WHERE  externalref = "{query.loc[j, "externalref"]}")/, 1, NOW(), "-1", -{query.loc[j, "amount"]}, NOW(), 3, 5, "manual - reversal"); \n')
        print(f'-- {query.loc[j, "msisdn"]}:\n'
      f'SELECT * FROM av_microservice_finance.advance WHERE advanceid = {query.loc[j, "advanceid"]};\n'
      # f'SELECT * FROM av_microservice_finance.charge WHERE advanceid = {query.loc[j, "advanceid"]};\n'
      f'SELECT * FROM av_microservice_finance.payment WHERE advanceid = {query.loc[j, "advanceid"]};\n')


