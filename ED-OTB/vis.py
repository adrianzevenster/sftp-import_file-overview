import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("vcl_qualifiedAmts_Dist.csv")


plt.figure(figsize=(12, 6))
plt.bar(file["qualifiedamount"], file["count(qualifiedamount)"])
plt.title("MO Qualified Amount Frequency Distribution")
plt.ylabel("Qualified Amount Counts")
plt.xlabel("Unique Qualified Amounts")

plt.show()
