import os
import pandas as pd
# import mysql.connector
# from mysql.connector import Error
# import numpy as np
# from IPython.display import display
# import matplotlib.pyplot as plt
# import seaborn as sns
import os.path
from datetime import datetime
import mysql.connector
from mysql.connector import Error



import pysftp

# def sftp_vcl_report(month, day, year):
with pysftp.Connection('10.0.44.22', username='christiaans001', password='Tmister083!') as sftp:

    print("Connection established")


    sftp.cwd('/opt/applications/checker/reports')
    directory_structure = sftp.listdir_attr()


    date_time = datetime.now()
    year = date_time.year
    month = '{:02d}'.format(date_time.month)
    print(month)
    day = '{:02d}'.format(date_time.day - 2)
    print(day)
#     print(day)
#     sftp.get(f'exceptionAdvanceReport2023-07-01.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Advances/exceptionAdvanceReport2023-07-01_Recon.csv')
#     sftp.get(f'exceptionPaymentReport2023-07-01.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Payments/exceptionPaymentReport2023-07-01_Recon.csv')
#     # sftp.get(f'exceptionRechargeReport2023-06-30.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Recharges/exceptionRechargeReport2023-06-30.csv')
#
    sftp.get(f'exceptionAdvanceReport2023-{month}-{day}.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Advances/exceptionAdvanceReport2023-{month}-{day}.csv')
    sftp.get(f'exceptionPaymentReport2023-{month}-{day}.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Payments/exceptionPaymentReport2023-{month}-{day}.csv')
    sftp.get(f'exceptionRechargeReport2023-{month}-{day}.csv', f'/home/adrian/PycharmProjects/Checkers/VCL | PC/Recharges/exceptionRechargeReport2023-{month}-{day}.csv')


    for attr in directory_structure:
        print(attr.filename, attr)

date_time = datetime.now()
year = date_time.year
month = '{:02d}'.format(date_time.month) #'{:02d}'.format(6)
day = '{:02d}'.format(date_time.day - 2)
# day_formatted = current_date.strftime("%d").lstrip("0").rjust(2, "0")
# # print(day)
# # # advancesDf = pd.read_csv(f'Advances/exceptionAdvanceReport2023-04-28_BR2.csv')
advances_file = open(f'Advances/exceptionAdvanceReport2023-{month}-{day}.csv', 'r')
payment_file = open(f'Payments/exceptionPaymentReport2023-{month}-{day}.csv', 'r')
recharge_file = open(f'Recharges/exceptionRechargeReport2023-{month}-{day}.csv', 'r')
# # # advances_file = open(f'Advances/exceptionAdvanceReport2023-05-31.csv', "r")
# # # payment_file = open(f'Payments/exceptionPaymentReport2023-05-31.csv', 'r')
# # # recharge_file = open(f'Recharges/exceptionRechargeReport2023-05-31.csv', 'r')
# # #
num_lines_advances = sum(1 for line in advances_file) - 1
num_lines_payments = sum(1 for line in payment_file) - 1
num_lines_recharges = sum(1 for line in recharge_file) - 1
# #
advances = open(f'Advances/exceptionAdvanceReport2023-{month}-{day}.csv', "r")
payment_file = open(f'Payments/exceptionPaymentReport2023-{month}-{day}.csv', 'r')
advances_name = os.path.basename(f'Advances/exceptionAdvanceReport2023-{month}-{day}.csv')
payment_name = os.path.basename(f'Payments/exceptionPaymentReport2023-{month}-{day}.csv')
recharge_name = os.path.basename(f'Recharges/exceptionRechargeReport2023-{month}-{day}.csv')


# advances = open(f'Advances/exceptionAdvanceReport2023-05-08_Recon.csv', "r")
# payment_file = open(f'Payments/exceptionPaymentReport2023-05-08_Recon.csv', 'r')
# advances_name = os.path.basename(f'Advances/exceptionAdvanceReport2023-05-08_Recon.csv')
# payment_name = os.path.basename(f'Payments/exceptionPaymentReport2023-05-08_Recon.csv')
print(num_lines_payments)

print(f'Good Morning\n'
      f'\n'
      f'*Advance checker ran for {year}-{month}-{day}: *\n'
      f'\n'
      f'- {num_lines_advances} issues to report\n'
      f'{advances_name}\n'
      f'{advances.read()}'
      )


print(f'*Payment checker ran for {year}-{month}-{day}: *\n'
      f'- {num_lines_payments} issues to report\n'
      f'\n'
      f'{payment_name}\n'
      f'{payment_file.read()}'
      )

print(f'*Recharge checker ran for {year}-{month}-{day}* \n'
      f'- {num_lines_recharges} issues to report(please see file attached)\n'
      f'{recharge_name} \n'
      f'{recharge_file}'
    )
#
minDay = date_time.day - (date_time.day - 2)
# x = None

if minDay > 1:
    advances_file = open(f'Advances/exceptionAdvanceReport2023-{month}-{day}.csv', 'r')
    payment_file = open(f'Payments/exceptionPaymentReport2023-{month}-{day}.csv', 'r')
    recharge_file = open(f'Recharges/exceptionRechargeReport2023-{month}-{day}.csv', 'r')
    print(f'Good Morning\n'
          f'\n'
          f'*Advance checker ran for {year}-{month}-{day} to {year}-{month}-{date_time.day - 1}: *\n'
          f'- {num_lines_advances} issues to report\n'
          f'{advances_name}\n'
          f'{advances_file.read()}'
          )

    print(f'*Payment checker ran for {year}-{month}-{day} to {year}-{month}-{date_time.day - 1}: *\n'
          f'- {num_lines_payments} issues to report\n'
          f'\n'
          # f'{(lambda x: x = x if num_lines_payments > 0 else x=None)(payment_name)}'
          f'{payment_name}\n'
          f'{payment_file.read()}'
          )

    print(f'*Recharge checker ran for {year}-{month}-{day} to {year}-{month}-{date_time.day - 1}: * \n'
          f'- {num_lines_recharges} issues to report(please see file attached)')

#
# """Start of  sql queries"""

# minDate =
# advances = pd.read_csv('exceptionAdvanceReport2023-01-01.csv')
# payments = pd.read_csv('exceptionPaymentReport2022-12-13.csv')
# path = pd.read_csv("/home/adrian/exceptionRechargeReport2022-09-20.csv", delimiter="|")
# filesize = os.path.getsize("/home/adrian/processedDigicel.csv")

