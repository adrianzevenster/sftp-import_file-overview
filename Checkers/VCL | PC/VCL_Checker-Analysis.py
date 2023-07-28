import pandas as pd
import numpy as np
import datetime
import glob
import os
# advances = pd.read_csv("Advances/exceptionAdvanceReport2023-05-26.csv", error_bad_lines=False)
# payments = pd.read_csv("Payments/exceptionPaymentReport2023-05-26.csv")


# advances = advances.groupby("advancedate").sum()


# advances = pd.read_csv("Advances/exceptionAdvanceReport2023-07-17.csv", sep=",", quotechar=" ", error_bad_lines=False)
# payments = pd.read_csv("Payments/exceptionPaymentReport2023-07-17.csv", sep=",", error_bad_lines=False)
#
# counts = advances['reason'].value_counts()
# counts2 = payments['reason'].value_counts()
# print(counts)
# print(counts2)
#
#
# # payments = payments.drop([payments.index[10360]])
# payments["paymentdate"] = pd.to_datetime(payments['paymentdate'], format= '%Y-%m-%d')
# payments.sort_values("paymentdate")
# payments['dating'] = payments["paymentdate"].dt.date
# counts2 = payments.groupby('dating')['reason'].value_counts()
#
# advances["advancedate"] = pd.to_datetime(advances['advancedate'], format= '%Y-%m-%d')
# advances['dating'] = advances["advancedate"].dt.date
# aReason = np.where(advances['reason'] == 'Advance missing in recon')
# aCheck = advances.loc[aReason]
# aValue = aCheck.groupby('dating')["amount"].sum()
# aCheck = aCheck.groupby('dating').count().reset_index()
#
# jj = np.where(payments['reason'] != 'Payment has been allocated to the wrong advance')
# ff = payments.loc[jj]
# ff["dating"] = ff["paymentdate"].dt.date
#
# ss = ff.groupby("dating").count().reset_index()
# # file = ff.groupby('advancedate').count().nunq
# ss = ff.groupby("dating")['amount'].sum()


# use glob to get all the csv files
# in the folder
# path = os.getcwd()
# csv_files = glob.glob(os.path.join("//home/adrian/PycharmProjects/Checkers/VCL | PC/Advances/", "*.csv"))

# # loop over the list of csv files
# for f in csv_files:
#     # read the csv file
#     df = pd.read_csv(f, error_bad_lines=False)
#
#     # print the location and filename
#     print('Location:', f)
#     print('File Name:', f.split("\\")[-1])
#
#     # print the content
#     print('Content:')
#     jj = np.where(df['reason'] == 'Advance missing in Recon')
#     ff = df.loc[jj]


directory_path = "Recharges/"
def import_recharges_fro(directory_path):
   for filename in os.listdir(directory_path):
      if filename.endswith(".csv"):
         file_path = f'{directory_path}/{filename}'
         df  = pd.read_csv(file_path) if filename.endswith(".csv") else None
         print(f'Files used {filename}')
         return df
def import_recharges_from_all_directories(directory_path):
   dFrame = []
   for root, _, files in os.walk(directory_path):
      for filename in files:
         if filename.endswith(".csv"):
            file_path = os.path.join(root, filename)
            try:
               df = pd.read_csv(file_path)
               if not df.empty:
                  print(f'Imported Files: {filename}')
                  dFrame.append(df)
               else:
                  print(f' File skipped {filename}')
            except pd.errors.EmptyDataError:
               print(f'file skipped {filename}')
            except Exception as e:
               print(F"Error when file read {filename}")


   return dFrame


recharges = import_recharges_from_all_directories(directory_path)
