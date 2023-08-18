# import os
import pandas as pd
# import mysql.connector
# from mysql.connector import Error
# import numpy as np
# from IPython.display import display
# import matplotlib.pyplot as plt
# import seaborn as sns
import os.path
from datetime import datetime


import pysftp

with pysftp.Connection('172.20.13.205', username='tomcat', password='3h9fEoWp7yIZ1ixqtytw') as sftp:

    print("Connection established")


    sftp.cwd('/opt/applications/checker/reports')
    directory_structure = sftp.listdir_attr()

    #sftp.get('exceptionAdvanceReport2023-01-01.csv')

    date_time = datetime.now()
    year = date_time.year
    month = date_time.month
    day = date_time.day - 1


    sftp.get(f'exceptionAdvanceReport2023-0{month}-0{day}.csv', f'/home/adrian/PycharmProjects/Checkers/MTC | PC/Advances/exceptionAdvanceReport2023-0{month}-0{day}.csv')
    sftp.get(f'exceptionPaymentReport2023-0{month}-0{day}.csv', f'/home/adrian/PycharmProjects/Checkers/MTC | PC/Payments/exceptionPaymentReport2023-0{month}-0{day}.csv')
    sftp.get(f'exceptionRechargeReport2023-0{month}-0{day}.csv', f'/home/adrian/PycharmProjects/Checkers/MTC | PC/Recharges/exceptionRechargeReport2023-0{month}-0{day}.csv')


    for attr in directory_structure:
        print(attr.filename, attr)




date_time = datetime.now()
year = date_time.year
month = date_time.month
day = date_time.day - 1
print(day)
# advancesDf = pd.read_csv(f'Advances/exceptionAdvanceReport2023-04-28_BR2.csv')
advances_file = open(f'Advances/exceptionAdvanceReport2023-0{month}-0{day}.csv', 'r')
payment_file = open(f'Payments/exceptionPaymentReport2023-0{month}-0{day}.csv', 'r')
recharge_file = open(f'Recharges/exceptionRechargeReport2023-0{month}-0{day}.csv', 'r')

num_lines_advances = sum(1 for line in advances_file) - 1
num_lines_payments = sum(1 for line in payment_file) - 1
num_lines_recharges = sum(1 for line in recharge_file) - 1

advances = open(f'Advances/exceptionAdvanceReport2023-0{month}-0{day}.csv', "r")
payment_file = open(f'Payments/exceptionPaymentReport2023-0{month}-0{day}.csv', 'r')
advances_name = os.path.basename(f'Advances/exceptionAdvanceReport2023-0{month}-0{day}.csv')
payment_name = os.path.basename(f'Payments/exceptionPaymentReport2023-0{month}-0{day}.csv')
recharge_name = os.path.basename(f'Recharge/exceptionRechargeReport2023-0{month}-0{day}.csv')
print(num_lines_payments)

print(f'Good Morning\n'
      f'\n'
      f'*Advance checker ran for {year}-0{month}-0{day}: *\n'
      f'\n'
      f'- {num_lines_advances} issues to report\n'
      f'{advances_name}\n')


print(f'*Payment checker ran for {year}-0{month}-{day}: *\n'
      f'- {num_lines_payments} issues to report\n'
      f'\n'
      f'{payment_name}\n')

print(f'*Recharge checker ran for {year}-0{month}-0{day}* \n'
      f'- {num_lines_recharges} issues to report\n'
      f'{recharge_name}\n'
      f'{recharge_file.read()}')

minDay = date_time.day - day
x = None

if minDay > 1:
    advances_file = open(f'Advances/exceptionAdvanceReport2023-0{month}-0{day}.csv', 'r')
    payment_file = open(f'Payments/exceptionPaymentReport2023-0{month}-0{day}.csv', 'r')
    recharge_file = open(f'Recharges/exceptionRechargeReport2023-0{month}-0{day}.csv', 'r')
    print(f'Good Morning\n'
          f'\n'
          f'*Advance checker ran for {year}-0{month}-0{day} to {year}-0{month}-0{date_time.day - 1}: *\n'
          f'\n'
          f'- {num_lines_advances} issues to report\n'
          f'{advances_name}\n'
          f'{advances_file.read()}')

    print(f'*Payment checker ran for {year}-0{month}-{day} to {year}-0{month}-0{date_time.day - 1}: *\n'
          f'- {num_lines_payments} issues to report\n'
          f'\n'
          # f'{(lambda x: x = x if num_lines_payments > 0 else x=None)(payment_name)}'
          f'{payment_name}\n'
          f'{payment_file.read()}')

    print(f'*Recharge checker ran for {year}-0{month}-0{day} to {year}-0{month}-0{date_time.day - 1}: * \n'
          f'- {num_lines_recharges} issues to report(please see file attached)\n'
          f'{recharge_name}'
          f'{recharge_file.read()}')



# minDate =
# advances = pd.read_csv('exceptionAdvanceReport2023-01-01.csv')
# payments = pd.read_csv('exceptionPaymentReport2022-12-13.csv')
# path = pd.read_csv("/home/adrian/exceptionRechargeReport2022-09-20.csv", delimiter="|")
# filesize = os.path.getsize("/home/adrian/processedDigicel.csv")

